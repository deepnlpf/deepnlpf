import smtplib

import deepnlpf.log as log
from deepnlpf.config import Config
from deepnlpf.core.util import Util
from deepnlpf.global_parameters import HERE


class Email(object):
    def __init__(self) -> None:
        self.smtp = Config().get_notification_email_smtp()
        self.port = Config().get_notification_email_port()
        self.email_address = Config().get_notification_email_address()
        self.password = Config().get_notification_email_pass()

    def send(self):
        sent_from = self.email_address
        to = self.email_address
        subject = "DeepNLPF Datalog"

        body = Util().open_log(HERE + "/data.log")

        email_text = """\
            From: %s  
            To: %s  
            Subject: %s

            %s
            """ % (
            sent_from,
            " ".join(to),
            subject,
            body,
        )

        try:
            server = smtplib.SMTP_SSL(self.smtp, self.port)
            server.ehlo()
            server.login(self.email_address, self.password)
            server.sendmail(self.email_address, self.email_address, email_text)
            server.close()
        except Exception as err:
            log.logger.error("Error loading file!" + str(err))
