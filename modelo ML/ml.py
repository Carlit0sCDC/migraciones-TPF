import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



df = pd.read_csv('undesa_3.csv')



#pude filtrar por norte america, es que tienen espacios vacios los campos
df_filtered = df[df['Region_group_of_destination'] == ' NORTHERN AMERICA']

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

print(f'Prediccion de inmigrantes Latinoamericanos a Norteamerica en el año 2025: {prediccion_2025[0]}')