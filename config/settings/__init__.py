try:
    from .env import *
except ImportError as exc:
    raise ImportError(
        "\n***********************************************\n"
        "Couldn't import the environment file for Market API \n"
        "Env file should exists on (config/settings/env.py) \n"
        "You should create a env file first\n"
        "***********************************************\n"
    ) from exc
