import os
from typing import Text


def get_root_path():
    cwd = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.abspath(os.path.join(cwd, '../..'))
    return root_path


def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return get_root_path() + path
