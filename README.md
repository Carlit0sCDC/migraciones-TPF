 # Proyecto de Análisis de Flujos Migratorios y sus Impactos

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/Logo.png" alt="Logo de Insight Analysts Collective">
</p>

## Descripción General

Somos **Insight Analysts collective** un equipo de analistas de datos contratados por el Ministerio de Migración de Canadá para llevar a cabo este proyecto en el que se analizarán patrones de migración en América, revelando información importante sobre oportunidades en distintos aspectos a tener en cuenta (económico, social, educativo, ambiental) para captar emigrantes y contribuir al enriquecimiento cultural y socioeconómico del país. A la vez se pondrá a dispoción los datos revelados por este análisis para ayudar a los futuros emigrantes a tomar una decisión informada en cuanto a la migración

<p align="center">
  <img src="https://github.com/Carlit0sCDC/migraciones-TPF/blob/main/img/mapa.png" alt="Logo de Insight Analysts Collective">
</p>

# Índice

1. [Objetivo Principal](#objetivo-principal)
2. [ETL (Extracción Transformación y Carga)](#etl-extracción-transformación-y-carga)
3. [Exploración de Datos (EDA)](#exploración-de-datos-eda)
4. [KPIs (Indicadores Clave de Desempeño)](#kpis-indicadores-clave-de-desempeño)
5. [Tecnologías Utilizadas](#tecnologías-utilizadas)
6. [Equipo](#equipo)

## Objetivo principal modificado

El objetivo principal de este proyecto es desarrollar una estrategia integral que promueva la emigración de la comunidad latina hacia Canadá, en lugar de Estados Unidos, basándonos en datos objetivos y análisis comparativos. Las meta son, en primer lugar, proporcionar al Ministerio de Migraciones de Canadá insights relevantes para realizar cambios en su estructura que den como resultado el aumento de migrantes latinos hacia Canadá. Y por otro lado, poner a disposición en el sitio de la embajada, éste mismo análisis, que provea información precisa sobre las oportunidades y ventajas que ofrece Canadá en términos de calidad de vida, empleo, educación y políticas de inmigración, guiando a futuros emigrantes hacia un proceso de toma de decisiones informado."

## Flujo de trabajo
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

## KPIs (Indicadores Clave de Desempeño)

Hemos definido cuatro Indicadores Clave de Desempeño (KPIs) que serán fundamentales para nuestro estudio:

1. **Oportunidades laborales y crecimiento económico:** Aumentando la oferta laboral el objetivo seria aumentar un 10% en algunos sectores como tecnología.
2. **Calidad de vida:** mejorar el ranking de estilo de vida mundial de Canada. Objetivo estar en los top 10 del mundo.
3. **Diversidad e inclusion:** Mejorar la inclusion y diversidad de Canada. Objetivo mejor el índice de diversidad de 0.75, reflejando el compromiso de la inclusividad y diferentes culturas en Canada. Resaltando la bienvenida del país a los inmigrantes.
4. **Educación:**  Crecimiento de los estudiantes en universidades. Objetivo de resaltar un 15% de mas estudiantes anualmente para que Canada resalte ante otros paises.

Nuevas propuestas:

5. **Vistas al informe**:
KPI: Conseguir 100 vistas del informe por mes.
Métrica: vistas al dashboard.
Cálculo del KPI: vistas_actuales/vistas_objetivo*100 (100)

6. **Variación en la Tasa de Migración por País de Origen**:
KPI: Observar un aumento del 10% en la tasa de migración desde países con alto indice de pobreza y alta tasa de alfabetización el próximo año.
Métrica: Cambio porcentual en la tasa de migración.
Cálculo del KPI: ((Tasa actual - Tasa anterior) / Tasa anterior) * 100

7. **Variación en la Tasa de Migración de EEUU** (Suponiendo que Canadá captaría estos emigrantes que se disminuyen en eeuu)
KPI: Observar una disminución del 5% en la tasa de migración desde países con alto desempleo y alta tasa de alfabetización el próximo año.
Métrica: Cambio porcentual en la tasa de migración de eeuu.
Cálculo del KPI: ((Tasa actual - Tasa anterior) / Tasa anterior) * 100

**Justificación y Alusión a la Atracción para Inmigrantes en relación con el PBI:**
Un aumento del PBI puede hacer que un país sea más atractivo para los inmigrantes, ya que suele estar relacionado con una mayor demanda de mano de obra y más oportunidades económicas. El PBI es una medida clave de la salud económica de un país y, si el PBI de Canadá aumenta significativamente en paralelo con un aumento en la tasa de migración desde América Latina, se podría argumentar que el país ofrece un entorno económico favorable y oportunidades de crecimiento, lo que a su vez atraería a más migrantes en busca de una mejor calidad de vida y mayores perspectivas laborales. Este KPI busca establecer una conexión tangible entre el aumento del PBI y el interés de los migrantes, demostrando cómo un entorno económico en crecimiento puede influir en la decisión de migrar hacia Canadá.

8. **Aumento del PIB nacional(canadá)**
KPI: Lograr un incremento del 10% en el PBI de Canadá el próximo año
Métrica: Cambio porcentual en el PBI de Canadá
Cálculo del KPI: ((PBI actual - PBI anterior) / PBI anterior) * 100

9. **2da opción kpi anterior: aumento del pib en conjunto con el aumento en la tasa de migración:**
KPI: Lograr un incremento del 10% en el PBI de Canadá en el mismo período en el que se observe un aumento del 15% en la tasa de migración desde América Latina del próximo año.
Métrica PBI: Cambio porcentual en el PBI de Canadá.
Métrica Tasa de Migración: Cambio porcentual en la tasa de migración desde América Latina hacia Canadá.
Cálculo del KPI:
a- Calcular el cambio porcentual en el PBI de Canadá: ((PBI actual - PBI anterior) / PBI anterior) * 100.
b- Calcular el cambio porcentual en la tasa de migración desde América Latina: ((Tasa actual - Tasa anterior) / Tasa anterior) * 100.
c- Evaluar si el aumento del PBI y el aumento en la tasa de migración coinciden en el mismo período y si la relación es al menos 10:15 (considerando el aumento del 10% en PBI y el aumento del 15% en migración).
d- Si se cumple la relación, se considera que el KPI se ha logrado.

## Tecnologías Utilizadas

- Data Pipeline y Data Lake: AWS Glue y S3 Amazon para la ingesta y transformación de datos.
- Base de Datos: PostgreSQL para almacenar y gestionar datos.
- Data Warehouse: Amazon Redshift para análisis de datos a gran escala.
- Dashboard: Tableau para visualización interactiva de resultados.
- Modelos Predictivos: Python con bibliotecas como scikit-learn y TensorFlow.

## Equipo

- Antonella Nieto
- Carlos Diaz Colodrero
- Florencia Miranda
- Yuri Diaz

** agregar link al monday y una captura de pantalla y link a la presentación**
---

¡Agradecemos a la ONG internacional por brindarnos la oportunidad de contribuir a este importante estudio sobre flujos migratorios y su impacto en la sociedad!
