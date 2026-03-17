import os
import sys


def _configure_tk_paths_on_windows() -> None:
    """Sets Tcl/Tk environment variables when Python cannot locate init.tcl."""
    if sys.platform != "win32":
        return

    candidate_bases = [os.path.dirname(sys.executable)]

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        version_folder = f"Python{sys.version_info.major}{sys.version_info.minor}"
        candidate_bases.append(
            os.path.join(local_app_data, "Programs", "Python", version_folder)
        )

    for base in candidate_bases:
        tcl_path = os.path.join(base, "tcl", "tcl8.6")
        tk_path = os.path.join(base, "tcl", "tk8.6")
        init_tcl = os.path.join(tcl_path, "init.tcl")

        if os.path.isfile(init_tcl) and os.path.isdir(tk_path):
            os.environ.setdefault("TCL_LIBRARY", tcl_path)
            os.environ.setdefault("TK_LIBRARY", tk_path)
            break


_configure_tk_paths_on_windows()

import tkinter as tk


class NotificationViewer:
    """Basic Tkinter interface for adding and viewing notifications."""

    def __init__(self, notification_system) -> None:
        self.notification_system = notification_system
        self.root = tk.Tk()
        self.root.title("Notification Viewer")
        self.root.geometry("700x500")

        self.message_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Write a message and click 'Add'.")

        self._build_interface()
        self._refresh_notifications()
        self.message_entry.focus_set()

    def _build_interface(self) -> None:
        # Main title for the interface.
        title_label = tk.Label(
            self.root,
            text="Notification System (Singly Linked List)",
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=(16, 10))

        # Input section to add notifications without console usage.
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=16, pady=(0, 10))

        self.message_entry = tk.Entry(
            input_frame,
            textvariable=self.message_var,
            font=("Helvetica", 11)
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        add_button = tk.Button(
            input_frame,
            text="Add",
            font=("Helvetica", 11, "bold"),
            command=self._add_notification
        )
        add_button.pack(side="left")

        self.root.bind("<Return>", self._add_notification_from_event)

        # Read-only area used to visualize the stored linked-list nodes.
        self.text_area = tk.Text(
            self.root,
            width=72,
            height=20,
            font=("Consolas", 11),
            wrap="word"
        )
        self.text_area.pack(padx=16, pady=(0, 8), fill="both", expand=True)

        # The visualization box is read-only.
        self.text_area.config(state="disabled")

        # Status label for basic user feedback.
        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            anchor="w",
            font=("Helvetica", 10)
        )
        status_label.pack(fill="x", padx=16, pady=(0, 14))

    def _set_text_content(self, content: str) -> None:
        """Updates the read-only text area content."""
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, content)
        self.text_area.config(state="disabled")

    def _refresh_notifications(self) -> None:
        """Loads current linked-list notifications into the viewer."""
        notifications_text = self.notification_system.get_notifications_for_ui()
        self._set_text_content(notifications_text)

    def _add_notification_from_event(self, _event) -> None:
        """Handles Enter key to add a notification."""
        self._add_notification()

    def _add_notification(self) -> None:
        """Adds a new message to the linked list and refreshes the view."""
        message = self.message_var.get().strip()

        if message == "":
            self.status_var.set("Please write a notification before adding.")
            return

        self.notification_system.add_notification(message)
        self.message_var.set("")
        self._refresh_notifications()
        self.status_var.set("Notification stored in the linked list.")

    def run(self) -> None:
        self.root.mainloop()
