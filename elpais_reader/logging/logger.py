import logging.config
import pathlib

import yaml


def configure() -> None:
    logging.config.dictConfig(config=_config())


def _config() -> dict:
    with open(_filepath(), "r") as f:
        return yaml.safe_load(f.read())


def _filepath() -> str:
    module_path = pathlib.Path(__file__).parent.absolute()
    result = module_path.joinpath("config.yaml")
    return str(result)
