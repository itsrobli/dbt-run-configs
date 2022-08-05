from dbt_run_configs.configs import RunConfig

DBT_RUN_COMMAND = 'dbt run'
DBT_TEST_COMMAND = 'dbt test'
DBT_SEED_COMMAND = 'dbt seed --full-refresh'
DBT_SNAPSHOT_COMMAND = 'dbt snapshot'
DBT_MODEL_SELECTION = ' -m '
DBT_TARGET_SELECTION = ' --target '


def get_dbt_cli_command(run_configs: RunConfig) -> str:
    # Create all the parts and then concatenate with ' && ' at the end
    run_command_parts = []

    # dbt seed
    if run_configs.seed is not None:
        seed_command = ''
        seed_models_string = ''
        if run_configs.seed.only is not None:
            seed_models_string = ' '.join(run_configs.seed.only)
            seed_models_string = DBT_MODEL_SELECTION + seed_models_string
        if run_configs.seed.all is True:
            seed_models_string = ''
        seed_command += f"{DBT_SEED_COMMAND}{seed_models_string}" \
                        f"{DBT_TARGET_SELECTION}{run_configs.target}"
        run_command_parts.append(seed_command)

    # dbt snapshot, an optional field to be included in config
    if run_configs.snapshot_models is not None:
        snapshot_command = ''
        snapshot_models_string = ''
        if run_configs.snapshot_models.only is not None:
            snapshot_models_string = ' '.join(run_configs.snapshot_models.only)
            snapshot_models_string = DBT_MODEL_SELECTION + snapshot_models_string
        if run_configs.snapshot_models.all is True:
            snapshot_models_string = ''
        snapshot_command += f"{DBT_SNAPSHOT_COMMAND}{snapshot_models_string}" \
                            f"{DBT_TARGET_SELECTION}{run_configs.target}"
        run_command_parts.append(snapshot_command)

    # dbt run
    if run_configs.models is not None:
        run_models_command = ''
        models_string = ' '.join(run_configs.models)
        run_models_command += f"{DBT_RUN_COMMAND}{DBT_MODEL_SELECTION}{models_string}" \
                              f"{DBT_TARGET_SELECTION}{run_configs.target}"
        run_command_parts.append(run_models_command)

    # dbt test
    if run_configs.test_models is not None:
        test_command = ''
        test_models_string = ' '.join(run_configs.test_models)
        test_command += f"{DBT_TEST_COMMAND}{DBT_MODEL_SELECTION}{test_models_string}" \
                        f"{DBT_TARGET_SELECTION}{run_configs.target}"
        run_command_parts.append(test_command)
    return ' && '.join(run_command_parts)
