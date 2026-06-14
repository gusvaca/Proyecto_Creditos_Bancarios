# Predicción de Aprobación de Créditos mediante Machine Learning

## Descripción del Proyecto

Este proyecto fue desarrollado como parte de la asignatura **Big Data, Analytics & Data Science** de la Maestría en Tecnologías de la Información.

El objetivo consiste en analizar información relacionada con solicitudes de crédito bancario mediante técnicas de análisis exploratorio de datos (EDA) y Machine Learning, con el fin de identificar los factores que influyen en la aprobación de créditos y construir un modelo predictivo de apoyo a la toma de decisiones.

---

## Problemática

Las instituciones financieras requieren mecanismos que permitan reducir los tiempos de evaluación crediticia y mejorar la gestión del riesgo.

La utilización de técnicas de analítica avanzada permite identificar patrones en el comportamiento de los clientes y optimizar los procesos de aprobación de créditos mediante modelos predictivos.

---

## Objetivo General

Desarrollar un modelo predictivo que permita estimar la aprobación de créditos utilizando técnicas de análisis de datos y Machine Learning.

## Objetivos Específicos

- Analizar la estructura y calidad del dataset.
- Aplicar procesos de limpieza y transformación de datos.
- Realizar análisis exploratorio de datos.
- Construir visualizaciones para identificar patrones relevantes.
- Implementar un modelo de clasificación utilizando Random Forest.
- Evaluar el desempeño mediante métricas de Machine Learning.

---

## Dataset

El conjunto de datos contiene información de 5.000 solicitudes de crédito bancario.

### Variables Principales

- Edad
- Género
- Estado Civil
- Ciudad
- Ingresos Mensuales
- Gastos Mensuales
- Score Crediticio
- Antigüedad Laboral
- Tipo de Empleo
- Monto Solicitado
- Plazo del Crédito
- Productos Bancarios
- Mora Histórica
- Canal de Solicitud
- Capacidad de Pago
- Crédito Aprobado (Variable Objetivo)

---

## Metodología Aplicada

El proyecto fue desarrollado siguiendo las siguientes etapas:

1. Carga y exploración inicial del dataset.
2. Limpieza y preparación de datos.
3. Análisis exploratorio de datos (EDA).
4. Visualización de información.
5. Transformación de variables.
6. Entrenamiento del modelo Random Forest.
7. Evaluación mediante métricas de clasificación.
8. Interpretación de resultados y conclusiones.

---

## Tecnologías Utilizadas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn

---

## Modelo de Machine Learning

Se utilizó el algoritmo **Random Forest Classifier**, seleccionado por su capacidad para manejar variables numéricas y categóricas, así como por su robustez para problemas de clasificación.

### Métricas Obtenidas

| Métrica | Resultado |
|----------|------------|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1 Score | 100% |

---

## Principales Hallazgos

- El score crediticio fue la variable más influyente en la aprobación de créditos.
- La capacidad de pago mostró una fuerte relación con la decisión crediticia.
- La mora histórica representa uno de los factores más relevantes para la gestión del riesgo.
- La antigüedad laboral contribuye positivamente a la probabilidad de aprobación.
- El modelo logró identificar correctamente las reglas de negocio incorporadas en el dataset.

---

## Impacto para el Negocio

La aplicación de modelos predictivos dentro del proceso de evaluación crediticia puede generar beneficios como:

- Reducción de tiempos de análisis.
- Optimización de la gestión del riesgo.
- Incremento de la productividad operativa.
- Mejora en la experiencia del cliente.
- Mayor consistencia en la toma de decisiones.

---

## Estructura del Repositorio

```text
Proyecto_Creditos_Bancarios/
│
├── README.md
├── data/
│   └── creditos_bancarios_5000.xlsx
│
├── notebook/
│   └── Analisis_Creditos_Bancarios.ipynb
│
├── outputs/
│   ├── visualizaciones
│   
│
└── informe/
    └── Informe_Final.pdf
```

---

## Resultados

El análisis permitió identificar que las variables con mayor influencia en la aprobación de créditos son:

1. Score Crediticio.
2. Capacidad de Pago.
3. Mora Histórica.
4. Antigüedad Laboral.
5. Ingresos Mensuales.

El modelo Random Forest alcanzó un desempeño sobresaliente en la clasificación de solicitudes de crédito.

---

## Autor

**Gustavo Vaca**

Maestría en Tecnologías de la Información

Big Data, Analytics & Data Science

Universidad Hemisferios
