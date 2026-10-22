# Arquitectura objetivo propuesta

No existe un PETI previo de Andina aportado. La derivación usa los objetivos del plan institucional, el objetivo TI de la ficha, los hechos del diagnóstico y los seis principios. La trazabilidad a las secciones 2.2, 3.1.5, 3.5 y 4 queda pendiente; no se inventan estrategias FODA aprobadas.

| Brecha | Capa | Actual | Objetivo propuesto | Origen | Elementos del modelo |
|---|---|---|---|---|---|
| B01 | Negocio | Registro y aprobación por el mismo usuario | Roles separados y control de operaciones fraccionadas | FICHA §G; objetivo TI §A; P01 | a-p1 → t-p1 |
| B02 | Negocio | Segregación inexistente en pagos | Doble control con usuarios distintos | FICHA §H; P01 | a-p5 → t-p5 |
| B03 | Datos | Sin dueño; 500 bodegas no conciliadas | ERP conciliado y dueño formalmente designado | Inventario §5; P02 | a-d-cliente → t-d-cliente |
| B04 | Datos | Fuente de hecho en libro; diferencia 4.7 % | Fuente ERP rehabilitada con conciliación | Inventario §5; objetivo TI; P02 | a-d-stock → t-d-stock |
| B05 | Aplicación | Portal sin mantenimiento y pedidos redigitados | Portal mantenido e integrado al ERP | Inventario §§2,4; OE-01,OE-02; P03,P05 | a-portal → t-portal |
| B06 | Aplicación | Sincronización nocturna; precios discrepantes | Sincronización con frescura acordada y precios únicos | Inventario §§4,5; OE-02; P03 | a-movil → t-movil |
| B07 | Tecnología | Disco local y restauración no probada | Copias separadas y recuperación verificada | FICHA §F; P04 | a-disco → t-backup |
| B08 | Tecnología | Red plana con invitados | Segmentos diferenciados y aislamiento de invitados | Inventario §6; P01,P04 | a-lan → t-lan |
| B09 | Tecnología | Enlace a Ilo sin respaldo | Contingencia de enlace con prueba de conmutación | Inventario §6; P04 | a-ilo → t-ilo |
| B10 | Aplicación | Hoja parcial y sin medición de acuerdos | Registro central con clasificación y seguimiento | Mesa §§1–5; OE-01,OE-02; P06 | a-mesa → t-mesa |
| B11 | Aplicación | Ubicaciones gestionadas en libro sin integración | Rehabilitar módulo y retirar libro tras aceptación | Inventario §§2,4; objetivo TI; P02,P03 | a-ubic → t-almacen |
| B12 | Negocio | Autorización informal y pruebas variables | Cambios con registro, pruebas y retorno | Mesa §7; P05 | a-cambio → t-cambio |

## Criterios de aceptación propuestos

- PT01: ninguna cuenta prueba puede registrar y aprobar la misma operación; operaciones relacionadas se someten a revisión según criterios acordados.
- PT02: las 500 bodegas discrepantes se revisan y se documenta su resolución; dueño de Cliente formalmente designado. No se decide eliminar registros sin investigar.
- PT03: ubicaciones y conteos aceptados por almacén; diferencias conciliadas antes de retirar libros operativos. No se presenta 4,7 % como meta tolerable.
- PT04: pedido trazable del portal al ERP sin redigitación; frescura de precios y stock acordada y probada; no se inventa una meta de 80 % digital.
- PT05: restauración y conmutación ensayadas con objetivos acordados tras completar BIA; invitados sin acceso a recursos internos según diseño aprobado.
- PT06: las atenciones del piloto quedan registradas, clasificadas y con responsable; cambios con autorización, prueba y plan de retorno.

Retiro: hojas de ubicaciones, conteos y registros paralelos solo después de migración y aceptación; los históricos se conservan conforme a una política por definir. El ERP y OSE con soporte se conservan.
