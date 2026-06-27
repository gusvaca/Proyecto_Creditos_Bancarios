# 🏦 Predicción de Aprobación de Créditos mediante Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![License](https://img.shields.io/badge/License-Academic-green)

---

## 📖 Descripción del Proyecto

Este proyecto fue desarrollado como parte de la asignatura **Big Data, Analytics & Data Science** de la **Maestría en Tecnologías de la Información** de la **Universidad Hemisferios**.

El objetivo consiste en aplicar técnicas de **Análisis Exploratorio de Datos (EDA)** y **Machine Learning** para analizar solicitudes de crédito bancario e identificar los factores que influyen en la aprobación o rechazo de un crédito.

Como resultado, se desarrolló un modelo predictivo basado en **Random Forest**, capaz de apoyar el proceso de evaluación crediticia mediante la identificación de patrones presentes en los datos históricos.

---

# 🎯 Problemática

Las instituciones financieras procesan diariamente un gran número de solicitudes de crédito. Una evaluación manual puede generar:

* Altos tiempos de respuesta.
* Incremento del riesgo operativo.
* Inconsistencias en la toma de decisiones.
* Costos elevados de análisis.

La aplicación de técnicas de **Machine Learning** permite automatizar parte del proceso de evaluación, reduciendo tiempos y mejorando la precisión en la toma de decisiones.

---

# 🎯 Objetivo General

Desarrollar un modelo predictivo que permita estimar la aprobación de créditos bancarios mediante técnicas de análisis de datos y Machine Learning.

---

# 📌 Objetivos Específicos

* Analizar la estructura y calidad del conjunto de datos.
* Aplicar procesos de limpieza y transformación de datos.
* Realizar un análisis exploratorio de datos (EDA).
* Construir visualizaciones para identificar patrones relevantes.
* Implementar un modelo de clasificación utilizando **Random Forest**.
* Evaluar el desempeño mediante métricas de Machine Learning.

---

# 📊 Dataset

El proyecto utiliza un conjunto de datos compuesto por **5.000 solicitudes de crédito bancario**.

## Variables principales

| Variable             | Descripción                       |
| -------------------- | --------------------------------- |
| Edad                 | Edad del solicitante              |
| Género               | Sexo del cliente                  |
| Estado Civil         | Estado civil                      |
| Ciudad               | Ciudad de residencia              |
| Ingresos Mensuales   | Ingresos del solicitante          |
| Gastos Mensuales     | Gastos registrados                |
| Score Crediticio     | Calificación crediticia           |
| Antigüedad Laboral   | Tiempo de permanencia laboral     |
| Tipo de Empleo       | Tipo de contratación              |
| Monto Solicitado     | Valor del crédito                 |
| Plazo del Crédito    | Tiempo de financiamiento          |
| Productos Bancarios  | Productos financieros existentes  |
| Mora Histórica       | Historial de mora                 |
| Canal de Solicitud   | Canal utilizado para la solicitud |
| Capacidad de Pago    | Indicador financiero              |
| **Crédito Aprobado** | Variable objetivo                 |

---

# 🔄 Metodología

El proyecto fue desarrollado siguiendo el flujo estándar de un proyecto de Ciencia de Datos:

1. Carga del dataset.
2. Exploración inicial de los datos.
3. Limpieza y preparación de datos.
4. Análisis Exploratorio de Datos (EDA).
5. Visualización de información.
6. Transformación de variables.
7. Entrenamiento del modelo Random Forest.
8. Evaluación mediante métricas de clasificación.
9. Interpretación de resultados.

---

# 🤖 Modelo de Machine Learning

Se implementó el algoritmo **Random Forest Classifier**, seleccionado debido a las siguientes ventajas:

* Excelente desempeño en problemas de clasificación.
* Capacidad para manejar variables numéricas y categóricas.
* Reducción del sobreajuste mediante múltiples árboles de decisión.
* Alta robustez frente a ruido en los datos.
* Permite identificar la importancia relativa de las variables.

---

# 📈 Métricas del Modelo

| Métrica   | Resultado |
| --------- | --------: |
| Accuracy  |  **100%** |
| Precision |  **100%** |
| Recall    |  **100%** |
| F1-Score  |  **100%** |

> **Nota:** El desempeño obtenido refleja el comportamiento del conjunto de datos utilizado para fines académicos. En escenarios reales, se recomienda validar el modelo con datos independientes y aplicar técnicas de validación cruzada para garantizar su capacidad de generalización.

---

# 🔍 Principales Hallazgos

El análisis permitió identificar que las variables con mayor influencia en la aprobación de créditos son:

* 📈 Score Crediticio.
* 💰 Capacidad de Pago.
* ⚠️ Mora Histórica.
* 💼 Antigüedad Laboral.
* 💵 Ingresos Mensuales.

Asimismo, el modelo logró identificar correctamente las reglas de negocio incorporadas en el conjunto de datos.

---

# 💼 Impacto para el Negocio

La implementación de modelos predictivos en procesos de evaluación crediticia puede generar beneficios como:

* Reducción de los tiempos de análisis.
* Optimización de la gestión del riesgo.
* Incremento de la productividad operativa.
* Mayor consistencia en las decisiones.
* Mejora de la experiencia del cliente.
* Apoyo a la toma de decisiones basada en datos.

---

# 🛠 Tecnologías Utilizadas

| Tecnología       | Uso                          |
| ---------------- | ---------------------------- |
| Python           | Desarrollo del proyecto      |
| Jupyter Notebook | Análisis y experimentación   |
| Pandas           | Manipulación de datos        |
| NumPy            | Procesamiento numérico       |
| Matplotlib       | Visualización de datos       |
| Seaborn          | Análisis estadístico         |
| Plotly           | Visualizaciones interactivas |
| Scikit-Learn     | Modelado de Machine Learning |

---

# 📁 Estructura del Repositorio

```text
Proyecto_Creditos_Bancarios/
│
├── README.md
│
├── data/
│   └── creditos_bancarios_5000.xlsx
│
├── notebook/
│   └── Analisis_Creditos_Bancarios.ipynb
│
├── outputs/
│   └── visualizaciones/
│
└── informe/
    └── Informe_Final.pdf
```

---

# 🚀 Ejecución del Proyecto

## Requisitos

* Python 3.11 o superior
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-Learn

## Pasos

1. Clonar el repositorio.

```bash
git clone https://github.com/usuario/Proyecto_Creditos_Bancarios.git
```

2. Instalar las dependencias.

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn openpyxl
```

3. Abrir el notebook.

```bash
jupyter notebook
```

4. Ejecutar el archivo:

```text
notebook/Analisis_Creditos_Bancarios.ipynb
```

---

# 📊 Resultados

El modelo Random Forest logró un desempeño sobresaliente en la clasificación de solicitudes de crédito, identificando correctamente las variables con mayor influencia en la aprobación.

Los resultados obtenidos evidencian el potencial de las técnicas de Machine Learning como herramienta de apoyo para la gestión del riesgo crediticio y la optimización de procesos dentro del sector financiero.

---

# 🎓 Contexto Académico

**Programa:** Maestría en Tecnologías de la Información

**Asignatura:** Big Data, Analytics & Data Science

**Universidad:** Universidad Hemisferios

---

# 👨‍💻 Autor

**Gustavo Vaca**

Subgerente de Soluciones TI

Ingeniero en Sistemas

Maestría en Tecnologías de la Información

Especialista en:

* Arquitectura Empresarial
* Arquitectura de Datos
* Desarrollo de Software
* Inteligencia Artificial
* Analítica de Datos
* Transformación Digital

---

# 📄 Licencia

Este proyecto fue desarrollado con fines exclusivamente académicos y educativos como parte de la Maestría en Tecnologías de la Información.

Su contenido puede utilizarse como referencia citando al autor correspondiente.

---

⭐ **Si este proyecto fue de utilidad para tu aprendizaje, considera darle una estrella al repositorio.**
