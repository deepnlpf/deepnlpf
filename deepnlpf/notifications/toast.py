# -*- coding: utf-8 -*-
import pathlib
import subprocess as sp

from deepnlpf.config import Config


class Toast(object):
    """Desktop notifications."""

    def __init__(self) -> None:
        """Load settings."""
        self.status = Config().get_notification_toast()

    def show(self, icon, title, message):
        """Run notification.

        Arguments:
            icon {str} -- Icon name.
            title {str} -- Title of the message.
            message {str} -- Notification message.
        """
        if self.status == "true":  # is true.
            sp.call(
                [
                    "notify-send",
                    "-i",
                    str(pathlib.Path.cwd())
                    + "/deepnlpf/notifications/img/"
                    + icon
                    + ".png",
                    title,
                    message,
                ]
            )

