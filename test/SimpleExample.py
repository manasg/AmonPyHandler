import logging
import amonplushandler

# get our own logger AS we cant attach handlers to root logger (??)
logger = logging.getLogger("Simple")
logger.setLevel(level=logging.INFO)

# add a streamhandler/Console for the kicks
logger.addHandler(logging.StreamHandler())

# add a file handler
fh = logging.FileHandler('/tmp/serious-stuff-only.log')
fh.setLevel(logging.WARNING)
formatter = logging.Formatter("[%(asctime)s][%(filename)s:%(lineno)d] %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# get the key, destination, port from a config file 
# will use chef to populate the right values
rh = amonplushandler.AmonPlusHandler(key="some_key",
                                     destinationIp="some_server",
                                     destinationPort="2464",
                                     appName="python-app-1")
rh.setFormatter(formatter)
logger.addHandler(rh)
    
logger.info("Hello! Informational message")
logger.warn("A warning message")
logger.error("Error! ohhhh")
logger.critical("Bad things")