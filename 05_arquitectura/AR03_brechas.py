"""Análisis S10 de Andina. Elaboración propia: no se recibió el programa base AR03 del curso.
Los esfuerzos son estimaciones académicas en días-persona, no costos ni duraciones calendario.
Ejecutar: python 05_arquitectura/AR03_brechas.py
"""
from pathlib import Path
import json, sys
from graphlib import TopologicalSorter, CycleError
import pandas as pd

BRECHAS = [{'id': 'B01', 'capa': 'Negocio', 'tipo': 'Modificar', 'elemento_actual_id': 'a-p1', 'elemento_objetivo_id': 't-p1', 'actual': 'Registro y aprobación por el mismo usuario', 'objetivo': 'Roles separados y control de operaciones fraccionadas', 'origen': 'FICHA §G; objetivo TI §A; P01', 'paquete': 'PT01', 'esfuerzo_dias_persona': 8, 'dependencias': [], 'justificacion_esfuerzo': 'Reconfiguración y pruebas de perfiles'}, {'id': 'B02', 'capa': 'Negocio', 'tipo': 'Modificar', 'elemento_actual_id': 'a-p5', 'elemento_objetivo_id': 't-p5', 'actual': 'Segregación inexistente en pagos', 'objetivo': 'Doble control con usuarios distintos', 'origen': 'FICHA §H; P01', 'paquete': 'PT01', 'esfuerzo_dias_persona': 6, 'dependencias': ['B01'], 'justificacion_esfuerzo': 'Revisión de flujo y pruebas de autorización'}, {'id': 'B03', 'capa': 'Datos', 'tipo': 'Modificar', 'elemento_actual_id': 'a-d-cliente', 'elemento_objetivo_id': 't-d-cliente', 'actual': 'Sin dueño; 500 bodegas no conciliadas', 'objetivo': 'ERP conciliado y dueño formalmente designado', 'origen': 'Inventario §5; P02', 'paquete': 'PT02', 'esfuerzo_dias_persona': 12, 'dependencias': [], 'justificacion_esfuerzo': 'Perfilado, depuración y aceptación comercial'}, {'id': 'B04', 'capa': 'Datos', 'tipo': 'Modificar', 'elemento_actual_id': 'a-d-stock', 'elemento_objetivo_id': 't-d-stock', 'actual': 'Fuente de hecho en libro; diferencia 4.7 %', 'objetivo': 'Fuente ERP rehabilitada con conciliación', 'origen': 'Inventario §5; objetivo TI; P02', 'paquete': 'PT03', 'esfuerzo_dias_persona': 15, 'dependencias': ['B03', 'B11'], 'justificacion_esfuerzo': 'Reglas de conciliación, carga y pruebas'}, {'id': 'B05', 'capa': 'Aplicación', 'tipo': 'Modificar', 'elemento_actual_id': 'a-portal', 'elemento_objetivo_id': 't-portal', 'actual': 'Portal sin mantenimiento y pedidos redigitados', 'objetivo': 'Portal mantenido e integrado al ERP', 'origen': 'Inventario §§2,4; OE-01,OE-02; P03,P05', 'paquete': 'PT04', 'esfuerzo_dias_persona': 20, 'dependencias': ['B03', 'B04', 'B11'], 'justificacion_esfuerzo': 'Interfaz, mantenimiento, pruebas y aceptación'}, {'id': 'B06', 'capa': 'Aplicación', 'tipo': 'Modificar', 'elemento_actual_id': 'a-movil', 'elemento_objetivo_id': 't-movil', 'actual': 'Sincronización nocturna; precios discrepantes', 'objetivo': 'Sincronización con frescura acordada y precios únicos', 'origen': 'Inventario §§4,5; OE-02; P03', 'paquete': 'PT04', 'esfuerzo_dias_persona': 10, 'dependencias': ['B03', 'B04', 'B11'], 'justificacion_esfuerzo': 'Acuerdo de datos, configuración y prueba con proveedor'}, {'id': 'B07', 'capa': 'Tecnología', 'tipo': 'Agregar', 'elemento_actual_id': 'a-disco', 'elemento_objetivo_id': 't-backup', 'actual': 'Disco local y restauración no probada', 'objetivo': 'Copias separadas y recuperación verificada', 'origen': 'FICHA §F; P04', 'paquete': 'PT05', 'esfuerzo_dias_persona': 10, 'dependencias': [], 'justificacion_esfuerzo': 'Diseño, copia y ensayo de restauración'}, {'id': 'B08', 'capa': 'Tecnología', 'tipo': 'Modificar', 'elemento_actual_id': 'a-lan', 'elemento_objetivo_id': 't-lan', 'actual': 'Red plana con invitados', 'objetivo': 'Segmentos diferenciados y aislamiento de invitados', 'origen': 'Inventario §6; P01,P04', 'paquete': 'PT05', 'esfuerzo_dias_persona': 8, 'dependencias': [], 'justificacion_esfuerzo': 'Diseño lógico y pruebas de aislamiento'}, {'id': 'B09', 'capa': 'Tecnología', 'tipo': 'Agregar', 'elemento_actual_id': 'a-ilo', 'elemento_objetivo_id': 't-ilo', 'actual': 'Enlace a Ilo sin respaldo', 'objetivo': 'Contingencia de enlace con prueba de conmutación', 'origen': 'Inventario §6; P04', 'paquete': 'PT05', 'esfuerzo_dias_persona': 6, 'dependencias': [], 'justificacion_esfuerzo': 'Factibilidad, contratación y pruebas; plazo proveedor no incluido'}, {'id': 'B10', 'capa': 'Aplicación', 'tipo': 'Sustituir', 'elemento_actual_id': 'a-mesa', 'elemento_objetivo_id': 't-mesa', 'actual': 'Hoja parcial y sin medición de acuerdos', 'objetivo': 'Registro central con clasificación y seguimiento', 'origen': 'Mesa §§1–5; OE-01,OE-02; P06', 'paquete': 'PT06', 'esfuerzo_dias_persona': 12, 'dependencias': [], 'justificacion_esfuerzo': 'Configuración del registro y diseño de métricas'}, {'id': 'B11', 'capa': 'Aplicación', 'tipo': 'Sustituir', 'elemento_actual_id': 'a-ubic', 'elemento_objetivo_id': 't-almacen', 'actual': 'Ubicaciones gestionadas en libro sin integración', 'objetivo': 'Rehabilitar módulo y retirar libro tras aceptación', 'origen': 'Inventario §§2,4; objetivo TI; P02,P03', 'paquete': 'PT03', 'esfuerzo_dias_persona': 18, 'dependencias': ['B01', 'B03', 'B07'], 'justificacion_esfuerzo': 'Ajuste funcional, migración y piloto'}, {'id': 'B12', 'capa': 'Negocio', 'tipo': 'Modificar', 'elemento_actual_id': 'a-cambio', 'elemento_objetivo_id': 't-cambio', 'actual': 'Autorización informal y pruebas variables', 'objetivo': 'Cambios con registro, pruebas y retorno', 'origen': 'Mesa §7; P05', 'paquete': 'PT06', 'esfuerzo_dias_persona': 5, 'dependencias': ['B10'], 'justificacion_esfuerzo': 'Diseño de flujo y piloto de cambios'}]

def analizar(rows):
    ids=[x['id'] for x in rows]
    if len(ids)!=len(set(ids)): raise ValueError('Identificadores duplicados')
    for row in rows:
        if row['esfuerzo_dias_persona']<=0: raise ValueError('Esfuerzo no positivo')
        if set(row['dependencias'])-set(ids): raise ValueError('Dependencia inexistente')
    orden=list(TopologicalSorter({x['id']:set(x['dependencias']) for x in rows}).static_order())
    byid={x['id']:x for x in rows}; deps={x['paquete']:set() for x in rows}
    for row in rows:
        deps[row['paquete']].update(byid[d]['paquete'] for d in row['dependencias'] if byid[d]['paquete']!=row['paquete'])
    ts=TopologicalSorter(deps);ts.prepare();oleadas=[]
    while ts.is_active():
        ready=sorted(ts.get_ready());oleadas.append(ready);ts.done(*ready)
    return orden,deps,oleadas

def main():
    base=Path(__file__).resolve().parent; root=base.parent
    orden,deps,oleadas=analizar(BRECHAS)
    df=pd.DataFrame(BRECHAS); out=df.copy();out['dependencias']=out['dependencias'].map(lambda x:';'.join(x))
    out.to_csv(base/'AR03_brechas.csv',index=False,encoding='utf-8-sig')
    paquetes=df.groupby('paquete',sort=True).agg(esfuerzo_dias_persona=('esfuerzo_dias_persona','sum'),brechas=('id',lambda s:';'.join(s))).reset_index()
    paquetes['dependencias']=paquetes['paquete'].map(lambda p:';'.join(sorted(deps[p])))
    paquetes.to_csv(base/'AR03_paquetes.csv',index=False,encoding='utf-8-sig')
    texto='ANDINA S10 — estimaciones académicas, no compromisos de ejecución\n'
    texto+=df.groupby('capa').size().to_string()+'\n\n'+paquetes.to_string(index=False)
    texto+='\n\nEsfuerzo total: '+str(df.esfuerzo_dias_persona.sum())+' días-persona\n'
    texto+='Orden válido de brechas: '+' -> '.join(orden)+'\n'
    texto+='Oleadas de paquetes por dependencias (no calendario ni capacidad): '+str(oleadas)+'\n'
    texto+='PT03 contiene B11 antes de B04; PT01 contiene B01 antes de B02; PT06 contiene B10 antes de B12.\n'
    texto='\n'.join(line.rstrip() for line in texto.splitlines())+'\n'
    print(texto)
    outdir=root/'evidencias/S10/salidas';outdir.mkdir(parents=True,exist_ok=True)
    (outdir/'AR03_resultados.txt').write_text(texto,encoding='utf-8')
    (outdir/'AR03_secuencia.json').write_text(json.dumps({'orden_brechas':orden,'oleadas_paquetes':oleadas},ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__': main()
