from configparser import ConfigParser

from deepnlpf.global_parameters import FILE_CONFIG


class Config(object):
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read(FILE_CONFIG)

    def get_debug(self) -> str:
        return self.config.get("debug", "is_enabled")

    def set_debug(self, status: str):
        self.config.set("debug", "is_enabled", status)

    def get_notification_toast(self):
        return self.config.get("notification", "toast")

    def set_notification_toast(self, status:str):
        return self.config.set("notification", "toast", status)
