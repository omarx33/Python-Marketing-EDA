"""
Bank Marketing - Análisis Exploratorio de Datos (EDA)
Aplicación Streamlit para análisis de campaña de marketing bancario

Autor: carlos mori huamani
Curso: Especialización en Python for Analytics

"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_analyzer import DataAnalyzer

# Configuración de la página
st.set_page_config(
    page_title="Bank Marketing EDA",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        font-weight: bold;
        margin-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# =======================
# FUNCIONES AUXILIARES
# =======================

def load_data(uploaded_file):
    """
    Carga el dataset desde un archivo CSV
    """
    try:
        df = pd.read_csv(uploaded_file, sep=';')
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# =======================
# MÓDULO 1: HOME
# =======================

def show_home():
    """
    Módulo de presentación del proyecto
    """
    st.markdown('<h1 class="main-header">Bank Marketing - Análisis Exploratorio de Datos</h1>', 
                unsafe_allow_html=True)
    
    # Descripción del proyecto
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Objetivo del Proyecto")
        st.write("""
        Este proyecto tiene como objetivo realizar un **Análisis Exploratorio de Datos (EDA)** 
        sobre el dataset **BankMarketing.csv**, que contiene información de una campaña de marketing 
        directo de una institución financiera portuguesa.
        
        El análisis busca identificar patrones, relaciones y características relevantes de los clientes 
        que permitan comprender mejor los factores que influyen en la aceptación de depósitos a plazo.
        """)
        
        st.markdown("### 🎯 Contexto del Negocio")
        st.write("""
        La efectividad de las campañas de marketing cayó del **12%** al **8%** en los últimos 6 meses, 
        afectando los incentivos del equipo comercial. Este análisis exploratorio busca descubrir 
        insights que ayuden a mejorar futuras campañas.
        """)
    
    with col2:
        st.markdown("### 👨‍💻 Datos del Autor")
        st.info("""
        **Nombre:** Carlos Mori Huamani
        
        **Curso:** Especialización en Python for Analytics
        
        """)
    
    # Información del dataset
    st.markdown("---")
    st.markdown("### 📁 Sobre el Dataset")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Registros", "41,188")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Variables", "21")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Objetivo", "Variable 'y' (yes/no)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    El dataset contiene información demográfica, económica y de la campaña de marketing, 
    incluyendo variables como edad, ocupación, educación, contactos previos, y el resultado 
    de la campaña (si el cliente aceptó o no el depósito a plazo).
    """)
    
    # Tecnologías utilizadas
    st.markdown("---")
    st.markdown("### 🛠️ Tecnologías Utilizadas")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**🐍 Python**")
        st.write("Lenguaje base")
    
    with col2:
        st.markdown("**📊 Pandas**")
        st.write("Manipulación de datos")
    
    with col3:
        st.markdown("**📈 Matplotlib/Seaborn**")
        st.write("Visualización")
    
    with col4:
        st.markdown("**🎨 Streamlit**")
        st.write("Interfaz web")
    
    st.markdown("---")
    st.info("💡 **Nota:** Navega por el menú lateral para explorar los diferentes análisis del dataset.")

# =======================
# MÓDULO 2: CARGA DEL DATASET
# =======================

def show_data_loading():
    """
    Módulo para cargar y validar el dataset
    """
    st.markdown('<h1 class="main-header">📂 Carga del Dataset</h1>', unsafe_allow_html=True)
    
    st.markdown("### 📤 Sube tu archivo CSV")
    st.write("Por favor, carga el archivo **BankMarketing.csv** para comenzar el análisis.")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Selecciona el archivo CSV",
        type=['csv'],
        help="El archivo debe estar en formato CSV con separador ';'"
    )
    
    if uploaded_file is not None:
        # Cargar datos
        with st.spinner('Cargando datos...'):
            df = load_data(uploaded_file)
        
        if df is not None:
            # Guardar en session_state
            st.session_state['df'] = df
            st.session_state['data_loaded'] = True
            
            st.success("✅ ¡Archivo cargado exitosamente!")
            
            # Mostrar información básica
            st.markdown("---")
            st.markdown("### 📋 Vista Previa del Dataset")
            
            # Mostrar primeras filas
            st.dataframe(df.head(10), use_container_width=True)
            
            # Información de dimensiones
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("📊 Total de Filas", f"{df.shape[0]:,}")
            
            with col2:
                st.metric("📋 Total de Columnas", df.shape[1])
            
            with col3:
                memory_usage = df.memory_usage(deep=True).sum() / 1024**2
                st.metric("💾 Tamaño en Memoria", f"{memory_usage:.2f} MB")
            
            # Mostrar tipos de datos
            st.markdown("---")
            st.markdown("### 🔍 Tipos de Datos")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Columnas del Dataset:**")
                dtypes_df = pd.DataFrame({
                    'Columna': df.columns,
                    'Tipo de Dato': df.dtypes.values
                })
                st.dataframe(dtypes_df, use_container_width=True, height=400)
            
            with col2:
                st.write("**Resumen de Tipos:**")
                type_counts = df.dtypes.value_counts()
                fig, ax = plt.subplots(figsize=(8, 6))
                type_counts.plot(kind='bar', ax=ax, color='skyblue')
                ax.set_title('Distribución de Tipos de Datos', fontsize=14, fontweight='bold')
                ax.set_xlabel('Tipo de Dato')
                ax.set_ylabel('Cantidad')
                ax.tick_params(axis='x', rotation=45)
                st.pyplot(fig)
            
            st.markdown("---")
            st.info("✨ **Datos cargados correctamente.** Ahora puedes proceder con el análisis exploratorio desde el menú lateral.")
    
    else:
        st.warning("⚠️ Por favor, carga un archivo CSV para continuar.")
        st.info("💡 **Tip:** Asegúrate de que el archivo tenga el formato correcto y use ';' como separador.")

# =======================
# MÓDULO 3: EDA COMPLETO
# =======================
# Este código reemplaza la función show_eda() en app.py

def show_eda():
    """
    Módulo principal de Análisis Exploratorio de Datos con 10 ítems
    """
    st.markdown('<h1 class="main-header">📊 Análisis Exploratorio de Datos (EDA)</h1>', 
                unsafe_allow_html=True)
    
    # Verificar si hay datos cargados
    if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
        st.warning("⚠️ No hay datos cargados. Por favor, carga el dataset primero desde el menú 'Carga del Dataset'.")
        return
    
    df = st.session_state['df']
    
    # Crear instancia del analizador
    analyzer = DataAnalyzer(df)
    
    # Crear tabs para organizar los análisis
    tabs = st.tabs([
        "📋 Info General",
        "🔢 Variables",
        "📊 Estadísticas",
        "❌ Valores Faltantes",
        "📈 Dist. Numéricas",
        "📊 Dist. Categóricas",
        "🔀 Bivariado Num-Cat",
        "🔀 Bivariado Cat-Cat",
        "⚙️ Análisis Dinámico",
        "💡 Hallazgos Clave"
    ])
    
    # ======================
    # ÍTEM 1: INFORMACIÓN GENERAL
    # ======================
    with tabs[0]:
        st.markdown("## 📋 Ítem 1: Información General del Dataset")
        st.markdown("---")
        
        # Métricas principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📊 Filas", f"{df.shape[0]:,}")
        with col2:
            st.metric("📋 Columnas", df.shape[1])
        with col3:
            st.metric("💾 Memoria", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        with col4:
            st.metric("🔢 Valores Totales", f"{df.shape[0] * df.shape[1]:,}")
        
        st.markdown("---")
        
        # Información detallada
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📝 Tipos de Datos")
            info_dict = analyzer.get_basic_info()
            dtypes_df = pd.DataFrame({
                'Columna': list(info_dict['dtypes'].keys()),
                'Tipo': [str(v) for v in info_dict['dtypes'].values()],
                'Nulos': list(info_dict['null_counts'].values())
            })
            st.dataframe(dtypes_df, use_container_width=True, height=400)
        
        with col2:
            st.markdown("### 📊 Resumen de Tipos")
            type_summary = df.dtypes.value_counts()
            fig, ax = plt.subplots(figsize=(8, 6))
            type_summary.plot(kind='bar', ax=ax, color='steelblue')
            ax.set_title('Distribución de Tipos de Datos', fontsize=14, fontweight='bold')
            ax.set_xlabel('Tipo de Dato')
            ax.set_ylabel('Cantidad')
            ax.tick_params(axis='x', rotation=45)
            for i, v in enumerate(type_summary.values):
                ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        st.markdown("---")
        st.markdown("### 🔍 Vista Previa del Dataset")
        st.dataframe(df.head(20), use_container_width=True)
    
    # ======================
    # ÍTEM 2: CLASIFICACIÓN DE VARIABLES
    # ======================
    with tabs[1]:
        st.markdown("## 🔢 Ítem 2: Clasificación de Variables")
        st.markdown("---")
        
        var_class = analyzer.get_variable_classification()
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🔢 Variables Numéricas", var_class['n_numeric'])
        with col2:
            st.metric("📝 Variables Categóricas", var_class['n_categorical'])
        with col3:
            st.metric("📊 Total Variables", var_class['n_numeric'] + var_class['n_categorical'])
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🔢 Variables Numéricas")
            st.info("Variables que contienen valores numéricos (int, float)")
            for i, col in enumerate(var_class['numeric'], 1):
                st.write(f"{i}. `{col}` - Tipo: {df[col].dtype}")
        
        with col2:
            st.markdown("### 📝 Variables Categóricas")
            st.info("Variables que contienen categorías o texto")
            for i, col in enumerate(var_class['categorical'], 1):
                unique_count = df[col].nunique()
                st.write(f"{i}. `{col}` - Valores únicos: {unique_count}")
        
        st.markdown("---")
        
        # Gráfico de clasificación
        fig, ax = plt.subplots(figsize=(10, 6))
        counts = [var_class['n_numeric'], var_class['n_categorical']]
        labels = ['Numéricas', 'Categóricas']
        colors = ['#3498db', '#e74c3c']
        
        bars = ax.bar(labels, counts, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
        ax.set_title('Clasificación de Variables', fontsize=16, fontweight='bold')
        ax.set_ylabel('Cantidad', fontsize=12)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    # ======================
    # ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
    # ======================
    with tabs[2]:
        st.markdown("## 📊 Ítem 3: Estadísticas Descriptivas")
        st.markdown("---")
        
        st.markdown("### 🔢 Variables Numéricas")
        desc_stats = analyzer.get_descriptive_stats()
        st.dataframe(desc_stats.style.background_gradient(cmap='Blues'), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 💡 Interpretación de Estadísticas Clave")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📈 Medidas de Tendencia Central")
            selected_var = st.selectbox("Selecciona una variable:", analyzer.numeric_cols)
            
            stats = analyzer.get_summary_statistics(selected_var)
            
            st.metric("Media (Promedio)", f"{stats['Media']:.2f}")
            st.metric("Mediana (Valor Central)", f"{stats['Mediana']:.2f}")
            st.metric("Moda (Más Frecuente)", f"{stats['Moda']:.2f}" if stats['Moda'] else "N/A")
            
            st.info(f"""
            **Interpretación:**
            - La **media** es {stats['Media']:.2f}
            - La **mediana** es {stats['Mediana']:.2f}
            - {'La media es mayor que la mediana, sugiriendo una distribución sesgada a la derecha.' if stats['Media'] > stats['Mediana'] else 'La media es menor que la mediana, sugiriendo una distribución sesgada a la izquierda.' if stats['Media'] < stats['Mediana'] else 'Media y mediana son similares, sugiriendo una distribución simétrica.'}
            """)
        
        with col2:
            st.markdown("#### 📊 Medidas de Dispersión")
            st.metric("Desviación Estándar", f"{stats['Desviación Estándar']:.2f}")
            st.metric("Rango (Max - Min)", f"{stats['Máximo'] - stats['Mínimo']:.2f}")
            st.metric("Coeficiente de Variación", f"{(stats['Desviación Estándar'] / stats['Media'] * 100):.2f}%")
            
            st.info(f"""
            **Interpretación:**
            - **Desviación Estándar:** {stats['Desviación Estándar']:.2f}
            - Los datos varían en promedio ±{stats['Desviación Estándar']:.2f} unidades respecto a la media
            - **Rango IQR (Q3-Q1):** {stats['Q3'] - stats['Q1']:.2f}
            """)
    
    # ======================
    # ÍTEM 4: VALORES FALTANTES
    # ======================
    with tabs[3]:
        st.markdown("## ❌ Ítem 4: Análisis de Valores Faltantes")
        st.markdown("---")
        
        missing_analysis = analyzer.get_missing_values_analysis()
        
        total_missing = missing_analysis['Valores_Nulos'].sum()
        total_cells = df.shape[0] * df.shape[1]
        missing_pct = (total_missing / total_cells) * 100
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🔢 Total Valores Faltantes", f"{total_missing:,}")
        with col2:
            st.metric("📊 Porcentaje Total", f"{missing_pct:.2f}%")
        with col3:
            status = "✅ Excelente" if missing_pct == 0 else "⚠️ Requiere Atención"
            st.metric("Estado", status)
        
        st.markdown("---")
        
        if total_missing == 0:
            st.success("✅ **¡Excelente!** Este dataset no tiene valores faltantes.")
            st.balloons()
        else:
            st.warning(f"⚠️ Se encontraron {total_missing:,} valores faltantes ({missing_pct:.2f}%)")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 📋 Tabla de Valores Faltantes")
                st.dataframe(missing_analysis, use_container_width=True)
            
            with col2:
                st.markdown("### 📊 Visualización")
                fig, ax = plt.subplots(figsize=(10, 6))
                missing_cols = missing_analysis[missing_analysis['Valores_Nulos'] > 0]
                if len(missing_cols) > 0:
                    ax.barh(missing_cols['Columna'], missing_cols['Porcentaje'], color='salmon')
                    ax.set_xlabel('Porcentaje de Valores Faltantes')
                    ax.set_title('Distribución de Valores Faltantes', fontweight='bold')
                    plt.tight_layout()
                    st.pyplot(fig)
                else:
                    st.info("No hay valores faltantes para visualizar")
                plt.close()
    
    # ======================
    # ÍTEM 5: DISTRIBUCIÓN VARIABLES NUMÉRICAS
    # ======================
    with tabs[4]:
        st.markdown("## 📈 Ítem 5: Distribución de Variables Numéricas")
        st.markdown("---")
        
        st.markdown("### 🔍 Selecciona Variables a Analizar")
        
        selected_numeric = st.multiselect(
            "Elige una o más variables numéricas:",
            analyzer.numeric_cols,
            default=analyzer.numeric_cols[:3]
        )
        
        if selected_numeric:
            # Mostrar distribuciones
            for col in selected_numeric:
                st.markdown(f"### 📊 Distribución de: **{col}**")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    analyzer.plot_numeric_distribution(col, ax=ax)
                    st.pyplot(fig)
                    plt.close()
                
                with col2:
                    stats = analyzer.get_summary_statistics(col)
                    st.markdown("#### 📊 Estadísticas")
                    st.metric("Media", f"{stats['Media']:.2f}")
                    st.metric("Mediana", f"{stats['Mediana']:.2f}")
                    st.metric("Desv. Std", f"{stats['Desviación Estándar']:.2f}")
                    st.metric("Mínimo", f"{stats['Mínimo']:.2f}")
                    st.metric("Máximo", f"{stats['Máximo']:.2f}")
                
                st.markdown("---")
        else:
            st.info("Por favor, selecciona al menos una variable numérica.")
    
    # ======================
    # ÍTEM 6: VARIABLES CATEGÓRICAS
    # ======================
    with tabs[5]:
        st.markdown("## 📊 Ítem 6: Análisis de Variables Categóricas")
        st.markdown("---")
        
        selected_cat = st.selectbox(
            "Selecciona una variable categórica:",
            analyzer.categorical_cols
        )
        
        if selected_cat:
            st.markdown(f"### 📊 Análisis de: **{selected_cat}**")
            
            # Conteos y proporciones
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🔢 Conteos Absolutos")
                counts = analyzer.get_value_counts(selected_cat, normalize=False)
                st.dataframe(counts.reset_index().rename(columns={'index': selected_cat, selected_cat: 'Frecuencia'}), 
                           use_container_width=True)
            
            with col2:
                st.markdown("#### 📊 Proporciones (%)")
                proportions = analyzer.get_value_counts(selected_cat, normalize=True) * 100
                st.dataframe(proportions.reset_index().rename(columns={'index': selected_cat, selected_cat: 'Porcentaje'}), 
                           use_container_width=True)
            
            st.markdown("---")
            
            # Visualización
            st.markdown("### 📈 Visualización")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Gráfico de Barras")
                fig, ax = plt.subplots(figsize=(10, 6))
                analyzer.plot_categorical_distribution(selected_cat, ax=ax)
                st.pyplot(fig)
                plt.close()
            
            with col2:
                st.markdown("#### Gráfico de Pastel")
                fig, ax = plt.subplots(figsize=(10, 6))
                counts = analyzer.get_value_counts(selected_cat, normalize=False)
                ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
                ax.set_title(f'Distribución de {selected_cat}', fontweight='bold', fontsize=14)
                st.pyplot(fig)
                plt.close()
    
    # ======================
    # ÍTEM 7: BIVARIADO NUMÉRICO VS CATEGÓRICO
    # ======================
    with tabs[6]:
        st.markdown("## 🔀 Ítem 7: Análisis Bivariado (Numérico vs Categórico)")
        st.markdown("---")
        
        st.markdown("### 🔍 Selecciona Variables a Comparar")
        
        col1, col2 = st.columns(2)
        
        with col1:
            numeric_var = st.selectbox("Variable Numérica:", analyzer.numeric_cols, key='biv_num')
        
        with col2:
            categorical_var = st.selectbox("Variable Categórica:", analyzer.categorical_cols, key='biv_cat')
        
        if numeric_var and categorical_var:
            st.markdown(f"### 📊 Análisis: **{numeric_var}** vs **{categorical_var}**")
            
            # Boxplot
            st.markdown("#### 📦 Boxplot Comparativo")
            fig, ax = plt.subplots(figsize=(14, 6))
            analyzer.plot_bivariate_numeric_categorical(numeric_var, categorical_var, ax=ax)
            st.pyplot(fig)
            plt.close()
            
            st.markdown("---")
            
            # Estadísticas por grupo
            st.markdown("#### 📊 Estadísticas por Grupo")
            group_stats = df.groupby(categorical_var)[numeric_var].describe()
            st.dataframe(group_stats.style.background_gradient(cmap='Greens'), use_container_width=True)
            
            # Interpretación
            st.markdown("#### 💡 Interpretación")
            max_mean_group = df.groupby(categorical_var)[numeric_var].mean().idxmax()
            min_mean_group = df.groupby(categorical_var)[numeric_var].mean().idxmin()
            
            st.info(f"""
            **Hallazgos:**
            - El grupo con mayor promedio de **{numeric_var}** es: **{max_mean_group}**
            - El grupo con menor promedio es: **{min_mean_group}**
            - Esto sugiere que existe una relación entre {categorical_var} y {numeric_var}
            """)
    
    # ======================
    # ÍTEM 8: BIVARIADO CATEGÓRICO VS CATEGÓRICO
    # ======================
    with tabs[7]:
        st.markdown("## 🔀 Ítem 8: Análisis Bivariado (Categórico vs Categórico)")
        st.markdown("---")
        
        st.markdown("### 🔍 Selecciona Variables a Cruzar")
        
        col1, col2 = st.columns(2)
        
        with col1:
            cat_var1 = st.selectbox("Primera Variable:", analyzer.categorical_cols, key='cat1')
        
        with col2:
            cat_var2 = st.selectbox("Segunda Variable:", analyzer.categorical_cols, key='cat2')
        
        if cat_var1 and cat_var2 and cat_var1 != cat_var2:
            st.markdown(f"### 📊 Análisis: **{cat_var1}** vs **{cat_var2}**")
            
            # Tabla cruzada
            st.markdown("#### 📋 Tabla Cruzada (Frecuencias)")
            crosstab = pd.crosstab(df[cat_var1], df[cat_var2])
            st.dataframe(crosstab, use_container_width=True)
            
            st.markdown("---")
            
            # Heatmap
            st.markdown("#### 🔥 Heatmap de Relación")
            fig, ax = plt.subplots(figsize=(12, 8))
            analyzer.plot_categorical_crosstab(cat_var1, cat_var2, ax=ax)
            st.pyplot(fig)
            plt.close()
            
            st.markdown("---")
            
            # Proporciones
            st.markdown("#### 📊 Tabla de Proporciones (%)")
            crosstab_pct = pd.crosstab(df[cat_var1], df[cat_var2], normalize='index') * 100
            st.dataframe(crosstab_pct.style.background_gradient(cmap='YlOrRd'), use_container_width=True)
        
        elif cat_var1 == cat_var2:
            st.warning("⚠️ Por favor, selecciona dos variables diferentes.")
    
    # ======================
    # ÍTEM 9: ANÁLISIS DINÁMICO
    # ======================
    with tabs[8]:
        st.markdown("## ⚙️ Ítem 9: Análisis Basado en Parámetros Seleccionados")
        st.markdown("---")
        
        st.markdown("### 🎨 Crea Tu Propio Análisis Personalizado")
        
        analysis_type = st.radio(
            "Tipo de análisis:",
            ["Filtrado por Rango", "Comparación Múltiple", "Correlación Personalizada"]
        )
        
        if analysis_type == "Filtrado por Rango":
            st.markdown("#### 📊 Filtrado Dinámico por Rango")
            
            numeric_col = st.selectbox("Variable numérica:", analyzer.numeric_cols, key='filter_col')
            
            min_val = float(df[numeric_col].min())
            max_val = float(df[numeric_col].max())
            
            range_vals = st.slider(
                f"Selecciona el rango de {numeric_col}:",
                min_val, max_val, (min_val, max_val)
            )
            
            filtered_df = df[(df[numeric_col] >= range_vals[0]) & (df[numeric_col] <= range_vals[1])]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Registros Filtrados", f"{len(filtered_df):,}")
            with col2:
                st.metric("% del Total", f"{(len(filtered_df)/len(df)*100):.1f}%")
            with col3:
                st.metric("Registros Excluidos", f"{len(df)-len(filtered_df):,}")
            
            st.dataframe(filtered_df.head(20), use_container_width=True)
        
        elif analysis_type == "Comparación Múltiple":
            st.markdown("#### 📊 Comparación de Múltiples Variables")
            
            selected_vars = st.multiselect(
                "Selecciona variables numéricas a comparar:",
                analyzer.numeric_cols,
                default=analyzer.numeric_cols[:3]
            )
            
            if len(selected_vars) >= 2:
                # Gráfico de dispersión
                fig, ax = plt.subplots(figsize=(12, 8))
                for var in selected_vars:
                    ax.hist(df[var], alpha=0.5, label=var, bins=30)
                ax.legend()
                ax.set_xlabel('Valor')
                ax.set_ylabel('Frecuencia')
                ax.set_title('Comparación de Distribuciones', fontweight='bold', fontsize=14)
                st.pyplot(fig)
                plt.close()
        
        elif analysis_type == "Correlación Personalizada":
            st.markdown("#### 📊 Matriz de Correlación Personalizada")
            
            selected_vars = st.multiselect(
                "Selecciona variables para análisis de correlación:",
                analyzer.numeric_cols,
                default=analyzer.numeric_cols[:5]
            )
            
            if len(selected_vars) >= 2:
                fig, ax = plt.subplots(figsize=(10, 8))
                analyzer.plot_correlation_heatmap(selected_vars, ax=ax)
                st.pyplot(fig)
                plt.close()
                
                st.markdown("---")
                st.markdown("#### 📋 Tabla de Correlación")
                corr_matrix = analyzer.get_correlation_matrix(selected_vars)
                st.dataframe(corr_matrix.style.background_gradient(cmap='coolwarm', vmin=-1, vmax=1), 
                           use_container_width=True)
    
    # ======================
    # ÍTEM 10: HALLAZGOS CLAVE
    # ======================
    with tabs[9]:
        st.markdown("## 💡 Ítem 10: Hallazgos Clave del Análisis")
        st.markdown("---")
        
        st.markdown("### 🎯 Resumen Ejecutivo del Análisis")
        
        # Métricas principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            acceptance_rate = (df['y'].value_counts()['yes'] / len(df)) * 100
            st.metric("📈 Tasa de Aceptación", f"{acceptance_rate:.2f}%")
        
        with col2:
            avg_age = df['age'].mean()
            st.metric("👥 Edad Promedio", f"{avg_age:.1f} años")
        
        with col3:
            avg_duration = df['duration'].mean()
            st.metric("⏱️ Duración Promedio", f"{avg_duration:.0f} seg")
        
        with col4:
            most_common_job = df['job'].mode()[0]
            st.metric("💼 Ocupación Más Común", most_common_job)
        
        st.markdown("---")
        
        # Insights visuales
        st.markdown("### 📊 Visualizaciones de Hallazgos Clave")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 Tasa de Aceptación por Educación")
            fig, ax = plt.subplots(figsize=(10, 6))
            education_acceptance = pd.crosstab(df['education'], df['y'], normalize='index') * 100
            education_acceptance['yes'].sort_values(ascending=False).plot(kind='barh', ax=ax, color='green', alpha=0.7)
            ax.set_xlabel('Porcentaje de Aceptación (%)')
            ax.set_title('Aceptación por Nivel Educativo', fontweight='bold')
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.markdown("#### 📞 Tasa de Aceptación por Canal")
            fig, ax = plt.subplots(figsize=(10, 6))
            contact_acceptance = pd.crosstab(df['contact'], df['y'], normalize='index') * 100
            contact_acceptance['yes'].plot(kind='bar', ax=ax, color='steelblue', alpha=0.7)
            ax.set_xlabel('Canal de Contacto')
            ax.set_ylabel('Porcentaje de Aceptación (%)')
            ax.set_title('Aceptación por Canal de Comunicación', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig)
            plt.close()
        
        st.markdown("---")
        
        # Conclusiones principales
        st.markdown("### 📝 Conclusiones Principales")
        
        st.success(f"""
        **1. Tasa de Conversión General**
        - La campaña actual tiene una tasa de aceptación del **{acceptance_rate:.2f}%**
        - Esto representa una caída respecto al objetivo del 12%
        - Se necesita optimizar la estrategia de contacto
        """)
        
        st.info(f"""
        **2. Perfil del Cliente Objetivo**
        - Edad promedio: **{avg_age:.1f} años**
        - Ocupación más frecuente: **{most_common_job}**
        - Duración promedio de contacto: **{avg_duration:.0f} segundos**
        """)
        
        # Análisis de duration vs acceptance
        duration_yes = df[df['y'] == 'yes']['duration'].mean()
        duration_no = df[df['y'] == 'no']['duration'].mean()
        
        st.warning(f"""
        **3. Impacto de la Duración del Contacto**
        - Duración promedio (aceptó): **{duration_yes:.0f} segundos**
        - Duración promedio (rechazó): **{duration_no:.0f} segundos**
        - Los contactos más largos tienen {((duration_yes/duration_no - 1) * 100):.1f}% más probabilidad de éxito
        """)
        
        st.info(f"""
        **4. Canal de Comunicación Óptimo**
        - El canal **{df.groupby('contact')['y'].apply(lambda x: (x=='yes').sum()).idxmax()}** muestra mejor desempeño
        - Se recomienda priorizar este canal en futuras campañas
        """)
        
        st.success(f"""
        **5. Recomendaciones para Mejorar la Efectividad**
        - Enfocarse en perfiles con mayor tasa de conversión
        - Optimizar la duración de los contactos (target: >500 segundos)
        - Priorizar canales de comunicación más efectivos
        - Segmentar campañas según nivel educativo y ocupación
        """)

# =======================
# MAIN - NAVEGACIÓN
# =======================

def main():
    """
    Función principal con navegación
    """
    
    # Inicializar session_state
    if 'data_loaded' not in st.session_state:
        st.session_state['data_loaded'] = False
    
    # Sidebar - Navegación
    st.sidebar.title("Navegación")
    st.sidebar.markdown("---")
    
    menu_options = [
        "🏠 Home",
        "📂 Carga del Dataset",
        "📊 Análisis Exploratorio (EDA)"
    ]
    
    selection = st.sidebar.radio("Selecciona un módulo:", menu_options)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Estado")
    
    if st.session_state['data_loaded']:
        st.sidebar.success("✅ Datos cargados")
        if 'df' in st.session_state:
            st.sidebar.info(f"📊 {st.session_state['df'].shape[0]:,} registros")
    else:
        st.sidebar.warning("Sin datos cargados")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👨‍💻 Proyecto")
    st.sidebar.write("**Caso de Estudio N°1**")
    st.sidebar.write("Especialización Python for Analytics")
    
    # Renderizar módulo seleccionado
    if selection == "🏠 Home":
        show_home()
    elif selection == "📂 Carga del Dataset":
        show_data_loading()
    elif selection == "📊 Análisis Exploratorio (EDA)":
        show_eda()

# =======================
# PUNTO DE ENTRADA
# =======================

if __name__ == "__main__":
    main()
