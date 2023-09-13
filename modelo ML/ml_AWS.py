import boto3
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#MODELO MACHINE LEARNING OBTENIENDO DATA DIRECTO DEL DATA LAKE
# credenciales AWS
aws_access_key_id = 'AKIAWE2FC45LIYBCZY6I'
aws_secret_access_key = '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'


# Cliente B3 con las credenciales cargadas
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
  
)

# Especificar el bucket y el objeto dentro
bucket_name = 'flujos-migratorios-destination'
object_key = 'transformed-data/undesa.csv'

try:
    #Traer el objeto del bucket
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    #Leerlo como un df de pandas
    df = pd.read_csv(response['Body'])
except Exception as e:
    print(f"Erorr: {str(e)}")




#Filtrar la data por NorteAmerica no da resultados. sólo da predicciones con WORLD, por falta de datos para entrenar
df_filtered = df[df['Region_group_of_destination'] == 'WORLD']

# Seleccionar variables
X = df_filtered[['year']]
y = df_filtered['Latin_America_and_the_Caribbean']

# dimensiones para ver la cantidad de data
print("X shape:", X.shape)
print("y shape:", y.shape)

# Creacion de model y entrenamiento
model = LinearRegression()
model.fit(X, y)

# Predicciones para 2025
year_2025 = pd.DataFrame({'year': [2025]})
prediccion_2025 = model.predict(year_2025)

print(f'Prediccion de inmigrantes Latinoamericanos al mundo en el año 2025: {prediccion_2025[0]}')