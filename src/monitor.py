import time

class Monitor:
    def __init__(self, client, logger, host, interval, notifier=None, threshold=3):
        self.client = client
        self.logger = logger
        self.host = host
        self.interval = interval
        self.notifier = notifier
        self.threshold = threshold
        self.fail_count = 0
        self.server_down = False

    def start(self):
        if self.notifier:
            self.notifier.send(f"Monitoreo iniciado para {self.host}", f"Monitoreo del servidor {self.host} ha comenzado.")

        while True:
            try:
                status, latency = self.client.ping(self.host)
                log_entry = f"Servidor: {self.host} - Estado: {status} - Tiempo de respuesta: {latency}"
                self.logger.log(log_entry)
                print(log_entry)

                if status == 'Offline':
                    self.handle_server_down()
                elif status == 'Online':
                    self.handle_server_up()

                time.sleep(self.interval)
            except Exception as e:
                self.logger.log(f"Error durante el monitoreo: {str(e)}")

    def handle_server_down(self):
        self.fail_count += 1
        if self.fail_count >= self.threshold and not self.server_down:
            self.server_down = True
            if self.notifier:
                self.notifier.send(f"ALERTA: {self.host} no responde", f"El servidor {self.host} ha estado caído durante {self.fail_count * self.interval} segundos.")
            self.logger.log(f"ALERTA: El servidor {self.host} no responde.")

    def handle_server_up(self):
        if self.server_down:
            if self.notifier:
                self.notifier.send(f"RECUPERACIÓN: {self.host} en línea", f"El servidor {self.host} ha vuelto a estar en línea.")
            self.logger.log(f"RECUPERACIÓN: El servidor {self.host} ha vuelto a estar en línea.")
        self.fail_count = 0
        self.server_down = False
