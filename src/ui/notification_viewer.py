import tkinter as tk


class NotificationViewer:
    """Read-only Tkinter viewer for notifications already stored in the list."""

    def __init__(self, notification_system) -> None:
        self.notification_system = notification_system
        self.root = tk.Tk()
        self.root.title("Notification Viewer")
        self.root.geometry("620x420")

        self._build_interface()
        self._load_notifications()

    def _build_interface(self) -> None:
        # Main title for the screen.
        title_label = tk.Label(
            self.root,
            text="Stored Notifications",
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=(16, 8))

        # Read-only text area where notifications are shown.
        self.text_area = tk.Text(
            self.root,
            width=72,
            height=18,
            font=("Consolas", 11),
            wrap="word"
        )
        self.text_area.pack(padx=16, pady=(0, 16), fill="both", expand=True)

        # The viewer is intentionally read-only for the case study.
        self.text_area.config(state="disabled")

    def _load_notifications(self) -> None:
        notifications_text = self.notification_system.get_notifications_for_ui()

        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, notifications_text)
        self.text_area.config(state="disabled")

    def run(self) -> None:
        self.root.mainloop()
