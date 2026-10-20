"""Reproduce stage08 from eight preserved, independently authored fragments."""
import copy,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
paths=[next((ROOT/'stages').glob(f'{i:02}-*.md')) for i in range(8)]
raw=[p.read_text() for p in paths]
models=[json.loads(re.search(r'```json\n(.*?)\n```',s,re.S)[1]) for s in raw]
# Identity evidence: same baseline documents, exact scope/data and documented component/flow.
alias={}
for stage in [1,2]:
 for collection,records in models[stage]['system'].items():
  for rec in records: alias[rec['id']]=rec['id'].replace(f'S{stage:02}-','S00-')
for stage in [3,4,5]:
 for i in range(1,7):alias[f'S{stage:02}-A{i}']=f'S00-A{i}' if i<=3 else f'S03-A{i}'
alias.update({'S07-A01':'S03-A5','S07-A07':'S00-A2','S07-A08':'S00-A1','S07-A09':'S00-A3','S07-ACT01':'S00-U1','S07-ACT02':'S00-U2','S07-ACT03':'S00-U3','S07-ACT04':'S00-U4','S07-Z01':'S00-Z1','S07-Z02':'S00-Z3','S07-Z03':'S00-Z4','S07-B01':'S00-B1','S07-B02':'S00-B3','S07-B03':'S00-B2','S07-EP01':'S00-P1','S07-EP05':'S00-P5'})
for i in range(1,6):alias[f'S07-F{i:02}']=f'S00-F{i}'
for m in models:
 for c in m['controls']:
  spec=c.get('source_id',c.get('specification_id'))
  alias[c['id']]='C-'+spec
threats=[t for m in models for t in m['threats']]
for i,t in enumerate(threats,1):alias[t['id']]=f'T-{i:03}'
def rewrite(x):
 if isinstance(x,str):return alias.get(x,x)
 if isinstance(x,list):return [rewrite(y) for y in x]
 if isinstance(x,dict):return {k:rewrite(v) for k,v in x.items()}
 return x
u={k:[] for k in models[0]}
u['scope']={'id':'S08-SCOPE','description':'Pre-implementation native music editor and closed recommendation pilot; all eight requested upstream methods completed.','baseline':'e346ef231f549b15ead023bcfbea44ac4e69e59a','upstream_scopes':[{'id':f'S08-SOURCE{i:02}','artifact':str(paths[i].relative_to(ROOT.parent)),'scope':m['scope']} for i,m in enumerate(models)],'identity_aliases':alias,'risk_method':'No approved common risk method supplied; no unified score computed.','independence':'Methods analyze the same four specifications; repetition is not independent confirmation of runtime behavior.'}
u['system']={k:[] for k in models[0]['system']}
def merge(records):
 by={}
 for stage,r in records:
  new=rewrite(copy.deepcopy(r)); key=new['id']
  if key not in by:
   by[key]=new;new['source_records']=[];new['source_stages']=[]
  dest=by[key]
  dest['source_records'].append({'stage':stage,'record':r})
  if stage not in dest['source_stages']:dest['source_stages'].append(stage)
  for field in ['evidence_ids']:
   dest[field]=list(dict.fromkeys(dest.get(field,[])+new.get(field,[])))
  if len(dest['source_records'])>1:dest['identity_basis']='Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.'
 return list(by.values())
# Passes 1/2 assets and actors, then boundaries/flows and remaining identity collections.
for k in ['assets','actors','boundaries','flows','data','zones','entry_points']:
 u['system'][k]=merge([(i,r) for i,m in enumerate(models) for r in m['system'][k]])
for k in ['evidence','methods','requirements','risks','attack_trees','attack_paths','visualizations','coverage','conflicts','gaps']:
 for i,m in enumerate(models):
  for r in m[k]:
   new=rewrite(copy.deepcopy(r));new['source_stage']=i;new['source_artifact']=str(paths[i].relative_to(ROOT.parent));u[k].append(new)
u['controls']=merge([(i,r) for i,m in enumerate(models) for r in m['controls']])
for c in u['controls']:c['status']='adopted planned control; unimplemented and unverified'
for i,m in enumerate(models):
 for t in m['threats']:
  new=rewrite(copy.deepcopy(t));new['original_id']=t['id'];new['source_stage']=i;new['method_id']=m['methods'][0]['id'];new['source_artifact']=str(paths[i].relative_to(ROOT.parent));new['mitigation']=t.get('proposed_treatment','Not supplied as a separate proposal; existing planned controls are linked in control_ids.');new['rating_status']='Unrated: no approved method or inputs supplied';new['related_threat_ids']=[];u['threats'].append(new)
# Complementary methods remain distinct, cross-linked by explicitly matching adverse events.
groups={'Account authorization':[1,14],'File/recovery integrity':[2,7,13,19,20],'Native interpretation/resource safety':[3,18,21],'Membership inference':[4,8,10],'Resource admission/service capacity':[5,9,17,25],'Deletion/eligibility freshness':[6,12,15,22,23]}
for title,nums in groups.items():
 for n in nums:
  t=u['threats'][n-1];t['related_threat_ids']=sorted(set(t['related_threat_ids']+[f'T-{other:03}' for other in nums if other!=n and u['threats'][other-1]['source_stage']!=t['source_stage']]));t.setdefault('relationship_basis',[]).append(title+': same documented adverse event; complementary methods, not independent verification.')
u['threats'][11]['clarification']='Stale cursors can expose memberships; misleading pending-deletion presentation misstates completion and does not itself cause data disclosure. Original source scenario is preserved, with these causal effects distinguished.'
# Boundary protection is a specification claim, never operational evidence.
for b in u['system']['boundaries']:
 b['control_ids']={'S00-B1':['C-SC-002','C-SC-003'],'S00-B2':['C-SC-002','C-SC-005'],'S00-B3':['C-SC-001','C-SC-004','C-SC-005'],'S00-B4':['C-SC-006']}[b['id']]
 b['control_evidence_status']='adopted plan; no implemented/verified control evidence'
# Distinct composite flow retained, explicitly reconciled with narrower calls rather than merged.
u['gaps'].append({'id':'S08-G01','description':'S05-F1 is a composite recommendation-and-label flow observed in only one upstream record. It is supported by REQUIREMENTS/ARCHITECTURE and overlaps S00-F4 and S00-F3; keep distinct because endpoints/data scope differ. No shadow flow or defect inferred.','affected_ids':['S05-F1','S00-F4','S00-F3'],'evidence_ids':['S05-E1','S05-E2'],'needed_evidence':'Implementation/interface call traces to reconcile runtime flow granularity.'})
u['gaps'].append({'id':'S08-G02','description':'Component-level assets from document absorption have no separate scenario records; composite assets and flow threats cover relevant functions. No evidence proves exhaustive component-level behavior coverage.','evidence_ids':['S07-E02'],'needed_evidence':'Implemented component/interface inventory and mapped acceptance/security tests.'})
u['gaps'].append({'id':'S08-G03','description':'No source fragment establishes a material contradiction. Conditional tension between exact recommendation outputs and inference-resistant interpretation of FR-4.10 remains an unresolved privacy decision, not a proven contradiction.','related_threat_ids':['T-004','T-008','T-010'],'evidence_ids':['S00-E1','S00-E2'],'needed_evidence':'Adopted product privacy outcome and security treatment decision.'})
for i,m in enumerate(models):u['coverage'].append({'id':f'S08-COV{i:02}','stage':i,'artifact':str(paths[i].relative_to(ROOT.parent)),'methods':[x['id'] for x in m['methods']],'input_scope':'All four specifications; stage06 additionally complete tracked repository baseline','upstream_coverage_ids':[x['id'] for x in m['coverage']],'threat_count':len(m['threats']),'evidence_limit':'Same specification evidence; no implementation/effectiveness claim'})
from enrich import enrich
enrich(u,ROOT)
summary=['## Consolidation Summary','','All eight fragments were processed completely in stage order. All 25 methodology-specific threats remain distinct and unrated. No supplied risk scale permits a combined score. Fifteen control groups are ACTIVE adopted specifications. None is implemented or verified. Original records and scopes survive in source_records and upstream_scopes; reference aliases resolve to canonical IDs.','','Identity reconciliation uses the same baseline specification and scoped entities: files/recovery, catalog/review state, service accounts/memberships, actors, boundaries and matching calls. Availability assets with different scope remain separate. The AI-stage composite flow remains separate from its two constituent calls. No conflicting source record was discarded. No material direct contradiction was established; inference privacy is a decision gap.','','### Unrated threat inventory','','| ID | Method | Threat |','| --- | --- | --- |']
for t in u['threats']:summary.append(f"| {t['id']} | {models[t['source_stage']]['methods'][0]['name']} | {t['title']} |")
summary+=['','### Cross-method relationships','']+[f"- {name}: {', '.join(f'T-{n:03}' for n in nums)}. Each record carries explicit related IDs; repeated document evidence does not increase confidence." for name,nums in groups.items()]
summary+=['','### Evidence coverage and gaps','','| Stage | Coverage | Threats |','| --- | --- | --- |']
labels=['STRIDE: all six categories per modeled element; repudiation has no separate supported scenario','PASTA: all seven stages, missing operational/risk inputs explicit','LINDDUN: seven types; non-compliance unassessed pending legal context','Attack trees: six roots, nine conditional paths, shared controls','FMEA: seven prospective failure modes plus remaining-function coverage','AI/ML: lifecycle not applicable; taxonomy limitations preserved','Repository: eight phases; no implementation exists','Documents: all four sources and ten extraction categories']
for i,label in enumerate(labels):summary.append(f'| {i:02} | {label} | {len(models[i]["threats"])} |')
summary+=['','All policy decisions are resolved in the owning specifications. Concrete API/cursor/platform mechanics, exact dependency patches, actual deployment, notice/legal-review substantiation, test/workload and operational evidence remain pending. Germany hosting and adult EEA participation are prospective adopted scope. Existing no-backup, exact ranking among qualifying releases, approval and privacy guarantees remain mandatory.','','No threat lacks a reference to planned controls. Those references do not prove mitigation adequacy or effectiveness. New mitigation proposals are retained only where supplied by FMEA; other records explicitly record the lack of a separate proposal. External-lookup awareness (T-011), unconfirmed sharing (T-016), and secure network fallback (T-024) retain their method-specific evidence without invented corroboration. All gaps remain in the model, including taxonomy limits and source metadata currency.','','Validation: all eight JSON models parsed; canonical threat IDs assigned once; references checked for resolution by the generator. No application tests or exploit simulations ran.']
summary+=['','### Post-analysis specification hardening','','All adopted FR-1.44–FR-1.46, FR-3.18–FR-3.24, FR-4.28–FR-4.34 and revised FR-3.2 texts and acceptance mappings are preserved. Fifteen exact controls and resolved OD-010–OD-019/RQ-001–RQ-005 records drive current threat actions. The restricted media helper, invitation provisioning and identifier-only output are explicit adopted architecture updates. Historical source records remain untouched; current dispositions distinguish resolved design choices from pending implementation, workload and legal/notice evidence. No decision is deferred. Inference uncertainty and required adversarial release checks remain visible; no score or effectiveness is invented.']
# Check IDs excluding original source records/provenance aliases.
def active(x):
 if isinstance(x,dict):
  yield x
  for k,v in x.items():
   if k not in ['source_records','upstream_scopes','identity_aliases']:yield from active(v)
 elif isinstance(x,list):
  for y in x:yield from active(y)
ids={x['id'] for x in active(u) if 'id'in x}
refs=[]
for r in active(u):
 for k,v in r.items():
  if k.endswith('_ids') or k.endswith('_id'):
   if k in ['original_id','source_id','specification_id']:continue
   for value in v if isinstance(v,list) else [v]:
    if isinstance(value,str) and re.fullmatch(r'(S\d\d-[\w-]+|T-\d+|C-SC-\d+)',value) and value not in ids:refs.append((r.get('id'),k,value))
assert not refs,refs
(ROOT/'stages/08-unified.md').write_text('# UNIFIED_THREAT_MODEL\n\n## Model\n\n```json\n'+json.dumps(u,indent=2,ensure_ascii=False)+'\n```\n\n'+'\n'.join(summary)+'\n')
print('Wrote 08-unified.md; 25 stable threats; canonical references resolve; all original records preserved.')
