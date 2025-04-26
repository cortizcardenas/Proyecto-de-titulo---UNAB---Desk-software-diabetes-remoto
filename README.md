# DiabetesApp — Aplicación Local en Python para Educación y Control de Diabetes

**Autor:** Carlos Ortiz Cárdenas  
**Profesor Guía:** Barbarita Lara  
**Carrera:** Ingeniería en Computación e Informática  
**Fecha de inicio:** Marzo 2025  
**Versión:** 1.1

---

## 📌 Descripción del Proyecto

**DiabetesApp** es una aplicación web local desarrollada en Python utilizando **[Reflex](https://reflex.dev/)** como framework principal. Su objetivo es apoyar a personas con diabetes en el monitoreo personalizado de su condición, junto con un módulo educativo que entregue sugerencias dinámicas adaptadas a cada usuario, todo funcionando sin necesidad de conexión constante a internet.

---

## ⚠️ Problemática Detectada

En Chile, más del 11% de la población adulta sufre de diabetes. Muchos casos son detectados en etapas avanzadas, aumentando el riesgo de complicaciones graves. Las aplicaciones existentes suelen ser genéricas y dependen de conexión constante, sin adaptarse a las mediciones individuales ni ofrecer una experiencia educativa personalizada.

---

## 🎯 Objetivos

### Objetivo General
Desarrollar una aplicación local que facilite el monitoreo personalizado y la educación de los usuarios en el manejo de la diabetes, mejorando su calidad de vida.

### Objetivos Específicos
- Crear una plataforma amigable para registrar valores de glicemia, alimentación y ejercicio.
- Brindar recomendaciones inteligentes y educativas con base en reglas.
- Fomentar el autocuidado mediante alertas, refuerzo positivo y seguimiento de hábitos.

---

## 🔧 Producto Mínimo Viable (MVP)

- 📝 Registro manual de glicemia con fecha y hora.
- 💬 Sistema de recomendaciones educativas según reglas básicas.
- 🔔 Alertas locales dentro de la aplicación.
- 🧠 Funcionamiento completamente local usando SQLite.
- 👤 Uso sin login para facilitar la experiencia y privacidad.

---

##Rangos de Glicemia

- 🔴 Bajo: < 70 mg/dL
- ✅ Normal: 70-180 mg/dL
- 🟡 Alto: > 180 mg/dL

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje principal:** Python 3.x
- **Framework UI:** [Reflex](https://reflex.dev/)
- **Visualización de datos:** [Plotly](https://plotly.com/)
- **Almacenamiento:** SQLite (modo local)
- **Control de versiones:** Git + GitHub
- **Documentación:** Markdown (README.md), PDF (memoria técnica)

---

## 🚀 Cómo Ejecutar la Aplicación (usando Reflex)

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/diabetesapp.git
cd diabetesapp
```

### 2. Instalar Reflex

```bash
pip install reflex==0.7.3
```

### 3. Inicializar Reflex y correr la app

```bash
reflex init
reflex run
```

Esto levantará un servidor local y abrirá la aplicación en tu navegador (por defecto en http://localhost:3000).

---

## 📁 Estructura del Proyecto (actualizada)

```
diabetesapp/
├── app_diabetes/         # Código fuente del proyecto Reflex
│   ├── __init__.py
│   ├── app_diabetes.py   # Archivo principal
│   ├── charts/          # Módulo de gráficos
│   │   └── glucose_charts.py
│   ├── pages/           # Módulos de la aplicación
│   │   └── educacion.py
│   └── state/           # Estados de la aplicación
│       └── educational_state.py
├── assets/              # Íconos e imágenes
├── .gitignore          # Archivos ignorados por Git
├── README.md           # Este archivo
├── CHANGELOG.md        # Historial de cambios
└── requirements.txt    # Dependencias
```

## 🔄 Estado Actual del Proyecto

- ✔️ Fase de planificación completada
- ✔️ Interfaz inicial funcional con Reflex
- ✔️ Módulo de registro de glicemia implementado
- ✔️ Módulo de educación en desarrollo
- ✔️ Módulo de gráficos implementado
- 🔧 En desarrollo: persistencia de datos, recomendaciones dinámicas

---

## 📘 Licencia

Proyecto académico sin fines comerciales. Derechos reservados © Carlos Ortiz Cárdenas, 2025.

---
