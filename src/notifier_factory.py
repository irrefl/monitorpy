from src.email_config import EmailConfig
from src.email_notifier import EmailNotifier

class NotifierFactory:
    @staticmethod
    def create_notifier(email_alert):
        if email_alert:
            email_config = EmailConfig(
                from_email="irvin.flores6669@gmail.com",
                to_emails=[
                    "irvin.flores6669@gmail.com",
                    "renato.cruz@uth.hn",
                    "arielreyesflores@live.com"
                ],
                smtp_server="smtp.gmail.com",
                smtp_port=587,
                smtp_user="irvin.flores6669@gmail.com",
                smtp_password="xjpo bipn etsa yipa"
            )
            return EmailNotifier(email_config)
        return None
