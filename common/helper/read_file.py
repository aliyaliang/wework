from os.path import join
import yaml
from common.config_manager.get_project_root_path import get_root_path


def read_txt_file(file_path="testdata/repos_data/graphql/git_tree", is_absolute_path=False):
    if not is_absolute_path:
        file_path = join(get_root_path(), file_path)
    with open(file_path, "r") as f:
        data = f.read()
    return data


def read_yaml(file_path="conf.yaml"):
    file_path = join(get_root_path(), file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return yaml_data

