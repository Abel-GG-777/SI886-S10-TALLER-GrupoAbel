# 5.1 Principios de arquitectura

**Organización:** Distribuidora Andina del Sur S.A.C. — Empresa 06.

**Estado:** propuesta del equipo basada en los documentos del caso; pendiente de aprobación. Las referencias siguientes identifican evidencia disponible, no secciones del PETI que todavía no se han proporcionado.

## P01. Separación de funciones y mínimo privilegio

- **Declaración:** el registro y la aprobación de compras y pagos deben recaer en usuarios distintos, con permisos limitados a sus responsabilidades.
- **Razón:** el incidente del caso evidencia compras fraccionadas bajo S/ 5 000 y un usuario que registraba y aprobaba porque los perfiles del ERP lo permitían.
- **Implicancias:** revisar perfiles; impedir la autoaprobación; registrar las autorizaciones; establecer controles que detecten operaciones relacionadas potencialmente fraccionadas y someterlas a revisión. Los criterios de agrupación deben acordarse con Administración y Finanzas.
- **Trazabilidad:** FICHA.md, apartados A (objetivo de TI), G (incidente) y H (riesgo de segregación).

## P02. Fuente autoritativa y responsable por entidad

- **Declaración:** cada entidad crítica debe tener una fuente autoritativa identificada y un dueño designado por cargo; las copias deben estar controladas y conciliadas.
- **Razón:** el inventario físico y contable difiere en promedio 4,7 % y las ubicaciones del almacén se gestionan en hojas paralelas.
- **Implicancias:** inventariar las entidades y sus copias; acordar fuentes y responsables; establecer reglas de calidad y conciliación; resolver discrepancias antes de construir indicadores consolidados. No asumir que el ERP es la fuente autoritativa de todas las entidades sin validarlo.
- **Trazabilidad:** FICHA.md, apartados A, C y H; arquitectura-actual.md, apartado 5: Cliente carece de dueño y Stock usa una fuente de hecho. La discrepancia entre copias no equivale a ausencia de fuente declarada.

## P03. Integración controlada y trazable

- **Declaración:** los intercambios entre aplicaciones deben utilizar mecanismos documentados, con validación, control de acceso y registro de errores.
- **Razón:** el caso identifica ERP, fuerza de ventas móvil, facturación electrónica, portal y hojas de cálculo; es necesario conocer cómo intercambian información para sostener la conciliación y el control interno.
- **Implicancias:** documentar primero las integraciones existentes; definir contratos de intercambio y responsables; controlar duplicados, rechazos y reprocesamientos; evaluar interfaces soportadas antes de proponer nuevas integraciones. La ficha no prueba que existan API ni interfaces en tiempo real.
- **Trazabilidad:** FICHA.md, apartados A y C; arquitectura-actual.md, apartado 4: sincronización nocturna, conexión OSE en línea, transcripción manual del portal y ausencia de integración con libros del almacén.

## P04. Continuidad demostrable mediante recuperación probada

- **Declaración:** los servicios críticos deben contar con mecanismos de respaldo y recuperación cuya eficacia se compruebe mediante pruebas documentadas.
- **Razón:** los respaldos se guardan en disco local y nunca se ha probado una restauración completa; no existe un plan de continuidad y el BIA se describe como incompleto.
- **Implicancias:** completar el análisis de impacto; acordar objetivos de recuperación; separar adecuadamente las copias del entorno operativo; programar pruebas y corregir fallos. No fijar RTO o RPO sin datos validados del negocio.
- **Trazabilidad:** FICHA.md, apartados E y F; mesa-de-servicio-y-sla.md, apartados 3 y 7.

## P05. Plataformas mantenibles y cambios controlados

- **Declaración:** los componentes en operación deben tener responsables de mantenimiento y los cambios deben evaluarse, autorizarse, probarse y documentarse antes de su puesta en producción.
- **Razón:** el portal no tiene soporte vigente; existen contratos vencidos y los cambios carecen de un control formal consistente.
- **Implicancias:** evaluar mantener, renovar o sustituir componentes según riesgo y costo; registrar cambios, pruebas, autorizaciones y planes de retorno; verificar la vigencia contractual. La ausencia de soporte no demuestra por sí sola que el software esté en fin de vida.
- **Trazabilidad:** FICHA.md, apartados C, F y H; mesa-de-servicio-y-sla.md, apartado 7.

## P06. Servicios con responsables, medición y trazabilidad

- **Declaración:** cada servicio de TI debe tener responsable, alcance y niveles de servicio acordados y medidos; las atenciones deben registrarse y clasificarse de manera uniforme.
- **Razón:** no hay catálogo aprobado ni dueños designados; las metas no se miden sistemáticamente y el registro de atenciones es parcial, con campos incompletos.
- **Implicancias:** formalizar el catálogo; acordar indicadores y metas con el negocio; registrar incidentes y solicitudes; definir prioridades, escalamiento y seguimiento; evaluar el cumplimiento del proveedor del ERP con información verificable.
- **Trazabilidad:** mesa-de-servicio-y-sla.md, apartados 1–5 y 8; plan-institucional-extracto.md, objetivos OE-01 y OE-02.

## Observaciones de consistencia y pendientes

1. FICHA.md afirma que no se registran incidentes; mesa-de-servicio-y-sla.md describe 1 929 atenciones en una hoja con registro parcial. Se conservan ambas evidencias y se requiere aclarar su alcance; no se afirma que haya un sistema formal completo.
2. FICHA.md menciona un plan 2023–2027 y plan-institucional-extracto.md un plan 2024–2028. La vigencia debe confirmarse.
3. Al recibir el PETI, vincular estos principios con los identificadores y apartados reales del diagnóstico, las capacidades y las estrategias. No se han inventado referencias a hallazgos previos.
