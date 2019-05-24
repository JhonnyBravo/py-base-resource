# -*- coding: utf-8 -*-
"""
ディレクトリの作成 / 削除を CLI から実行する。
"""
import argparse
import sys

from py_base_resource.py_directory_resource import DirectoryResource


def main():
    """
    .. program:: py_directory_resource

    ディレクトリの作成 / 削除を CLI から実行する。

    .. option:: path

        操作対象とするディレクトリのパスを指定する。

    .. option:: --create

        ディレクトリを作成する。

    .. option:: --delete

        ディレクトリを削除する。

    .. option:: --get-list

        ディレクトリの配下に存在するファイルとディレクトリの一覧を表示する。

    .. option:: --owner <user_name>

        ディレクトリの所有者を変更する。

    .. option:: --group <group_name>

        ディレクトリのグループ所有者を変更する。

    .. option:: --mode <mode>

        ディレクトリのパーミッション設定を変更する。
    """
    parser = argparse.ArgumentParser(
        prog="py_directory_resource", description="ディレクトリを作成または削除します。")
    parser.add_argument("path", help="操作対象とするディレクトリのパスを指定します。")
    parser.add_argument("--create", action="store_true",
                        default=False, help="ディレクトリを作成します。")
    parser.add_argument("--delete", action="store_true",
                        default=False, help="ディレクトリを削除します。")
    parser.add_argument("--get-list", action="store_true",
                        default=False, help="ファイル / ディレクトリの一覧を表示します。")
    parser.add_argument("--owner", metavar="user_name",
                        help="ディレクトリの所有者を変更します。")
    parser.add_argument("--group", metavar="group_name",
                        help="ディレクトリのグループ所有者を変更します。")
    parser.add_argument("--mode", metavar="mode",
                        help="ディレクトリのパーミッション設定を変更します。")

    args = parser.parse_args()
    dr = DirectoryResource(args.path)

    if args.delete:
        dr.delete()
        sys.exit(dr.code)
    elif args.get_list:
        files = dr.get_files()

        if files:
            for file in files:
                print file

        sys.exit(dr.code)

    if args.create:
        dr.create()

        if dr.code == 1:
            sys.exit(dr.code)

    if args.owner:
        dr.set_owner(args.owner)

        if dr.code == 1:
            sys.exit(dr.code)

    if args.group:
        dr.set_group(args.group)

        if dr.code == 1:
            sys.exit(dr.code)

    if args.mode:
        dr.set_mode(int(args.mode, 8))

    sys.exit(dr.code)


if __name__ == "__main__":
    main()
