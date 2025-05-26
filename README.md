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
4. **Módulo educativo y sugerencias:** recomendaciones automáticas y personalizadas según el promedio de glicemia, con interfaz visual integrada y botón de sugerencia.
5. **Gráficos interactivos:** evolución semanal y global de glicemia.
6. **Visual web accesible:** navegación clara, diseño responsivo y logo institucional.
7. **Funciona sin conexión permanente:** datos almacenados en SQLite localmente.
8. **Rangos de referencia clínicos:** información detallada sobre rangos normales, prediabetes y diabetes, ahora con tabla mejorada, emoticonos y nota basada en la ADA.
9. **Sistema de contadores:** seguimiento de lecturas bajas, saludables y altas, ahora con iconos de caras (emojis) para facilitar la interpretación visual.
10. **Panel informativo:** visualización clara de rangos de referencia con códigos de color y emoticonos.
11. **Exportación de datos:** funcionalidad para exportar el historial completo a formato CSV.
12. **Mejoras visuales:** modo light con fondo gris suave para mayor comodidad visual, contraste mejorado y alineación uniforme de cajas en el dashboard.
13. **Footer global:** mensaje de disclaimer de prototipo siempre visible al final de la página, en todas las vistas.
14. **Layout mejorado:** el footer permanece pegado al fondo de la pantalla en todo momento.

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
- Contadores automáticos de lecturas por categoría, con iconos de caras.
- Rangos de referencia basados en guías clínicas actualizadas y visualizados con emoticonos.
- Footer de seguridad siempre visible.

---

## 🗂️ Estructura del Proyecto

```
diabeduca/
├── app/                    # Lógica principal de la aplicación
│   ├── pages/             # Páginas de la aplicación
│   ├── states/            # Estados y lógica de negocio
│   ├── components/        # Componentes reutilizables
│   ├── app.py            # Configuración principal de la aplicación
│   ├── database.py       # Configuración y modelos de la base de datos
│   └── __init__.py       # Inicialización del módulo
├── assets/                # Recursos estáticos
│   └── favicon.ico       # Ícono de la aplicación
├── .states/              # Estados de Reflex
├── .web/                 # Archivos generados por Reflex
├── build/                # Archivos de construcción
├── dist/                 # Distribución de la aplicación
├── venv/                 # Entorno virtual de Python
├── diabetes_management.db # Base de datos SQLite
├── rxconfig.py          # Configuración de Reflex
├── requirements.txt     # Dependencias del proyecto
├── CHANGELOG.md         # Registro de cambios
├── RELEASE_NOTES.md     # Notas de lanzamiento
└── README.md            # Documentación principal
```

---

## 🚀 Cómo Ejecutar

### Requisitos Previos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git
- Visual Studio Code (recomendado) o Cursor IDE

### Dependencias del Proyecto
```bash
# Framework y Backend
reflex==0.7.8a1        # Framework web principal
bcrypt==4.1.2         # Encriptación de datos
sqlalchemy==2.0.28    # ORM para base de datos
python-dotenv==1.0.1  # Manejo de variables de entorno

# Base de Datos
# SQLite3 viene incluido con Python 3.11, no requiere instalación adicional

# Análisis de Datos y Visualización
plotly==5.18.0        # Gráficos interactivos
pandas==2.2.1         # Manipulación de datos
numpy==1.26.4         # Cálculos numéricos

# Herramientas de Desarrollo
pytest==8.0.2         # Testing
black==24.2.0         # Formateador de código
ruff==0.2.2          # Linter
```

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/cortizcardenas/Proyecto-de-titulo---UNAB---Desk-software-diabetes-remoto.git
cd Proyecto-de-titulo---UNAB---Desk-software-diabetes-remoto

# 2. Crear y activar entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar el IDE (Visual Studio Code)
# Instalar las siguientes extensiones:
# - Python (Microsoft)
# - Pylance
# - Python Test Explorer
# - Python Docstring Generator
# - Black Formatter
# - Ruff

# 5. Inicializar la base de datos
# La base de datos se creará automáticamente al ejecutar la aplicación

# 6. Ejecutar el sistema
reflex run
```

### Notas Importantes
- La aplicación se ejecutará en `http://localhost:3000` por defecto
- La base de datos SQLite se creará automáticamente en la raíz del proyecto
- Asegúrate de tener todos los permisos necesarios en el directorio del proyecto
- Para desarrollo, se recomienda usar Visual Studio Code o Cursor IDE con las extensiones mencionadas

### Modos de Ejecución
1. **Modo Local (reflex run)**
   - Solo accesible desde la computadora donde se ejecuta
   - URL: `http://localhost:3000`
   - Ideal para desarrollo y pruebas locales

2. **Modo Red Local (reflex run --backend-host 0.0.0.0)**
   - Accesible desde cualquier dispositivo en la misma red
   - URL: `http://[IP-DEL-SERVIDOR]:3000` (ej: `http://192.168.0.12:3000`)
   - Requisitos:
     - Todos los dispositivos deben estar en la misma red WiFi/LAN
     - El firewall debe permitir conexiones al puerto 3000
   - Ideal para:
     - Pruebas en diferentes dispositivos
     - Validación de responsividad
     - Pruebas de usabilidad con usuarios reales

### Solución de Problemas Comunes
- Si hay problemas con reflex, intenta ejecutar `reflex init` antes de `reflex run`
- En caso de errores de dependencias, ejecuta `pip install --upgrade -r requirements.txt`
- Para limpiar la caché de reflex: `reflex db reset`
- Si hay problemas con las extensiones del IDE, intenta recargar la ventana
- Para problemas de formateo: `black .` en la raíz del proyecto
- Para problemas de linting: `ruff check .` en la raíz del proyecto

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
✅ Sistema de contadores implementado (ahora con iconos de caras)  
✅ Rangos de referencia clínicos agregados (ahora con tabla mejorada, emoticonos y nota ADA)  
✅ Panel informativo de rangos integrado  
✅ Módulo educativo y sugerencias automáticas funcionales  
✅ Visualización gráfica mejorada  
✅ Footer global de seguridad en todas las páginas  
✅ Mejoras visuales en modo light y alineación de dashboard  
✅ Corrección de eliminación de registros  
🧪 Pruebas unitarias en entorno local  
🧠 Retroalimentación educativa validada con fuentes confiables

---

## 💡 Próximos pasos

- Agregar gestión avanzada del perfil del usuario.
- Mejorar visualización para dispositivos móviles.
- Añadir exportación de datos en PDF.
- Iniciar validación formal con usuarios reales (fase piloto).

---

## 📝 Licencia y Créditos

Este proyecto fue desarrollado como parte del **Proyecto de Título** de la carrera Ingeniería en Computación e Informática de la Universidad Andrés Bello.  
Todos los derechos reservados © Carlos Ortiz Cárdenas, 2025.
