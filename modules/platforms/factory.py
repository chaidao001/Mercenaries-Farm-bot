from .platforms import find_os
from .window_managers.mac.darwin import WindowMgrDarwin
from .window_managers.windows import get_window_mgr_on_windows
from .window_managers.linux import WindowMgrLinux


def get_window_manager():
    os = find_os()

    if os == "windows":
        WindowMgrWindows = get_window_mgr_on_windows()
        return WindowMgrWindows()
    elif os == "linux":
        return WindowMgrLinux()
    elif os == "mac_darwin":
        return WindowMgrDarwin()
    else:
        raise Exception(f"OS not recognized: {os}")
