# Diabeduca: Aplicación Web Local para la Gestión y Educación de Usuarios Diabéticos

**Autor:** Carlos Ortiz Cárdenas  
**Carrera:** Ingeniería en Computación e Informática  
**Profesor guía seminario:** Francisco Alejandro Pérez  
**Profesor guía proyecto:** Barbarita Lara Martínez  
**Institución:** Universidad Andrés Bello – Sede Santiago  
**Versión del MVP:** Mayo 2025  

---

## 🩺 Contexto del Proyecto

En Chile, aproximadamente el 11% de la población adulta vive con diabetes. Esta enfermedad, que alguna vez se asoció principalmente a adultos mayores, ha aumentado considerablemente en jóvenes y adultos entre 25 y 50 años. A pesar del impacto sanitario, social y económico que conlleva, aún existen carencias en herramientas tecnológicas accesibles que promuevan la **educación, autocuidado y seguimiento efectivo** de los pacientes diabéticos.

---

## ❗ Problema Identificado

- Fragmentación en los sistemas de información.
- Falta de herramientas interactivas educativas.
- Aplicaciones actuales solo registran datos, sin entregar retroalimentación significativa.
- Desconocimiento generalizado sobre la diabetes en pacientes y familiares.

---

## 🎯 Objetivo del Proyecto

**Objetivo General:**  
Desarrollar un prototipo funcional de una aplicación web local que facilite el monitoreo personalizado y la educación continua de los usuarios en el manejo de la diabetes, mejorando su calidad de vida y reduciendo riesgos de complicaciones a largo plazo.

**Objetivos Específicos:**  
- Diseñar una aplicación accesible desde navegador web que permita registrar valores de glicemia.
- Implementar un módulo educativo que entregue recomendaciones basadas en guías clínicas reales (ADA, MINSAL, MedlinePlus).
- Agregar un sistema de visualización gráfica para detectar patrones y tendencias.
- Validar los registros clínicos ingresados por el usuario con retroalimentación inmediata.

---

## 🧩 Módulos del MVP Implementado

1. **Autenticación básica:** registro del usuario por nombre, sin uso de contraseñas.
2. **Ingreso de glicemia:** validación por rango (20–600 mg/dL) y formato numérico.
3. **Historial de lecturas:** listado ordenado con fecha, hora y observaciones.
4. **Módulo educativo:** recomendaciones basadas en los valores ingresados.
5. **Gráficos interactivos:** evolución semanal y global de glicemia.
6. **Visual web accesible:** navegación clara, diseño responsivo y logo institucional.
7. **Funciona sin conexión permanente:** datos almacenados en SQLite localmente.
8. **Rangos de referencia clínicos:** información detallada sobre rangos normales, prediabetes y diabetes.
9. **Sistema de contadores:** seguimiento de lecturas bajas, saludables y altas.
10. **Panel informativo:** visualización clara de rangos de referencia con códigos de color.

---

## 🛠️ Tecnologías y Herramientas

- **Frontend y Backend:** Python 3.11 + Reflex 0.7.3
- **Base de datos:** SQLite (persistencia local)
- **IDE:** Visual Studio Code
- **Gestión de tareas:** Notion
- **Control de versiones:** Git + GitHub

---

## 🧪 Validaciones y Controles

- Validación de nombre y formato del input.
- Restricción de rango fisiológico para glicemia.
- Solo se generan gráficos y sugerencias si hay registros válidos.
- Visualización educativa solo con contexto previo.
- Contadores automáticos de lecturas por categoría.
- Rangos de referencia basados en guías clínicas actualizadas.

---

## 🗂️ Estructura del Proyecto

```
diabeduca/
├── app_diabetes/           # Lógica Reflex: páginas, estados, componentes
│   ├── pages/
│   ├── state/
│   ├── charts/
│   ├── components/
│   └── utils/
├── assets/                 # Logos, íconos y material educativo
├── data/                   # SQLite y persistencia local
├── reflex.json             # Configuración del proyecto
├── requirements.txt        # Librerías requeridas
├── CHANGELOG.md            # Historial de cambios
└── README.md               # Este archivo
```

---

## 🚀 Cómo Ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/diabeduca.git
cd diabeduca

# 2. Instalar dependencias
pip install reflex==0.7.3

# 3. Ejecutar el sistema
reflex run
```

---

## 📅 Metodología y Planificación

**Metodología:** Scrum (sprints semanales)  
**Total de Sprints:** 5  
**Duración estimada del desarrollo:** Marzo a mayo 2025  
**Documentación de seguimiento:** Archivos académicos en `docs/` y Bitácoras en Notion  

---

## 📘 Bibliografía Principal

- Ministerio de Salud (2017). *La Diabetes Mellitus: prevalencias y evolución en Chile.*
- MedlinePlus. *Complicaciones de la diabetes a largo plazo.*
- American Diabetes Association (ADA). *Guías de tratamiento y autocuidado.*
- Ciomed (2023). *Informe sobre la prevalencia de la diabetes en Sudamérica.*
- Emol (2023). *Impacto de la fragmentación en sistemas de salud en Chile.*

---

## 📌 Estado Actual

✅ MVP funcional  
✅ Sistema de contadores implementado  
✅ Rangos de referencia clínicos agregados  
✅ Panel informativo de rangos integrado  
🔧 Desarrollo educativo en curso  
📊 Visualización gráfica mejorada  
🧪 Pruebas unitarias en entorno local  
🧠 Retroalimentación educativa validada con fuentes confiables

---

## 💡 Próximos pasos

- Agregar gestión avanzada del perfil del usuario.
- Mejorar visualización para dispositivos móviles.
- Añadir exportación de datos en PDF/Excel.
- Iniciar validación formal con usuarios reales (fase piloto).

---

## 📝 Licencia y Créditos

Este proyecto fue desarrollado como parte del **Proyecto de Título** de la carrera Ingeniería en Computación e Informática de la Universidad Andrés Bello.  
Todos los derechos reservados © Carlos Ortiz Cárdenas, 2025.
