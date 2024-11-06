# device_manager.py
# Administra la lista de dispositivos IoT

from modules.iot_control.device_connector import DeviceConnector

class DeviceManager:
    def __init__(self, devices):
        self.devices = [DeviceConnector(d) for d in devices]

    def encender_dispositivo(self, nombre):
        for device in self.devices:
            if device.device_info['name'] == nombre:
                device.cambiar_estado("on")

    def apagar_dispositivo(self, nombre):
        for device in self.devices:
            if device.device_info['name'] == nombre:
                device.cambiar_estado("off")
