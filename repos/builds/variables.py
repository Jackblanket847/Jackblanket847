"""Variable listing for repos/builds — Active builds — Termux site, Mothership, PowerBank, BlockDAG contracts, and the tools that run them.

Source of truth: the live GitHub inventory pulled 2026-11-16
(INVENTORY.json). Every repo here is one GitHub repo owned by
Jackblanket847. Values are the repo's own record — name, kind,
visibility, language, default branch, last update, URL.
"""

OWNER = "Jackblanket847"
HOME_PROFILE_REPO = "Jackblanket847/Jackblanket847"
HOME_URL = "https://github.com/Jackblanket847/Jackblanket847"
HOME_DEV_URL = "https://github.dev/Jackblanket847/Jackblanket847"
CATEGORY = "builds"
CATEGORY_URL = "https://github.com/Jackblanket847/Jackblanket847/tree/main/repos/builds"
REPO_COUNT = 12

REPOS = {
    'a16-system-console': {
        'full_name': 'Jackblanket847/a16-system-console',
        'kind': 'owned',
        'private': True,
        'language': 'Go',
        'default_branch': 'main',
        'updated': '2026-11-03',
        'url': 'https://github.com/Jackblanket847/a16-system-console',
        'description': '',
    },
    'blockdag-contracts': {
        'full_name': 'Jackblanket847/blockdag-contracts',
        'kind': 'owned',
        'private': True,
        'language': 'Solidity',
        'default_branch': 'main',
        'updated': '2026-10-07',
        'url': 'https://github.com/Jackblanket847/blockdag-contracts',
        'description': '',
    },
    'bossbot-code': {
        'full_name': 'Jackblanket847/bossbot-code',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-10-15',
        'url': 'https://github.com/Jackblanket847/bossbot-code',
        'description': '',
    },
    'cold-wallet': {
        'full_name': 'Jackblanket847/cold-wallet',
        'kind': 'owned',
        'private': True,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2026-10-15',
        'url': 'https://github.com/Jackblanket847/cold-wallet',
        'description': '',
    },
    'com-host-www-example': {
        'full_name': 'Jackblanket847/com-host-www-example',
        'kind': 'owned',
        'private': True,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-11-16',
        'url': 'https://github.com/Jackblanket847/com-host-www-example',
        'description': '',
    },
    'JackSonBlanket': {
        'full_name': 'Jackblanket847/JackSonBlanket',
        'kind': 'owned',
        'private': True,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-11-02',
        'url': 'https://github.com/Jackblanket847/JackSonBlanket',
        'description': '',
    },
    'mothership': {
        'full_name': 'Jackblanket847/mothership',
        'kind': 'owned',
        'private': True,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-11-13',
        'url': 'https://github.com/Jackblanket847/mothership',
        'description': 'Mothership Basestation — 4 Fleet Capsules, Global Internet Portal (Nuthouse Management Group LLC)',
    },
    'muse-database': {
        'full_name': 'Jackblanket847/muse-database',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-10-05',
        'url': 'https://github.com/Jackblanket847/muse-database',
        'description': '',
    },
    'pocket-xcode': {
        'full_name': 'Jackblanket847/pocket-xcode',
        'kind': 'owned',
        'private': True,
        'language': 'Swift',
        'default_branch': 'main',
        'updated': '2026-10-10',
        'url': 'https://github.com/Jackblanket847/pocket-xcode',
        'description': '',
    },
    'power-bank-facility': {
        'full_name': 'Jackblanket847/power-bank-facility',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-11-14',
        'url': 'https://github.com/Jackblanket847/power-bank-facility',
        'description': 'Power Bank Facility — UnifiedPowerBankFacility terminal console (GRFPB1002-WHT, 37Wh) + demo confirmation flow',
    },
    'soapbox-built': {
        'full_name': 'Jackblanket847/soapbox-built',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-11-02',
        'url': 'https://github.com/Jackblanket847/soapbox-built',
        'description': 'Prebuilt Soapbox frontend (2022-05-13 soapbox-fe build, flattened to repo root for static serving). Frontend only; needs a Mastodon-compatible API backend.',
    },
    'termux-site': {
        'full_name': 'Jackblanket847/termux-site',
        'kind': 'owned',
        'private': True,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-11-12',
        'url': 'https://github.com/Jackblanket847/termux-site',
        'description': '',
    },
}

# Filing links: this folder's anchor vars must agree with
# the .profile home (repos/home). That is the chain that
# connects every repo back into the profile repo home.
LINKS = {
    "HOME_PROFILE_REPO": ["home.HOME_PROFILE_REPO"],
    "OWNER": ["home.OWNER"],
    "HOME_URL": ["home.HOME_URL"],
    "HOME_DEV_URL": ["home.HOME_DEV_URL"],
}

VARIABLES = {
    "OWNER": OWNER,
    "HOME_PROFILE_REPO": HOME_PROFILE_REPO,
    "HOME_URL": HOME_URL,
    "HOME_DEV_URL": HOME_DEV_URL,
    "CATEGORY": CATEGORY,
    "CATEGORY_URL": CATEGORY_URL,
    "REPO_COUNT": REPO_COUNT,
}
