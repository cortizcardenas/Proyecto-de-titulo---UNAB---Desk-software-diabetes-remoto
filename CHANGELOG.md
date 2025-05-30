# CHANGELOG - Proyecto: Diabeduca - App local de manejo y educación en diabetes

---

## [2.4.0] - 26/05/2025
### Añadido y Cambiado
- Actualización de todos los rangos de glucosa y lógica matemática para MUY BAJO (<54), Bajo (54-69), Saludable (70-130), Alto (131-250), Muy Alto (>250).
- Eliminación de las categorías "Despues de comer", "2-3h Despues de comer" y "unspecified".
- Agregado de las categorías "3hrs Despues de Comer" y "Antes de Dormir" (ambas con lógica de Ayuno).
- Validación estricta de categorías permitidas en el input y en la lógica.
- Actualización de sugerencias educativas y base de datos para reflejar los nuevos rangos.
- Actualización de la tabla de referencia clínica y líneas de referencia en el gráfico.
- Colores y emojis consistentes en todos los estados: morado (MUY BAJO), azul (Bajo), verde (Saludable), amarillo (Alto), rojo (Muy Alto).
- Lógica de glucosa promedio ahora sigue los mismos rangos que Ayuno.
- Alerta de glucosa promedio ahora usa emojis y colores grandes y visibles, ideal para personas mayores.
- Cambio de nombre de la sección "Estadísticas" a "Resumen de Control Glucémico".
- Limpieza de referencias antiguas y refuerzo de coherencia visual y lógica en toda la app.

---

## [2.1.2] - 19/05/2025
### Añadido
- Soporte para Acceso desde Red Local
  - Implementación de modo de ejecución en red local
  - Acceso desde cualquier dispositivo en la misma red
  - Documentación de modos de ejecución:
    - Modo Local (reflex run)
    - Modo Red Local (reflex run --backend-host 0.0.0.0)

## [2.1.1] - 19/05/2025
### Añadido
- Funcionalidad de Exportación a CSV
  - Nuevo botón de exportación en el dashboard
  - Exportación de todas las lecturas de glucosa
  - Incluye información detallada:
    - Nombre del usuario
    - Fecha y hora (original y formateada)
    - Valor de glucosa
    - Estado
    - Categoría
    - Notas
  - Nombre de archivo personalizado con fecha y hora

## [2.1.0] - 18/05/2025
### Añadido
- Panel Informativo de Rangos
  - Nueva sección con rangos de referencia clínicos
  - Incluye valores normales, prediabetes y diabetes
  - Presentación visual con códigos de color

## [2.0.1] - 12/05/2025 al 18/05/2025
### Añadido
- Sistema de Contadores
  - Contador de lecturas bajas
  - Contador de lecturas saludables
  - Contador de lecturas altas

## [2.0.0] - 05/05/2025 al 11/05/2025
### Añadido
- Rangos de Referencia por Categoría
  - Rangos en ayunas
  - Rangos postprandiales (2 horas)
  - Rangos postprandiales (3 horas)

### Cambios
- Reemplazo completo del contenido del proyecto con nueva versión de Diabeduca.
- Eliminación de paginas individuales por modulos.
- Creación de Dashboard interactivo el cual contiene y contendrá todos los modulos en una sola ventana.
- Cambios no afectan los objetivos de projecto.
- Mejoras en el promedio de glicemia:
  - Implementación de promedio fijo.
  - Mejoras visuales.
  - Cálculo en tiempo real.
- Actualización de la documentación (README y CHANGELOG).

---

## [1.1.0] - 20/04/2025
### Cambios
- Implementación de persistencia real de datos.
- Mejoras en el sistema de login.
- Optimización de la navegación.
- Adición del botón home.
- Actualización de la documentación.

---

## [1.0.1] - 07/04/2025
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

## [1.0.0] - 05/04/2025 y 06/04/2025
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

## [0.9.0] - 01/04/2025
- Inicio de documentación para GitHub.
- Creación de CHANGELOG con fechas reales.
- Se actualiza repositorio de GitHub con código actual.

---

## [0.8.0] - 27/03/2025 al 31/03/2025
- Refactorización de funciones en el `State`.
- Revisión completa del flujo y detección de bugs menores.
- Mejoras en visualización del historial.

## [0.7.0] - 26/03/2025
- Ajuste de estilos.
- Se eliminan valores si están fuera del rango permitido.
- Se refactoriza código para separar lógica de validaciones.

## [0.6.0] - 25/03/2025
- Se prueba flujo completo: ingreso nombre + glicemia + tabla.
- Se valida limpieza de estado.
- Pruebas de compatibilidad y errores menores.

## [0.5.0] - 24/03/2025
- Se mejora el layout de los componentes.
- Validación de límites por glicemia ajustada.
- Añadida lógica para evitar duplicación de datos vacíos.

## [0.4.0] - 23/03/2025
- Se crea estructura `historial: list[dict]` para guardar registros localmente.
- Implementación de tabla para mostrar:
  - Fecha
  - Nombre del usuario
  - Valor de glicemia.
- Limpieza automática del campo después de guardar.

## [0.3.0] - 22/03/2025
- Se agrega input numérico para valores de glicemia.
- Se crea lógica para validar si el valor está dentro o fuera del rango saludable.
- Se muestra alerta según el resultado.

## [0.2.0] - 21/03/2025
- Reestructuración del flujo de navegación inicial con estados.
- Ajustes visuales básicos para desktop.
- Preparación para integrar nuevo input de glicemia.

## [0.1.0] - 20/03/2025
- Creación del primer `State` en Reflex.
- Implementación de campo de texto para ingresar nombre del usuario.
- Validación de campo vacío y navegación condicional.

## [0.0.1] - 19/03/2025
- Se crea la carpeta `app_diabetes` en Visual Studio Code.
- Se inicializa el proyecto con `reflex init`.
- Instalación y configuración de Reflex 0.7.3.

---

## [1.0.0] - 01/05/2025
### Cambios
- Versión inicial del proyecto.
- Implementación de la estructura base de la aplicación.
- Configuración inicial del entorno de desarrollo.

---

## [No publicado] - 19/03/2025
### Cambios
- Actualización del repositorio principal con la última versión del proyecto.

## [2.2.0] - 22/05/2025
### Añadido
- Módulo de sugerencia educativa completamente funcional:
  - Sugerencias automáticas según el promedio de glicemia
  - Botón para mostrar sugerencia personalizada
  - Sugerencias almacenadas y gestionadas localmente en SQLite
- Mejoras visuales en modo light:
  - Fondo general gris claro (#e5e7eb) para mayor comodidad visual
  - Mejor contraste de textos y elementos
- Alineación y coherencia visual:
  - Cajas del dashboard alineadas y uniformes en altura
  - Título de sugerencia educativa dentro de su caja
- Corrección de errores:
  - Solucionado el bug al eliminar registros de glucosa (parámetros invertidos)

## [2.3.0] - 23/05/2025
### Añadido
- Footer global con disclaimer de prototipo, visible en todas las páginas (dashboard, login, registro).
- Contadores de lecturas con iconos de caras (emojis) para bajas, saludables y altas.
- Tabla de rangos clínicos mejorada: filas alternadas, bordes redondeados, colores de texto consistentes y emoticonos para cada rango.
- Nueva nota en la tabla: "Nota: Estas son pautas generales basadas según la ADA (American Diabetes Association). Siempre consulte a su Medico para asesoramiento personalizado."
- Mejoras de layout: el footer permanece pegado al fondo de la pantalla en todo momento.
- Ajustes visuales generales para mayor coherencia y legibilidad en modo claro y oscuro.

