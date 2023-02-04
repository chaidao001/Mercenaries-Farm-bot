import sys
import logging

log = logging.getLogger(__name__)


def find_os():
    # try to detect the OS (Windows, Linux, Mac, ...)
    # to load specific libs
    if sys.platform in ["Windows", "win32", "cygwin"]:
        myOS = "windows"
    elif sys.platform in ["linux", "linux2"]:
        myOS = "linux"
    elif sys.platform in ["darwin"]:
        myOS = "mac_darwin"
    else:
        log.info(f"sys.platform='{sys.platform}' is unknown.")
        sys.exit()
    return myOS
