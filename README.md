# SI886 S10 Taller GrupoAbel

Arquitectura empresarial de **Distribuidora Andina del Sur S.A.C.**, Empresa 06 del banco de casos ficticios del curso.

Autor: **Pacompía Ortiz Abel Fernando**, código **2023076797**. GrupoAbel es el identificador del repositorio; no se declara número oficial de grupo.

## Contenido

- `05_arquitectura/AR01_principios.md`: seis principios y evidencia de origen.
- `05_arquitectura/AR02_entidades.csv`: seis entidades; campos no informados señalados explícitamente.
- `05_arquitectura/AR03_brechas.py` y `.csv`: 12 brechas, estimaciones y dependencias.
- `05_arquitectura/AR03_paquetes.csv`: seis paquetes y sus predecesores.
- `05_arquitectura/AR04_modelo_arquitectura.archimate`: modelo nativo para Archi, con estados actual y propuesto y nueve vistas.
- `05_arquitectura/AR05_cambios_objetivo.md`: trazabilidad y criterios de aceptación propuestos.
- `05_arquitectura/AR06_validar.py`: validaciones reproducibles.
- `05_arquitectura/AR07_validacion_y_limites.md`: comprobaciones, resultados parciales y transferencia.
- `05_arquitectura/SECCION_5_PETI.md`: redacción de la sección 5.
- `graficos/`: nueve PNG exportados desde Archi.
- `evidencias/S10/`: salidas reales y lista de comprobación.
- `fuentes/`: documentos del caso utilizados.

## Ejecutar el análisis

Requisitos: Python 3.11 o posterior y pandas. Desde la raíz:

```text
python -m pip install -r requirements.txt
python 05_arquitectura/AR03_brechas.py
python 05_arquitectura/AR06_validar.py
```

La comprobación adicional de relaciones usa `--reglas-archi` con el archivo `model/relationships.xml` de la distribución oficial de Archi. La ejecución registrada sí incluyó esa matriz.

## Abrir el modelo

En Archi 5.10 o compatible, elegir Archivo > Abrir y seleccionar el archivo `.archimate`. En Vistas se encuentran 01–09. El ERP repetido en una vista representa el mismo componente, no sistemas distintos. Amarillo: negocio; azul: aplicación/datos; verde: tecnología.

| PNG | Vista |
|---|---|
| v01 | Cooperación actual proceso–aplicación |
| v02 | Inventario actual de aplicaciones y datos |
| v03 | Tecnología actual |
| v04 | Cooperación objetivo proceso–aplicación |
| v05 | Aplicaciones y datos objetivo |
| v06 | Tecnología objetivo |
| v07 | Integraciones automáticas actuales |
| v08 | Distribución propuesta de datos maestros |
| v09 | Actores, roles y servicios de negocio actuales |

## Límites que deben conservarse

La arquitectura objetivo es una propuesta, no una decisión aprobada por Andina. No hay PETI previo de esta empresa para completar toda la trazabilidad exigida. Proveedor, Trabajador y Pedido conservan campos pendientes. Leer AR07 antes de declarar el taller totalmente logrado.

Por indicación del autor, este proyecto no incluye el informe Word/PDF. El repositorio público está autorizado según la confirmación del docente comunicada por el autor.
