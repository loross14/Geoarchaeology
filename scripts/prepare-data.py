"""Build bundled atlas evidence and SVG paths from reviewed source snapshots; stdlib only."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/'data/source-snapshots';out=ROOT/'public/data'
def read(p):return json.loads(p.read_text())
def write(p,data):p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
def project(lon,lat):
 x=6378137*lon*math.pi/180;y=6378137*math.log(math.tan(math.pi/4+lat*math.pi/360))
 return ((x+10500000)/1000,(6200000-y)/1000)
geo=read(out/'counties.geojson');counties=[]
for f in geo['features']:
 p=f['properties']; polys=f['geometry']['coordinates'] if f['geometry']['type']=='MultiPolygon' else [f['geometry']['coordinates']]
 paths=[];pts=[]
 for poly in polys:
  for ring in poly:
   points=[project(*c[:2]) for c in ring];pts.extend(points)
   paths.append('M'+'L'.join(f'{x:.2f},{y:.2f}' for x,y in points)+'Z')
 counties.append({'id':p['id'],'name':p['name'],'state':p['state'],'path':''.join(paths),'x':sum(p[0] for p in pts)/len(pts),'y':sum(p[1] for p in pts)/len(pts)})
counties.sort(key=lambda c:(c['name'],c['state']))
write(out/'map.json',{'projection':'EPSG:3857;1000m per SVG unit','extent':[-10500000,4400000,-8500000,6200000],'counties':counties})
cores=read(raw/'cores.json')
for c in cores:
 c['state']='MI' if c['countyId'].startswith('26') else 'OH'
 if c['id']=='C03051':c['location_status']='provisional'
 # Original inconsistent catalogue fields stay in the inherited snapshot; normalized warnings retain their values.
sources=read(raw/'geology-sources.json')+read(raw/'archaeology-sources.json')
for s in sources:
 if not s.get('notes'):s['notes']=s.get('provenance_notes','')
sources.append({'id':'esri-relief','title':'World Shaded Relief','publisher':'Esri / USGS / SRTM / GTOPO30','url':'https://services.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer','accessed':'2026-09-06','notes':'Modern georeferenced relief at regional display resolution. This is not LiDAR or historical terrain. Export extent and attribution retained in terrain.json.'})
leads=[{'id':'guernsey-paleosol','countyId':'39059','coreId':'C03082','title':'A possible buried soil','observation':'The original geologist describes a possible paleosol around 13–16+ ft below the core surface. The logged sequence ends at 24.5 ft. This tentative interpretation has no established age in the imported record.','alternative':'The features may reflect sediment structure or alteration without an intact former land surface. Human association is a separate, untested question.','nextCheck':'Inspect the original log and retained samples for an in-place soil horizon, then locate the paleomagnetic results and assess suitable independent dating.','blockers':['Horizon integrity','Numerical age','Archaeological investigation footprint and depth','Prior reuse audit'],'sourceIds':['geo-C03082']},{'id':'sandusky-lamination','countyId':'39143','coreId':'C03051','title':'Laminated sediment beneath diamict','observation':'The core describes laminated silt at 47.3–51 ft, with disturbance and specimen-removal issues elsewhere. The catalogue/log location association is disputed.','alternative':'Observed beds may be disturbed or reworked; preserved lamination alone does not establish an undisturbed occupation surface.','nextCheck':'Resolve the catalogue/log location association first. Then inspect sediment structures and retained samples before considering chronology or any archaeological comparison.','blockers':['Location association','Integrity','Chronology','Investigation coverage'],'sourceIds':['geo-C03051']},{'id':'muskegon-succession','countyId':'26121','coreId':'MUS-24-01','title':'What survives below diamicton?','observation':'The geological record contains sorted and fine-grained sediment beneath an upper diamicton package. Recovery values are inconsistent in some intervals.','alternative':'The sequence may contain redeposited or disturbed material; lithology does not establish an intact ancient land surface or its age.','nextCheck':'Identify recovered intervals with interpretable structures, reconcile the recovery records, and check available sample dating.','blockers':['Recovery accounting','Sedimentary integrity','Independent dating'],'sourceIds':['geo-MUS-24-01']}]
for lead in leads:lead['status']='awaiting evidence'
data={'version':'0.1','generated':'2026-09-06','cores':cores,'sites':read(raw/'sites.json'),'sources':sources,'landscape':read(raw/'landscape.json'),'leads':leads,'researchCandidates':read(raw/'geology-candidates.json'),'limitations':['Seven inherited geological cores are a convenience sample.','No admitted geological age model; dated landscape evidence is empty.','Site reference locations are approximate public visitor points; Norton is county-only.','Archaeological excavation depth and spatial footprint not established.','Prior archaeological reuse of geological cores unaudited.','No archaeological floor, depth-gap, absence or discovery claim.']}
write(out/'evidence.json',data)
(ROOT/'public/MVP-SPEC.md').write_text((ROOT/'docs/MVP-SPEC.md').read_text())
log='# Landscape Atlas — research and acquisition log\n\n'+(ROOT/'docs/GEOLOGY-RESEARCH.md').read_text()+'\n\n'+(ROOT/'docs/ARCHAEOLOGY-RESEARCH.md').read_text()
(ROOT/'docs/RESEARCH-LOG.md').write_text(log);(ROOT/'public/RESEARCH-LOG.md').write_text(log)
print(json.dumps({'counties':len(counties),'cores':len(cores),'intervals':sum(len(c['intervals']) for c in cores),'sites':len(data['sites']),'mappedSites':sum(s.get('latitude') is not None for s in data['sites']),'datedLandscapeEvidence':len(data['landscape']),'sources':len(sources)}))
