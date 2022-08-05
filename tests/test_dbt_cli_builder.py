import pytest
from dbt_run_configs import configs


def get_test_input_configs() -> [configs.RunConfig]:
    import os
    return configs.parse_configs(
        os.path.join('.', 'test_sample_dbt_run_config_user.yml')).run_configs


def get_test_expected_outputs() -> [str]:
    expected_result_1 = "dbt seed --full-refresh -m reference_mapping1 --target dev && " \
                        "dbt snapshot -m scd_model1 scd_model2 --target dev && " \
                        "dbt run -m model1 model2 model3+ --target dev && " \
                        "dbt test -m model1 --target dev"
    return [expected_result_1]


@pytest.mark.parametrize("test_input, expected",
                         zip(get_test_input_configs(),
                             get_test_expected_outputs()))
def test_get_dbt_cli_command(test_input, expected):
    from dbt_run_configs import dbt_cli_builder

    assert dbt_cli_builder.get_dbt_cli_command(test_input) == expected
