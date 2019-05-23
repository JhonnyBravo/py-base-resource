# -*- coding: utf-8 -*-
"""
基本動作を定義する。
"""
from abc import abstractmethod
import abc


class BaseResource(object):
    """
    基本動作を定義する抽象基底クラス。
    """
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def create(self):
        """
        ファイルまたはディレクトリを作成する。
        """
        pass

    @abstractmethod
    def delete(self):
        """
        ファイルまたはディレクトリを削除する。
        """
        pass

    @abstractmethod
    def set_owner(self, owner_name):
        """
        ファイルまたはディレクトリの所有者を変更する。

        :param str owner_name: 新しい所有者として設定するユーザの名前を指定する。
        """
        pass

    @abstractmethod
    def set_group(self, group_name):
        """
        ファイルまたはディレクトリのグループ所有者を変更する。

        :param str group_name: 新しいグループ所有者として設定するグループの名前を指定する。
        """
        pass

    @abstractmethod
    def set_mode(self, mode):
        """
        ファイルまたはディレクトリのパーミッション設定を変更する。

        :param int mode: 新しく設定するパーミッションの値を 4 桁の 8 進数で指定する。
        """
        pass
