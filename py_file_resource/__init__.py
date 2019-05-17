# -*- coding: utf-8 -*-
"""
ファイルの操作を管理する。
"""
import codecs
import os
import sys

from py_status_resource import StatusResource


class FileResource(StatusResource):
    """
    ファイルの操作を管理する。
    """

    def __init__(self, path):
        """
        :param str path: 操作対象とするファイルのパスを指定する。
        """
        StatusResource.__init__(self)
        self.__path = path

    @property
    def path(self):
        """
        :return: 操作対象とするファイルのパスを返す。
        :rtype: str
        """
        return self.__path

    def create(self):
        """
        ファイルを作成する。
        """
        if not os.path.isfile(self.path):
            self.print_message(0, self.path + " を作成しています。")
            with open(self.path, "w"):
                self.code = 2
        else:
            self.code = 0

    def set_content(self, content):
        """
        既存ファイルの内容を上書きする。

        :param str content: ファイルへ書き込む文字列を指定する。
        """
        if not os.path.isfile(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return

        self.print_message(0, self.path + " を上書きしています。")

        with open(self.path, "wt") as file:
            file.write(content + "\n")
            self.code = 2

    def append_content(self, content):
        """
        既存ファイルへ追記する。

        :param str content: ファイルへ追記する文字列を指定する。
        """
        if not os.path.isfile(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return

        self.print_message(0, self.path + " へ追記しています。")

        with open(self.path, "at") as file:
            file.write(content + "\n")
            self.code = 2

    def read_content(self, encoding=""):
        """
        ファイルの内容を読込む。

        :param str encoding: 読込時に使用する文字コードを指定する。
        :return: ファイルの内容を納めたリストを返す。
        :rtype: list
        """
        content = []

        if not os.path.isfile(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return content

        self.print_message(0, self.path + " を読込んでいます。")

        if not encoding:
            with codecs.open(self.path, "r", sys.getdefaultencoding()) as file:
                content = file.readlines()
        else:
            with codecs.open(self.path, "r", encoding) as file:
                content = file.readlines()

        if content:
            self.code = 2
        else:
            self.code = 0

        return content

    def delete(self):
        """
        ファイルを削除する。
        """
        if os.path.isfile(self.path):
            self.print_message(0, self.path + " を削除しています。")
            os.remove(self.path)
            self.code = 2
        else:
            self.code = 0
