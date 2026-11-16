# repos/ — every GitHub repo, filed into the .profile home

**500 repos** under `Jackblanket847` — **86 owned, 414 forks** —
sorted out from GitHub on 2026-11-16 and filed here, in the profile
repo home (`Jackblanket847/Jackblanket847`).

Open it in the browser: [https://github.dev/Jackblanket847/Jackblanket847](https://github.dev/Jackblanket847/Jackblanket847)

## The chain

```
home (the .profile home itself)
  ├── enterprise · builds · sites · learn        (owned repos)
  └── forks_ai · forks_crypto · forks_gov · forks_payments
      · forks_space · forks_dev · forks_web · forks_misc   (forks)
```

Each folder is a variable listing (`variables.py`): one record per repo
(name, kind, visibility, language, default branch, last update, URL),
plus the home-anchor variables (`OWNER`, `HOME_PROFILE_REPO`, `HOME_URL`,
`HOME_DEV_URL`) and a `LINKS` map. Every folder except `home/` links its
anchor variables back to `home/` — that is the chain that connects all
repos into the profile repo home.

## Folders

| Folder | Repos | What lives there | Chain anchor |
| --- | --- | --- | --- |
| `home/` | 10 | The .profile home itself — the profile repo, the home site, and the GitHub config. | anchor `Jackblanket847` |
| `enterprise/` | 11 | Business and entity scaffolding — enterprise tree, REPO databank, nested master. | anchor `enterprise` |
| `builds/` | 12 | Active builds — Termux site, Mothership, PowerBank, BlockDAG contracts, and the tools that run them. | anchor `termux-site` |
| `sites/` | 28 | Web properties and media — Mental Health Enterprise, Smith Seed Roots, Newspaper Media Agency, and the landing pages. | anchor `mental-health-enterprise` |
| `learn/` | 25 | Learning, practice, and demos — tutorials, games, and starter projects. | anchor `hello-world` |
| `forks_ai/` | 21 | Forks — AI, LLMs, and agents (Karpathy trio, cookbooks, agent frameworks). | anchor `nanoGPT` |
| `forks_crypto/` | 48 | Forks — crypto, chains, wallets, and web3. | anchor `go-ethereum` |
| `forks_gov/` | 39 | Forks — government, open data, and public research identity (data.gov, USGPO, ORCID). | anchor `catalog.data.gov` |
| `forks_payments/` | 15 | Forks — payments and commerce SDKs (Braintree, PayPal, Plaid, Stripe, Shopify). | anchor `braintree-web` |
| `forks_space/` | 2 | Forks — space and fleet (Stellarium sky engine, proto-fleet). | anchor `stellarium-web-engine` |
| `forks_dev/` | 78 | Forks — developer tools, languages, and infrastructure. | anchor `git` |
| `forks_web/` | 57 | Forks — web, mobile, and docs. | anchor `wordpress` |
| `forks_misc/` | 154 | Forks — everything else, unclassified by keyword. | anchor `core` |

## Verify it

```sh
python3 filing.py          # coverage 500/500, links, 13-step chain
python3 -m unittest discover -s tests -v
python3 api/variable_listing.py --port 8096   # serves /api/repos, /api/filing, ...
```

`filing.py` checks three things: (1) the live inventory
(`INVENTORY.json`, 500 repos) is covered exactly once — no missing,
no duplicated, no extra repos; (2) every `LINKS` entry holds, i.e. every
folder agrees with `home/` on the profile home; (3) the chain resolves:
home → each category → its anchor repo.

## Files

- `INVENTORY.json` — the full 500-repo inventory with category + kind.
- `REPOS.md` — the same inventory as a readable table.
- `connections.json` — manifest: home anchor, categories, connections, API routes.
- `filing.py` — the coded filing that verifies the whole chain.
- `api/variable_listing.py` — stdlib-only API on port 8096.
- `tests/test_filing.py` — the checks above, as tests.
