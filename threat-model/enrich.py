"""Append adopted resolution evidence; preserve baseline scenarios and observations."""
import hashlib,re

def enrich(u,root):
 texts={f:(root.parent/f).read_text() for f in ['REQUIREMENTS.md','ARCHITECTURE.md','SECURITY.md','DESIGN.md']};evidence={}
 for i,(f,text) in enumerate(texts.items(),1):
  eid=f'POST-E{i:02}';evidence[f]=eid
  u['evidence'].append({'id':eid,'source':f,'locator':'Final adopted threat-driven specification and resolved decisions','sha256':hashlib.sha256(text.encode()).hexdigest(),'status':'adopted specification under maintainer authorization; no implementation or verification','baseline_preserved':True})
 rq=texts['REQUIREMENTS.md'];sec=texts['SECURITY.md'];arch=texts['ARCHITECTURE.md']
 def threats(text):return list(dict.fromkeys(re.findall(r'T-\d{3}',text)))
 # Parse table range notation into exact members, preserving source acceptance text.
 def ids(text):
  result=set(re.findall(r'FR-\d+\.\d+',text))
  for a,b,c,d in re.findall(r'FR-(\d+)\.(\d+)–FR-(\d+)\.(\d+)',text):
   if a==c:result.update(f'FR-{a}.{n}' for n in range(int(b),int(d)+1))
  return result
 acceptance=[]
 for line in rq.splitlines():
  if line.startswith('| FR-'):
   cells=[x.strip() for x in line.split('|')[1:-1]];acceptance.append((ids(cells[0]),cells[1]))
 for line in rq.splitlines():
  match=re.match(r'- \*\*(FR-\d+\.\d+)\*\* (.*)',line)
  if not match:continue
  rid,text=match.groups()
  wanted=rid=='FR-3.2' or rid in [f'FR-1.{n}' for n in range(44,47)]+[f'FR-3.{n}' for n in range(18,25)]+[f'FR-4.{n}' for n in range(28,35)]
  if not wanted:continue
  flow='S00-F2' if rid in ['FR-1.44','FR-1.46'] else 'POST-F01' if rid=='FR-1.45' else 'S00-F3' if rid in ['FR-3.18','FR-3.24'] else 'S00-F4'
  ac=[{'id':'AC-'+rid+'-'+str(i+1),'exact_text':t,'status':'required future check; not executed'} for i,(rs,t) in enumerate(acceptance) if rid in rs or rid=='FR-3.2' and 'FR-3.20'in rs]
  u['requirements'].append({'id':'REQ-'+rid,'specification_id':rid,'exact_text':text.split(' Threat')[0],'authority':'project REQUIREMENTS.md','edition':'final resolution source hash in POST-E01','status':'adopted; future verification required','applicability':'first-release native desktop and closed pilot','evidence_ids':[evidence['REQUIREMENTS.md']],'threat_ids':threats(text),'flow_ids':[flow]+(['S00-F5'] if rid=='FR-3.18' else []),'acceptance_criteria':ac})
 decisions={};productmap={'OD-010':'RQ-001','OD-011':'RQ-002','OD-015':'RQ-005','OD-016':'RQ-003','OD-017':'RQ-004'}
 for line in sec.splitlines():
  if re.match(r'\| OD-01\d \|',line):
   cells=[x.strip() for x in line.split('|')[1:-1]];oid=cells[0];deps=re.findall(r'SC-\d{3}',cells[-1])
   decisions[oid]={'id':'DEC-'+oid,'specification_id':oid,'status':'RESOLVED; adopted, verification pending','description':cells[1],'dependent_control_ids':['C-'+x for x in deps],'threat_ids':threats(cells[-1]),'owning_product_items':[productmap[oid]] if oid in productmap else [],'evidence_ids':[evidence['SECURITY.md']]};u['gaps'].append(decisions[oid])
 for line in rq.splitlines():
  if line.startswith('| RQ-'):
   cells=[x.strip() for x in line.split('|')[1:-1]];u['gaps'].append({'id':'DEC-'+cells[0],'specification_id':cells[0],'owner':'REQUIREMENTS.md','status':'RESOLVED; adopted product policy, unimplemented','description':cells[1],'dependencies':cells[2],'evidence_ids':[evidence['REQUIREMENTS.md']]})
 # Every current control's exact source text is retained; historic observations stay intact.
 for n in range(1,16):
  sid=f'SC-{n:03}';section=re.search(r'### '+sid+r' — (.*?)(?=\n### |\n## |\Z)',sec,re.S)[1].strip();cs=next((x for x in u['controls'] if x['id']=='C-'+sid),None)
  if cs is None:cs={'id':'C-'+sid,'specification_id':sid};u['controls'].append(cs)
  cs.update({'name':section.splitlines()[0].replace(' — ACTIVE',''),'exact_text':section,'status':'ACTIVE adopted specification; unimplemented and unverified','decision_ids':[d['id'] for d in decisions.values() if 'C-'+sid in d['dependent_control_ids']],'threat_ids':threats(section)})
  cs['evidence_ids']=list(dict.fromkeys(cs.get('evidence_ids',[])+[evidence['SECURITY.md']]))
 # Newly adopted architecture is explicit post-analysis evidence, not discovered code.
 def add(coll,record):record['status']='adopted post-analysis design; unimplemented';record['evidence_ids']=[evidence['ARCHITECTURE.md']];u['system'][coll].append(record)
 add('assets',{'id':'POST-A01','name':'Restricted local media helper','technology':'Child process behind media adapter; TagLib 2.x media parsing/transformation','threat_ids':['T-003','T-005','T-021'],'control_ids':['C-SC-002','C-SC-003','C-SC-011'],'authority':'Local domain retains approval, recovery and final replacement; helper has no service credentials or catalog-wide access'})
 add('boundaries',{'id':'POST-B01','name':'Desktop media adapter to restricted helper process','control_ids':['C-SC-002','C-SC-003','C-SC-011'],'control_evidence_status':'ACTIVE adopted limits and isolation, not verified','threat_ids':['T-003','T-005','T-021']})
 add('flows',{'id':'POST-F01','name':'Bounded media adapter to restricted helper: selected input/staged file and operation data, then validated result','source_id':'S07-A03','destination_id':'POST-A01','boundary_ids':['POST-B01'],'threat_ids':['T-003','T-005','T-021']})
 add('flows',{'id':'POST-F02','name':'Local operator provisioning path to service account domain: issue invitations','source_id':'S00-U4','destination_id':'S07-A05','threat_ids':['T-001','T-009','T-017'],'protocol':'Local command; concrete invocation format not specified'})
 add('entry_points',{'id':'POST-EP01','name':'Local operator invitation issue command','threat_ids':['T-001','T-009','T-017'],'control_ids':['C-SC-010']})
 add('data',{'id':'POST-D01','name':'Registration invitation token; stored digest and expiry/consumption state','control_ids':['C-SC-010'],'threat_ids':['T-009','T-017'],'sensitivity':'Invitation secret must not be logged or put in URLs'})
 for e in u['system']['entry_points']:
  if e['id'] in ['S00-P3','S07-EP03']:e['current_contract']='Registration requires invitation token, canonical ASCII username and password; invitation/admission validation precedes hashing under SC-010/SC-012.';e['post_analysis_evidence_ids']=[evidence['REQUIREMENTS.md'],evidence['SECURITY.md']]
 for f in u['system']['flows']:
  if f['id'] in ['S00-F4','S05-F1']:
   f['historical_description']=f.get('description',f.get('name'));f['current_output']='Ranked qualifying release identifiers only; no numerical contributor counts, identities, individual libraries, cohort sizes or suppressed releases; internal exact ranking counts retained.';f['post_analysis_evidence_ids']=[evidence['REQUIREMENTS.md'],evidence['ARCHITECTURE.md']]
 u['scope']['deployment_plan']={'location':'Germany','participants':'EEA residents aged 18 or older admitted by operator invitations; no additional identity-document collection','status':'prospective adopted scope; actual host/eligibility and legal review evidence required before collection','evidence_ids':[evidence['ARCHITECTURE.md'],evidence['REQUIREMENTS.md'],evidence['SECURITY.md']]}
 # Baseline gap narratives retained verbatim, with precise current dispositions.
 gapresolve={'S00-G2':['OD-010'],'S00-G3':['OD-012','OD-013','OD-014'],'S01-G4':['OD-011','OD-012'],'S01-G5':['OD-010'],'S02-G2':['OD-010'],'S03-G2':['OD-011','OD-012'],'S04-G2':['OD-016'],'S04-G3':['OD-017'],'S07-G03':['OD-012','OD-013','OD-014'],'S07-G05':['OD-010'],'S08-G03':['OD-010']}
 for g in u['gaps']:
  if g['id'].startswith('DEC-'):continue
  if g['id'] in gapresolve:g['post_analysis_status']='Design choice resolved; implementation and effectiveness remain unverified';g['resolved_by_decision_ids']=['DEC-'+x for x in gapresolve[g['id']]]
  else:g['post_analysis_status']='Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence.'
  if g['id'] in ['S02-G1','S07-G04']:g['current_context']='Germany/EEA scope and intended operation-specific bases adopted in OD-018/OD-019; actual deployment, notice, applicable review and substantiation still required before collection.';g['decision_ids']=['DEC-OD-018','DEC-OD-019']
  if g['id']=='S07-G02':g['current_context']='Account-name policy resolved by OD-015/FR-4.30; concrete API route/schema and cursor implementation evidence still pending.';g['decision_ids']=['DEC-OD-015']
 # Actual actions, including exact adopted rule text, flow through report generation.
 for t in u['threats']:
  t['post_analysis_actions']=[]
  for c in u['controls']:
   if t['id'] in c.get('threat_ids',[]):t['post_analysis_actions'].append({'control_id':c['id'],'status':'ACTIVE adopted treatment; implementation/acceptance evidence pending','decision_ids':c.get('decision_ids',[]),'action':c['name'],'exact_treatment':c['exact_text'],'evidence_ids':c['evidence_ids']})
  for r in u['requirements']:
   if t['id'] in r.get('threat_ids',[]):t['post_analysis_actions'].append({'requirement_id':r['id'],'acceptance_ids':[a['id'] for a in r['acceptance_criteria']],'status':'adopted behavior; future acceptance verification required','action':r['exact_text'],'evidence_ids':r['evidence_ids']})
  if t['id'] in ['T-002','T-006','T-019','T-022','T-023']:t['post_analysis_actions'].append({'status':'implementation evidence task','action':'Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.','evidence_ids':[evidence['ARCHITECTURE.md']]})
  if t['id'] in ['T-001','T-004','T-009','T-010','T-011','T-012','T-020','T-022','T-023','T-025']:t['post_analysis_actions'].append({'status':'adopted presentation; native verification pending','action':'Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.','evidence_ids':[evidence['DESIGN.md']]})
  if t['id'] in ['T-003','T-005','T-021']:t['post_analysis_actions'].append({'status':'adopted isolation; enforcement evidence pending','action':'Use the restricted media helper and SC-011 process/memory budgets; keep final replacement authority in the local domain.','asset_ids':['POST-A01'],'flow_ids':['POST-F01'],'evidence_ids':[evidence['ARCHITECTURE.md']]})
  if t['id'] in ['T-004','T-008','T-010']:
   t['current_scenario_disposition']='Baseline exact-count exposure is historical and superseded by FR-3.20–FR-3.23. Original scenario preserved for audit; current identifier-only output, thresholds and access limits do not prove absence of inference.'
   t['residual_uncertainty']='Prior knowledge, colluding invited accounts and differential outputs over time remain inference concerns. No anonymity or complete inference resistance claimed. SC-009 adversarial verification and FR-4.10 release gate remain outstanding; risk remains unrated.'
  if not t['post_analysis_actions']:t['post_analysis_actions'].append({'status':'implementation evidence pending','action':'Implement and verify existing adopted controls; no further unanswered policy choice is identified.'})
 u['scope']['post_analysis_status']='All ten security decisions and five product decisions resolved under maintainer authorization; all fifteen controls adopted ACTIVE, none implemented/verified. No decision deferred. Implementation, workload, privacy review, notice and release evidence remain pending.'
 tech={'S03-A5':'Qt 6.8 Widgets, C++17','S07-A12':'Node.js 24 LTS, Fastify 5, JavaScript ES2022','S00-A2':'SQLite 3.x local catalog','S00-A3':'SQLite 3.x service store','S07-A03':'TagLib 2.x adapter with restricted media helper; filesystem and SQLite adapters'}
 for a in u['system']['assets']:
  if a['id'] in tech:a['technology']=tech[a['id']];a.setdefault('evidence_ids',[]).append(evidence['ARCHITECTURE.md'])
 u['coverage'].append({'id':'POST-COV01','selected_flow_id':'S00-F2','selection_basis':'PASTA T-007 and FMEA T-019/T-020 assess cross-store integrity; explanatory sequence emphasis, not risk rank.','threat_ids':['T-007','T-019','T-020'],'evidence_ids':['S01-E1','S01-E2','S04-E1','S04-E2',evidence['SECURITY.md']]})
 u['coverage'].append({'id':'POST-COV02','description':'Resolved policy and post-analysis architecture coverage: all adopted new FR texts, fifteen exact controls, ten OD and five RQ resolutions; helper, invitation, identifier-only output and prospective deployment added. No runtime evidence inferred.','element_ids':['POST-A01','POST-B01','POST-F01','POST-F02','POST-EP01','POST-D01'],'evidence_ids':list(evidence.values())})
