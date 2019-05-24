# -*- coding: utf-8 -*-
"""
ディレクトリの操作を管理する。
"""
import os

from py_attribute_resource.py_group_resource import GroupResource
from py_attribute_resource.py_mode_resource import ModeResource
from py_attribute_resource.py_owner_resource import OwnerResource
from py_base_resource import BaseResource
from py_status_resource import StatusResource


class DirectoryResource(StatusResource, BaseResource):
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

    def set_owner(self, owner_name):
        """
        ディレクトリの所有者を変更する。

        :param str owner_name: 新しい所有者として設定するユーザの名前を指定する。
        """
        resource = OwnerResource(self.path)
        resource.set_attribute(owner_name)
        self.code = resource.code

    def set_group(self, group_name):
        """
        ディレクトリのグループ所有者を変更する。

        :param str group_name: 新しいグループ所有者として設定するグループの名前を指定する。
        """
        resource = GroupResource(self.path)
        resource.set_attribute(group_name)
        self.code = resource.code

    def set_mode(self, mode):
        """
        ディレクトリのパーミッション設定を変更する。

        :param int mode: 新しく設定するパーミッション値を 4 桁の 8 進数で指定する。
        """
        resource = ModeResource(self.path)
        resource.set_attribute(mode)
        self.code = resource.code
