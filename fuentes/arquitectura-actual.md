<div align="center">
  <strong>DISTRIBUIDORA ANDINA DEL SUR S.A.C.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | DISTRIBUIDORA ANDINA DEL SUR S.A.C. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 11 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **ERP comercial** | Producto peruano con módulos de compras, ventas, almacén, tesorería y contabilidad | Servidor propio | Sí |
| **Fuerza de ventas móvil** | App del proveedor del ERP | Nube del proveedor | Sí |
| **Facturación electrónica** | OSE contratado | SaaS | Sí |
| **Gestión de almacén** | Módulo del ERP más hojas de cálculo paralelas | Mixto | Parcial |
| **Portal de pedidos para clientes** | Desarrollo propio | Hosting compartido | No |
| **Hoja de cálculo · Ubicaciones de almacén** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Conteos de inventario** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Precios y promociones** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Compras a proveedores y reposición | ERP comercial |
| Almacenamiento y despacho | Gestión de almacén |
| Venta y distribución en ruta | Fuerza de ventas móvil |
| Cobranza y crédito a clientes | ERP comercial |
| Tesorería y pagos | ERP comercial |
| Contabilidad y cierre | ERP comercial |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| ERP | Fuerza de ventas móvil | Sincronización nocturna del proveedor |
| ERP | Facturación electrónica | En línea con el operador de servicios electrónicos |
| ERP almacén | Libros de almacén | Ninguna. El módulo se dejó de usar |
| Portal de pedidos | ERP | Manual. Los pedidos del portal se digitan |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Cliente | ERP · Fuerza de ventas · Portal de pedidos · Libro de cobranza | 8 400 · 8 400 · 340 · 8 900 | ERP, declarada | Ninguno | 500 bodegas en cobranza que no están en el ERP | Confidencial | Sí |
| Producto | ERP · Libro de precios · Fuerza de ventas · Portal | 6 200 · 6 400 · 6 200 · 1 100 | ERP | Jefe comercial | Precios distintos en la app y en el libro | Interna | No |
| Stock | ERP almacén, abandonado · Libro de almacén · Fuerza de ventas · Portal | 6 200 · 4 900 · 6 200 · 1 100 | El libro del almacén, de hecho | Jefe de almacén | 4.7 % de diferencia, S/ 310 000 | Interna | No |
| Pedido | Fuerza de ventas · Portal · ERP · Papel | 220 000 líneas al año | ERP | Jefe comercial | Pedidos del portal digitados dos veces | Confidencial | Sí, de contacto |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor propio del ERP en Tacna · la nube del proveedor para la fuerza de ventas · hosting compartido del portal · el almacén de Ilo por el enlace de un operador · 70 estaciones y 24 móviles de vendedores.

**Redes.** Red plana con red inalámbrica de invitados. Ilo por enlace del operador, sin respaldo.

## 7. Lo que la organización responde

| Pregunta del equipo | Respuesta |
|---|---|
| ¿Existe un diagrama de arquitectura? | «Hay uno de red en una pizarra. Nunca se dibujaron los sistemas» |
| ¿Quién aprueba que un área cree una hoja de cálculo para operar? | «Nadie. Aparecen y después hay que alimentarlas» |
| ¿Quién es el dueño de cada dato? | «El sistema que lo tiene. Si está en dos, los dos» |
| ¿Qué pasa cuando dos sistemas dicen cifras distintas? | «Se pregunta al que lo lleva y se usa esa» |
| ¿Hay principios de arquitectura escritos? | «No» |

## 8. Marco de referencia

| Marco | Qué aporta |
|---|---|
| **TOGAF, 10.ª edición · ADM** | Fases B, C y D para la arquitectura de negocio, de sistemas de información y de tecnología, y el análisis de brechas |
| **ArchiMate 3.2** | El lenguaje con el que se modelan las capas y sus relaciones |
| **COBIT 2019 · APO03** | Gestión de la arquitectura empresarial |

