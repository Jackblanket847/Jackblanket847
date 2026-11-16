"""Variable listing for repos/home — The .profile home itself — the profile repo, the home site, and the GitHub config.

Source of truth: the live GitHub inventory pulled 2026-11-16
(INVENTORY.json). Every repo here is one GitHub repo owned by
Jackblanket847. Values are the repo's own record — name, kind,
visibility, language, default branch, last update, URL.
"""

OWNER = "Jackblanket847"
HOME_PROFILE_REPO = "Jackblanket847/Jackblanket847"
HOME_URL = "https://github.com/Jackblanket847/Jackblanket847"
HOME_DEV_URL = "https://github.dev/Jackblanket847/Jackblanket847"
CATEGORY = "home"
CATEGORY_URL = "https://github.com/Jackblanket847/Jackblanket847/tree/main/repos/home"
REPO_COUNT = 10

REPOS = {
    '-': {
        'full_name': 'Jackblanket847/-',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-07-01',
        'url': 'https://github.com/Jackblanket847/-',
        'description': '',
    },
    '.family.means.more': {
        'full_name': 'Jackblanket847/.family.means.more',
        'kind': 'owned',
        'private': False,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2025-06-04',
        'url': 'https://github.com/Jackblanket847/.family.means.more',
        'description': '',
    },
    '.github': {
        'full_name': 'Jackblanket847/.github',
        'kind': 'owned',
        'private': True,
        'language': 'Dockerfile',
        'default_branch': 'main',
        'updated': '2026-10-12',
        'url': 'https://github.com/Jackblanket847/.github',
        'description': '',
    },
    'example': {
        'full_name': 'Jackblanket847/example',
        'kind': 'owned',
        'private': False,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2026-06-21',
        'url': 'https://github.com/Jackblanket847/example',
        'description': '',
    },
    'github': {
        'full_name': 'Jackblanket847/github',
        'kind': 'owned',
        'private': False,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2026-06-21',
        'url': 'https://github.com/Jackblanket847/github',
        'description': '',
    },
    'github.io': {
        'full_name': 'Jackblanket847/github.io',
        'kind': 'owned',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2024-12-23',
        'url': 'https://github.com/Jackblanket847/github.io',
        'description': 'My clone repository',
    },
    'Jackblanket847': {
        'full_name': 'Jackblanket847/Jackblanket847',
        'kind': 'owned',
        'private': False,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-11-15',
        'url': 'https://github.com/Jackblanket847/Jackblanket847',
        'description': 'Config files for my GitHub profile.',
    },
    'jackblanket847.github.io': {
        'full_name': 'Jackblanket847/jackblanket847.github.io',
        'kind': 'owned',
        'private': False,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2025-04-28',
        'url': 'https://github.com/Jackblanket847/jackblanket847.github.io',
        'description': '',
    },
    'jackblanket847.io': {
        'full_name': 'Jackblanket847/jackblanket847.io',
        'kind': 'owned',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2025-08-08',
        'url': 'https://github.com/Jackblanket847/jackblanket847.io',
        'description': 'Experience macOS just like before',
    },
    'www': {
        'full_name': 'Jackblanket847/www',
        'kind': 'owned',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2025-06-18',
        'url': 'https://github.com/Jackblanket847/www',
        'description': '',
    },
}

# home/ IS the anchor: nothing to link up to. Every other
# category links its anchor vars back to this folder.
LINKS = {}

VARIABLES = {
    "OWNER": OWNER,
    "HOME_PROFILE_REPO": HOME_PROFILE_REPO,
    "HOME_URL": HOME_URL,
    "HOME_DEV_URL": HOME_DEV_URL,
    "CATEGORY": CATEGORY,
    "CATEGORY_URL": CATEGORY_URL,
    "REPO_COUNT": REPO_COUNT,
}
