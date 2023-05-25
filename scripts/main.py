import json
from argparse import ArgumentParser
from constants import CATALOGUE_FOLDER, META_FOLDER, MAPPING_FILE
from collections import namedtuple

import os
import typing as ty


WalkedDir = namedtuple('WalkedDir', 'dirpath dirnames filenames')
Iterable = ty.Optional[ty.Iterable]


def __update(folder, included_suffixes: Iterable = None, excluded_prefixes: Iterable = None):
    if included_suffixes is None:
        included_suffixes = []
    if excluded_prefixes is None:
        excluded_prefixes = []

    for folder in os.walk(folder):
        folder = WalkedDir(*folder)
        for file in folder.filenames:  # type: str
            matched = True
            for suf in included_suffixes:
                if not file.endswith(suf):
                    matched = False
            for pre in excluded_prefixes:
                if file.startswith(pre):
                    matched = False

            path = os.path.join(folder.dirpath, file)
            if not matched:
                print(f'Excluded {path}')
                continue

            print(f'Processing {file}...')
            with open(MAPPING_FILE, 'r', encoding='utf8') as f:
                to_replace: dict = json.load(f)

            path = os.path.join(folder.dirpath, file)
            with open(path, 'r', encoding='utf8') as f:
                data = f.read()

            for old, new in to_replace.items():
                data = data.replace(old, new)

            with open(path, 'w', encoding='utf8') as f:
                f.write(data)


def update_data():
    print('Processing meta branch')
    __update(META_FOLDER, included_suffixes=['.json'], excluded_prefixes=['.'])


def update_doc():
    print('Processing catalogue branch')
    __update(CATALOGUE_FOLDER, included_suffixes=['.md'])


def main():
    parser = ArgumentParser(
        prog='python manager', description='Plugin Catalogue (FastGit Accelerated) Manager'
    )

    subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
    subparsers.add_parser('meta', help='Update meta branch')
    subparsers.add_parser('doc', help="Update documents in catalogue branch")

    args = parser.parse_args()
    if args.subparser_name == 'meta':
        update_data()
    elif args.subparser_name == 'doc':
        update_doc()


if __name__ == "__main__":
    main()
