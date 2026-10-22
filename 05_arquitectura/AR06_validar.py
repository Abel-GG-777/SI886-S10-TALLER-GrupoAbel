"""Validación documental y estructural; no sustituye aceptación del negocio.
Uso: python 05_arquitectura/AR06_validar.py [--reglas-archi RUTA/relationships.xml]
"""
from pathlib import Path
import argparse, csv, json, importlib.util, xml.etree.ElementTree as E
from graphlib import CycleError

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--reglas-archi');args=ap.parse_args()
    base=Path(__file__).resolve().parent;root=base.parent
    m=E.parse(base/'AR04_modelo_arquitectura.archimate').getroot();xsi='{http://www.w3.org/2001/XMLSchema-instance}type'
    allids=[e.get('id') for e in m.iter() if e.get('id')];assert len(allids)==len(set(allids)), 'IDs duplicados'
    elements={e.get('id'):e for f in m.findall('folder') for e in f.findall('element') if f.get('type') not in ['relations','diagrams']}
    relationships=m.findall("folder[@type='relations']/element");views=m.findall("folder[@type='diagrams']/element")
    for e in relationships:assert e.get('source') in elements and e.get('target') in elements,'Relación colgante'
    for v in views:
        for o in v.findall('child'):assert o.get('archimateElement') in elements,'Objeto visual colgante'
    rules_status='No ejecutada: pasar --reglas-archi'
    if args.reglas_archi:
        rules=E.parse(args.reglas_archi).getroot();allowed={(s.get('concept'),t.get('concept')):t.get('relations') for s in rules for t in s}
        keys={'AccessRelationship':'a','FlowRelationship':'f','RealizationRelationship':'r','ServingRelationship':'v','AssociationRelationship':'o','AssignmentRelationship':'i'}
        for e in relationships:
            s=elements[e.get('source')].get(xsi).split(':')[-1];t=elements[e.get('target')].get(xsi).split(':')[-1];typ=e.get(xsi).split(':')[-1]
            assert keys[typ] in allowed.get((s,t),''),f'Relación inválida: {s} {typ} {t}'
        rules_status=f'{len(relationships)} relaciones permitidas por matriz ArchiMate {rules.get("version")}'
    with open(base/'AR03_brechas.csv',encoding='utf-8-sig',newline='') as f:gaps=list(csv.DictReader(f))
    assert len(gaps)>=10
    shown={o.get('archimateElement') for v in views for o in v.findall('child')}
    for g in gaps:
        assert g['elemento_actual_id'].startswith('a-') and g['elemento_objetivo_id'].startswith('t-')
        assert g['elemento_actual_id'] in shown and g['elemento_objetivo_id'] in shown
    with open(base/'AR02_entidades.csv',encoding='utf-8-sig',newline='') as f:entities=list(csv.DictReader(f))
    assert len(entities)>=6
    spec=importlib.util.spec_from_file_location('brechas',base/'AR03_brechas.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    order,deps,waves=mod.analizar(mod.BRECHAS);pos={v:i for i,v in enumerate(order)}
    assert all(pos[d]<pos[r['id']] for r in mod.BRECHAS for d in r['dependencias'])
    # Comprobar que el programa detecta errores de dependencias, no solo el caso válido.
    for rows in [[dict(id='X',paquete='P',esfuerzo_dias_persona=1,dependencias=['Z'])], [dict(id='X',paquete='P',esfuerzo_dias_persona=1,dependencias=['X'])]]:
        try:mod.analizar(rows)
        except (ValueError,CycleError):pass
        else:raise AssertionError('Se aceptó dependencia inválida')
    summary={'elementos':len(elements),'vistas':len(views),'relaciones':len(relationships),'reglas_archimate':rules_status,'brechas':len(gaps),'entidades':len(entities),'secuencia_valida':True,'deteccion_dependencia_inexistente_y_ciclo':True,'esfuerzo_estimado_dias_persona':sum(int(g['esfuerzo_dias_persona']) for g in gaps),'limites':['Pedido sin conteos por sistema','Proveedor y Trabajador con sistemas, fuentes y dueños no informados','Sin PETI previo de Andina para trazabilidad completa','Validación contra el caso ficticio; no auditoría ni aprobación de la organización']}
    path=root/'evidencias/S10/salidas/AR06_validacion.json';path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
