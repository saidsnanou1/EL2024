import os


def get_environment_variable(variable_name):
    value = os.environ.get(variable_name)
    if value is not None:
        print(f"The value of the {variable_name} environment variable is: {value}")
    else:
        print(f"The environment variable {variable_name} is not set.")
    return value


variable_name = "PATH"
get_environment_variable(variable_name)
