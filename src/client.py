import subprocess
import time

class Client:
    def ping(self, host):
        try:
            param = '-n' if subprocess.os.name == 'nt' else '-c'
            start_time = time.time()
            command = ['ping', param, '1', host]
            output = subprocess.run(command, capture_output=True, text=True, timeout=5)
            end_time = time.time()

            if output.returncode == 0:
                latency = (end_time - start_time) * 1000
                return 'Online', f'{latency:.2f} ms'
            return 'Offline', 'N/A'
        except subprocess.TimeoutExpired:
            return 'Offline', 'N/A'
        except Exception:
            return 'Error', 'N/A'
