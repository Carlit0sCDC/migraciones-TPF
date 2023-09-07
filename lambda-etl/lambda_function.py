import csv
import json 
import psycopg2
import os
import boto3


def lambda_handler(event, context):
    print("Event collected is {}".format(event))
    s3_client = boto3.client('s3')
    source_bucket = "flujos-migratorios-source"
    destination_bucket = "flujos-migratorios-destination"

    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        print("Bucket name is {}".format(s3_bucket))
        s3_key = record['s3']['object']['key']
        print("Bucket key name is {}".format(s3_key))
        from_path = "s3://{}/{}".format(s3_bucket, s3_key)
        print("From path {}".format(from_path))

        # Descarga archivos del bucket source
        s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
        data = s3_object['Body'].read().decode('utf-8')

        # Transformación de la data
        transformed_data = []

        # Uso de csv reader para hacer un parse de la CSV data
        csv_reader = csv.DictReader(data.splitlines())
        for row in csv_reader:
            # Verificar si hay valor nulo en la filas y saltearlo
            if all(value is not None for value in row.values()):
                # Convertir los strings a uppercase
                transformed_item = {key: value.upper() if isinstance(value, str) else value for key, value in row.items()}
                transformed_data.append(transformed_item)


        # Crear una nueva S3 key para la data transformada
        transformed_key = "transformed-data/{}".format(s3_key)

        # Carga de la data transformada al bucket de destino
        s3_client.put_object(Bucket=destination_bucket, Key=transformed_key, Body=json.dumps(transformed_data))

      

        print('ETL proceso completado')