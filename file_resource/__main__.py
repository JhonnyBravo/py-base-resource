# -*- coding: utf-8 -*-
"""
ファイルの作成 / 削除を CLI から実行する。
"""
import argparse
import sys

from file_resource import FileResource


def main():
    """
    .. program:: file_resource

    ファイルの作成 / 削除を CLI から実行する。

    .. option:: path

        操作対象とするファイルのパスを指定する。

    .. option:: --create

        ファイルを作成する。

    .. option:: --delete

        ファイルを削除する。

    .. option:: update <content>

        ファイルの内容を上書きする。

    .. option:: append <content>

        ファイルへ新しい文字列を追記する。

    .. option:: read

        ファイルを読込み、内容をコンソールへ出力する。

    .. encoding <encoding>

        ファイル読込時に使用する文字エンコーディングを指定する。
    """
    parser = argparse.ArgumentParser(
        prog="file_resource", description="ファイルを作成または削除します。")
    parser.add_argument("path", help="操作対象とするファイルのパスを指定します。")
    parser.add_argument("--create", action="store_true",
                        default=False, help="ファイルを作成します。")
    parser.add_argument("--delete", action="store_true",
                        default=False, help="ファイルを削除します。")
    parser.add_argument("--update", metavar="content",
                        help="既存ファイルの内容を上書きします。")
    parser.add_argument("--append", metavar="content", help="既存ファイルへ追記します。")
    parser.add_argument("--read", action="store_true",
                        default=False, help="ファイルの内容を出力します。")
    parser.add_argument("--encoding", metavar="encoding", help="文字コードを指定します。")

    args = parser.parse_args()
    fr = FileResource(args.path)

    if args.delete:
        fr.delete()
        sys.exit(fr.code)
    elif args.read:
        content = fr.read_content(args.encoding)

        if content:
            for line in content:
                line = line.replace("\r", "")
                line = line.replace("\n", "")
                print line

        sys.exit(fr.code)

    if args.create:
        fr.create()

    if fr.code == 1:
        sys.exit(fr.code)

    if args.update:
        fr.set_content(args.update)
    elif args.append:
        fr.append_content(args.append)

    sys.exit(fr.code)


if __name__ == "__main__":
    main()
