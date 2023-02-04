import logging

from AppKit import NSWorkspace, NSApplicationActivateIgnoringOtherApps

from ..base import WindowMgr
from ....exceptions import WindowManagerError

log = logging.getLogger(__name__)

HEARTHSTONE_WINDOW_NAME = "Hearthstone"


class WindowMgrDarwin(WindowMgr):
    """Encapsulates some calls for Linux window management"""

    def __init__(self):
        """Constructor"""
        self.win = None

    def find_game(self):
        """find the hearthstone game window"""
        applications = NSWorkspace.sharedWorkspace().runningApplications()

        for application in applications:
            if application.localizedName() == HEARTHSTONE_WINDOW_NAME:
                application.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
                self.win = application
                return application

        raise WindowManagerError("No 'Hearthstone' window found.")

    def get_window_geometry(self):
        # TODO: find geometry
        return 0, 0, 1920, 1080
