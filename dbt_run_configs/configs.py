from __future__ import annotations
from typing import List, Optional
from pydantic import AnyUrl, BaseModel, Field
import yaml
import os


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
    config_file_path = os.path.join('dbt_run_configs', 'dbt_run_config_template.yml')
    with open(config_file_path) as config_file:
        obj = yaml.load(config_file, Loader=yaml.FullLoader)
        return Configs.parse_obj(obj)
