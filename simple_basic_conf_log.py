"""
Print log to file and to the console with a basic easy config
"""
import logging

LOG_FILE = '.\\logs\\aladin.log'

# FILE LOG 
filelog=logging.FileHandler(filename=LOG_FILE)
logfmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
filelog.setFormatter(logfmt)

# CONSOLE LOG
stream = logging.StreamHandler()
# set the level to print only from error in the console
stream.setLevel(logging.ERROR) 
fmt = logging.Formatter('%(levelname)s - %(message)s')
stream.setFormatter(fmt)

# LEAVE IT TO THE HANDLER IN A EASY WAY
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        filelog,
        stream
    ]
)

# will print only in file 
logging.info("Aladin simple log configuration on file only")

# will print in file and console  
logging.error("Aladin simple log configuration on file and screen")
