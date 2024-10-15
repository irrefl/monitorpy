# Monitoreo Básico de Servidor con Python

Este proyecto tiene como objetivo monitorear un servidor en intervalos de tiempo predefinidos, verificando si el servidor está en línea (activo) o fuera de línea (caído). Además, mide el tiempo de respuesta (latencia) desde el cliente que ejecuta el script hasta el servidor y envía alertas por correo electrónico cuando el servidor no responde.

## Características Completas

- [✅] **Monitoreo de Estado del Servidor**: Verifica si un servidor está en línea enviando pings periódicos a una dirección IP o un dominio.
- [✅] **Medición de la Latencia**: Registra el tiempo de respuesta en milisegundos (ms) desde el envío del ping hasta recibir la respuesta.
- [✅] **Intervalo de Monitoreo Configurable**: Permite al usuario definir el intervalo en segundos entre cada monitoreo.
- [✅] **Registro en Archivo de Log**: Guarda en un archivo `server_log.txt` cada evento de monitoreo con la fecha, hora, estado del servidor (online/offline) y el tiempo de respuesta.
- [✅] **Envío de Alertas por Correo Electrónico**: Envía un correo cuando el servidor está caído o cuando se recupera.
- [✅] **Creación de un Ejecutable Profesional**: Genera un archivo ejecutable (`.exe`) usando PyInstaller.

## Requisitos Previos

1. **Python 3.10** o superior.
2. **Conda** o **Miniconda** para la gestión del entorno virtual.
3. Dependencias incluidas en el archivo `environment.yml`.

## Instalación

### 1. Clonar el Repositorio

Clona el repositorio desde GitHub usando el siguiente comando:

```sh
git clone https://github.com/irrefl/monitorpy.git
cd monitorpy
```

### 2. Crear y Activar el Entorno Virtual

Utiliza conda para crear un entorno virtual basado en el archivo `environment.yml`:

```sh
conda env create -f environment.yml
conda activate server_monitor_env
```

### 3. Instalar Dependencias Adicionales (opcional)

Si necesitas instalar dependencias adicionales, puedes hacerlo utilizando pip:

```sh
pip install -r requirements.txt
```

### 4. Configurar el Monitoreo

Ejecuta el archivo `main.py` para iniciar el monitoreo de un servidor. Se te pedirá ingresar la dirección IP o dominio del servidor a monitorear, el intervalo de monitoreo y si deseas activar las alertas por correo electrónico.

```sh
python -m src.main
```

### 5. Crear un Ejecutable (.exe)

Para generar el ejecutable del programa, puedes utilizar PyInstaller. Asegúrate de tenerlo instalado y luego ejecuta el siguiente comando:

```sh
pyinstaller --onefile src/main.py --name server_monitor
```

Esto generará un archivo `server_monitor.exe` en el directorio `dist/`. Puedes distribuir este ejecutable en otros sistemas sin necesidad de tener Python instalado.

## Ejecución del Programa

## Video de Ejemplo

Puedes ver un ejemplo del monitoreo en funcionamiento en el siguiente video de YouTube: [Video de Monitoreo Básico de Servidor](https://youtu.be/Ye7qnss8rHo)


### Pasos para Ejecutar el Monitoreo

1. Ejecuta el programa con el siguiente comando si tienes el entorno activado:

    ```sh
    python -m src.main
    ```

2. Ingresa la dirección IP o el dominio del servidor que deseas monitorear:

    ```
    Ingresa la dirección IP o el dominio del servidor a monitorear: 192.168.1.1
    ```

3. Ingresa el intervalo de monitoreo en segundos (por ejemplo, 5 segundos):

    ```
    Ingresa el intervalo de monitoreo en segundos: 5
    ```

4. Decide si deseas activar la alerta por correo electrónico (yes/no):

    ```
    ¿Deseas activar la alerta por correo electrónico? (yes/no): yes
    ```

## Logs Generados

El programa genera un archivo `server_log.txt` donde se registra cada evento de monitoreo con la siguiente estructura:

```yaml
2024-10-07 10:30:15 - Servidor: 192.168.1.1 - Estado: Online - Tiempo de respuesta: 25 ms
2024-10-07 10:30:20 - Servidor: 192.168.1.1 - Estado: Online - Tiempo de respuesta: 27 ms
2024-10-07 10:30:25 - Servidor: 192.168.1.1 - Estado: Offline - Tiempo de respuesta: N/A
```

## Alertas por Correo Electrónico

Si has activado las alertas por correo electrónico, recibirás correos como estos cuando el servidor cambie de estado:

- **Servidor en línea**:

    ```text
    Asunto: Monitoreo iniciado para 192.168.1.1
    Contenido: El monitoreo del servidor 192.168.1.1 ha comenzado.
    ```

- **Servidor caído**:

    ```text
    Asunto: ALERTA: 192.168.1.1 no responde
    Contenido: El servidor 192.168.1.1 ha estado caído durante X segundos.
    ```

- **Servidor recuperado**:

    ```text
    Asunto: RECUPERACIÓN: 192.168.1.1 en línea
    Contenido: El servidor 192.168.1.1 ha vuelto a estar en línea.
    ```

## Funcionalidades Implementadas

- **Monitoreo del Servidor**: El script verifica continuamente el estado del servidor mediante pings.
- **Logs de Monitoreo**: Cada estado y tiempo de respuesta se registra en un archivo de log.
- **Alerta por Correo**: Se envían alertas cuando el servidor se cae o se recupera, utilizando la configuración de SMTP de Gmail.
- **Ejecutable (.exe)**: El programa puede ser compilado en un archivo ejecutable utilizando PyInstaller.