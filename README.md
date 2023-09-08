 # Proyecto de Análisis de Flujos Migratorios y sus Impactos

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/Logo.png" alt="Logo de Insight Analysts Collective">
</p>

## Descripción General

Somos **Insight Analysts collective**, un equipo de analistas de datos contratados por el Ministerio de Migración de Canadá para llevar a cabo este proyecto en el que se analizarán patrones de migración en América, revelando información importante sobre oportunidades en distintos aspectos a tener en cuenta (económico, social, educativo, ambiental) para captar emigrantes y contribuir al enriquecimiento cultural y socioeconómico del país. A la vez se pondrá a disposición los datos revelados por este análisis para ayudar a los futuros emigrantes a tomar una decisión informada en cuanto a la migración.

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/mapa.png" alt="Logo de Insight Analysts Collective">
</p>

## Índice

1. [Objetivo Principal](#objetivo-principal)
2. [Metodología de trabajo](#metodología-de-trabajo)
3. [📜 Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos](#📜-sprint-1-puesta-en-marcha-del-proyecto-y-trabajo-con-datos)
4. [ETL (Extracción Transformación y Carga)](#etl-extracción-transformación-y-carga)
5. [Exploración de Datos (EDA)](#exploración-de-datos-eda)
6. [KPIs (Indicadores Clave de Desempeño)](#kpis-indicadores-clave-de-desempeño)
7. [Stack tecnológico seleccionado](#stack-tecnológico-seleccionado)
8. [Presentación sprint 1](#presentación-sprint-1)
9. [👨‍💻 Sprint #2: Data Engineering](#👨‍💻-sprint-2-data-engineering)
10. [Estructura de datos implementada (Data Lake)](#estructura-de-datos-implementada-data-lake)
11. [WorkFlow y tecnologías](#workflow-y-tecnologías)
12. [PIPELINE ETL (AWS CLOUD)](#pipeline-etl-aws-cloud)
13. [Validación de datos](#validación-de-datos)
14. [Diccionario de datos](#diccionario-de-datos)
15. [MVP Dashboard](#mvp-dashboard)
16. [Presentación](#presentación)

## Objetivo principal

El objetivo principal de este proyecto es desarrollar una estrategia integral que promueva la emigración de la comunidad latina hacia Canadá, en lugar de Estados Unidos, basándonos en datos objetivos y análisis comparativos. Las meta son, en primer lugar, proporcionar al Ministerio de Migraciones de Canadá insights relevantes para realizar cambios en su estructura que den como resultado el aumento de migrantes latinos hacia Canadá. Y por otro lado, poner a disposición en el sitio de la embajada, éste mismo análisis, que provea información precisa sobre las oportunidades y ventajas que ofrece Canadá en términos de calidad de vida, empleo, educación y políticas de inmigración, guiando a futuros emigrantes hacia un proceso de toma de decisiones informado."

## Metodología de trabajo

En el marco del proyecto actual se ha adoptado la metodología ágil Scrum para la gestión y ejecución de tareas. El proyecto consta de 3 sprints, cada uno está definido por un período de tiempo de una semana durante la cual se desarrolla y entrega un conjunto de funcionalidades:

- 📜 Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos
- 👨‍💻 Sprint #2: Data Engineering
- 📈 Sprint #3: Data Analytics + ML

Esta metodología nos permite usar un enfoque iterativo e incremental en el que día a día se ven los avances y agregados de valor al proyecto en conjunto con el Scrum Master. Luego al finalizar cada semana se culmina con el sprint mediante una presentación del proyecto a nuestro Product Owner.

El **equipo de trabajo** está compuesto por un grupo de 4 desarrolladores:
* **Antonella Nieto** - Ingeniera de datos
* **Carlos Días Colodrero** - Ingeniero de datos
* **Yuri Díaz** - Analista de datos
* **Florencia Miranda** - Científica de datos

Nuestro **cronograma de trabajo** fue gestionado a través de la plataforma Monday y lo pueden ver en en el siguiente [Enlace](https://flormiranda1995s-team.monday.com/boards/5064412581/).

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/semana1.png" alt="Logo de Insight Analysts Collective">
</p>

# 📜 Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos

## ETL (Extracción Transformación y Carga)
Para este trabajo utilizamos un dataset de la ONU, en específico del Department of Economics and Social Affairs. El dataset nos proporciona datos cada 5 años desde 1990 a 2020 con el destino de los migrantes, segmentado por regiones, continentes, nivel de ingresos y de desarrollo de los países receptores. En el siguiente
[link](https://www.un.org/development/desa/pd/content/international-migrant-stock) puede encontrarse más información relacionada. También se puede encontrar el dataset titulado *undesa.csv* en la carpeta "data" del repositorio.

Los procesos realizados fueron los siguientes:

* El dataset constaba de 8 tablas. Las tablas de la 2 a la 8 representaban cada año. Procedimos a crear una columna año a cada tabla. 
* Unimos las tablas en un solo dataset.
* Sustituímos valores no numéricos y cambiamos los tipos de datos de las columnas.
* Cambiamos nombres de las columnas y eliminamos las no pertinentes para nuesto objetivo.
* Exportamos el dataset resultante limpio. 

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

Hemos definido cuatro Indicadores Clave de Desempeño (KPIs) que serán fundamentales para nuestro estudio:

1. **Vistas al informe**:
   
KPI: Conseguir 100 vistas del informe por mes

Métrica: vistas al dashboard

Cálculo del KPI: vistas_actuales/vistas_objetivo*100 (100)

2. **Aumento de migrantes Canadá**:
   
KPI: Observar un aumento del 10% en la cantidad de migrantes desde países con alta tasa de alfabetización el próximo año

Métrica: Cantidad de migrantes anual

Cálculo del KPI: ((Migrantes a la fecha / Migrantes un año atras) - 1) * 100

3. **Disminución de migrantes EEUU** (Suponiendo que Canadá captaría estos migrantes)
   
KPI: Observar una disminución del 3% en la cantidad de migrantes que eligen como destino EEUU provenientes de países con alta tasa de desempleo durante el próximo año

Métrica: Cantidad de migrantes anual

Cálculo del KPI: ((Migrantes a la fecha / Migrantes un año atras) - 1) * 100

**Justificación y Alusión a la Atracción para Inmigrantes en relación con el PIB:**
Un aumento del PBI puede hacer que un país sea más atractivo para los inmigrantes, ya que suele estar relacionado con una mayor demanda de mano de obra y más oportunidades económicas. El PIB es una medida clave de la salud económica de un país y, si el PBI de Canadá aumenta significativamente en paralelo con un aumento en la tasa de migración desde América Latina, se podría argumentar que el país ofrece un entorno económico favorable y oportunidades de crecimiento, lo que a su vez atraería a más migrantes en busca de una mejor calidad de vida y mayores perspectivas laborales. Este KPI busca establecer una conexión tangible entre el aumento del PIB y el interés de los migrantes, demostrando cómo un entorno económico en crecimiento puede influir en la decisión de migrar hacia Canadá.

4. **Aumento del PIB per cápita (Canadá)**
   
KPI: Lograr un incremento del 5% en el PIB de Canadá el próximo año

Métrica: PIB per cápita anual

Cálculo del KPI: ((PIB actual / PBI año anterior) - 1) * 100

5. **Aumento del PIB en conjunto con el aumento en la tasa de migración:**
   
KPI: Lograr un incremento del 5% en el PIB de Canadá en el mismo período en el que se observe un aumento del 10% en la tasa de migración desde América Latina del próximo año

Métrica PBI: Cambio porcentual en el PBI de Canadá

Métrica Tasa de Migración: Cambio porcentual en la tasa de migración desde América Latina hacia Canadá

Cálculo del KPI:

a- Calcular el cambio porcentual en el PBI de Canadá: ((PBI actual - PBI anterior) / PBI anterior) * 100

b- Calcular el cambio porcentual en la tasa de migración desde América Latina: ((Tasa actual - Tasa anterior) / Tasa anterior) * 100

c- Evaluar si el aumento del PBI y el aumento en la tasa de migración coinciden en el mismo período y si la relación es al menos 10:15 (considerando el aumento del 10% en PBI y el aumento del 15% en migración)

d- Si se cumple la relación, se considera que el KPI se ha logrado

## Stack tecnológico seleccionado:

- Data Pipeline y Data Lake: AWS Glue y S3 Amazon para la ingesta y transformación de datos.
* Bibliotecas de Python: Pandas, Numpy, Seaborn, Matplotlib.
- Base de Datos: PostgreSQL para almacenar y gestionar datos.
- Data Warehouse: Amazon Redshift para análisis de datos a gran escala.
- Dashboard: PowerBI para visualización interactiva de resultados.
- Modelos Predictivos: Python con bibliotecas como scikit-learn y TensorFlow.


# 👨‍💻 Sprint #2: Data Engineering

## Estructura de datos implementada (Data Lake):

En nuestro proyecto de Análisis de Flujos Migratorios y sus Impactos, hemos optado por implementar un modelo no relacional, específicamente un Data Lake, en lugar de un modelo relacional tradicional. Esta elección se basa en una serie de fundamentos clave que respaldan nuestra decisión:

1. **Naturaleza de los Datos:**

Los datos que manejamos son heterogéneos y no siguen una estructura fija de relaciones. Un modelo relacional tradicional sería inadecuado para representar eficazmente esta variedad de datos, que incluyen flujos migratorios y datos socioeconómicos de diversas fuentes.

2. **Escalabilidad y Flexibilidad:**

Un Data Lake, en particular Amazon S3, proporciona escalabilidad ilimitada y flexibilidad necesaria para manejar grandes volúmenes de datos no estructurados o semiestructurados. Esto es esencial ya que trabajamos con una amplia gama de datos que pueden crecer con el tiempo.

3. **Rendimiento de Análisis:**

La estructura del Data Lake permite la ejecución de análisis de datos avanzados y personalizados sin restricciones impuestas por un esquema de tabla predefinido. Esto es esencial para nuestro proyecto, donde necesitamos explorar datos complejos y buscar patrones específicos.

## WorkFlow y tecnologías

El flujo de trabajo comienza con la carga de datos crudos en el Data Lake (bucket de S3 "Data inicial"). Luego, una primera función Lambda realiza la transformación inicial y carga los datos transformados en un segundo bucket de S3 llamado "Data Final". Una segunda función Lambda se encarga de la carga incremental y la validación de datos duplicados en el mismo "Data Final" bucket. Este flujo de trabajo garantiza que los datos se transformen, procesen y validen de manera eficiente antes de ser almacenados en el "Data Final" bucket, lo que proporciona un proceso de ETL escalable y confiable.

1) Creación del Data-lake (Buckets data inicial y data final) - **AWS S3**
  
2) Creación de función para la carga inicial y transformaciones de datos crudos - **AWS Lambda**
  
3) Creación de función para la carga incremental de datos y validación de duplicados - **AWS Lambda**
  
4) Conexión del bucket de data final con PowerBI - **AWS S3/Script de python**
  
5) MVP Dashboard con los datos extraídos - **PowerBI**

## PIPELINE ETL (AWS CLOUD)

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/PIPELINE.png" alt="PIPELINE">
</p>

## [Función Lambda para ETL Automatizado:](https://github.com/Carlit0sCDC/migraciones-TPF/tree/main/lambda-etl)

La función Lambda, denominada "lambda_handler," es una parte esencial de nuestro flujo de trabajo de procesamiento de datos en la nube. Esta función se encarga de realizar la etapa de transformación en el proceso ETL (Extracción, Transformación y Carga) de datos. Permíteme desglosar cómo funciona en detalle:

1. **Detección de Eventos:**

Lambda se encuentra en un estado de escucha activa, esperando eventos que desencadenen su ejecución. En este caso, está configurada para responder a eventos relacionados con cambios en los "buckets" de Amazon S3. Cuando se carga un nuevo archivo en un "bucket" específico, Lambda se inicia automáticamente. Esta detección de eventos es fundamental para el flujo de trabajo automatizado.

2. **Preparación para el Trabajo:**

Antes de procesar los datos, Lambda necesita información sobre dónde encontrar el archivo y dónde colocar los resultados. Esto se logra a través de la configuración previa, lo que permite a Lambda interactuar con los servicios de AWS.

3. **Recuperación de Datos:**

Lambda accede al archivo en el "bucket" de S3 especificado y recupera los datos. Esto se realiza de manera eficiente y sin problemas, lo que garantiza que ningún dato se pierda en el proceso.

4. **Transformación de Datos:**

Aquí reside el núcleo del trabajo de Lambda. Los datos brutos generalmente no están en el formato ideal para su análisis. Lambda realiza una serie de transformaciones según las reglas especificadas. Por ejemplo, puede convertir cadenas en mayúsculas, corregir datos erróneos y eliminar duplicados. Este proceso de transformación es altamente personalizable y se adapta a las necesidades específicas del proyecto.

5. **Almacenamiento de Datos Transformados:**

Una vez que los datos se han transformado con éxito, Lambda los coloca en un nuevo lugar dentro del mismo o de otro "bucket" de S3. Los datos transformados están ahora en un formato limpio y listos para su uso futuro.

6. **Finalización del Trabajo:**

Lambda completa su tarea y queda nuevamente en espera de eventos futuros. La velocidad y escalabilidad de Lambda permiten procesar grandes cantidades de datos en poco tiempo, lo que es esencial para un ETL ágil y eficiente.

En resumen, esta función Lambda realiza la fase de transformación del ETL de manera eficaz, asegurando que los datos estén limpios y listos para el análisis posterior. Su capacidad de respuesta a eventos y escalabilidad hacen que sea una herramienta poderosa en nuestro arsenal tecnológico para gestionar y transformar datos de manera automatizada.

## Validación de datos

En nuestro proyecto, damos una gran importancia a la validación de datos para garantizar la calidad y la integridad de la información que manejamos. Aquí hay algunas de las prácticas de validación de datos que implementamos:

- **Verificación de Integridad**: Antes de la carga de datos en nuestro sistema, realizamos comprobaciones de integridad para asegurarnos de que los datos sean coherentes y cumplan con las reglas establecidas.

- **Limpieza de Datos**: Implementamos procesos de limpieza de datos para eliminar valores nulos, duplicados y datos inconsistentes. Esto nos permite trabajar con datos confiables.

- **Validación de Formato**: Verificamos que los datos sigan el formato esperado, lo que incluye asegurarnos de que las fechas, números, minúsculas y mayúsculas y otros tipos de datos estén en el formato correcto.


- **Auditorías y Registros**: Mantenemos registros de las validaciones realizadas, lo que nos permite rastrear cambios y problemas en los datos.


<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/validacion_1.jpeg" alt="validacion1">
</p>

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/validacion_2.jpeg" alt="validacion2">
</p>

adjuntar imagenes de tabla antes del etl y despues del etl aqui...


## Diccionario de datos

Este es el link del [Diccionario de datos.](https://docs.google.com/spreadsheets/d/1Kqbgxvg3pzMPJwpafznR0o5v2Fp2Tjm3/edit#gid=1757762391)
 También puede encontrarse  dentro de la carpeta "documentación" del repositorio.
 

## MVP Dashboard

pegar screenshots dashboard aqui...


## Presentación
A continuación les dejamos el link a la [presentación](https://www.canva.com/design/DAFs-WJPipA/HwFAwaGHidStTdXKRimmOQ/edit) del proyecto.


**Queremos enfatizar que este proyecto es completamente ficticio y no implica ninguna relación de trabajo con el Ministerio de Migraciones ni con ninguna entidad gubernamental real. Tiene como único propósito fines educativos y de aprendizaje académico.**
