import os
from dotenv import dotenv_values

REQUIRED_ENV_VALUES = ("GITHUB_TOKEN", "GITHUB_REPO")


class MissingEnvVarException(Exception):
    def __init__(self, missing_env_var_keys: tuple[str]):
        super().__init__(
            f"Missing environment variable(s) defined in env.py: {missing_env_var_keys}"
        )


def validate_required_env(env):
    missing = list(filter(lambda k: env.get(k) is None, REQUIRED_ENV_VALUES))

    if len(missing) > 0:
        print("Missing env vars", missing)
        # raise MissingEnvVarException(missing)

    return env


env = validate_required_env({**dotenv_values(), **os.environ})
