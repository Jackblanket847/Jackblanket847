"""Variable listing for repos/forks_space — Forks — space and fleet (Stellarium sky engine, proto-fleet).

Source of truth: the live GitHub inventory pulled 2026-11-16
(INVENTORY.json). Every repo here is one GitHub repo owned by
Jackblanket847. Values are the repo's own record — name, kind,
visibility, language, default branch, last update, URL.
"""

OWNER = "Jackblanket847"
HOME_PROFILE_REPO = "Jackblanket847/Jackblanket847"
HOME_URL = "https://github.com/Jackblanket847/Jackblanket847"
HOME_DEV_URL = "https://github.dev/Jackblanket847/Jackblanket847"
CATEGORY = "forks_space"
CATEGORY_URL = "https://github.com/Jackblanket847/Jackblanket847/tree/main/repos/forks_space"
REPO_COUNT = 2

REPOS = {
    'proto-fleet': {
        'full_name': 'Jackblanket847/proto-fleet',
        'kind': 'fork',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-07-14',
        'url': 'https://github.com/Jackblanket847/proto-fleet',
        'description': 'Proto Fleet. Mining management software. Evolved.',
    },
    'stellarium-web-engine': {
        'full_name': 'Jackblanket847/stellarium-web-engine',
        'kind': 'fork',
        'private': False,
        'language': None,
        'default_branch': 'master',
        'updated': '2026-11-13',
        'url': 'https://github.com/Jackblanket847/stellarium-web-engine',
        'description': 'JavaScript planetarium engine',
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
