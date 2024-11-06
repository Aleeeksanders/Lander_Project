#!/bin/bash

# Navega a la carpeta de la función Lambda
cd ../lambda_functions/ProcessCommand/

# Crear el directorio temporal para empaquetar
mkdir -p package

# Instala dependencias en el directorio package
pip install -r requirements.txt -t package/

# Copia solo los módulos necesarios al paquete
cp -r ../../modules/iot_control package/
cp -r ../../modules/nlp package/
cp -r ../../modules/speech package/
cp ../../config/settings.py package/
cp ../../config/devices.yaml package/

# Copia el archivo principal para Lambda
cp lambda_main.py package/

# Empaqueta los archivos en un ZIP
cd package
zip -r ../ProcessCommand.zip .
cd ..

# Despliega la función en Lambda
aws lambda update-function-code --function-name ProcessCommand --zip-file fileb://ProcessCommand.zip

# Limpia el paquete temporal
rm -r package ProcessCommand.zip

echo "Despliegue completado para la función ProcessCommand."
