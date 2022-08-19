import dbt_run_configs.configs
import dbt_cli_builder
import click


@click.command()
@click.option('--name', default=None, help='Config name in user_space/dbt_run_config_user.yml.')
def run_config(name):
    configs = dbt_run_configs.configs.parse_configs().run_configs
    run_config = next(filter(lambda config: config.name == name, configs))
    run_command = dbt_cli_builder.get_dbt_cli_command(run_config)
    print(run_command)


if __name__ == '__main__':
    run_config()
