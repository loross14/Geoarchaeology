export type Period = {oldestBP:number|null;youngestBP:number|null;original:string;method?:string;sourceId?:string;scope?:string};
export type Source = {id:string;title:string;publisher?:string;url:string;accessed?:string;notes?:string;locator?:string};
export type Site = {id:string;name:string;countyId:string;county:string;state:string;longitude:number|null;latitude:number|null;locationBasis:string;description:string;periods:Period[];sourceIds:string[];investigationStatus:string};
export type Core = {id:string;countyId:string;county:string;state:string;source_url:string;original_purpose:string;depth_ft:number;age_status:string;archaeological_reuse_status:string;quality_flags:string[];intervals:Record<string,unknown>[];short_reading:string;location_status:string};
export type Landscape = {id:string;countyId:string;phenomenon:string;oldestBP:number|null;youngestBP:number|null;spatialSupport:'local'|'regional';status:string;sourceIds:string[];description?:string};
export type Lead = {id:string;countyId:string;title:string;observation:string;alternative:string;nextCheck:string;blockers:string[];sourceIds:string[];coreId?:string};
export type Evidence = {version:string;generated:string;cores:Core[];sites:Site[];sources:Source[];landscape:Landscape[];leads:Lead[];limitations:string[];researchCandidates:{id:string;blocker:string;sourceIds:string[]}[]};
export type County = {id:string;name:string;state:string;path:string;x:number;y:number};
export function validAge(p:{oldestBP:number|null;youngestBP:number|null}) {return typeof p.oldestBP==='number' && Number.isFinite(p.oldestBP) && typeof p.youngestBP==='number' && Number.isFinite(p.youngestBP) && p.oldestBP>=p.youngestBP;}
export function overlaps(p:{oldestBP:number|null;youngestBP:number|null},youngest:number,oldest:number) {return validAge(p) && p.youngestBP!<=oldest && p.oldestBP!>=youngest;}
export function siteStatus(site:Site,youngest:number,oldest:number):'overlap'|'outside'|'undated' {if(site.periods.some(p=>overlaps(p,youngest,oldest)))return 'overlap';if(!site.periods.length || site.periods.some(p=>!validAge(p)))return 'undated';return 'outside';}
export function provisional(c:Core) {return c.location_status==='provisional' || c.id==='C03051';}
export function countyClass(id:string,mode:string,data:Evidence,youngest:number,oldest:number) {
 if(mode==='coverage') {const cs=data.cores.filter(c=>c.countyId===id);if(cs.some(c=>!provisional(c)))return 'available';if(cs.length)return 'provisional';return 'none';}
 const e=data.landscape.filter(p=>p.countyId===id && p.status!=='unresolved' && overlaps(p,youngest,oldest));
 if(e.some(p=>p.status==='conflicting'))return 'conflicting';
 if(e.some(p=>p.spatialSupport==='regional'))return 'regional';
 if(e.length)return 'local';return 'unknown';
}
export function calendarBP(year:number,era:'BCE'|'CE') {if(!Number.isInteger(year)||year<1)throw new Error('Historical calendar requires a positive year and an era');return era==='BCE'?1949+year:1950-year;}
export function formatBP(n:number) {return n.toLocaleString('en-US');}
export function historicalYear(bp:number) {return bp>=1950?`${formatBP(bp-1949)} BCE`:`${formatBP(1950-bp)} CE`;}
export const MAP_EXTENT={xmin:-10500000,ymin:4400000,xmax:-8500000,ymax:6200000};
export function project(lon:number,lat:number):[number,number] {const x=6378137*lon*Math.PI/180,y=6378137*Math.log(Math.tan(Math.PI/4+lat*Math.PI/360));return [(x-MAP_EXTENT.xmin)/1000,(MAP_EXTENT.ymax-y)/1000];}
