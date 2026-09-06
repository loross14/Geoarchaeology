# Archaeological reference and geography acquisition — 6 September 2026

## Delivered snapshot

- `counties.geojson`: 171 real modern county geometries, 83 Michigan and 88 Ohio. All 15 Upper Peninsula counties included. Unique five-character FIPS identifiers. All geometries valid.
- `sites.json`: 8 curated public archaeological reference records: 3 Michigan and 5 Ohio. Seven have approximate public reference coordinates; Norton has county attribution and null coordinates. Six records have source calendar ranges; Sanilac and Hopeton retain unresolved dating. Five of the dated records are ancient cultural/construction attributions, one is the Fayette historical industrial phase.
- `sources.json`: 18 institutional source records, with URLs, publishers and locators.
- `site-candidates.json`: Norton duplicate retained as acquisition checkpoint only. Do not combine with sites.json or it will double-count Norton.
- `build-sites.py` and `convert-counties.py`: reproducible normalization scripts; requirements for county conversion: pyshp, pyproj, shapely.

This is a small curated reference set, heavily concentrated on interpreted Ohio Hopewell sites. It is not an exhaustive inventory, a density sample, a list of deepest excavations, or a measure of archaeological activity. Its selection did not influence geological acquisition.

## Geography source and transformation

Source: US Census Bureau, 2024 Cartographic Boundary File, counties at 1:500,000:
https://www2.census.gov/geo/tiger/GENZ2024/shp/cb_2024_us_county_500k.zip

Documentation: https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html

Downloaded the national shapefile (11,626,066-byte ZIP), selected STATEFP26 and39, preserved GEOID as string, transformed NAD83 (EPSG4269) to WGS84 (EPSG4326) with pyproj and always_xy=True. Original cartographic simplification retained; no further polygon simplification. Output GeoJSON has longitude/latitude axis order. US federal government public-domain data; attribution to US Census Bureau retained. Original data is intended for small-scale thematic mapping, not parcel boundaries. Modern shoreline/county objects are organizational context, not a reconstructed ancient landscape.

Validated: 171 unique county FIPS; 83MI;88OH;15/15 Upper Peninsula names; all Shapely geometries valid. Seven displayed approximate public site points lie inside their assigned modern county polygon after corrections below. Source joins resolve, all numerical periods have oldestBP>=youngestBP.

## Bounded acquisition method

Search institutional public sources for Michigan and Ohio archaeological reference sites, chronology and public visitor location. Sources inspected: Michigan DNR/History Center, Michigan SHPO/MiPlace, Grand Rapids Public Museum statement in Federal Register, NPS Hopewell Culture pages and GPS directions, Ohio History Connection, Arc of Appalachia, Ancient Ohio Trail university-led partnership. Representative searches: `site.michigan.gov Sanilac Petroglyphs`, `site.michigan.gov Fayette1867`, `site.nps.gov Hopewell Culture`, `site.ohiohistory.org Fort Hill`, `Norton Mound Group MiPlace`, plus source-specific coordinate queries. No restricted archaeological inventory accessed.

Some direct Ohio History Connection HTML downloads returned403; web search/open retrieved the institutional text. Michigan DNR public POI coordinates were extracted from the HTML map configuration, not guessed from town names. NPS directions supplied visitor GPS coordinates. Long-form source text was not bundled for website republication; source URLs and concise factual paraphrases are delivered.

## Location QA and corrections

- Sanilac: DNR's interpretive hiking trail POI43.656454,-83.01777, rounded to0.001°. This is a public trail reference, not the carving or excavation coordinate.
- Fayette: an official marina coordinate was first evaluated but falls outside the land-clipped Census county polygon because it is on water. The displayed reference instead uses the DNR Furnace Hill Lodge public park POI45.719248,-86.662387, rounded to0.001°. This is explicitly a nearby park visitor location, not a precise townsite feature.
- Four Ross County NPS units: official published DMS visitor coordinates converted to decimal degrees and rounded to0.001°. No dig coordinate inferred.
- Fort Hill: the manager's webpage printsN39 6.2′/W83 21.73′. That point failed Highland County containment, and differs from the institutional Ancient Ohio Trail guide point39.122193,-83.396375. The former is retained as a source discrepancy but not mapped. The latter is mapped rounded to0.001°, labelled approximate public visitor reference. The university-led partnership provenance is documented by Ohio History Connection. This is not a site survey or navigation dataset.
- Norton: reliable primary chronology and Kent County attribution, but no primary public marker coordinate verified within bounded search. Contract clarification approved by primary engineer: keep this archaeological record searchable and visible in Kent evidence with null latitude/longitude and omit its map marker. Do not substitute a guessed coordinate or county centroid.

## Chronology and limits

Calendar BCE=>1949+BCE; CE=>1950-CE. These are mechanical conversions of institutional calendar statements, not new laboratory age estimates. Preserve the `scope`, `method`, `original` and `sourceId` fields of each period. Broad cultural attributions are not continuous occupation, exact construction dates or statistical confidence intervals. No uncalibrated radiocarbon BP converted to calendar BP. No calibration undertaken.

Norton has two nested source statements: Michigan SHPO400BC–AD400 and Grand Rapids Museum100BC–AD200. Preserve both, not separate occupations or averaged bounds. Museum statement cites radiocarbon, pottery and lithics but raw determinations and calibration have not been extracted. The source's calendar labels support broad source attribution only.

Mound CityAD1–400 is a construction attribution. Seip and Hopewell Mound GroupAD1–400 use broad regional/cultural attribution. Fort Hill100BC–AD500 likewise uses cultural attribution. Fayette1867–1891 describes industrial operation only. Relative descriptions such as '2000years ago' were not anchored to an arbitrary publication/retrieval year. Sanilac and Hopeton therefore have empty periods in this bounded import.

All maximum excavation depths and investigated footprints remain null. NPS explicitly documents substantial prior archaeological work at several units; these remain comparison evidence, not discarded for contradicting a presumed research gap. Particularly, Hopewell Mound Group has reported below-ground excavation, Seip has buried surviving earthwork foundations, and Hopeton has LiDAR/magnetic/artifact survey. None establishes a geological age-depth comparison with the separate seven-core pilot.

## Deferred records

Story Mound chronology was verified (800BC–AD100), but its source linked only a street-name public map; an independently verified primary visitor point was not acquired. It is not imported. Norton is retained county-only by explicit integration decision. No ranking of research opportunity is generated from this reference subset.
