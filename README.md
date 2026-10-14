# 🚀 Optimización y Predicción de Rangos Salariales en el Mercado IT de Argentina

Proyecto final orientado a la aplicación de Machine Learning para la atracción y retención de talento tecnológico.

---

## 📋 1. Resumen del Dataset

El proyecto se basa en la **Encuesta de Remuneración Salarial IT en Argentina (2023)**. Este dataset recopila información detallada sobre miles de profesionales del sector tecnológico en el país, abarcando variables clave como:

- **Compensación:** Salarios netos/brutos percibidos.
- **Perfil profesional:** Puesto (Rol), Años de experiencia general y en el puesto actual, Nivel de _Seniority_.
- **Stack tecnológico:** Tecnologías principales utilizadas (lenguajes, frameworks, bases de datos), nivel de inglés.
- **Datos demográficos y laborales:** Género, tipo de contratación (relación de dependencia, monotributo, etc.), modalidad de trabajo (remoto, híbrido, presencial).

---

## 💡 2. Objetivo Propuesto y _Storytelling_ de Negocio

### El Problema

Al momento de abrir una vacante laboral en el sector tecnológico, las empresas se enfrentan a un mercado hipercompetitivo y volátil. Definir una oferta salarial imprecisa genera dos problemas críticos:

1. **Ofertas muy bajas:** Ahuyentan al mejor talento, generando pérdida de candidatos calificados.
2. **Ofertas desproporcionadamente altas:** Impactan negativamente en el presupuesto de la compañía y generan inequidad interna.

### La Solución (El Modelo)

El objetivo de este proyecto es desarrollar una herramienta predictiva orientada a **RRHH y líderes técnicos**.

- **Paso base:** Dado un perfil de puesto con requisitos específicos (ej. tecnologías requeridas, años de experiencia necesarios, nivel de _seniority_ y modalidad), el modelo predice un rango salarial de mercado (la media y sus intervalos de confianza/dispersión).
- **Lógica de ajuste (El valor agregado):** A partir de ese valor base, el sistema permite simular incrementos o ajustes dinámicos según exigencias adicionales (ej. si requiere manejo avanzado de una tecnología crítica con alta demanda o un nivel de inglés fluido, calculando cuánto debería subir la oferta salarial propuesta para captar de manera efectiva a ese perfil ideal).

---

## 📊 3. Variables Clave del Proyecto

- **Variable Objetivo (Target - $y$):** Salario (Neto/Bruto mensual).
- **Variables Predictoras (Features - $X$):**
  - **Experiencia:** Años de experiencia total y en el puesto.
  - **Seniority:** Junior, Semi-Senior, Senior, Lead, etc.
  - **Tecnologías:** Lenguajes de programación, herramientas, nube y frameworks utilizados.
  - **Contexto laboral:** Nivel de inglés, tipo de contratación y modalidad.

---

## 🤖 4. Modelos Elegidos y Justificación

Para resolver este problema de negocio, se implementará una estrategia de Machine Learning dividida en etapas:

### A. Modelos Supervisados (Regresión)

- **Modelos a evaluar:** `Random Forest Regressor` y `Gradient Boosting` (XGBoost / LightGBM).
- **Por qué:** Permiten modelar relaciones no lineales complejas (por ejemplo, cómo el impacto de los años de experiencia en el salario no siempre crece de forma lineal, o cómo la combinación de ciertas tecnologías multiplica el valor del perfil). Además, manejan muy bien variables categóricas codificadas.
- **Métricas de éxito:**
  - $RMSE$ (Root Mean Squared Error) para medir el error en pesos/moneda.
  - $R^2$ Score para evaluar qué porcentaje de la variabilidad salarial explica nuestro modelo.

### B. Modelos No Supervisados (Clustering)

- **Modelo a evaluar:** `K-Means`.
- **Por qué:** Agrupar perfiles tecnológicos similares en función de su compensación y habilidades para identificar "clústeres de mercado" (ej. perfiles de datos, desarrollo backend, infraestructura), lo que ayuda a entender mejor los nichos salariales antes de aplicar la regresión.

---

## 📂 Estructura del Repositorio

```text
├── dataset/                  # Datos crudos y procesados
├── notebooks/
│   ├── 01_EDA_y_Limpieza.ipynb       # Análisis exploratorio y transformación
│   ├── 02_Modelos_Supervisados.ipynb  # Regresión y optimización de hiperparámetros
│   └── 03_Modelo_No_Supervisado.ipynb # Clustering y segmentación
└── README.md
```
