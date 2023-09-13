import csv
import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    print("Event collected is {}".format(event))
    s3_client = boto3.client('s3')
    source_bucket = "flujos-migratorios-ingreso"
    destination_bucket = "flujos-migratorios-destino"

    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        print("Bucket name is {}".format(s3_bucket))
        s3_key = record['s3']['object']['key']
        print("Bucket key name is {}".format(s3_key))
        from_path = "s3://{}/{}".format(s3_bucket, s3_key)
        print("From path {}".format(from_path))

        # Carga de archivo CSV desde el bucket inicial
        s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
        data = s3_object['Body'].read().decode('utf-8')

        # Transformación de la data
        transformed_data = []

        # Lectura de la data
        csv_reader = csv.DictReader(data.splitlines())
        for row in csv_reader:
            # Verificar si hay nulos y saltearlos
            if all(value is not None for value in row.values()):
                # Transformar a mayúsculas
                transformed_item = {key.replace(' ', '_'): value.upper() if isinstance(value, str) else value for key, value in row.items()}
                # Reemplazar numeros nulos con 0
                for key, value in transformed_item.items():
                    if value is None or value == '':
                        transformed_item[key] = 0
                transformed_data.append(transformed_item)

        # Creación de nueva S3 key para la data transformada
        transformed_key = "data-transformada/{}".format(s3_key)

        # Convertir la data transformada a un CSV
        transformed_csv = pd.DataFrame(transformed_data).to_csv(index=False)

        # Carga de la data a el bucket de destino
        s3_client.put_object(Bucket=destination_bucket, Key=transformed_key, Body=transformed_csv)

        print('ETL process completed')
