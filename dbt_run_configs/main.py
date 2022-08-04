from dbt_run_configs import configs


def print_hi(name):
    print(configs.parse_configs())


if __name__ == '__main__':
    print_hi('World')


