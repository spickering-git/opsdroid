"""Constants used by OpsDroid."""
import os

__version__ = "0.10.0"

DEFAULT_GIT_URL = "https://github.com/opsdroid/"
MODULES_DIRECTORY = "opsdroid-modules"
DEFAULT_ROOT_PATH = os.path.expanduser("~/.opsdroid")
DEFAULT_LOG_FILENAME = os.path.join(DEFAULT_ROOT_PATH, 'output.log')
DEFAULT_MODULES_PATH = os.path.join(DEFAULT_ROOT_PATH, "modules")
DEFAULT_MODULE_DEPS_PATH = os.path.join(DEFAULT_ROOT_PATH, "site-packages")
DEFAULT_CONFIG_PATH = os.path.join(DEFAULT_ROOT_PATH, "configuration.yaml")
DEFAULT_MODULE_BRANCH = "master"
EXAMPLE_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "configuration/example_configuration.yaml")
REGEX_MAX_SCORE = 0.6
DIALOGFLOW_API_ENDPOINT = "https://api.dialogflow.com/v1/query"
DIALOGFLOW_API_VERSION  = "20150910"
LUISAI_API_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/"
RECASTAI_API_ENDPOINT = "https://api.recast.ai/v2/request"
WITAI_API_ENDPOINT = "https://api.wit.ai/message"
WITAI_API_VERSION = "20170307"