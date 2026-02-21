"""


📌 Today's Learning Topic
Using the logging module with:
- Custom Formatter
- StreamHandler (console output)
- FileHandler (log file output)
- Log level control

This structure is commonly used in real-world automation,
server applications, and cybersecurity monitoring systems.
"""

import logging
from datetime import datetime


# -----------------------------------------------------------
# 1️⃣ Create Log Formatter
# -----------------------------------------------------------
# Format: time [log level] message
logFormatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
)


# -----------------------------------------------------------
# 2️⃣ Create Logger Object
# -----------------------------------------------------------
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Show DEBUG and above


# -----------------------------------------------------------
# 3️⃣ Stream Handler (Console Output)
# -----------------------------------------------------------
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)


# -----------------------------------------------------------
# 4️⃣ File Handler (Save Logs to File)
# -----------------------------------------------------------
filename = datetime.now().strftime(
    "mylogfile_%Y%m%d%H%M%S.log"
)

fileHandler = logging.FileHandler(
    filename,
    encoding="utf-8"
)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)


# -----------------------------------------------------------
# 5️⃣ Test Log Message
# -----------------------------------------------------------
logger.debug("Running a logging test message.")
