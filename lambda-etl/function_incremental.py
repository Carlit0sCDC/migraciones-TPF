import boto3
import csv
import pandas as pd
import io

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    destination_bucket = "flujos-migratorios-destino"

    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']

        # Verificar si el CSV existe con el mismo nombre en el bucket de destino
        try:
            s3_client.head_object(Bucket=destination_bucket, Key=s3_key)
            # If the object exists, retrieve it and merge with the new data
            existing_object = s3_client.get_object(Bucket=destination_bucket, Key=s3_key)
            existing_data = existing_object['Body'].read().decode('utf-8')

            # Carga la nueva data
            new_data = []

            #Unir la data existente
            existing_df = pd.read_csv(io.StringIO(existing_data))
            new_df = pd.DataFrame(new_data)

            # Concatenarla
            merged_df = pd.concat([existing_df, new_df], ignore_index=True)

            # Transformar nombre de las columnas separadas por un guion bajo
            merged_df.columns = [column.replace(' ', '_').lower() for column in merged_df.columns]
            merged_df = merged_df.fillna(0)

            # Convert all string columns to uppercase
            merged_df = merged_df.apply(lambda x: x.str.upper() if x.dtype == 'object' else x)

            #Convertir todas las columnas a mayúsculas
            merged_csv = merged_df.to_csv(index=False)

            # Carga del csv al bucket de destino
            s3_client.put_object(Bucket=destination_bucket, Key=s3_key, Body=merged_csv)
        except s3_client.exceptions.ClientError as e:
            # Si el objeto no existe, no hay nada que unir
            if e.response['Error']['Code'] == '404':
                pass

    print('Merging process completed')
