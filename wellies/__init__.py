# flake8: noqa

from .config import (concatenate_yaml_files, get_parser, get_user_globals,
                     overwrite_entries, parse_execution_contexts,
                     parse_yaml_files, substitute_variables)
from .data import DeployDataFamily, StaticDataStore
from .deployment import deploy_suite
from .hosts import get_host
from .tasks import EcfResourcesTask
from .tools import DeployToolsFamily, ToolStore

try:
    # NOTE: the `_version.py` file must not be present in the git repository
    #   as it is generated by setuptools at install time
    from ._version import __version__
except ImportError:  # pragma: no cover
    # Local copy or not installed with setuptools
    __version__ = ""