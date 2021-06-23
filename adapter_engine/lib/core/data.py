from adapter_engine.lib.core.datatype import AttribDict

# logger
from adapter_engine.lib.core.log import LOGGER

logger = LOGGER
# object to share within function and classes command
# line options and settings
conf = AttribDict()

# Dictionary storing
# (1)targets, (2)registeredPocs, (3) bruteMode
# (4)results, (5)pocFiles
# (6)multiThreadMode \ threadContinue \ threadException
kb = AttribDict()

# object to store merged options (command line, configuration file and default options)
merged_options = AttribDict()
