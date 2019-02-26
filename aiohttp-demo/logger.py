import logging
import os
import logging.handlers

# define logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# handler:file
log_dir = "/var/log"
log_name = "test.log"
fh = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, log_name), when='D', interval=1, backupCount=40)
fh.setLevel(logging.DEBUG)

# handler:console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# bind handler to logger
logger.addHandler(fh)
logger.addHandler(ch)