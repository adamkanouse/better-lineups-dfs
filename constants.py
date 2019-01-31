DRAFT_KINGS = 'DRAFT_KINGS'
FAN_DUEL = 'FAN_DUEL'

SALARY_CAP = {
    'NBA': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 60000,
    },
    'CBB': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 60000,
    },
    'WNBA': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 40000,
    },
    'NFL': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 60000,
    },
    'CFB': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 60000,
    },
    'MLB': {
        DRAFT_KINGS: 50000,
        FAN_DUEL: 35000,
    },
    'PGA': {
        FAN_DUEL: 60000,
    },
    'NASCAR': {
        FAN_DUEL: 50000,
    },
}

ROSTER_SIZE = {
    DRAFT_KINGS: {
        'NFL': 9,
        'CFB': 8,
        'NBA': 8,
        'CBB': 8,
        'WNBA': 6,
        'MLB': 10,
    },
    FAN_DUEL: {
        'NBA': 9,
        'CBB': 9,
        'NFL': 9,
        'CFB': 9,
        'MLB': 9,
        'WNBA': 7,
        'NASCAR': 5,
        'PGA': 6,
    }
}


def get_nfl_positions(
    rb_min=2,
    wr_min=3,
    te_min=1,
    te_upper=2
):
    return [
        ['QB', 1, 1],
        ['RB', rb_min, 3],
        ['WR', wr_min, 4],
        ['TE', te_min, te_upper],
        ['DST', 1, 1]
    ]

def get_cfb_positions(
    rb_min=2,
    wr_min=3,
):
    return [
        ['QB', 1, 2],
        ['RB', rb_min, 3],
        ['WR', wr_min, 4],
    ]


POSITIONS = {
    DRAFT_KINGS: {
        'NBA': [
            ['PG', 1, 3],
            ['SG', 1, 3],
            ['SF', 1, 3],
            ['PF', 1, 3],
            ['C', 1, 2]
        ],
        'CBB': [
            ['PG', 0, 5],
            ['SG', 0, 5],
            ['SF', 0, 3],
            ['PF', 0, 3],
            ['C', 0, 2]
        ],
        'WNBA': [
            ['PG', 1, 3],
            ['SG', 1, 3],
            ['SF', 1, 4],
            ['PF', 1, 4],
        ],
        'NFL': get_nfl_positions(),
        'CFB': get_cfb_positions(),
        'MLB': [
            ['SP', 2, 2],
            ['C', 1, 1],
            ['1B', 1, 1],
            ['2B', 1, 1],
            ['3B', 1, 1],
            ['SS', 1, 1],
            ['OF', 3, 3],
        ]
    },
    FAN_DUEL: {
        'NBA': [
            ['PG', 2, 2],
            ['SG', 2, 2],
            ['SF', 2, 2],
            ['PF', 2, 2],
            ['C', 1, 1],
        ],
        'NFL': get_nfl_positions(),
        'CFB': get_cfb_positions(),
        'MLB': [
            ['P', 1, 1],
            ['1B', 1, 2],  # TODO - allow C or 1B
            ['2B', 1, 2],
            ['3B', 1, 2],
            ['SS', 1, 2],
            ['OF', 3, 4],
        ],
        'WNBA': [
            ['G', 3, 3],
            ['F', 4, 4],
        ],
        'NASCAR': [
            ['D', 5, 5],
        ],
        'PGA': [
          ['G', 6, 6],
        ],
    }
}

NBA_GENERAL_POSITIONS = [
    ['G', 3, 4],
    ['F', 3, 4],
    ['C', 1, 2],
]
CBB_GENERAL_POSITIONS = [
    ['G', 3, 5],
    ['F', 3, 5],
]

WNBA_GENERAL_POSITIONS = [
    ['G', 2, 3],
    ['F', 3, 4],
]

DUO_TYPE = {
  'wr': [
    ['QB', 1, 1],
    ['WR', 1, 1]
  ],
  'te': [
    ["QB", 1, 1],
    ["TE", 1, 1]
  ],
  'rb': [
    ["QB", 1, 1],
    ["rb", 1, 1]
    ]
}

DK_TO_NFL_DRAFTKINGS = {
    'Panthers': 'Carolina Panthers',
    'Buccaneers': 'Tampa Bay Buccaneers',
    'Dolphins': 'Miami Dolphins',
    'Bears': 'Chicago Bears',
    'Raiders': 'Oakland Raiders',
    'Patriots': 'New England Patriots',
    'Vikings': 'Minnesota Vikings',
    'Eagles': 'Philadelphia Eagles',
    '49ers': 'San Francisco 49ers',
    'Bengals': 'Cincinnati Bengals',
    'Bills': 'Buffalo Bills',
    'Broncos': 'Denver Broncos',
    'Browns': 'Cleveland Browns',
    'Cardinals': 'Arizona Cardinals',
    'Chargers': 'San Diego Chargers',
    'Chiefs': 'Kansas City Chiefs',
    'Colts': 'Indianapolis Colts',
    'Cowboys': 'Dallas Cowboys',
    'Falcons': 'Atlanta Falcons',
    'Giants': 'New York Giants',
    'Jaguars': 'Jacksonville Jaguars',
    'Jets': 'New York Jets',
    'Lions': 'Detroit Lions',
    'Packers': 'Green Bay Packers',
    'Rams': 'Los Angeles Rams',
    'Ravens': 'Baltimore Ravens',
    'Redskins': 'Washington Redskins',
    'Saints': 'New Orleans Saints',
    'Seahawks': 'Seattle Seahawks',
    'Steelers': 'Pittsburgh Steelers',
    'Texans': 'Houston Texans',
    'Titans': 'Tennessee Titans'
}
