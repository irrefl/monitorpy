import signal
import sys
from src.monitor_factory import MonitorFactory

def signal_handler(signal, frame):
    print("\nMonitoreo interrumpido. Saliendo...")
    sys.exit(0)

def validate_interval(input_value):
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print("Por favor, ingresa un número entero positivo para el intervalo.")
        sys.exit(1)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    host = input("Ingresa la dirección IP o el dominio del servidor a monitorear: ").strip()
    if not host:
        print("La dirección IP o el dominio no puede estar vacío.")
        sys.exit(1)

    interval = validate_interval(input("Ingresa el intervalo de monitoreo en segundos: ").strip())

    alert_email = input("¿Deseas activar la alerta por correo electrónico? (yes/no): ").strip().lower()
    if alert_email not in ("yes", "no"):
        print("Por favor, responde con 'yes' o 'no'.")
        sys.exit(1)

    email_alert = alert_email == "yes"
    
    try:
        monitor = MonitorFactory.create_monitor(host, interval, email_alert)
        if monitor is None:
            print("Error al crear el monitor. Verifique la configuración.")
            sys.exit(1)
        print("Iniciando monitoreo...")
        monitor.start()
    except Exception as e:
        print(f"Error durante el monitoreo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
