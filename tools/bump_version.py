#!/usr/bin/env python3

from pathlib import Path
import argparse
import re
import subprocess
import sys

REPO_DIR = Path(__file__).resolve().parent.parent


SETUP_CFG = REPO_DIR / 'setup.cfg'
CHANGELOG = REPO_DIR / 'CHANGELOG.md'

VERSION_RX = r'version = (\d+\.\d+\.\d+)'


def get_current_version() -> str:
    with SETUP_CFG.open('r') as f:
        content = f.read()

    match = re.search(VERSION_RX, content)
    if match is None:
        sys.exit('Unable to find current version')
    return match[1]


def bump_setup_cfg(current_version: str, new_version: str) -> None:
    with SETUP_CFG.open('r', encoding='utf8') as f:
        content = f.read()

    content = content.replace(current_version, new_version, 1)

    with SETUP_CFG.open('w', encoding='utf8') as f:
        f.write(content)


def make_changelog(new_version: str) -> None:

    cmd = [
        'git-chglog',
        '--next-tag',
        new_version
    ]

    result = subprocess.run(cmd,
                            cwd=REPO_DIR,
                            text=True,
                            check=True,
                            capture_output=True)

    changes = result.stdout
    changes = changes.removeprefix('\n')

    current_changelog = CHANGELOG.read_text()

    with CHANGELOG.open('w') as f:
        f.write(changes + current_changelog)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bump Version')
    parser.add_argument('version', help='The new version, e.g. 1.5.0')
    args = parser.parse_args()

    current_version = get_current_version()
    bump_setup_cfg(current_version, args.version)
    make_changelog(args.version)
