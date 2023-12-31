 # Proyecto de Análisis de Flujos Migratorios y sus Impactos

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/Logo.png" alt="Logo de Insight Analysts Collective" >
</p>

## Descripción General

Somos **Insight Analysts collective**, un equipo de analistas de datos contratados por el Ministerio de Migración de Canadá para analizar patrones de migración en América. Nuestro objetivo es revelar información importante sobre oportunidades en aspectos económicos, sociales, educativos y ambientales para captar emigrantes y contribuir al enriquecimiento cultural y socioeconómico del país. Además, pondremos a disposición los datos revelados por el análisis para ayudar a futuros emigrantes a tomar decisiones informadas sobre la migración.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/mapa.png" alt="mapa_ilustrativo" height="400">
</p>

## Índice

1. [Objetivo Principal](#objetivo-principal)
2. [Metodología de trabajo](#metodología-de-trabajo)
3. [Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos](#sprint-1-puesta-en-marcha-y-trabajo-con-datos)
4. [ETL (Extracción Transformación y Carga)](#etl-extracción-transformación-y-carga)
5. [Exploración de Datos (EDA)](#exploración-de-datos-eda)
6. [KPIs (Indicadores Clave de Desempeño)](#kpis-indicadores-clave-de-desempeño)
7. [Sprint #2: Data Engineering](#sprint-2-data-engineering)
8. [WorkFlow y tecnologías](#workflow-y-tecnologías)
9. [PIPELINE ETL (AWS CLOUD)](#pipeline-etl-aws-cloud)
10. [Validación de datos](#validación-de-datos)
11. [Diccionario de datos](#diccionario-de-datos)
12. [Sprint #3: Data Analytics + ML](#sprint-3-data-analytics--ml)
13. [Producto entregable: Dashboard](#producto-entregable-tablero-de-control-para-uso-interno-ministerio-de-migraciones-canadá)
14. [Producto entregable: Modelo de ML](#producto-entregable-api-para-predicción-de-migraciones)
15. [Presentación proyecto](#presentación)

## Objetivo principal

Desarrollar una estrategia que promueva la emigración de la comunidad latina hacia Canadá en lugar de Estados Unidos, basándonos en datos objetivos y análisis comparativos. Esto se logrará proporcionando al Ministerio de Migraciones de Canadá información relevante para aumentar el número de migrantes latinos hacia Canadá y ofreciendo en el sitio web de la embajada un análisis detallado sobre las oportunidades y ventajas que ofrece Canadá en términos de calidad de vida, empleo, educación y políticas de inmigración, para guiar a futuros emigrantes en su proceso de toma de decisiones.

## Metodología de trabajo

Para el proyecto actual, se utiliza la metodología ágil Scrum con 3 sprints. Cada sprint dura una semana y se enfoca en desarrollar y entregar ciertas funcionalidades:

- 📜 Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos
- 👨‍💻 Sprint #2: Data Engineering
- 📈 Sprint #3: Data Analytics + ML

Usamos un enfoque iterativo e incremental para agregar valor al proyecto día a día, trabajando en conjunto con el Scrum Master. Al final de cada semana, presentamos el proyecto al Product Owner.

El **equipo de trabajo** está formado por 4 desarrolladores:
* **Antonella Nieto** - Ingeniera de datos
* **Carlos Días Colodrero** - Ingeniero de datos
* **Yuri Díaz** - Analista de datos
* **Florencia Miranda** - Científica de datos

El **cronograma de trabajo** se gestiona en la plataforma Monday. Pueden verlo en este [Enlace](https://flormiranda1995s-team.monday.com/boards/5064412581/).

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/semana1.png" alt="Logo de Insight Analysts Collective" width="700">
</p>

# 📜Sprint #1: Puesta en marcha y Trabajo con Datos

## ETL (Extracción Transformación y Carga)
Para este trabajo utilizamos un dataset de la ONU del Department of Economics and Social Affairs que nos proporcionó datos cada 5 años desde 1990 a 2020 sobre los migrantes según su destino, región, continente, nivel de ingresos y desarrollo de los países receptores. En el siguiente
[link](https://www.un.org/development/desa/pd/content/international-migrant-stock) puede encontrarse más información relacionada. Puede encontrar el dataset titulado undesa.csv en la carpeta "data" del repositorio.

Los procesos realizados fueron:

* Creamos una columna de año en las tablas 2 a 8 del dataset de 8 tablas. 
* Unimos las tablas en un solo dataset.
* Limpiamos el dataset cambiando los tipos de datos de las columnas, cambiando nombres de columnas y eliminando las no pertinentes.
* Exportamos el dataset limpio resultante. 

## Exploración de Datos (EDA)

Para comprender mejor la naturaleza de los flujos migratorios realizamos las siguientes indagaciones:

* Graficar la tendencia migratoria de la región Latin America and the Caribbean 1990-2020.
* Extraer el aumento porcentual quinquenal y el promedio quinquenal histórico. 
* Observar la distribución geográfica de migrantes dentro la propia región Latin America and the Caribbean.
* Segmentación por nivel de ingreso de países de destino
* Top 2 de regiones a las que más han migrado los latinoamericanos según el nivel de ingresos y porcentaje histórico según el nivel de ingresos. 
* Regiones preferidas por los migrantes latinoamericanos históricamente. 

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/aumento%20de%20la%20migracion%20de%20latinos%20en%20el%20tiempo.jpeg" alt="Variación en la tasa de migración de latinos a lo largo del tiempo" width="400"/> <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/variaci%C3%B3n%20de%20migracion%20de%20latinos%20al%20mundo.jpeg" alt="Migración de latinos al mundo a lo largo del tiempo" width="400"/>
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/distribuci%C3%B3n%20por%20nivel%20de%20ingreso%20paises%20destino.jpeg" alt="distribución por nivel de ingresos del pais destino" width="400"/> <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/regiones%20preferidas%20para%20migrar.jpeg" alt="regiones preferidas por los latinos para migrar" width="400"/>
</p>

## KPIs (Indicadores Clave de Desempeño)

1. **Vistas al dashboard informativo para inmigrantes**:
   
KPI: Conseguir 100 vistas del informe por mes. El propósito de este KPI es dar a conocer la información relevante sobre migraciones a los inmigrantes para que al ver los beneficios de Canadá, decidan a este como su país de destino migratorio. Podrán encontrar la construcción de este dashboard en el siguiente [repositorio](https://github.com/flormiranda1/migraciones_streamlit/tree/main)

Métrica: vistas al dashboard [Dataset vistas](https://docs.google.com/spreadsheets/d/1qm1LBKiuc4hovNiY6hodRRXADZIhW7yCQqoqDswfOn4/edit?resourcekey#gid=1060175855)

Cálculo del KPI: vistas_actuales/vistas_objetivo*100 (100)

2. **Aumento de migrantes Canadá**:
   
KPI: Observar un aumento del 7% en la cantidad de inmigrantes calificados/universitarios (teniendo en cuenta el promedio de años de estudio de la población) en el próximo año hacia Canadá

Métrica: Cantidad de inmigrantes anual en Canada provenientes de dichos paises

Cálculo del KPI: ((Inmigrantes a la fecha / Inmigrantes un año atras) - 1) * 100

3. **Disminución de migrantes EEUU** (Suponiendo que Canadá captaría estos migrantes)
   
KPI: Observar una disminución del 1% en la cantidad de inmigrantes calificados/universitarios que eligen como destino EEUU durante el próximo año, considerando que estos inmigrantes serían captados por Canadá

Métrica: Cantidad de inmigrantes anual en EEUU provenientes de dichos paises

Cálculo del KPI: ((Inmigrantes a la fecha / inmigrantes un año atras) - 1) * 100

4. **Aumento del PIB per cápita (Canadá)**
   
KPI: Lograr un incremento del 5% en el PIB de Canadá el próximo año

Métrica: PIB per cápita anual

Cálculo del KPI: ((PIB actual / PBI año anterior) - 1) * 100

**Relación entre PIB per cápita y Atracción de Inmigrantes:**
El aumento del PIB per cápita de un país puede hacerlo más atractivo para los inmigrantes, ya que generalmente se asocia con una mayor demanda de trabajo y más oportunidades económicas, como así también el mayor poder adquisitivo de sus habitantes. Si el PIB de Canadá aumenta significativamente junto con la tasa de migración desde América Latina, se podría argumentar que el país ofrece un entorno económico favorable y atrae a más inmigrantes en busca de mejores oportunidades. Este KPI establece una conexión entre el aumento del PIB y el interés de los migrantes, demostrando cómo un entorno económico en crecimiento puede influir en la decisión de migrar a Canadá


# 👨‍💻Sprint #2: Data Engineering

## Data Lake:

Para nuestro proyecto de Análisis de Flujos Migratorios y sus Impactos, implementamos un modelo no relacional llamado Data Lake en lugar de uno relacional tradicional. Elegimos esto por tres razones clave:

1. **Naturaleza de los Datos:**

Manejamos datos heterogéneos sin una estructura de relaciones fija. Un modelo relacional no sería adecuado, ya que nuestros datos incluyen flujos migratorios y datos socioeconómicos de diversas fuentes.

2. **Escalabilidad y Flexibilidad:**

Amazon S3, el Data Lake que usamos, es escalable e ideal para grandes volúmenes de datos no estructurados o semiestructurados. Esto es esencial ya que trabajamos con una amplia gama de datos que pueden crecer con el tiempo.

3. **Rendimiento de Análisis:**

El Data Lake permite la ejecución de análisis de datos avanzados y personalizados, sin restricciones impuestas por un esquema de tabla predefinido. Esto es esencial para nuestro proyecto, donde necesitamos explorar datos complejos y buscar patrones específicos.

## WorkFlow y tecnologías

Los datos crudos se cargan en el Data Lake, en el bucket de S3 "Data inicial". Se transforman y se cargan en un segundo bucket de S3 llamado "Data final" mediante la primera función Lambda. La segunda función Lambda se encarga de la carga incremental y la validación de datos duplicados en el mismo bucket "Data final". Este flujo de trabajo garantiza que los datos se transformen, procesen y validen de manera eficiente antes de ser almacenados en el "Data final", proporcionando así un proceso de ETL escalable y confiable.

1) Creación del Data-lake (Buckets data inicial y data final) - **AWS S3**
  
2) Creación de función para la carga inicial y transformaciones de datos crudos - **AWS Lambda**
  
3) Creación de función para la carga incremental de datos y validación de duplicados - **AWS Lambda**
  
4) Conexión del bucket de data final con PowerBI - **AWS S3/Script de python**
  
5) MVP Dashboard con los datos extraídos - **PowerBI**

## PIPELINE ETL (AWS CLOUD)

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/PIPELINE.png" alt="PIPELINE" width="700">
</p>

## [Función Lambda para ETL Automatizado:](https://github.com/Carlit0sCDC/migraciones-TPF/tree/main/lambda-etl)

La función Lambda "lambda_handler" es esencial para el procesamiento de datos en la nube. Realiza la etapa de transformación del proceso ETL de datos.

1. **Detección de Eventos:**

Lambda espera eventos que desencadenen su ejecución, en este caso, cambios en los "buckets" de Amazon S3.

2. **Preparación para el Trabajo:**

Lambda interactúa con los servicios de AWS para obtener información sobre la ubicación del archivo y dónde colocar los resultados.

3. **Recuperación de Datos:**

Lambda accede al archivo en el "bucket" de S3 y recupera los datos sin perder ninguno.

4. **Transformación de Datos:**

Lambda transforma los datos según las reglas especificadas, por ejemplo, convirtiendo cadenas en mayúsculas, corrigiendo datos erróneos y eliminando duplicados.

5. **Almacenamiento de Datos Transformados:**

Lambda coloca los datos transformados en un nuevo lugar dentro de un "bucket" de S3.

6. **Finalización del Trabajo:**

Lambda completa su tarea y espera eventos futuros. Su velocidad y escalabilidad permiten procesar grandes cantidades de datos en poco tiempo.

En resumen, la función Lambda realiza la transformación del ETL de manera eficaz, asegurando que los datos estén limpios y listos para el análisis posterior. Su capacidad de respuesta a eventos y escalabilidad hacen que sea una herramienta poderosa en la gestión y transformación automatizada de datos.

## Validación de datos

En nuestro proyecto, aseguramos la calidad e integridad de la información mediante las siguientes prácticas:

- **Limpieza de Datos**: Eliminamos valores nulos, duplicados y datos inconsistentes para trabajar con datos confiables.

- **Validación de Formato**: Verificamos que los datos sigan el formato esperado, incluyendo fechas, números, minúsculas y mayúsculas, y otros tipos de datos.

- **Auditorías y Registros**: Mantenemos registros de las validaciones realizadas para rastrear cambios y problemas en los datos.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/validacion_1.jpeg" alt="validacion1" width="500"/> <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/validacion_2.jpeg" alt="validacion2" width="500"/>
</p>

## Diccionario de datos

Este es el link del [Diccionario de datos.](https://docs.google.com/spreadsheets/d/1Kqbgxvg3pzMPJwpafznR0o5v2Fp2Tjm3/edit#gid=1757762391)
 También puede encontrarse  dentro de la carpeta "documentación" del repositorio.


# 📈Sprint #3: Data analytics + ML

## Producto entregable: Tablero de control para uso interno (ministerio de migraciones Canadá)

El dashboard esta estructurado en su inicio con una portada interactiva que lleva a las diferentes páginas en donde se ven reflejados los KPIs con sus respectivos gráficos informativos. Además se incluyeron páginas adicionales para un mejor entendimiento del porque de los KPIs y a la vez mejorar la visualización global del tablero.

Se eligieron los colores corporativos de la consultora para el diseño y se agregaron diferentes botones con fucionalidades para obtener información detallada de los gráficos. Cada página es interactiva, el usuario puede filtrar según su necesidad de análisis

La información que alimenta este dashboard fue tomada directamente del bucket de data procesada en nuestra estructura de datos en la nube (AWS)

**Portada**
<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/portada.png" alt="portadadash" width="700">
</p>

**Diseño general**
<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/dashboard.png" alt="dash" width="700">
</p>

**KPIs**
<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/kpi2.png" alt="kpi2" width="500"/> <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/KPI3.png" alt="kpi3" width="500"/>
</p>

**Informe de análisis**
En el siguiente [documento] (pegar aqui el informe de analisis) podrán encontrar las conclusiones obtenidas luego del análisis hecho a partir del dashboard

## Producto entregable: Predicción de migraciones

En el siguiente link https://prediccion-migracion-canada-provincias.onrender.com/ encontrarán el deployed de una aplicación web en la que podrán predecir la cantidad de migrantes esperados según la provincia de Canadá o predicción para el total del país, esto fue desarrollado en base a un modelo de machine learning (Linear Regressor) que nos permite predecir el número de migrantes en base a los datos obtenidos de migraición por cada provincia y el país de los últimos años.
El código se encuentra en el siguiente link: https://github.com/antonellanieto/ml-migracion-canada

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/render.png" alt="render" width="800">
</p>

**[Feature engineering](https://github.com/antonellanieto/ml-migracion-canada)**

El flujo de trabajo para obtener este producto fue en una primera instancia conectar los datos contenidos en la nube (en el bucket de data procesada de AWS) mediante Python, luego se hizo un análisis exploratorio de los datos para detectar patrones y decidir el modelo a usar, por último se entrenó el modelo con sets de entrenamiento y prueba usando la librería de Scikit-Learn de python. Al tener el modelo entrenado se creó una [API] (link al codigo .py de la api) con la librería Fast-API, luego de tenerlo funcionando de manera local se hizo un deploy en render para generar una interfaz amigable para el usuario.

**El modelo usado fue con el fin de que el cliente pueda tomar decisiones en base a los datos predecidos por provincias, para tener en cuenta la posible distribución de próximos flujos migratorios. Estos resultados de posible flujos migratorios pueden servir para la implementación de desentralización dentro del país, tomando en cuenta los datos previstos en el análisis**


## Presentación
A continuación les dejamos el link a la [presentación](https://www.canva.com/design/DAFs-WJPipA/HwFAwaGHidStTdXKRimmOQ/edit) del proyecto.


**Queremos enfatizar que este proyecto es completamente ficticio y no implica ninguna relación de trabajo con el Ministerio de Migraciones ni con ninguna entidad gubernamental real. Tiene como único propósito fines educativos y de aprendizaje académico.**
