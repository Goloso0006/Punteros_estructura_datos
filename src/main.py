import os
import subprocess
import sys

from notification_system import NotificationSystem
from ui.notification_viewer import NotificationViewer


def _relaunch_without_console_on_windows() -> None:
    """Relaunches the app with pythonw.exe to avoid opening a console window."""
    if sys.platform != "win32":
        return

    if os.environ.get("NOTIFICATION_APP_NO_RELAUNCH") == "1":
        return

    if sys.executable.lower().endswith("pythonw.exe"):
        return

    pythonw_candidates = [os.path.join(os.path.dirname(sys.executable), "pythonw.exe")]

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        version_folder = f"Python{sys.version_info.major}{sys.version_info.minor}"
        pythonw_candidates.append(
            os.path.join(local_app_data, "Programs", "Python", version_folder, "pythonw.exe")
        )

    pythonw_path = next((path for path in pythonw_candidates if os.path.isfile(path)), None)
    if pythonw_path is None:
        return

    env = os.environ.copy()
    env["NOTIFICATION_APP_NO_RELAUNCH"] = "1"
    subprocess.Popen([pythonw_path, os.path.abspath(__file__)], env=env)
    raise SystemExit(0)


def main() -> None:
    # The system stores messages in a manual singly linked list.
    notification_system = NotificationSystem()

    # Open the Tkinter interface for adding and viewing notifications.
    viewer = NotificationViewer(notification_system)
    viewer.run()    


if __name__ == "__main__":
    _relaunch_without_console_on_windows()
    main()
