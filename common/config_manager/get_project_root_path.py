import os


def get_root_path():
    cwd = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.abspath(os.path.join(cwd, '../..'))
    return root_path
