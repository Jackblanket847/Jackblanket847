"""Variable listing for repos/enterprise — Business and entity scaffolding — enterprise tree, REPO databank, nested master.

Source of truth: the live GitHub inventory pulled 2026-11-16
(INVENTORY.json). Every repo here is one GitHub repo owned by
Jackblanket847. Values are the repo's own record — name, kind,
visibility, language, default branch, last update, URL.
"""

OWNER = "Jackblanket847"
HOME_PROFILE_REPO = "Jackblanket847/Jackblanket847"
HOME_URL = "https://github.com/Jackblanket847/Jackblanket847"
HOME_DEV_URL = "https://github.dev/Jackblanket847/Jackblanket847"
CATEGORY = "enterprise"
CATEGORY_URL = "https://github.com/Jackblanket847/Jackblanket847/tree/main/repos/enterprise"
REPO_COUNT = 11

REPOS = {
    'billing-system': {
        'full_name': 'Jackblanket847/billing-system',
        'kind': 'owned',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2025-04-28',
        'url': 'https://github.com/Jackblanket847/billing-system',
        'description': '',
    },
    'data-gov-starter': {
        'full_name': 'Jackblanket847/data-gov-starter',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-10-07',
        'url': 'https://github.com/Jackblanket847/data-gov-starter',
        'description': '',
    },
    'DevelopmentFiles': {
        'full_name': 'Jackblanket847/DevelopmentFiles',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-04-09',
        'url': 'https://github.com/Jackblanket847/DevelopmentFiles',
        'description': 'dev',
    },
    'enterprise': {
        'full_name': 'Jackblanket847/enterprise',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-11-15',
        'url': 'https://github.com/Jackblanket847/enterprise',
        'description': '',
    },
    'Enterprises': {
        'full_name': 'Jackblanket847/Enterprises',
        'kind': 'owned',
        'private': False,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2025-04-28',
        'url': 'https://github.com/Jackblanket847/Enterprises',
        'description': '',
    },
    'NESTED-MASTER': {
        'full_name': 'Jackblanket847/NESTED-MASTER',
        'kind': 'owned',
        'private': True,
        'language': 'Python',
        'default_branch': 'main',
        'updated': '2026-10-23',
        'url': 'https://github.com/Jackblanket847/NESTED-MASTER',
        'description': 'Nested repository: core -> components -> services -> platform. Container-ready, tested, not deployed.',
    },
    'orcid-platform': {
        'full_name': 'Jackblanket847/orcid-platform',
        'kind': 'owned',
        'private': True,
        'language': 'JavaScript',
        'default_branch': 'main',
        'updated': '2026-10-09',
        'url': 'https://github.com/Jackblanket847/orcid-platform',
        'description': '',
    },
    'platform': {
        'full_name': 'Jackblanket847/platform',
        'kind': 'owned',
        'private': True,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-10-09',
        'url': 'https://github.com/Jackblanket847/platform',
        'description': '',
    },
    'platform-sites': {
        'full_name': 'Jackblanket847/platform-sites',
        'kind': 'owned',
        'private': True,
        'language': 'HTML',
        'default_branch': 'main',
        'updated': '2025-01-28',
        'url': 'https://github.com/Jackblanket847/platform-sites',
        'description': '',
    },
    'REPO': {
        'full_name': 'Jackblanket847/REPO',
        'kind': 'owned',
        'private': False,
        'language': None,
        'default_branch': 'main',
        'updated': '2026-10-05',
        'url': 'https://github.com/Jackblanket847/REPO',
        'description': '',
    },
    'Repos': {
        'full_name': 'Jackblanket847/Repos',
        'kind': 'owned',
        'private': True,
        'language': 'Shell',
        'default_branch': 'main',
        'updated': '2024-10-19',
        'url': 'https://github.com/Jackblanket847/Repos',
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
