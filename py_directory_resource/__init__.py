# -*- coding: utf-8 -*-
"""
ディレクトリの操作を管理する。
"""
import os

from py_status_resource import StatusResource


class DirectoryResource(StatusResource):
    """
    ディレクトリの操作を管理する。
    """

    def __init__(self, path):
        """
        :param str path: 操作対象とするディレクトリのパスを指定する。
        """
        StatusResource.__init__(self)
        self.__path = path

    @property
    def path(self):
        """
        :return: 操作対象とするディレクトリのパスを返す。
        :rtype: str
        """
        return self.__path

    def create(self):
        """
        ディレクトリを作成する。
        """
        if not os.path.isdir(self.path):
            self.print_message(0, self.path + " を作成しています。")
            os.makedirs(self.path)
            self.code = 2
        else:
            self.code = 0

    def delete(self):
        """
        ディレクトリを削除する。
        """
        if os.path.isdir(self.path):
            self.print_message(0, self.path + " を削除しています。")
            os.removedirs(self.path)
            self.code = 2
        else:
            self.code = 0

    def get_files(self):
        """
        :return: ファイル / ディレクトリの一覧を返す。
        :rtype: list
        """
        files = []

        if not os.path.isdir(self.path):
            self.print_message(1, self.path + " が見つかりません。")
            return files

        files = os.listdir(self.path)

        if files:
            self.code = 2
        else:
            self.code = 0

        return files
