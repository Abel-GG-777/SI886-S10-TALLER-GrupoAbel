# 5 Arquitectura empresarial

Distribuidora Andina del Sur S.A.C. necesita restablecer el control sobre compras y pagos y conciliar su inventario. La arquitectura propuesta conserva el ERP y el OSE soportados, corrige permisos, rehabilita el almacén y controla el intercambio de datos. Es una propuesta académica basada en el caso; no acredita aprobación de la empresa ni completa por sí sola todo el PETI.

## 5.1 Principios de arquitectura

Los seis principios, con declaración, razón, implicancias y trazabilidad, están desarrollados en [AR01_principios.md](AR01_principios.md): separación de funciones y mínimo privilegio; fuente autoritativa y responsable; integración controlada; recuperación probada; mantenimiento y cambios controlados; servicios con responsables y medición.

## 5.2 Arquitectura actual

### 5.2.1 Negocio

Se modelan los seis procesos de la ficha: compras y reposición, almacenamiento y despacho, venta en ruta, cobranza y crédito, tesorería y pagos y contabilidad y cierre. La vista 09 incorpora cargos documentados y una interpretación explícita de sus roles y servicios; no atribuye compromisos de servicio inexistentes.

### 5.2.2 Datos

[AR02_entidades.csv](AR02_entidades.csv) contiene Cliente, Producto, Stock y Pedido del inventario, más Proveedor y Trabajador identificados en la ficha. En las cuatro entidades del inventario hay cero ausencias explícitas de fuente: tres señalan ERP y Stock usa el libro de almacén de hecho, cuya formalización debe confirmarse. Hay una ausencia confirmada de dueño: Cliente. En las dos entidades complementarias la fuente y el dueño no se informan; no se contabilizan como ausencias comprobadas.

Las 500 bodegas del libro de cobranza ausentes del ERP requieren conciliación. La diferencia de inventario es 4,7 %, valorizada en S/ 310 000 según el caso. Los 220 000 de Pedido son líneas por año, no un conteo por sistema. Los 78 proveedores y 157 trabajadores son registros declarados de archivos de 2025. Estos límites impiden declarar seis entidades íntegramente levantadas.

### 5.2.3 Aplicaciones

ERP, aplicación móvil, OSE y portal conviven con libros de ubicaciones, conteos, precios y cobranza y una hoja parcial de atenciones de TI. El móvil sincroniza por la noche y el OSE se conecta en línea. Los pedidos del portal se transcriben al ERP; el almacén depende de libros sin integración. No se introduce un WMS independiente como sistema actual.

### 5.2.4 Tecnología

El inventario identifica servidor ERP en Tacna, nube del proveedor, hosting compartido, 70 estaciones, 24 móviles, red plana con invitados y enlace a Ilo sin respaldo. La ficha añade copias a disco local sin prueba de restauración completa. Las vistas no contienen direcciones IP ni credenciales.

### 5.2.5 Cooperación proceso–aplicación

El criterio documentado en [B_levantamiento_actual.md](B_levantamiento_actual.md) identifica cuatro de seis procesos con soporte deficiente y dos con soporte parcial. Ninguno carece por completo de una aplicación identificada. La deficiencia incluye controles y consistencia de datos, no solo ausencia de software. La vista 01 muestra los servicios y componentes; el ERP repetido visualmente es un único elemento del modelo.

## 5.3 Arquitectura objetivo

### 5.3.1 Derivación

Los cambios se sustentan en el objetivo TI de FICHA.md, los objetivos OE-01, OE-02 y OE-05 del extracto institucional, el inventario y los principios. No se ha aportado un PETI previo de Andina: no se inventan metas de visión digital, evaluaciones de capacidades ni estrategias FODA aprobadas. La trazabilidad a las secciones 2.2, 3.1.5, 3.5 y 4 debe completarse posteriormente.

### 5.3.2 Cambios por capa

[AR05_cambios_objetivo.md](AR05_cambios_objetivo.md) registra los doce cambios, su origen y los identificadores de ambos estados. En negocio se separan aprobaciones y se controlan cambios; en datos se concilian clientes y stock; en aplicaciones se rehabilita el almacén, integra el portal, controla la sincronización y centralizan atenciones; en tecnología se proponen recuperación, segmentación y contingencia del enlace.

### 5.3.3 Vistas objetivo

Las vistas 04–06 contienen la cooperación, aplicaciones/datos y tecnología objetivo. La vista 08 representa distribución de datos maestros; las relaciones del modelo también incluyen recepción de pedidos del portal y validación hacia ERP. Los libros se retiran de la operación solo después de migración, conciliación y aceptación, preservando los históricos.

## 5.4 Análisis de brechas

### 5.4.1 Brechas por capa y tipo

[AR03_brechas.csv](AR03_brechas.csv) contiene doce brechas: tres de negocio, dos de datos, cuatro de aplicación y tres de tecnología. Cada fila incluye tipo, situación actual, propuesta, origen, IDs del modelo, esfuerzo estimado, dependencias y justificación. Son cambios de modificación, incorporación o sustitución; no se exige una cuota artificial de cada tipo.

### 5.4.2 Paquetes de trabajo

| Paquete | Alcance | Brechas | Esfuerzo estimado en días-persona |
|---|---|---|---:|
| PT01 | Segregación en compras y pagos | B01, B02 | 14 |
| PT02 | Gobierno y conciliación de clientes | B03 | 12 |
| PT03 | Rehabilitación de almacén y conciliación de stock | B04, B11 | 33 |
| PT04 | Portal e integración móvil | B05, B06 | 30 |
| PT05 | Recuperación, red y enlace de contingencia | B07, B08, B09 | 24 |
| PT06 | Registro de servicios y control de cambios | B10, B12 | 17 |
| Total | Estimación académica | 12 brechas | 130 |

El esfuerzo no representa presupuesto ni duración calendario. Requiere estimación con responsables, disponibilidad y proveedores antes de planificar ejecución.

### 5.4.3 Dependencias y secuencia

El programa calcula una primera oleada PT01, PT02, PT05 y PT06; después PT03; por último PT04. Son precedencias propuestas, sin considerar restricciones de personal. Internamente B01 precede B02, B11 precede B04 y B10 precede B12. Los paquetes son insumo del portafolio de la sección 7.1, que no se desarrolla en este taller.

## Validación y alcance

[AR07_validacion_y_limites.md](AR07_validacion_y_limites.md) documenta las comprobaciones y pendientes. Las salidas de AR03 y AR06 y el registro de exportación de Archi están en `evidencias/S10/salidas/`. Este archivo es la sección técnica del proyecto; no es el informe de entrega Word/PDF, excluido por el usuario.
