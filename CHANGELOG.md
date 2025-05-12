# CHANGELOG - Proyecto: Diabeduca - App local de manejo y educación en diabetes

---

## [2.0.0] - 2025-05-03
### Cambios
- Reemplazo completo del contenido del proyecto con nueva versión de Diabeduca.
- Eliminación de paginas individuales por modulos.
-Creación de Dashboard interactivo el cual contiene y contendrá todos los modulos en una sola ventana.
-Cambios no afectan los objetivos de projecto.
- Mejoras en el promedio de glicemia:
  - Implementación de promedio fijo.
  - Mejoras visuales.
  - Cálculo en tiempo real.
- Actualización de la documentación (README y CHANGELOG).

---

## [1.1.0] - 2025-04-20
### Cambios
- Implementación de persistencia real de datos.
- Mejoras en el sistema de login.
- Optimización de la navegación.
- Adición del botón home.
- Actualización de la documentación.

---

## [2025-04-07] - Implementación de módulos y navegación
### Añadido
- Nuevo menú desplegable para navegación entre módulos.
- Módulo de Educación con página dedicada.
- Módulo de Gráficos con visualización de datos.
- Opción de Registro para volver al formulario principal.
- Estado para el módulo de educación.

### Cambiado
- Mejorada la navegación entre módulos.
- Actualizado el diseño del menú desplegable.
- Optimizada la experiencia de usuario en la navegación.
- Mejorada la presentación de los módulos.

### Técnico
- Implementación de redirección entre módulos.
- Integración de Plotly para visualización de gráficos.
- Creación de estados específicos para cada módulo.
- Optimización del código para mejor mantenibilidad.

---

## [2025-04-05] y [2025-04-06] - Personalización visual y estructura modular
### Añadido
- Logotipo personalizado de **Diabeduca** en todas las pantallas.
- Eslogan oficial: *"Educación y control, en tus manos"*.
- Nuevo diseño de la pantalla de bienvenida con logo prominente.
- Mejor contraste y visibilidad en los inputs.
- Estilo visual coherente con tipografía y distribución.
- Nueva estructura modular del proyecto para mejor organización:
  - Módulo de páginas (`pages/`) para diferentes vistas.
  - Módulo de gráficos (`charts/`) para visualización de datos.
  - Módulo de componentes (`components/`) para elementos reutilizables.
  - Módulo de estados (`state/`) para manejo de datos.
  - Módulo de utilidades (`utils/`) para funciones auxiliares.
  - Directorio de datos (`data/`) para almacenamiento.
  - Nueva sección en `assets/` para contenido educativo.

### Cambiado
- Actualización del diseño visual general para mejorar experiencia de usuario.
- Mejora en la presentación del historial de glicemia.
- Optimización de espaciados y márgenes entre componentes.
- Ajuste en los colores para mejor contraste.
- Tamaños de fuente más consistentes entre pantallas.

---

## [2025-04-01] - Preparación de documentación
- Inicio de documentación para GitHub.
- Creación de CHANGELOG con fechas reales.
- Se actualiza repositorio de GitHub con código actual.

---

## [2025-03-27] al [2025-03-31] - Estabilización del código base
- Refactorización de funciones en el `State`.
- Revisión completa del flujo y detección de bugs menores.
- Mejoras en visualización del historial.

## [2025-03-26] - Validaciones finales y limpieza de inputs
- Ajuste de estilos.
- Se eliminan valores si están fuera del rango permitido.
- Se refactoriza código para separar lógica de validaciones.

## [2025-03-25] - Ajustes menores
- Se prueba flujo completo: ingreso nombre + glicemia + tabla.
- Se valida limpieza de estado.
- Pruebas de compatibilidad y errores menores.

## [2025-03-24] - Refinamiento visual y funcional
- Se mejora el layout de los componentes.
- Validación de límites por glicemia ajustada.
- Añadida lógica para evitar duplicación de datos vacíos.

## [2025-03-23] - Historial local de glicemias
- Se crea estructura `historial: list[dict]` para guardar registros localmente.
- Implementación de tabla para mostrar:
  - Fecha
  - Nombre del usuario
  - Valor de glicemia.
- Limpieza automática del campo después de guardar.

## [2025-03-22] - Registro de glicemia
- Se agrega input numérico para valores de glicemia.
- Se crea lógica para validar si el valor está dentro o fuera del rango saludable.
- Se muestra alerta según el resultado.

## [2025-03-21] - Validación de usuario y navegación
- Reestructuración del flujo de navegación inicial con estados.
- Ajustes visuales básicos para desktop.
- Preparación para integrar nuevo input de glicemia.

## [2025-03-20] - Estructura de bienvenida
- Creación del primer `State` en Reflex.
- Implementación de campo de texto para ingresar nombre del usuario.
- Validación de campo vacío y navegación condicional.

## [2025-03-19] - Inicio del proyecto
- Se crea la carpeta `app_diabetes` en Visual Studio Code.
- Se inicializa el proyecto con `reflex init`.
- Instalación y configuración de Reflex 0.7.3.

---

## [1.0.0] - 2024-05-01
### Cambios
- Versión inicial del proyecto.
- Implementación de la estructura base de la aplicación.
- Configuración inicial del entorno de desarrollo.

---

## [No publicado] - 2024-03-19
### Cambios
- Actualización del repositorio principal con la última versión del proyecto.

