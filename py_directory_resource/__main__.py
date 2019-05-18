# -*- coding: utf-8 -*-
import argparse
import sys

from py_directory_resource import DirectoryResource


def main():
    parser = argparse.ArgumentParser(
        prog="py_directory_resource", description="ディレクトリを作成または削除します。")
    parser.add_argument("path", help="操作対象とするディレクトリのパスを指定します。")
    parser.add_argument("--create", action="store_true",
                        default=False, help="ディレクトリを作成します。")
    parser.add_argument("--delete", action="store_true",
                        default=False, help="ディレクトリを削除します。")
    parser.add_argument("--get-list", action="store_true",
                        default=False, help="ファイル / ディレクトリの一覧を表示します。")

    args = parser.parse_args()
    dr = DirectoryResource(args.path)

    if args.delete:
        dr.delete()
        sys.exit(dr.code)
    elif args.create:
        dr.create()
        sys.exit(dr.code)
    elif args.get_list:
        files = dr.get_files()

        if files:
            for file in files:
                print file

        sys.exit(dr.code)


if __name__ == "__main__":
    main()
