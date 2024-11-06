# device_connector.py
# Conecta y controla dispositivos IoT

class DeviceConnector:
    def __init__(self, device_info):
        self.device_info = device_info

    def conectar_dispositivo(self):
        print(f"Conectando al dispositivo {self.device_info['name']}...")

    def cambiar_estado(self, estado):
        print(f"Cambiando {self.device_info['name']} a estado {estado}")
        self.device_info['status'] = estado
