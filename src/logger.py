from datetime import datetime

class Logger:
    def __init__(self, filename="server_log.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as log_file:
            log_file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {message}\n')
