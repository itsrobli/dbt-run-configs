from __future__ import annotations
from typing import List, Optional
from pydantic import AnyUrl, BaseModel, Field
import yaml
import os
import sys
import shutil


class RunConfigSwitch(BaseModel):
    all: bool
    only: Optional[List[str]]


class RunConfig(BaseModel):
    name: str
    target: str
    models: Optional[List[str]]
    test_models: Optional[List[str]]
    snapshot_models: Optional[RunConfigSwitch]
    seed: Optional[RunConfigSwitch]


class Configs(BaseModel):
    version: str
    name: str
    run_configs: List[RunConfig]


def parse_configs() -> Configs:
    config_file_path_template = os.path.join('dbt_run_configs', 'dbt_run_config_template.yml')
    config_file_path_user = os.path.join('user_space', 'dbt_run_config_user.yml')
    if not os.path.exists(config_file_path_user):
        print(f'First time setup.\n'
              f'Creating {config_file_path_user}')
        shutil.copyfile(config_file_path_template, config_file_path_user)
        print(
            f'Done. Edit your configs in: {config_file_path_user} and run this script again.\n')
        sys.exit()
    with open(config_file_path_user) as config_file:
        obj = yaml.load(config_file, Loader=yaml.FullLoader)
        return Configs.parse_obj(obj)
