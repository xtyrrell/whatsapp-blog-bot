from typing import Literal, Type
from dotenv import dotenv_values

REQUIRED_ENV_VALUES = ("GITHUB_TOKEN", "GITHUB_REPO")


class MissingEnvVarException(Exception):
    def __init__(self, missing_env_var_keys: tuple[str]):
        super().__init__(
            f"Missing environment variable(s) defined in env.py: {missing_env_var_keys}"
        )


def validate_required_env(env: dict[str, str | None]):
    missing = filter(lambda k: env.get(k) is None, REQUIRED_ENV_VALUES)

    if len(list(missing)) > 0:
        raise MissingEnvVarException(missing)

    return env


env = validate_required_env(dotenv_values())
