from src.client import Client
from src.logger import Logger
from src.notifier_factory import NotifierFactory
from src.monitor import Monitor

class MonitorFactory:
    @staticmethod
    def create_monitor(host, interval, email_alert):
        client = Client()
        logger = Logger()
        
        notifier = NotifierFactory.create_notifier(email_alert)
        
        return Monitor(client, logger, host, interval, notifier)
