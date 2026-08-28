#!/usr/bin/env python3
"""Serve the lessons and their shared static dependencies on a local LAN."""

from __future__ import annotations

import argparse
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ALLOWED_ROOTS = {
    "lessons": PROJECT_ROOT / "lessons",
    "assets": PROJECT_ROOT / "assets",
    "reference": PROJECT_ROOT / "reference",
}
NOT_FOUND = PROJECT_ROOT / ".lesson-server-not-found"


class LessonHandler(SimpleHTTPRequestHandler):
    """Map only the course's public directories into the HTTP namespace."""

    def translate_path(self, url_path: str) -> str:
        path = unquote(urlsplit(url_path).path)
        parts = [part for part in path.split("/") if part]
        if not parts or parts[0] not in ALLOWED_ROOTS:
            return str(NOT_FOUND)

        root = ALLOWED_ROOTS[parts[0]].resolve()
        candidate = (root.joinpath(*parts[1:])).resolve()
        if candidate != root and root not in candidate.parents:
            return str(NOT_FOUND)
        return str(candidate)

    def do_GET(self) -> None:
        path = urlsplit(self.path).path
        if path in ("", "/"):
            self.send_response(302)
            self.send_header("Location", "/lessons/")
            self.end_headers()
            return
        if path in ("/lessons", "/assets", "/reference"):
            self.send_response(301)
            self.send_header("Location", f"{path}/")
            self.end_headers()
            return
        super().do_GET()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0", help="interface to bind (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="TCP port (default: 8000)")
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), LessonHandler)
    print(f"Serving lessons on http://{args.host}:{args.port}/lessons/ (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
