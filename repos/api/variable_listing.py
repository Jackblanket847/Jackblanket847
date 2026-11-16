"""API variable listing: serves the repos chain over HTTP.

Stdlib only. No dependencies, no secrets, no live lookups — it
serves the coded filing in filing.py.

Endpoints:
  GET /                    index of endpoints
  GET /api/repos           all category listings
  GET /api/repos/<cat>     one category listing
  GET /api/filing          full filing: coverage + listings + links + chain
  GET /api/links           link check records only
  GET /api/inventory       the 500-repo inventory with categories

Run:  python3 api/variable_listing.py --port 8096
"""

import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import filing


def _payload():
    data = filing.filing()
    routes = {"/": {"endpoints": ["/", "/api/repos", "/api/repos/home", "/api/repos/enterprise", "/api/repos/builds", "/api/repos/sites", "/api/repos/learn", "/api/repos/forks_ai", "/api/repos/forks_crypto", "/api/repos/forks_gov", "/api/repos/forks_payments", "/api/repos/forks_space", "/api/repos/forks_dev", "/api/repos/forks_web", "/api/repos/forks_misc", "/api/filing", "/api/links", "/api/inventory"]},
              "/api/repos": data["listings"],
              "/api/filing": data,
              "/api/links": {"links": data["links"],
                             "links_ok": data["links_ok"],
                             "chain": data["chain"],
                             "chain_ok": data["chain_ok"]},
              "/api/inventory": filing.inventory()}
    for cat in filing.CATEGORIES:
        routes[f"/api/repos/{cat}"] = data["listings"][cat]
    return routes


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = _payload()
        path = self.path.split("?", 1)[0].rstrip("/") or "/"
        if path in routes:
            body = json.dumps(routes[path], indent=2, default=str).encode()
            self.send_response(200)
        else:
            body = json.dumps({"error": "not found", "path": self.path}).encode()
            self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8096)
    ap.add_argument("--host", default="127.0.0.1")
    args = ap.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"api.variable.listing on http://{args.host}:{args.port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
