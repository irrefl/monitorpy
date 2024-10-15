import smtplib
from email.message import EmailMessage

class EmailNotifier:
    def __init__(self, email_config):
        self.email_config = email_config

    def send(self, subject, content):
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['From'] = self.email_config.from_email
        msg['To'] = self.email_config.to_emails[0]
        msg['Cc'] = ', '.join(self.email_config.to_emails[1:])

        try:
            with smtplib.SMTP(self.email_config.smtp_server, self.email_config.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.email_config.smtp_user, self.email_config.smtp_password)
                smtp.send_message(msg)
            print(f"Correo enviado: {subject}")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
