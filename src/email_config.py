class EmailConfig:
    def __init__(self, from_email, to_emails, smtp_server, smtp_port, smtp_user, smtp_password):
        self.from_email = from_email
        self.to_emails = to_emails
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
