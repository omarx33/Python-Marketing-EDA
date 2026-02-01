# 🏦 Bank Marketing - Análisis Exploratorio de Datos (EDA)

## 📋 Descripción del Proyecto

Aplicación interactiva desarrollada con **Streamlit** para realizar un análisis exploratorio exhaustivo del dataset **BankMarketing**, que contiene información de una campaña de marketing directo de una institución financiera portuguesa.

### 🎯 Objetivo

Analizar los factores que influyen en la aceptación de depósitos a plazo por parte de los clientes, identificando patrones y relaciones relevantes en los datos que permitan mejorar futuras campañas de marketing.

---

## 👨‍💻 Autor

- **Nombre:** carlos mori huamani
- **Curso:** Especialización en Python for Analytics

---

## 🗂️ Estructura del Proyecto

```
bank-marketing-eda/
├── app.py                    # Aplicación principal de Streamlit
├── data_analyzer.py          # Clase para análisis de datos (POO)
├── requirements.txt          # Dependencias del proyecto
├── BankMarketing.csv         # Dataset
└── README.md                 # Este archivo
```

---

## 📊 Sobre el Dataset

### Información General
- **Registros:** 41,188 clientes
- **Variables:** 21 columnas
- **Fuente:** UCI Machine Learning Repository
- **Contexto:** Campaña de marketing de institución bancaria portuguesa

### Variables Principales

| Variable | Descripción |
|----------|-------------|
| `age` | Edad del cliente |
| `job` | Tipo de trabajo |
| `marital` | Estado civil |
| `education` | Nivel educativo |
| `default` | ¿Tiene crédito en mora? |
| `housing` | ¿Tiene crédito hipotecario? |
| `loan` | ¿Tiene crédito personal? |
| `contact` | Canal de comunicación |
| `duration` | Duración del contacto (segundos) |
| `campaign` | Número de contactos en la campaña |
| `y` | **Variable objetivo:** ¿Aceptó el depósito? (yes/no) |

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Streamlit** - Framework para aplicaciones web
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Matplotlib** - Visualización de datos
- **Seaborn** - Visualización estadística

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/omarx33/Python-Marketing-EDA.git

```

### 2. Crear entorno virtual 

```bash
python -m venv venv


```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📱 Funcionalidades

### 🏠 Módulo Home
- Presentación del proyecto
- Contexto del negocio
- Información del dataset
- Tecnologías utilizadas

### 📂 Módulo Carga de Datos
- Carga interactiva de archivos CSV
- Validación de datos
- Vista previa del dataset
- Información de dimensiones y tipos de datos

### 📊 Módulo EDA (Análisis Exploratorio)
El módulo de EDA incluye **10 análisis completos**:

1. **Información general del dataset** - `.info()`, tipos de datos, valores nulos
2. **Clasificación de variables** - Numéricas vs Categóricas
3. **Estadísticas descriptivas** - Media, mediana, dispersión
4. **Análisis de valores faltantes** - Identificación y visualización
5. **Distribución de variables numéricas** - Histogramas con KDE
6. **Análisis de variables categóricas** - Gráficos de barras y proporciones
7. **Análisis bivariado numérico vs categórico** - Boxplots y comparaciones
8. **Análisis bivariado categórico vs categórico** - Tablas cruzadas y heatmaps
9. **Análisis dinámico con parámetros** - Widgets interactivos
10. **Hallazgos clave** - Insights y conclusiones

---

## 🎨 Características Técnicas

### Programación Orientada a Objetos (POO)
- Clase `DataAnalyzer` que encapsula toda la lógica de análisis
- Métodos reutilizables y bien documentados
- Separación de responsabilidades

### Widgets Interactivos de Streamlit
- ✅ `st.sidebar` - Navegación principal
- ✅ `st.tabs` - Organización del contenido
- ✅ `st.columns` - Layout responsivo
- ✅ `st.selectbox` - Selección de opciones
- ✅ `st.multiselect` - Selección múltiple
- ✅ `st.slider` - Filtros numéricos
- ✅ `st.checkbox` - Opciones booleanas
- ✅ `st.file_uploader` - Carga de archivos

---

## 📈 Resultados y Conclusiones

### Principales Hallazgos

1. **Tasa de Conversión Crítica**: La campaña actual tiene una tasa de aceptación del 11.27%, por debajo del objetivo del 12%, lo que requiere una optimización urgente de la estrategia de contacto.

2. **Impacto de la Duración del Contacto**: Los contactos que resultaron en aceptación tienen una duración promedio significativamente mayor (558 segundos) comparado con los rechazos (221 segundos), sugiriendo que invertir más tiempo por llamada incrementa las probabilidades de éxito.

3. **Segmentación por Nivel Educativo**: Los clientes con educación universitaria muestran una tasa de aceptación 40% mayor que aquellos con educación básica, indicando la importancia de segmentar las campañas por perfil educativo.

4. **Canal de Comunicación Óptimo**: El contacto celular demuestra una efectividad 2.5 veces superior al contacto telefónico fijo, recomendando priorizar este canal en futuras campañas.

5. **Perfil del Cliente Ideal**: Los clientes entre 30-40 años, con educación universitaria, empleados en servicios administrativos y sin préstamos personales vigentes, presentan la mayor tasa de conversión (18.5%), definiendo el target prioritario para las próximas campañas.

---

## 🔗 Enlaces

- **Repositorio GitHub:** https://github.com/omarx33/Python-Marketing-EDA.git
- **Aplicación Desplegada:** https://bank-marketing-eda-omarx33.streamlit.app/

---

