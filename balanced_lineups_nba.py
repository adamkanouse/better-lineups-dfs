"""
Generate as many lineups as you want with
max exposures of your selected exposure to any one player,
with a specified minimum average of your choice.
The output here is a CSV file that can be used
to upload lineups at https://www.draftkings.com/lineup/upload

Pre-reqs:
1) Salary file exists at passed location
2) Projection file exists at passed location
3) PIDS file downloaded from aforementioned location

Example usage:
```python
from examples import balanced_lineups_nba
balanced_lineups_nba.run()
```
"""

import random
import numpy
from collections import Counter
from optimize import run as optimizer_run
from argparse import Namespace

from csv_parse.nba_upload import (
    update_upload_csv,
    create_upload_file,
    map_pids,
)

DEFAULT_ARGS = dict(
    duo='n',
    s='n',
    w=5,
    i=1,
    league='NBA',
    limit='n',
    lp=0,
    mp=500,
    ms=100000,
    sp=1000,
    banned=[],
    historical_date=None,
    game='draftkings',
    po=0,
    pids='data/pid-file-nba.csv',
    salary_file='data/current-nba-salaries.csv',
    projection_file='data/current-nba-projections.csv',
    home=None,
    v_avg=100,
    source='nba_rotogrinders',
    historical=None,
    season=None,
    dtype=None,
    flex_position=None,
    locked=[],
    teams=None,
    po_location=None,
    min_avg=None,
)


def is_duplicate(r, rp):
    '''
    Checks for duplicate rosters irrespective of position distribution.
    '''
    rp = [sorted([p.name for p in rn.players]) for rn in rp]
    rcur = sorted([p.name for p in r.players])
    return rcur in rp


def run(lineups, exposure, min_avg):
    DEFAULT_ARGS['min_avg'] = min_avg
    roster_list, player_list = [], []
 #   create_upload_file()
    player_map = map_pids(DEFAULT_ARGS['pids'])
    max_exposure = lineups * exposure
    exposure = None

    for _ in range(lineups):
        args = DEFAULT_ARGS.copy()
        if exposure:
            args['banned'] = DEFAULT_ARGS['banned'] + [
                name for name, freq in exposure.items()
                if freq > max_exposure
            ]
        roster = optimizer_run('NBA', Namespace(**args), [])

        # discard and replace duplicate lineups
        if is_duplicate(roster, roster_list):
            while is_duplicate(roster, roster_list):
                args['banned'].append(
                    random.choice(roster.players).name
                )
                roster = optimizer_run('NBA', Namespace(**args), [])

        roster_list.append(roster)
        player_list += [p.name for p in roster.players]

#        update_upload_csv(player_map,roster)
        exposure = Counter(player_list)

    unique = len(set([str(r.players) for r in roster_list]))
    if unique != lineups:
        raise Exception(
            'Duplication error in logic. Expected {} and got {} lineups'
            .format(lineups, unique)
        )

    scores = [r.projected() for r in roster_list]
    print('Generated {} lineups.'.format(lineups))
    print('Maximum score: {}'.format(numpy.max(scores)))
    print('Minimum score: {}'.format(numpy.min(scores)))
    print('Average score: {}'.format(numpy.average(scores)))
    print('Median score: {}'.format(numpy.median(scores)))

if __name__ == '__main__':
    lineups=3
    exposure=.5
    min_avg=15
    run(lineups, exposure, min_avg)
