"""Reproduce stage 11 from the complete, most downstream stage-10 artifact."""
from pathlib import Path
import json
from collections import Counter
root=Path(__file__).resolve().parent.parent
source=(root/'threat-model/stages/10-visual.md').read_text()
raw=source.split('```json\n',1)[1].split('\n```',1)[0]
m=json.loads(raw)
T=m['threats']; C={c['id']:c for c in m['controls']}; M={x['id']:x for x in m['methods']}; V={x['id']:x for x in m['visualizations']}
entities={x['id']:x for group in m['system'].values() for x in group}
def text(v):
 if isinstance(v,list):return '; '.join(map(text,v)) or 'None recorded'
 if isinstance(v,dict):return '; '.join(f'{k}: {text(x)}' for k,x in v.items())
 return str(v)
def cell(v):return text(v).replace('|','\\|').replace('\n',' ')
def label(i):return entities.get(i,{}).get('name',entities.get(i,{}).get('description',i))
def table(headers,rows):return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+'\n'.join('| '+' | '.join(cell(v) for v in row)+' |' for row in rows)+'\n'
def slim(x):return {k:v for k,v in x.items() if k not in ['source_records','source_stages','identity_basis']}
def figure(n):
 f=V[f'F10-{n:02}'];d=V[f['source_diagram_id']]
 preview=d['specification'].get('text_preview','')
 if f.get('steps'):preview=text(f['steps'])
 return f"#### Figure {n}: {f['title']}\n\n{f['purpose']} Source: {f['id']} / {d['id']}.\n\n**Alt text:** {f['alt_text']}\n\n```text\n"+preview.replace('; ','\n')+'\n```\n\nFigure brief only; no rendered image or export is attached. Full layout, legend, reading order and omissions are preserved in Appendix A `visualizations` and indexed in Appendix B.\n'
counts=Counter(t['source_stage'] for t in T)
parts=[]
def add(s):parts.append(s.strip()+'\n')
add('# THREAT_MODEL_REPORT\n\n**System:** Tag Zeppelin\n**Date:** 2026-10-20\n**Classification:** Not supplied\n**Version:** 1.0')
add('## Table of Contents\n\n'+ '\n'.join(f'- [{n}. {title}](#{n}-{title.lower().replace(" ","-")})' for n,title in enumerate(['Executive Summary','Scope and Methodology','System Architecture','Threat Inventory','Risk Matrix','Control Gap Analysis','Action Register','Requirement Traceability','Appendices'],1)))
add('''## 1. Executive Summary

Overall risk is **Undetermined**: no approved likelihood/impact method, ratings or runtime evidence was supplied. The model contains **25 unrated design scenarios**, including overlapping views of the same adverse events. This is not a count of demonstrated vulnerabilities. STRIDE contributed 6, PASTA 3, LINDDUN 3, attack trees 6, and FMEA 7. AI/ML review, repository reconnaissance and document absorption contributed no separate threats.

The modeled consequences include unintended music-file changes, disclosure of shared memberships, unauthorized account operations, and service interruption. The evidence does not rank these consequences. Existing controls are adopted plans; none has been shown effective in an implementation. The repository has no application implementation or acceptance-test results.

Supported hardening adds privacy-qualified recommendations, invitation-only enrollment, bounded resource work, consistent account names, safe restoration, explicit backup-free service recovery, and a prospective Germany-hosted pilot for EEA adults. Eighteen exact threat-driven or revised product requirements and their future acceptance checks are traceable in section 8. All fifteen secure-coding rules are complete ACTIVE adopted specifications, not implemented protections. Ten security decisions and five product items are resolved under the user’s best-judgment authorization; none is deferred. Section 7 records the adopted resolutions rather than an interview queue. Implementation, workload, adversarial privacy and legal/operational release evidence remain pending.

All stages 00–11 ran. AI/ML analysis found the specified recommendations deterministic, so model-specific methods are not applicable. Seven figure briefs and five diagram specifications are preserved; no image rendering or export is claimed. Repeated methods examined the same documents and do not independently verify implementation behavior.''')
add('## 2. Scope and Methodology\n\n### 2.1 System Description\n\nTag Zeppelin is a native desktop tool for reviewing and approving local music metadata changes, retaining recovery copies, discovering releases through MusicBrainz, and obtaining recommendations from explicitly submitted release memberships in a closed pilot. Current users, participating users, Admins, operators and the maintainer are modeled actors (S00-E1–S00-E4, S07-E01–S07-E04).\n\n### 2.2 Scope\n\nIncluded: native presentation, local domain/media/catalog/recovery, the constrained media helper process, discovery and sharing adapters, service API/account/sharing/recommendation domains, service database, invitation issuance and their documented boundaries. Excluded by the supplied product scope: renaming, moving, transcoding, automatic cover retrieval, playback, unspecified viewer features, prices/payments/affiliate revenue, web/embedded-browser application UI, and mobile UI. External services are modeled only at documented interfaces, not internally.\n\n### 2.3 Methodology')
add(table(['Method / ID','Edition or basis','Coverage limitation'],[(x['name']+' / '+x['id'],x.get('edition','Project pipeline method; edition not supplied'),x.get('verification',x.get('rating_method','Specification analysis only; no runtime effectiveness evidence'))) for x in m['methods']]))
add('STRIDE checks documented security categories; PASTA follows business/system/risk passes; LINDDUN checks privacy interests; attack trees decompose supported adverse goals; FMEA checks documented failure states; AI/ML checks lifecycle applicability. Repository analysis verifies what files exist; document analysis extracts adopted decisions and gaps. Stages 08–10 reconcile identities and preserve diagrams/briefs; stage 11 reports the most downstream model unchanged. These purposes are the upstream method contracts, not additional findings.\n\n### 2.4 Automation Coverage\n\nThe consolidator evidence coverage matrix follows. Each stage read all four supplied specifications; stage 06 additionally inspected the complete tracked baseline.')
add(table(['Stage','Method IDs','Artifact','Threat records','Evidence limit'],[(c['stage'],c['methods'],c['artifact'],c['threat_count'],c['evidence_limit']) for c in m['coverage'] if c['id'].startswith('S08-COV')]))
add('### 2.5 Data Sources')
add(table(['Evidence ID','Source / locator','Revision / status'],[(e['id'],e.get('file',e.get('source','Not supplied'))+' — '+e.get('locator',e.get('claim','')),e.get('revision',e.get('sha256','Not supplied'))+'; '+e.get('status','See source claim')) for e in m['evidence']]))
add('### 2.6 Limitations\n\nBaseline: '+m['scope']['baseline']+'. Document controls are not implementation evidence. No source code, running application, operational history, exploit demonstration, risk method, control-effectiveness result, legal determination, or rendered-figure validation is established. Threats remain conditional; missing evidence is not proof of vulnerability. Baseline scenarios remain historical audit evidence; each current_scenario_disposition and post-analysis action records the adopted treatment. Geography and participant eligibility are prospective policies, not assertions about an existing deployment. ATLAS latest-release status and the exact OWASP ML draft revision were not fully verified. The consolidated composite flow S05-F1 comes from one upstream record, overlaps other flows, and does not establish a hidden implementation path. Component-level completeness awaits implementation evidence (S08-G01–S08-G03). Historical baseline gaps remain preserved even where post-analysis specification text addresses their wording; no missing runtime evidence is marked resolved.')
add('## 3. System Architecture\n\n### 3.1 System Context\n\nFigure 1 shows the documented actors and external systems. No direct server access to local music files is modeled.')
add(figure(1));add('### 3.2 Component Architecture\n\nFigure 2 separates logical components without implying extra deployments. Adopted technology is Qt 6.8 Widgets/C++17, TagLib 2.x and SQLite 3.x locally; Node.js 24 LTS/Fastify 5 and local SQLite on one Ubuntu 24.04 LTS service host. These are selections, not installed-version evidence (S06-E03, S07-E02).');add(figure(2))
add('### 3.3 Data Flow');add(figure(3));add(figure(4));add(figure(6))
add('### 3.4 Trust Boundaries\n\nThe following boundary inventory is the trust map accompanying Figures 2, 3 and 5. Zones and boundaries remain distinct from ordinary component grouping.')
add(table(['Boundary','Name','Planned controls','Status'],[(b['id'],b['name'],b.get('control_ids',[]),b.get('control_evidence_status',b.get('status'))) for b in m['system']['boundaries']]))
add(table(['Zone','Recorded description'],[(z['id'],label(z['id'])) for z in m['system']['zones']]))
add(figure(5));add('### 3.5 Attack Surface');add(figure(7))
add(table(['Entry point','Recorded contract'],[(x['id'],text(slim(x))) for x in m['system']['entry_points']]))
add('## 4. Threat Inventory\n\nThreats retain method order and stable consolidator IDs. Categories are kept within their own methods. Attack scenarios below are conceptual prerequisite/failure paths, not exploit procedures. All ratings are Unrated and residual risks Not assessed.')
for t in T:
 tree=next((a for a in m['attack_trees'] if a['id']==t.get('tree_id')),None)
 affected=t.get('affected_ids',[])
 if tree:affected=list(dict.fromkeys(i for n in tree['nodes'] for i in n.get('affected_ids',[])))
 boundaries=[i for i in affected if i in {b['id'] for b in m['system']['boundaries']}]
 description=t.get('scenario',t.get('cause',t['title']))
 scenario=description
 if tree:
  nodes={n['id']:n for n in tree['nodes']};r=nodes[tree['root_id']]
  scenario=r['operator']+' prerequisites/alternatives: '+ '; '.join(nodes[c]['name'] for c in r['children'])+'. Conditional path; feasibility not demonstrated.'
 elif t.get('local_effect'):scenario=t['cause']+' → '+t['local_effect']+' → '+t['downstream_effect']+'. Prospective failure mode, not an incident.'
 controls='\n'.join('- '+i+': '+C[i]['status']+'; evidence '+text(C[i].get('evidence_ids',[]))+'.' for i in t['control_ids'])
 actions='\n'.join('- '+a['action']+(' Treatment: '+a['exact_treatment'] if a.get('exact_treatment') else '')+' Status: '+a['status']+'. Dependencies: '+text(a.get('decision_ids',[]))+'.' for a in t.get('post_analysis_actions',[]))
 add(f'''<a id="{t['id'].lower()}"></a>
### {t['id']}: {t['title']}

**Rating:** Unrated

**Rating method:** Not supplied

**Category:** {M[t['method_id']]['name']} / {t.get('category',t.get('function','attack-tree goal'))}

**Affected Assets:** {text([i+': '+label(i) for i in affected])}

**Trust Boundary:** {text(boundaries) if boundaries else 'Not separately mapped in this threat record; see section 3.4 and associated flow/tree records.'}

#### Description

{description}

**Current disposition:** {t.get('current_scenario_disposition','Baseline scenario remains conditional; see adopted post-analysis actions below.')}

Evidence: {text(t['evidence_ids'])}. Locators: {text(t.get('source_locators',t.get('locator','Not supplied')))}. Status: {t.get('status','prospective failure mode')}. Related scenarios: {text(t.get('related_threat_ids',[]))}.

#### Attack Scenario

{scenario}

#### Business Impact

{t.get('downstream_effect','The adverse consequence described above is supported qualitatively; business magnitude and financial impact are Unknown.')}

#### Existing Controls

{controls}

#### Recommended Mitigations

{t['mitigation']}

{actions}

Owner, priority, effort and target date: Not supplied. Specification clarification is not proof of mitigation effectiveness.

#### Residual Risk

Not assessed. {t.get('residual_uncertainty','No effectiveness or treated-state assessment supplied.')} {text(t.get('assumptions',[]))}
''')
add('## 5. Risk Matrix\n\n### 5.1 Risk Heat Map\n\nNo combined heat map is valid: no common likelihood-impact method or mappings were supplied. All 25 scenarios are unrated. Seven FMEA risk records preserve unranked status; no residual assessment exists.\n\n### 5.2 Risk by Category')
cat=Counter((M[t['method_id']]['name'],t.get('category',t.get('function','attack-tree goal'))) for t in T)
add(table(['Method','Recorded category/function','Unrated records'],[(a,b,c) for (a,b),c in cat.items()]))
add('### 5.3 Risk by Component\n\nCounts below rank only explicit affected-asset references, including root-node mappings for attack trees. They do not rank risk. A scenario can affect several assets; component granularity differs across methods.')
ac=Counter()
for t in T:
 ids=set(t.get('affected_ids',[]));tree=next((x for x in m['attack_trees'] if x['id']==t.get('tree_id')),None)
 if tree:ids.update(i for n in tree['nodes'] for i in n.get('affected_ids',[]))
 for i in ids:
  if i in {a['id'] for a in m['system']['assets']}:ac[i]+=1
add(table(['Affected asset','Count'],[(i+': '+label(i),n) for i,n in sorted(ac.items(),key=lambda x:(-x[1],x[0]))]))
add('### 5.4 Risk Trend\n\nNo prior assessed threat model was supplied. No risk trend is claimed. Baseline findings and post-analysis adopted wording coexist in this model; none is marked runtime-resolved.\n\n## 6. Control Gap Analysis\n\n### 6.1 Controls Inventory')
add(table(['Control','Exact status','Evidence','Dependencies'],[(c['id'],c['status'],c['evidence_ids'],c.get('decision_ids',[])) for c in m['controls']]))
add('### 6.2 Gap Analysis\n\nNo demonstrated implementation control failure exists because no implementation exists. All policy decisions identified by this review are resolved as listed in section 7. Evidence gaps below preserve provenance; they do not automatically become user policy questions.')
add(table(['Gap','Evidence limit / conflict','Evidence'],[(g['id'],g.get('description',g.get('claim',text(g)))+' Current disposition: '+g.get('post_analysis_status','See linked adopted treatment; evidence still pending'),g.get('evidence_ids',[])) for g in m['gaps'] if not g['id'].startswith('DEC-')]))
add('### 6.3 Defense in Depth Review\n\nAccount operations depend on authentication, revocation, HTTP validation and domain authorization (T-001/T-014). Media writes depend on approval binding, recovery, identity checks, atomic replacement and catalog reconciliation (T-002/T-007/T-019). Pagination depends on authenticated requester binding, eligibility rechecks and revision invalidation (T-006/T-015/T-023). These are planned layers, not tested independence. Some threat records map only one control family (for example T-003 to SC-002); that is a documentation mapping, not proof of a runtime single point of failure. Recovery objectives, inference protection and resource budgets are now adopted under SC-009–SC-015. Their effectiveness and release evidence remain unverified.\n\n### 6.4 Evidence Coverage Analysis\n\nThe matrix uses exact element-level records where available. Assessed means the method considered the documented element; Partial includes unresolved subcategories or aggregate-only analysis; Not assessed means no element-level record. Stage 05 is lifecycle-scope Not applicable and stage 06 has no implementation to assess. Broader aggregate coverage is retained in Appendix A.')
rows=[]
for i,e in entities.items():
 vals=[]
 for stage in range(8):
  cv=[x for x in m['coverage'] if x.get('source_stage')==stage and x.get('element_id')==i]
  if cv:
   status='Partial' if any('not assessed' in json.dumps(x).lower() for x in cv) else 'Assessed'
  elif stage==7:status='Assessed' if 7 in e.get('source_stages',[]) or e.get('source_stage')==7 else 'Partial'
  elif stage in [3,4]:status='Partial' if any(t.get('source_stage')==stage and i in t.get('affected_ids',[]) for t in T) else 'Not assessed'
  else:status='Not assessed'
  vals.append(status)
 rows.append([i+': '+label(i)]+vals)
add(table(['Element','00','01','02','03','04','05','06','07'],rows))
add('Strongest specification traceability, not runtime assurance, occurs where exact requirements, controls and cross-file flows align: file integrity, account authorization and sharing freshness. All 25 threat records cite all four specifications for context; those repeated citations are not independent observations, and they do not mean each document independently proves every scenario. S05-F1 and component completeness limitations are explicitly retained in S08-G01/S08-G02. Attack-tree failure branches and FMEA failure occurrences remain conditional assumptions. The conflicts collection is empty: no established material contradiction was found. The historical tension between exact ranking and inference protection (S08-G03) is treated by privacy eligibility before exact ranking of qualifying results, count suppression and bounded access. Inference residuals remain explicitly unassessed; no contradictory implementation is inferred.')
add('## 7. Action Register\n\nActions below come only from threat-linked mitigations. No priority, owner, effort or deadline was supplied; model order is preserved.')
rows=[]
for t in T:
 for a in t.get('post_analysis_actions',[]):rows.append([t['id'],a['action'],'Not supplied','Not supplied','Not supplied','Not supplied',a['status']+'; '+text(a.get('evidence_ids',[]))])
add(table(['Threat','Mitigation','Priority','Owner','Effort','Target date','Evidence/status'],rows))
add('### Adopted Decision Register\n\nThe user authorized resolution using best judgment. All ten decisions below and their five owning product items are RESOLVED; no interview queue or deferred policy item remains. The owning specifications retain authoritative policy. This resolution does not establish implementation or legal/operational evidence.')
order=[10,11,15,16,17,12,13,14,18,19]
for n,num in enumerate(order,1):
 g=next(g for g in m['gaps'] if g['id']==f'DEC-OD-{num:03}')
 add(f"{n}. **{g['specification_id']}** — {g['description']} Product owner items: {text(g['owning_product_items'])}. Security owner: SECURITY.md. Status: **RESOLVED; adopted, verification pending**. Dependent controls: {text(g['dependent_control_ids'])}. Threats: {text(g['threat_ids'])}.")
add('Historical implementation, tests, rating-method, metadata and taxonomy gaps remain evidence limitations. No policy decision is deferred. All fifteen controls are ACTIVE as adopted specifications, with no claim of implemented effectiveness. Current requirements, acceptance criteria, threat actions and downstream artifacts reflect the resolutions; historical scenarios and source fragments remain preserved for audit.\n\n## 8. Requirement Traceability\n\nOnly exact project requirements and applicability supplied by the model are included. Baseline records S07-R01/S07-R02 are aggregate locators, not an invented individual mapping. No compliance conclusion follows.')
add(table(['Requirement / source','Edition / applicability','Threats / controls','Evidence / gaps'],[(r.get('specification_id',r['id'])+' — '+r.get('source',r.get('exact_text','')),r.get('edition','Not supplied')+'; '+r.get('applicability','Not supplied'),text(r.get('threat_ids',[]))+' / '+text(r.get('control_ids',[])),text(r.get('evidence_ids',[]))+'; '+r['status']+'; conflicts: none recorded; implementation verification not assessed') for r in m['requirements']]))
for r in m['requirements']:
 for a in r.get('acceptance_criteria',[]):add(f"- **{a['id']}** ({r['specification_id']}): {a['exact_text']} Status: {a['status']}.")
add('## 9. Appendices\n\n### Appendix A. Full Downstream Model\n\nThe JSON below is copied byte-for-byte from the Model block of `threat-model/stages/10-visual.md`. No fields, threat IDs, conflicts, gaps or visualization records have been edited.\n\n```json\n'+raw+'\n```')
add('### Appendix B. Diagram Specifications and Figure Briefs\n\nAll supplied records are preserved in full in Appendix A under `visualizations`; this index avoids reproducing large machine records twice. No rendered figures were attached. Source architecture diagram S07-V01 is also retained there.')
add(table(['Record','Title/source','Kind'],[(v['id'],v.get('title',v.get('source','Not supplied')),'Figure brief' if v['id'].startswith('F10') else 'Diagram specification/source') for v in m['visualizations']]))
add('### Appendix C. Automation and Evidence Coverage Summary\n\nStages 00–07 completed independently; all eight fragments entered 08; 09 generated five diagram specifications; 10 generated seven figure briefs; 11 consumed 10 as the most downstream model. The entire coverage collection, including category-by-element dispositions, is preserved in Appendix A. Only data/reference validation was performed; no application test or visual rendering check is claimed.\n\nRepository unresolved-item scan disposition: the root task scanned repository Markdown/JSON/Python files case-insensitively, excluded `.git` and intentional REQUIREMENT_TEMPLATE.md placeholders, and checked the logo separately. Baseline specifications had no open-question markers. After the user authorized best-judgment resolution, RQ-001–RQ-005 and OD-010–OD-019 became adopted resolutions; SC-001–SC-015 are ACTIVE. There is no current open-policy or BLOCKED-rule queue. Historical artifacts preserve their former OPEN/BLOCKED wording only as provenance. “Proposed” metadata is a legitimate review state; historical unknown/assumption and implementation/test/risk/taxonomy limitations remain evidence gaps. Required Requirement Inputs, Required Architecture Inputs and Secure-Coding Inputs headings were absent, not blank provisional inputs. No decision is deferred. This scan disposition records task validation and does not change Appendix A.\n\n### Appendix D. Repository Analysis Findings\n\nStage 06 establishes that no implementation exists at the analyzed baseline: seven tracked documentation/static-asset files, no application/build/test harness/CI or deployment configuration (S06-E01/S06-E02). Runtime control and dependency effectiveness are therefore not assessed. Adopted technology versions are intentions (S06-E03); rejected external corpus packs are not project authority (S06-E04). The static logo and intentional requirement template are not application source.\n\n### Appendix E. Document Sources Reviewed\n\nREQUIREMENTS.md, ARCHITECTURE.md, SECURITY.md and DESIGN.md were fully supplied to each analysis. Repository analysis additionally covered AGENTS.md, REQUIREMENT_TEMPLATE.md and logo.svg. Evidence IDs, baseline locators and post-analysis hashes are enumerated in section 2.5 and preserved in Appendix A. Source pipeline README and every numbered agent instruction governed their respective stages.\n\n### Appendix F. Glossary\n\n- **Adopted control:** a required specification plan, not a tested mechanism.\n- **BLOCKED:** historical status for a rule awaiting named decisions; no current rule retains that status.\n- **Evidence gap:** missing support, not proof of a flaw.\n- **Unrated:** no approved rating method or inputs support a score.\n- **Residual risk:** risk after a verified treated state; not assessed here.\n- **AND/OR attack tree:** all prerequisites versus alternative sufficient branches; conditional, not demonstrated exploits.\n- **FMEA:** failure-mode and effects analysis.\n- **WAL:** database write-ahead log.\n- **RQ / OD / SC:** owning product question, decision, and secure-coding rule identifiers.\n- **Figure brief:** renderer-neutral design instructions; no rendered artifact is implied.')
(root/'THREAT_MODEL.md').write_text('\n'.join(parts))
assert (root/'THREAT_MODEL.md').read_text().split('```json\n',1)[1].split('\n```',1)[0]==raw
assert all(f'<a id="{t["id"].lower()}"></a>' in (root/'THREAT_MODEL.md').read_text() for t in T)
print('THREAT_MODEL.md written; full downstream JSON preserved; 25 explicit anchors verified.')
