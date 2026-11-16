"""Coded filing: the registry that connects all 500 repos into
the .profile home (Jackblanket847/Jackblanket847).

Every category folder lists its own repos in variables.py plus a LINKS
map of anchor variables that must agree with repos/home — the profile
home itself. This module loads all 13 folders, checks that the live
inventory (INVENTORY.json, 500 repos pulled 2026-11-16) is covered
exactly once, resolves every link, and resolves the 13-step chain
(home -> each category -> its anchor repo).

Run:  python3 filing.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from home import variables as home
from enterprise import variables as enterprise
from builds import variables as builds
from sites import variables as sites
from learn import variables as learn
from forks_ai import variables as forks_ai
from forks_crypto import variables as forks_crypto
from forks_gov import variables as forks_gov
from forks_payments import variables as forks_payments
from forks_space import variables as forks_space
from forks_dev import variables as forks_dev
from forks_web import variables as forks_web
from forks_misc import variables as forks_misc

CATEGORIES = ["home", "enterprise", "builds", "sites", "learn", "forks_ai", "forks_crypto", "forks_gov", "forks_payments", "forks_space", "forks_dev", "forks_web", "forks_misc"]

FOLDERS = {
    "home": home,
    "enterprise": enterprise,
    "builds": builds,
    "sites": sites,
    "learn": learn,
    "forks_ai": forks_ai,
    "forks_crypto": forks_crypto,
    "forks_gov": forks_gov,
    "forks_payments": forks_payments,
    "forks_space": forks_space,
    "forks_dev": forks_dev,
    "forks_web": forks_web,
    "forks_misc": forks_misc,
}


def listing():
    """All category listings, keyed by folder."""
    return {name: dict(mod.REPOS) for name, mod in FOLDERS.items()}


def inventory():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "INVENTORY.json")) as f:
        return json.load(f)


def check_coverage():
    """Every inventory repo present exactly once, nowhere duplicated."""
    inv = inventory()
    seen = {}
    for folder, mod in FOLDERS.items():
        for name in mod.REPOS:
            seen.setdefault(name, []).append(folder)
    missing = [n for n in inv if n not in seen]
    duplicated = {n: f for n, f in seen.items() if len(f) > 1}
    extra = [n for n in seen if n not in inv]
    return {
        "inventory_total": len(inv),
        "listed_total": sum(len(m.REPOS) for m in FOLDERS.values()),
        "missing": missing,
        "duplicated": duplicated,
        "extra": extra,
        "ok": not missing and not duplicated and not extra,
    }


def _value(folder, dotted):
    mod_name, var = dotted.split(".", 1)
    return getattr(FOLDERS[mod_name], var)


def check_links():
    """Resolve every LINKS entry. Returns a list of link records."""
    records = []
    for folder, mod in FOLDERS.items():
        for var, targets in mod.LINKS.items():
            mine = getattr(mod, var)
            for target in targets:
                theirs = _value(folder, target)
                records.append({
                    "from": f"{folder}.{var}",
                    "to": target,
                    "from_value": mine,
                    "to_value": theirs,
                    "ok": mine == theirs,
                })
    return records


def check_chain():
    """Resolve the chain: home -> each category -> its anchor repo."""
    steps = []
    for folder, anchor in CHAIN.items():
        repos = FOLDERS[folder].REPOS
        ok = anchor in repos and repos[anchor]["full_name"] == (
            f"{FOLDERS[folder].OWNER}/{anchor}")
        steps.append({
            "folder": folder,
            "anchor_repo": anchor,
            "full_name": repos.get(anchor, {}).get("full_name"),
            "home": FOLDERS[folder].HOME_PROFILE_REPO,
            "ok": bool(ok),
        })
    return all(s["ok"] for s in steps), steps


CHAIN = {
    "builds": "termux-site",
    "enterprise": "enterprise",
    "forks_ai": "nanoGPT",
    "forks_crypto": "go-ethereum",
    "forks_dev": "git",
    "forks_gov": "catalog.data.gov",
    "forks_misc": "core",
    "forks_payments": "braintree-web",
    "forks_space": "stellarium-web-engine",
    "forks_web": "wordpress",
    "home": "Jackblanket847",
    "learn": "hello-world",
    "sites": "mental-health-enterprise"
}


def filing():
    """The full filing: coverage, listings, link checks, chain check."""
    coverage = check_coverage()
    links = check_links()
    chain_ok, chain = check_chain()
    return {
        "home": FOLDERS["home"].HOME_PROFILE_REPO,
        "home_url": FOLDERS["home"].HOME_URL,
        "home_dev_url": FOLDERS["home"].HOME_DEV_URL,
        "counts": {c: len(FOLDERS[c].REPOS) for c in CATEGORIES},
        "coverage": coverage,
        "listings": listing(),
        "links": links,
        "links_ok": all(r["ok"] for r in links),
        "chain": chain,
        "chain_ok": chain_ok,
    }


if __name__ == "__main__":
    data = filing()
    print("repos — coded filing for the .profile home")
    print(f"home: {data['home']}")
    print(f"coverage: {data['coverage']['listed_total']}/"
          f"{data['coverage']['inventory_total']} repos, "
          f"missing={data['coverage']['missing']} "
          f"duplicated={data['coverage']['duplicated']} "
          f"extra={data['coverage']['extra']}")
    print(f"links: {sum(r['ok'] for r in data['links'])}/{len(data['links'])} hold")
    for r in data["links"]:
        mark = "OK  " if r["ok"] else "FAIL"
        print(f"  {mark} {r['from']} == {r['to']}")
    print(f"chain: {'OK' if data['chain_ok'] else 'FAIL'} "
          f"({sum(s['ok'] for s in data['chain'])}/{len(data['chain'])} steps)")
    for s in data["chain"]:
        mark = "OK  " if s["ok"] else "FAIL"
        print(f"  {mark} home -> {s['folder']} -> {s['anchor_repo']}")
    sys.exit(0 if data["coverage"]["ok"] and data["links_ok"]
             and data["chain_ok"] else 1)
