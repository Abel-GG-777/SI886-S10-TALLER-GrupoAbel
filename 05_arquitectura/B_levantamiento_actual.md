# Paso B — Arquitectura actual de Distribuidora Andina del Sur

Base: arquitectura-actual.md, entregado el 11 de julio de 2026, contrastado con FICHA.md y mesa-de-servicio-y-sla.md.

Estado: levantamiento documental incorporado al modelo AR04_modelo_arquitectura.archimate, cargado y guardado con Archi 5.10.0. Las nueve vistas se exportaron en PNG. Los datos pendientes del caso se conservan explícitamente.

## B.1 Negocio y B.4 Cooperación proceso–aplicación

La clasificación siguiente es un análisis del equipo: deficiente cuando existen fallos relevantes de control o inconsistencias operativas documentadas; parcial cuando existe soporte con limitaciones. No es una calificación literal del inventario.

| Proceso | Soporte | Evaluación y evidencia |
|---|---|---|
| Compras y reposición | ERP | Deficiente: autoaprobación y fraccionamiento, FICHA.md §G. |
| Almacenamiento y despacho | Hojas de ubicaciones y conteos; módulo ERP abandonado | Deficiente: sin integración, diferencia de inventario de 4,7 %. |
| Venta y distribución en ruta | Fuerza de ventas móvil | Parcial: sincronización nocturna y precios distintos entre app y libro. |
| Cobranza y crédito | ERP y libro de cobranza | Deficiente: 500 bodegas del libro no están en ERP y Cliente no tiene dueño. |
| Tesorería y pagos | ERP | Deficiente en control: segregación inexistente según FICHA.md §H. |
| Contabilidad y cierre | ERP | Parcial: lentitud durante cierres y discrepancia entre inventario contable y físico. |

Con este criterio: **4 de 6 procesos con soporte deficiente, 2 de 6 con soporte parcial y 0 de 6 sin aplicaciones identificadas**. Debe validarse la evaluación con el equipo.

La recepción por portal tiene transcripción manual. Se registra como flujo adicional, sin aumentar artificialmente el denominador de seis procesos de la ficha.

Actores y cargos documentados: vendedores, jefe comercial, jefe de almacén, Jefe de Sistemas, Gerencia General y Gerencia de Administración y Finanzas. Falta contrastar la asignación de roles y servicios con la cadena de valor del PETI. No se importan del ejemplo compromisos de entrega en 24 horas o crédito a 30 días.

## B.2 Aplicaciones e integraciones

| Componente | Situación |
|---|---|
| ERP comercial | Compras, ventas, almacén, tesorería y contabilidad; soporte vigente. |
| Fuerza de ventas móvil | Aplicación del proveedor; soporte vigente. |
| Facturación electrónica | OSE contratado, SaaS, soporte vigente. |
| Portal | Desarrollo propio sin soporte vigente. |
| Hoja de ubicaciones | PC del área o carpeta compartida; componente de aplicación. |
| Hoja de conteos de inventario | PC del área o carpeta compartida; componente de aplicación. |
| Hoja de precios y promociones | PC del área o carpeta compartida; componente de aplicación. |
| Libro de cobranza | Identificado en la tabla de entidades; alojamiento y soporte no informados. |
| Hoja de atenciones de TI | Registro parcial, según mesa-de-servicio-y-sla.md. |

Gestión de almacén describe una combinación de módulo ERP y hojas, no un WMS independiente. El módulo está abandonado según el inventario y no debe figurar como soporte operativo pleno.

| Origen | Destino | Mecanismo actual |
|---|---|---|
| ERP | Fuerza de ventas móvil | Sincronización nocturna del proveedor. |
| ERP | Facturación electrónica | En línea con el OSE. |
| ERP almacén | Libros de almacén | Ninguna integración; módulo abandonado. |
| Portal | ERP | Transcripción manual. |

No se han especificado API, protocolos o interfaces concretas. La transcripción no es integración automática.

## B.3 Tecnología

- Servidor propio del ERP en Tacna.
- Nube del proveedor para fuerza de ventas.
- Hosting compartido del portal y servicio externo SaaS del OSE.
- 70 estaciones y 24 móviles de vendedores.
- Red plana con red inalámbrica de invitados; segmentación efectiva no descrita.
- Enlace del operador a Ilo sin respaldo.
- Respaldos a disco local sin prueba completa de restauración, según la ficha.

No se deduce la infraestructura física de los servicios externos ni se añaden direcciones, credenciales o versiones.

## B.5 Información

AR02_entidades.csv contiene las cuatro entidades del inventario y dos complementarias de FICHA.md §I: Proveedor y Trabajador.

| Indicador | Resultado documental |
|---|---|
| Fuentes declaradas | ERP para Cliente, Producto y Pedido. |
| Fuente de hecho | Libro de almacén para Stock; formalización no acreditada. |
| Entidades explícitamente sin fuente | 0 de las 4 del inventario; las 2 complementarias tienen información pendiente. |
| Entidades explícitamente sin dueño | 1 de las 4 del inventario: Cliente. |
| Dueños del catálogo ampliado | 1 ausencia confirmada, 3 dueños identificados y 2 no informados. |
| Datos personales | Cliente, Pedido, Proveedor y Trabajador. |

No informado no equivale a inexistente. Las clasificaciones de Proveedor y Trabajador se proponen para validación, no se atribuyen a la fuente.

Cliente, Producto y Stock tienen conteos por sistema. Pedido solo tiene 220 000 líneas al año: no representa número de pedidos ni desglose por sistema. Proveedor y Trabajador tienen 78 y 157 registros respectivamente en archivos del periodo 2025, no conteos por sistema. No se suman copias de la misma entidad ni se interpreta un subconjunto del portal como error sin evidencia.

## Pendientes para cerrar B

1. Modelo cargado, guardado y exportado mediante Archi. Validación de sus 60 relaciones contra la matriz de ArchiMate 3.2 completada; ver AR07 y las salidas de validación.
2. Obtener desglose de Pedido y confirmar sistemas, conteos, fuentes y dueños de las dos entidades complementarias. Seis filas no equivalen a seis entidades completas.
3. Contrastar actores, roles y servicios con la cadena de valor del equipo.

## Continuación C–G

La arquitectura objetivo está modelada como propuesta y documentada en AR05. AR03 calcula doce brechas y seis paquetes; AR06 y AR07 registran las validaciones y límites. La trazabilidad completa a las secciones previas del PETI sigue pendiente por falta de esos documentos. El estado de Git se registra por separado; no se presume una publicación o fusión a partir de la existencia de archivos locales.
