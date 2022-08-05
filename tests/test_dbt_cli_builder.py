import pytest
from dbt_run_configs import configs


@pytest.fixture
def get_test_configs() -> configs.RunConfig:
    import os
    return configs.parse_configs(os.path.join('.', 'test_dbt_run_config_user.yml')).run_configs[0]


def test_get_dbt_cli_command():
    from dbt_run_configs import dbt_cli_builder
    import os

    test_configs = configs.parse_configs(os.path.join('.', 'test_dbt_run_config_user.yml')).run_configs[0]
    expected_result = "dbt seed --full-refresh -m reference_mapping1 --target dev && " \
                      "dbt snapshot -m scd_model1 scd_model2 --target dev && " \
                      "dbt run -m model1 model2 model3+ --target dev && " \
                      "dbt test -m model1 --target dev"

    assert dbt_cli_builder.get_dbt_cli_command(test_configs) == expected_result
