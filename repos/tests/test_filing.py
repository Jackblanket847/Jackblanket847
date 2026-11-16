"""Tests for the repos coded filing and the API variable listing."""

import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import filing
from api import variable_listing


class FilingTests(unittest.TestCase):
    def test_all_categories_present(self):
        data = filing.listing()
        self.assertEqual(set(data), set(filing.CATEGORIES))
        for folder in data:
            self.assertTrue(data[folder], f"{folder} listing is empty")

    def test_coverage_is_500_exactly_once(self):
        cov = filing.check_coverage()
        self.assertTrue(cov["ok"], f"coverage broken: {cov}")
        self.assertEqual(cov["inventory_total"], 500)
        self.assertEqual(cov["listed_total"], 500)
        self.assertEqual(cov["missing"], [])
        self.assertEqual(cov["duplicated"], {})
        self.assertEqual(cov["extra"], [])

    def test_owned_forks_split(self):
        inv = filing.inventory()
        owned = [n for n, r in inv.items() if r["kind"] == "owned"]
        forks = [n for n, r in inv.items() if r["kind"] == "fork"]
        self.assertEqual(len(owned), 86)
        self.assertEqual(len(forks), 414)

    def test_every_link_holds(self):
        links = filing.check_links()
        self.assertTrue(links)
        broken = [r for r in links if not r["ok"]]
        self.assertEqual(broken, [], f"broken links: {broken}")

    def test_chain_resolves(self):
        ok, steps = filing.check_chain()
        self.assertTrue(ok, f"chain broken: {[s for s in steps if not s['ok']]}")
        self.assertEqual(len(steps), len(filing.CATEGORIES))

    def test_every_repo_url_is_yours(self):
        for folder, repos in filing.listing().items():
            for name, rec in repos.items():
                self.assertTrue(
                    rec["url"].startswith("https://github.com/Jackblanket847/"),
                    f"{folder}/{name}: {rec['url']}")
                self.assertEqual(rec["full_name"], f"Jackblanket847/{name}")

    def test_home_anchor_agrees_everywhere(self):
        for folder in filing.CATEGORIES:
            mod = filing.FOLDERS[folder]
            self.assertEqual(mod.HOME_PROFILE_REPO, "Jackblanket847/Jackblanket847")
            self.assertEqual(mod.OWNER, "Jackblanket847")
            self.assertEqual(mod.HOME_URL,
                             "https://github.com/Jackblanket847/Jackblanket847")
            self.assertEqual(mod.HOME_DEV_URL,
                             "https://github.dev/Jackblanket847/Jackblanket847")

    def test_connections_json_matches_filing(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(root, "connections.json")) as f:
            manifest = json.load(f)
        self.assertEqual(manifest["repo"], "Jackblanket847/Jackblanket847")
        self.assertEqual(manifest["totals"]["repos"], 500)
        self.assertEqual(manifest["totals"]["owned"], 86)
        self.assertEqual(manifest["totals"]["forks"], 414)
        self.assertEqual(manifest["folders"], filing.CATEGORIES)
        self.assertEqual(len(manifest["connections"]),
                         len(filing.CATEGORIES) - 1)


class ApiTests(unittest.TestCase):
    def test_payload_has_every_route(self):
        routes = variable_listing._payload()
        self.assertIn("/", routes)
        self.assertIn("/api/repos", routes)
        self.assertIn("/api/filing", routes)
        self.assertIn("/api/links", routes)
        self.assertIn("/api/inventory", routes)
        for cat in filing.CATEGORIES:
            self.assertIn(f"/api/repos/{cat}", routes)

    def test_filing_route_reports_all_ok(self):
        data = variable_listing._payload()["/api/filing"]
        self.assertTrue(data["coverage"]["ok"])
        self.assertTrue(data["links_ok"])
        self.assertTrue(data["chain_ok"])

    def test_inventory_route_has_500(self):
        inv = variable_listing._payload()["/api/inventory"]
        self.assertEqual(len(inv), 500)


if __name__ == "__main__":
    unittest.main(verbosity=2)
