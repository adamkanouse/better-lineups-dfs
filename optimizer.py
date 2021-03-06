from ortools.linear_solver import pywraplp


class Optimizer(object):
    def __init__(
        self,
        players,
        existing_rosters,
        salary,
        roster_size,
        position_limits,
        general_position_limits,
        settings,
    ):
        self.solver = pywraplp.Solver(
            'FD',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING
        )
        self.players = players
        self.enumerated_players = list(enumerate(players))
        self.existing_rosters = existing_rosters or []
        self.salary = salary
        self.roster_size = roster_size
        self.position_limits = position_limits
        self.general_position_limits = general_position_limits
        self.settings = settings

        self.player_to_idx_map = {}
        self.variables = []
        for idx, player in self.enumerated_players:
            if player.lock and not player.multi_position:
                self.variables.append(
                    self.solver.IntVar(
                        1, 1, player.solver_id
                    )
                )
            else:
                self.variables.append(
                    self.solver.IntVar(0, 1, player.solver_id)
                )

            self.player_to_idx_map[player.solver_id] = idx

        self.objective = self.solver.Objective()
        self.objective.SetMaximization()

    def solve(self):
        self._optimize_on_projected_points()
        self._set_salary_cap()
        self._set_roster_size()
        self._set_no_multi_player()
        self._set_positions()
        self._set_general_positions()
        self._set_stack()
        self._set_combo()
        self._set_no_duplicate_lineups()
        solution = self.solver.Solve()
        return solution == self.solver.OPTIMAL

    def _optimize_on_projected_points(self):
        for i, player in self.enumerated_players:
            proj = player.proj if self.settings.projection_file \
                else player.average_score
            self.objective.SetCoefficient(
                self.variables[i],
                proj
            )

    def _set_salary_cap(self):
        salary_cap = self.solver.Constraint(
            0,
            self.salary,
        )
        for i, player in self.enumerated_players:
            salary_cap.SetCoefficient(
                self.variables[i],
                player.cost
            )

    def _set_roster_size(self):
        size_cap = self.solver.Constraint(
            self.roster_size,
            self.roster_size,
        )

        for variable in self.variables:
            size_cap.SetCoefficient(variable, 1)

    def _set_no_multi_player(self):
        multi_caps = {}
        for i, p in self.enumerated_players:
            if not p.multi_position:
                continue

            if p.name not in multi_caps:
                if p.lock:
                    multi_caps[p.name] = self.solver.Constraint(1, 1)
                else:
                    multi_caps[p.name] = self.solver.Constraint(0, 1)

            multi_caps[p.name].SetCoefficient(
                self.variables[i],
                1
            )

    def _set_stack(self):
        stack = self.settings.__dict__.get('stack')
        stack_count = self.settings.__dict__.get('stack_count')

        if stack and stack_count:
            position_cap = self.solver.Constraint(
                stack_count,
                stack_count,
            )

            for i, player in self.enumerated_players:
                if self.settings.stack == player.team:
                    position_cap.SetCoefficient(
                        self.variables[i],
                        1
                    )

    def _set_combo(self):
        combo = self.settings.__dict__.get('force_combo')
        if combo:
            teams = set([p.team for p in self.players])
            enumerated_players = self.enumerated_players

            for team in teams:
                wrs_on_team = [
                    self.variables[i] for i, p in enumerated_players
                    if p.team == team and p.pos == 'WR'
                ]
                qbs_on_team = [
                    self.variables[i] for i, p in enumerated_players
                    if p.team == team and p.pos == 'QB'
                ]
                self.solver.Add(
                    self.solver.Sum(wrs_on_team) >=
                    self.solver.Sum(qbs_on_team)
                )

    def _set_positions(self):
        for position, min_limit, max_limit in self.position_limits:
            position_cap = self.solver.Constraint(
                min_limit,
                max_limit
            )

            for i, player in self.enumerated_players:
                if position == player.pos:
                    position_cap.SetCoefficient(self.variables[i], 1)

    def _set_general_positions(self):
        for general_position, min_limit, max_limit in \
                self.general_position_limits:
            position_cap = self.solver.Constraint(min_limit, max_limit)

            for i, player in self.enumerated_players:
                if general_position == player.nba_general_position:
                    position_cap.SetCoefficient(
                        self.variables[i],
                        1
                    )

    def _set_no_duplicate_lineups(self):
        for roster in self.existing_rosters:
            unique_players = self.solver.Constraint(
                0,
                self.roster_size - 1
            )

            for player in roster.sorted_players():
                i = self.player_to_idx_map[player.solver_id]
                unique_players.SetCoefficient(self.variables[i], 1)
