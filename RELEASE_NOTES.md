# Notas de Lanzamiento - Diabeduca

## Versión 2.1.2 (19/05/2025)
### Características Principales
- **Soporte para Acceso desde Red Local**
  - Nuevo modo de ejecución para acceso desde red local
  - Acceso desde cualquier dispositivo en la misma red WiFi/LAN
  - Dos modos de ejecución disponibles:
    1. Modo Local (reflex run)
       - Solo accesible desde la computadora servidor
       - URL: http://localhost:3000
    2. Modo Red Local (reflex run --backend-host 0.0.0.0)
       - Accesible desde cualquier dispositivo en la red
       - URL: http://[IP-DEL-SERVIDOR]:3000
  - Mejora en la documentación de modos de ejecución
  - Optimización para pruebas en diferentes dispositivos

## Versión 2.1.1 (19/05/2025)
### Características Principales
- **Exportación de Datos a CSV**
  - Implementación de nueva funcionalidad de exportación
  - Botón de exportación integrado en el dashboard
  - Exportación completa de historial de lecturas
  - Formato CSV con información detallada
  - Nombres de archivo personalizados
  - Interfaz en español

## Versión 2.1.0 (19/05/2025)
### Características Principales
- **Panel Informativo de Rangos**
  - Nueva sección con rangos de referencia clínicos
  - Visualización de valores normales, prediabetes y diabetes
  - Sistema de códigos de color para mejor comprensión
  - Información detallada sobre rangos en diferentes momentos del día

## Versión 2.0.1 (12/05/2025 - 18/05/2025)
### Características Principales
- **Sistema de Contadores**
  - Implementación de contadores automáticos para:
    - Lecturas bajas (< 70 mg/dL)
    - Lecturas saludables (70-100 mg/dL)
    - Lecturas altas (> 100 mg/dL)
  - Visualización en tiempo real de estadísticas
  - Mejora en la presentación de datos

## Versión 2.0.0 (05/05/2025 - 11/05/2025)
### Características Principales
- **Rangos de Referencia por Categoría**
  - Rangos en ayunas
  - Rangos postprandiales (2 horas)
  - Rangos postprandiales (3 horas)
- **Mejoras Generales**
  - Reemplazo completo del contenido del proyecto
  - Eliminación de páginas individuales por módulos
  - Creación de Dashboard interactivo unificado
  - Mejoras en el cálculo del promedio de glicemia
  - Actualización de la documentación

## Versión 1.1.0 (20/04/2025)
### Características Principales
- Implementación de persistencia real de datos
- Mejoras en el sistema de login
- Optimización de la navegación
- Adición del botón home
- Actualización de la documentación

## Versión 1.0.1 (07/04/2025)
### Características Principales
- Nuevo menú desplegable para navegación
- Módulo de Educación con página dedicada
- Módulo de Gráficos con visualización de datos
- Opción de Registro para volver al formulario principal
- Estado para el módulo de educación

## Versión 1.0.0 (05/04/2025 - 06/04/2025)
### Características Principales
- Logotipo personalizado de Diabeduca
- Eslogan oficial: "Educación y control, en tus manos"
- Nuevo diseño de la pantalla de bienvenida
- Mejor contraste y visibilidad en los inputs
- Estructura modular del proyecto

## Versión 0.9.0 (01/04/2025)
### Características Principales
- Inicio de documentación para GitHub
- Creación de CHANGELOG
- Actualización del repositorio

## Versión 0.8.0 (27/03/2025 - 31/03/2025)
### Características Principales
- Refactorización de funciones en el State
- Revisión completa del flujo
- Mejoras en visualización del historial

## Versión 0.7.0 (26/03/2025)
### Características Principales
- Ajuste de estilos
- Eliminación de valores fuera de rango
- Refactorización de código de validaciones

## Versión 0.6.0 (25/03/2025)
### Características Principales
- Prueba de flujo completo
- Validación de limpieza de estado
- Pruebas de compatibilidad

## Versión 0.5.0 (24/03/2025)
### Características Principales
- Mejora del layout de componentes
- Ajuste de validación de límites
- Lógica anti-duplicación de datos

## Versión 0.4.0 (23/03/2025)
### Características Principales
- Creación de estructura de historial
- Implementación de tabla de registros
- Limpieza automática de campos

## Versión 0.3.0 (22/03/2025)
### Características Principales
- Input numérico para glicemia
- Lógica de validación de rangos
- Sistema de alertas

## Versión 0.2.0 (21/03/2025)
### Características Principales
- Reestructuración de navegación
- Ajustes visuales para desktop
- Preparación para input de glicemia

## Versión 0.1.0 (20/03/2025)
### Características Principales
- Creación del primer State
- Implementación de campo de nombre
- Validación de campos

## Versión 0.0.1 (19/03/2025)
### Características Principales
- Creación del proyecto
- Inicialización con Reflex
- Configuración inicial

## Versión 2.2.0 (22/05/2025)
### Características Principales
- **Módulo de Sugerencia Educativa**
  - Sugerencias automáticas y personalizadas según el promedio de glicemia
  - Botón para mostrar sugerencia educativa
  - Sugerencias almacenadas localmente en SQLite
- **Mejoras Visuales en Modo Light**
  - Fondo general gris claro (#e5e7eb) para mayor comodidad visual
  - Mejor contraste de textos y elementos
- **Alineación y Coherencia Visual**
  - Cajas del dashboard alineadas y uniformes en altura
  - Título de sugerencia educativa dentro de su caja
- **Corrección de Errores**
  - Solucionado el bug al eliminar registros de glucosa (parámetros invertidos)

---

## Notas Adicionales
- Todas las versiones incluyen correcciones de errores menores
- Las actualizaciones de documentación son continuas
- Se mantiene retrocompatibilidad con versiones anteriores
- Las mejoras de rendimiento son constantes

---

## Próximas Características Planificadas
- Gestión avanzada de perfil de usuario
- Mejoras en visualización móvil
- Exportación de datos en PDF/Excel
- Validación formal con usuarios reales 