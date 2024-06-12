import json
from argparse import ArgumentParser
from constants import CATALOGUE_FOLDER, META_FOLDER, GHPROXY_URL, CREATE_LZMA, CREATE_GZ, COMPACT
from collections import namedtuple

import os
import typing as ty

import gzip
import lzma

from contextlib import contextmanager


WalkedDir = namedtuple('WalkedDir', 'dirpath dirnames filenames')
Iterable = ty.Optional[ty.Iterable]


@contextmanager
def open_for_write(file_path: str):
    """
    Just like open() in 'w' mode, but create the directory automatically
    """
    dir_path = os.path.dirname(file_path)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    with open(file_path, 'w', encoding='utf8') as file:
        yield file


def save_json(data: dict, file_path: str, *, compact: bool = False, with_gz: bool = False, with_xz: bool = False):
    if compact:
        s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    else:
        s = json.dumps(data, indent=2, ensure_ascii=False)

    with open_for_write(file_path) as f:
        f.write(s)
    if with_gz:
        with gzip.GzipFile(file_path + '.gz', 'wb', mtime=0) as zf:
            zf.write(s.encode('utf8'))
    if with_xz:
        with lzma.open(file_path + '.xz', 'wb', format=lzma.FORMAT_XZ) as xf:
            xf.write(s.encode('utf8'))


def _update(folder, included_suffixes: Iterable = None, excluded_prefixes: Iterable = None):
    return __walk_n_process(
        folder, __update,
        included_suffixes=included_suffixes, excluded_prefixes=excluded_prefixes
    )


def __update(matched: bool, path: str):
    if not matched:
        print(f'Excluded {path}')
        return
    print(f'Processing {path}...')

    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)
    result_data = recursively_add_ghproxy_prefix(data)

    file_name = os.path.basename(path)
    save_json(result_data, path, compact=file_name in COMPACT, with_gz=file_name in CREATE_GZ, with_xz=file_name in CREATE_LZMA)


def __walk_n_process(folder, func: ty.Callable[[bool, str], ty.Any], included_suffixes: Iterable = None, excluded_prefixes: Iterable = None):
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
            func(matched, path)


def recursively_add_ghproxy_prefix(data: ty.Union[dict, list, ty.Any]):
    if isinstance(data, dict):
        result_dict = {}
        for k, v in data.items():
            if k == "browser_download_url" and isinstance(v, str):
                result_dict[k] = GHPROXY_URL + v
            else:
                result_dict[k] = recursively_add_ghproxy_prefix(v)
        return result_dict
    elif isinstance(data, list):
        result_list = []
        for item in data:
            result_list.append(recursively_add_ghproxy_prefix(item))
        return result_list
    else:
        return data


def update_data():
    print('Processing meta branch')
    _update(META_FOLDER, included_suffixes=['.json'], excluded_prefixes=['.'])


def update_doc():
    print('Processing catalogue branch')
    _update(CATALOGUE_FOLDER, included_suffixes=['.md'])


def _remove(folder, included_suffixes: Iterable = None, excluded_prefixes: Iterable = None):
    __walk_n_process(
        folder, __remove,
        included_suffixes=included_suffixes, excluded_prefixes=excluded_prefixes
    )


def __remove(match: bool, path: str):
    if match:
        print(f"Removing file {path}")
        os.remove(path)


def remove_meta_archives():
    print("Remove LZMA and GZ files...")
    _remove(META_FOLDER, included_suffixes=['.xz', '.gz'])


def main():
    parser = ArgumentParser(
        prog='python manager', description='Plugin Catalogue (GitHub Proxy Accelerated) Manager'
    )

    subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
    subparsers.add_parser('meta', help='Update meta branch')
    subparsers.add_parser('doc', help="Update documents in catalogue branch")

    args = parser.parse_args()
    if args.subparser_name == 'meta':
        update_data()
    elif args.subparser_name == 'remove':
        remove_meta_archives()
    elif args.subparser_name == 'doc':
        update_doc()


if __name__ == "__main__":
    main()
