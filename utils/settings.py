import re
import os
from pathlib import Path
# BUTTONS
REPAIR = "4"
CRAFT_ITEM = "5"
FOOD_KEY = ""
POTION_KEY = ""

# SETTINGS
REPAIR_COUNTER = 85
TIME_PADDING_0 = 3 # Time padding for in between pressing keys

# MISC
RE_WAIT = re.compile(r"<wait.(.+?)>")
RE_KEY = re.compile(r"KEY")
MACRO_TIME_PAD = 3 # Time padding for misclicks on macro
BEFORE_KEY = 1 # If laggy in game, make this higher
AFTER_COLLECT_MENU = 2
FILENAME_MACROS = ".profiles.json"
FILENAME_LOGS = ".logs.json"
CWDPATH = os.getcwd()
ABSPATH = os.path.dirname(os.path.realpath(__file__))
PROFILES_PATH = os.path.join(Path(ABSPATH).parent, FILENAME_MACROS)
LOGS_PATH = os.path.join(Path(ABSPATH).parent, FILENAME_LOGS)
MACROS_FOLDER = "macros"
FLAGS = ["-repair", "-food", "-pot"]
PROFILES = {}
LOGS = {}

# MESSAGES
PROMPT = " > "
SELECT_MACRO = f"Macro profile name:\n{PROMPT}"
CRAFT_AMT = f"\nHow many crafts?\n{PROMPT}"
FLAGS_LIST = f"\nAvailable options: {FLAGS}\nLeave blank if none\n{PROMPT}"
DELETE_MACRO = f"Which macro do you want to delete?\n{PROMPT}"
CREATE_MACRO = f"What is the filename in the macros folder?\n{PROMPT}"