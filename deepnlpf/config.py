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

    def set_notification_toast(self, status: str):
        return self.config.set("notification", "toast", status)


    def get_notification_email_smtp(self):
        value = self.config.get("notification", "email.smtp")
        return str(value)

    def set_notification_email_smtp(self, smtp: str):
        return self.config.set("notification", "email.smtp", smtp)


    def get_notification_email_port(self):
        value = self.config.get("notification", "email.port")
        return int(value)

    def set_notification_email_port(self, port: str):
        return self.config.set("notification", "email.port", port)


    def get_notification_email_address(self):
        value = self.config.get("notification", "email.email_address")
        return str(value)

    def set_notification_email_address(self, email_address: str):
        return self.config.set("notification", "email.email_address", email_address)


    def get_notification_email_pass(self):
        value = self.config.get("notification", "email.pass")
        return str(value)

    def set_notification_email_pass(self, password: str):
        return self.config.set("notification", "email.pass", password)
