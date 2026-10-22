# Paso F — Validación y problemas pendientes

## Comprobaciones

1. **Carga en Archi y capas:** el modelo se carga y guarda mediante Archi 5.10.0, compatible con ArchiMate 3.2. Las nueve vistas se exportan desde su generador de vistas. El registro real está en `evidencias/S10/salidas/Archi_exportacion.txt`. AR06 comprueba identificadores, referencias y, al proporcionar la matriz oficial incluida en Archi, los tipos de relaciones permitidos. La revisión visual de los PNG verifica rótulos y legibilidad. No se afirma haber utilizado la interfaz gráfica del editor.
2. **Aplicaciones actuales:** ERP, móvil, OSE, portal, ubicaciones, conteos y precios se contrastan con arquitectura-actual.md §2. Libro de cobranza se acredita en §5. Hoja de atenciones se acredita en mesa-de-servicio-y-sla.md §§1–5. No se añadieron WMS, CRM ni plataforma analítica existentes. Roles y servicios inferidos están identificados como interpretación, no como catálogo aprobado.
3. **Brechas entre estados:** las 12 filas del CSV incluyen identificadores de elementos actuales y objetivo. AR06 comprueba que existen y aparecen en vistas; AR05 explica el cambio y su origen. El paso de una condición diagnosticada a una solución sigue siendo una propuesta académica.

## Problemas y mejoras

| Problema | Tratamiento y dato pendiente |
|---|---|
| El inventario contiene cuatro entidades y la guía exige seis | Se agregan Proveedor y Trabajador desde FICHA.md §I, sin inventar sistemas ni responsables. Sus campos pendientes impiden declarar cumplimiento íntegro del requisito. |
| Pedido tiene 220 000 líneas anuales, no registros por sistema | Se conserva la unidad original; obtener desglose sin convertir líneas en pedidos. |
| Fuente de Stock es de hecho | Confirmar su formalización; no marcarla como inexistente ni como gobierno del dato resuelto. |
| No hay PETI previo de Andina disponible | La propuesta se vincula al objetivo TI y al plan institucional. Falta trazabilidad a visión de TI, capacidades, FODA y marcos adoptados del PETI. |
| Plan 2023–2027 en ficha frente a 2024–2028 en extracto | Se usa el extracto para identificar OE-01 a OE-05, sin afirmar que la discrepancia de vigencia esté resuelta. |
| Ficha dice que no se registran incidentes; mesa describe hoja parcial | Se modela la hoja con registro parcial, dejando la contradicción documentada. |
| AR03 original del curso no aportado | Se desarrolló un programa propio equivalente para cálculos, agrupación y orden topológico. No se presenta como copia del programa del docente. |
| Estimaciones sin validación operativa | Los 130 días-persona son estimaciones académicas con justificación por brecha; no equivalen a 130 días de calendario ni a presupuesto. |

## Pregunta de transferencia

Si una organización modela mal su arquitectura, puede invertir en integraciones y aplicaciones que mantienen la duplicidad de datos y las fallas de aprobación. Si además ignora las dependencias, puede digitalizar pedidos sobre inventarios no conciliados y amplificar los errores operativos.

## Alcance de entrega

Se entregan proyecto y evidencias. El usuario excluyó expresamente la elaboración del informe Word/PDF; no se declara realizada la entrega al aula virtual. El uso de repositorio público fue autorizado por el docente según confirmación del usuario; se trabaja con el caso ficticio y sin direcciones IP ni credenciales.
