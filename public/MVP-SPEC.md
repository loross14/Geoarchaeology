# Landscape Atlas — MVP specification

Version 0.1 · 6 September 2026 · Michigan and Ohio

## 1. Mission and release contract

Build a research instrument for comparing archaeological observations with independently acquired geological and engineering evidence through time. The useful output is a traceable question about preservation, burial, erosion, dating or investigation coverage, with the evidence needed to pursue it. The product must not turn missing observations into historical absence or turn a borehole bottom, bedrock contact, glacial limit or oldest known site into a universal archaeological floor.

The first release is a private, working browser application plus this specification, versioned datasets, source register, transformation code and verification report. It covers Michigan and Ohio at county level. Its visible map markers are archaeological sites. Geological cores feed evidence records and time-dependent interpretations; they are not the default marker layer. County boundaries organize research, rather than representing ancient political units or uniform geological conditions.

The user audits the working site, supplies one further turn of feedback, and the team implements it. Only then, when the user supplies a GitHub repository, push the agreed source and data there. Private review hosting is authorized now; GitHub publication is deferred. No new image mockups are part of this phase.

## 2. Questions the product must answer

1. At this place and selected interval, which archaeological observations are documented?
2. Which independently collected geological observations could inform preservation or landscape history here?
3. Is there sufficient dating and spatial support to connect those observations to the selected interval?
4. What is actually known about archaeological investigation depth, extent and methods?
5. What specific missing measurement, report or source check would advance the comparison?

A research lead is not a discovery, a demonstration of archaeological neglect, or a probability of finding artifacts. The application must say when it cannot yet answer a question.

## 3. Research protocol

### Geological acquisition

Fix the geographic search area before examining archaeological distributions. Search geological surveys, groundwater studies, transportation/geotechnical investigations, lake sediment archives and university geology repositories. Include physical cores as the primary specimen class; distinguish cuttings, geophysical logs and driller descriptions. Record search query, archive, retrieval date, selection rule, results inspected and access failures. Do not select geological records because they overlap known archaeological sites. The inherited seven-core set is a convenience pilot, not a representative sample.

Extract source descriptions before interpretations. Preserve original units, depth reference, interval boundaries, recovery, removed specimens, tentative language, row/page locators and contradictory catalogue fields. Never interpret collection date as sediment age. Separate material, structure/integrity, age and human activity as independent questions.

### Archaeological acquisition

Acquire an independent public reference set from primary institutional sources such as park services, state museums, universities and published excavation reports. Start with publicly interpreted sites whose location and chronological scope can be cited. Label this set as curated and incomplete; its counts are not statewide activity or artifact-density estimates. Visitor locations may be used only when explicitly labelled as approximate public reference locations. Do not infer precise excavation coordinates from a visitor address. Do not ingest restricted site inventories.

### Chronology and spatial support

Store original date wording, dating method and time basis. Normalize supported calendar ranges to calendar years before 1950 (cal BP). A calendar AD/CE year becomes 1950 minus that year; a positive BC/BCE year becomes 1949 plus that year, because the historical calendar has no year zero. Do not treat uncalibrated radiocarbon BP as calendar BP or automatically calibrate it. Preserve uncertainty and broad cultural attribution. The application's time window reports overlap, not continuous occupation or exact event timing.

Numerical age-depth interpolation requires dated horizons, stated calibration/model method and uncertainty. The MVP does not interpolate between undated lithological boundaries, convert depth to age, or animate ice margins from undated maximum-extent lines. A dated core interval indicates evidence at that core, not automatically the whole county. No unmeasured radius of representativeness is assumed. Excavation depths remain footprint-specific: do not compute a county maximum as its searched depth. A depth comparison requires compatible spatial support, datum, methods and stratigraphy.

### Testable leads

Each lead contains observation, alternative explanation/null, discriminating check, blocking information, provenance and status. Example: C03082 describes a possible paleosol. Working null: observed features need not represent an intact former land surface. Check original specimen/log, pedogenic structure, stratigraphic integrity and suitable dates. Human occupation is a separate hypothesis requiring archaeological evidence. A regional statistical null could compare preservation frequencies across glacial-history categories after controlling for setting and sampling effort; the current pilot cannot test it.

Prior archaeological reuse has independent states: not audited, relevant reuse found, no reuse found in a documented bounded search. None means “never examined.” Deep archaeological work remains comparison evidence and a control; it removes a claimed depth gap where appropriate rather than being discarded from the dataset.

## 4. Dataset inventory and delivery gates

| Dataset | MVP requirement | Present baseline / handling |
|---|---|---|
| Counties | Real polygons, stable five-character county FIPS, names, state, geometry source and CRS | Acquire all MI/OH counties; validate unique IDs and joins |
| Terrain | Georeferenced present-day relief, correctly projected and attributed | Existing Esri shaded relief can be reused; always label as modern context |
| Geological cores | Seven inherited physical-core records with source links, intervals and flags | MUS-24-01, ALL-22-01, KAL-03-02, CA-15-01, C03046, C03051, C03082 |
| Geological ages | Independently sourced dates with methods, intervals and explicit spatial support | Inherited seven cores have no established age models; bounded additional geological search permitted |
| Archaeological sites | Sourced public reference sites in both states, temporal ranges and location basis | Acquire now; never fabricate sites or occupation dates |
| Archaeological investigations | Method, sampled footprint, maximum tested depth, depth datum, date range and source | Unavailable by default; null values remain unknown, not zero |
| Geological interpretations | Source-backed conditions/processes with age range and spatial support | Empty until records pass the age and location gates |
| Research leads | Source-backed observations, null, next check, blockers | Include C03082 as an undated lead, not a dated landscape or archaeological finding |
| Sources and retrieval log | Source URL/title, institution, locator, accessed date, use, transformation and limitations | Include inherited provenance and new acquisition results |

Before release, report actual record counts and excluded records. A complete temporal landscape reconstruction is data-gated. If dated geological records cannot be verified, the released application still provides the archaeological time filter and county evidence workflow, while historical landscape state remains unknown. That limitation is prominent beside the time control and in the release report; it must not be called a completed paleolandscape reconstruction.

## 5. Canonical data contract

Use versioned UTF-8 JSON/GeoJSON and a deterministic build-time normalization script. Original source snapshots remain distinct from normalized records. IDs are stable strings. Missing values are null or explicit status enums; zero is a measured value. Store depths in original units and normalized metres where useful. Never align depths from separate holes without a common elevation datum.

| Entity | Required fields and relationships |
|---|---|
| County | id/FIPS, stateFIPS, name, state, geometry; modern boundary source |
| Source | id, title, publisher, URL, locator if needed, accessed, provenance notes |
| Core | id, countyId, original purpose, specimen type, location basis/status, total logged depth, sources, age status, reuse status, quality flags, intervals |
| Interval | coreId, top/bottom depth, original description, normalized material, recovery status, source locator; optional age and integrity assessment |
| Age | oldest/youngest cal BP when justified, original expression and basis, dating method, uncertainty, source; unresolved when conversion is unsupported |
| Site | id, name, countyId, approximate public location or null for county-only records, location basis, source IDs, one or more dated ranges, date precision, investigation status |
| Investigation | id, siteId/footprint, methods, depth value/unit/datum, extent, source; unknown fields explicit |
| Landscape evidence | id, countyId, phenomenon, oldest/youngest cal BP, spatial support (local/regional), interpretation status, source IDs, conflicts |
| Lead | id, countyId, core/site links as applicable, observation, alternative explanation, next check, blockers, status, source IDs |

Separate occupancy periods from discovery and excavation dates. Keep source records distinct even when they disagree. Deduplicate only exact duplicate intervals with preserved row IDs. C03051 must not support precise spatial inference while its catalogue/log association is unresolved.

## 6. Time and county semantics

The slider selects a 500-year inspection window, initially 2,000–2,500 cal BP. Its start can range from 0 to 29,500 cal BP. The 30,000-year view limit is a navigation choice, not an earliest-human cutoff. Display the actual interval and time basis, with a note that records outside the viewport range are not excluded from research. A point estimate overlaps when inside the window; a range overlaps when its youngest age is at or below the window's oldest boundary and its oldest age is at or above the youngest boundary. Range overlap means possible temporal relevance at the source's stated resolution.

All georeferenced public site reference markers remain visible by default. County-only records with unverified coordinates remain searchable and available in county evidence, with no fabricated marker. Filled markers overlap the selected interval; hollow markers are dated outside the interval; markers bearing a question mark have unresolved dating. If any dated period overlaps, show overlap; otherwise any unresolved period keeps the site unresolved. Distinct occupation periods are not joined into a continuous span. Selecting a marker opens its source-backed dates and county evidence. Undated records remain available in county evidence regardless of the selected window.

Two explicitly named county views:

1. **Evidence coverage** (default): categorical counts of imported geological records: no imported record / record available / unresolved location association. Colour is inventory coverage, never geological condition, research effort, archaeological absence or temporal reconstruction. It does not change when time changes. Classification precedence is at least one nonprovisional imported record, then provisional records only, then no imported record. Mixed counties retain provisional flags in their details; nonprovisional does not mean independently surveyed.
2. **Dated landscape evidence**: unknown / local evidence / regional evidence / conflicting evidence for the selected time window. Colour indicates the level of support, not a county-wide reconstructed surface. The panel lists specific supported phenomena. An undated or spatially unresolved core cannot change this colour. Conflicting records remain visible rather than averaged. Precedence is explicit relevant conflict, then regional support, then local support, then unknown. Conflict requires contradictory claims about the same phenomenon at a relevant location/time; different phenomena do not automatically conflict. Regional entries require a cited county linkage or support footprint and never imply uniform county coverage.

This separates physical conditions (ice cover/water/exposed terrain), processes (burial/erosion) and record coverage. Those are not a single interchangeable legend. Future phenomenon-specific reconstructions require independent source-backed geometries and appropriate coverage; they do not ship as invented animation.

## 7. User workflow and website

Open directly onto the map with real county boundaries and archaeological reference sites. Keep modern terrain prominent, a compact header, county/site search, a small map-view selector, a legible legend and a slim time slider. No marketing page, generated historical imagery, large summary cards or permanent oversized sidebar.

Select a county by map or accessible search/list. Open a dismissible evidence sheet containing: selected time relevance; documented archaeological sites and dates; geological core summaries with expandable original intervals; what investigation depth is known; research leads and next checks; source links and quality flags. On mobile this becomes a usable bottom/side sheet rather than consuming the initial map. Provide pan, zoom and reset; do not make geographic geometry a decorative picture.

Select a site to inspect its source and chronological attribution. Search must match county and site names in both states. Include an accessible textual county list so keyboard users can reach the same evidence. Escape closes details; focus returns to the trigger. Timeline and controls are labelled and keyboard operable. Main text is readable, controls usable on touch, and neither desktop nor mobile should overflow horizontally.

Provide a compact Sources & method panel, downloadable normalized evidence JSON and downloadable MVP specification. Do not expose credentials or restricted source data. The evidence record includes enough information to follow the observation back to its original source.

Required states: data loading, failed dataset load with retry, county without imported records, missing age, missing excavation depth, disputed location, conflicting source fields, empty time window, and no search matches. Missing geological dating must not disappear into a generic empty state.

## 8. Engineering architecture

Single working route using the provided React/Vinext Sites starter, TypeScript, existing accessible UI primitives and a versioned local JSON/GeoJSON bundle. Prefer a bounded geographic SVG/map implementation for the two-state view when it supports real projection, pan/zoom, selection and overlays without external runtime dependence. Use trusted georeferenced raster relief as optional modern context, never the AI mockup as map geometry. Bundle core application data so a third-party map outage does not erase county/site evidence. No database, accounts beyond private review hosting, scraping on each page load, AI inference service or API secrets are required for the MVP.

Implement chronology and county classification in small pure functions with meaningful tests. Keep source datasets, normalization, derived display data and UI separate. The evidence engine is deterministic; a date change recomputes supported records, not randomly recoloured polygons. Data updates are reviewed snapshots, followed by validation and deployment. Preserve source URLs and redistribution notes; link to original reports when redistribution is unresolved.

Artifacts: docs/MVP-SPEC.md; docs/RELEASE-NOTES.md; docs/RESEARCH-LOG.md; public/data county GeoJSON and normalized evidence JSON; source manifest; ingestion/validation scripts; tests; app source; README with install/build commands and data update procedure. Retain the lockfile. No credentials in source, exports or Git history.

## 9. Team and execution order

Specification first, followed by three bounded team workstreams: geological data research and normalization; archaeological reference data and geography research; independent engineering/method review. The primary engineer owns the Site checkout, integrates returned datasets, implements interactions, validates, and publishes the private review build. Team research outputs are prepared outside the Site checkout to avoid conflicting edits. No team member may turn an unsourced hypothesis into application data.

Sequence: finalize this execution contract; launch team; acquire and validate data while implementing the map/evidence engine; integrate datasets; run data and temporal tests; perform desktop/mobile browser checks when supported; publish privately; hand over the review URL and spec; await the user's audit; implement that feedback; accept the supplied GitHub destination and push only then.

## 10. Acceptance criteria

- All MI/OH county objects use real geometry, unique FIPS, source attribution and correct state membership; unresolved joins fail validation.
- At least one verified public archaeological reference site per state; each displayed location and date range has an explicit source/basis. The delivered count is documented.
- All seven inherited geological records retain original purposes, interval information, absent-age status and relevant quality flags. No default core dots.
- Changing time demonstrably changes eligible archaeological markers; boundary and missing-age cases pass tests. Unknown-age geology never gains a date through display logic.
- County colours and legends exactly implement the selected metric; local evidence is never labelled county-wide certainty. Blank coverage is “no imported records,” not “no archaeology.”
- Core loss, specimen removal, geological erosion and uninvestigated depth stay distinct. No unsupported age/depth comparison or research-opportunity score.
- Selecting Guernsey exposes the possible paleosol, source, unknown age, alternative explanation and concrete next check. No claim that it is human-associated or below the known excavation limit.
- C03051 is visibly flagged and excluded from precise spatial inference. Original logged bottom controls C03082's profile, with the conflicting catalogue values retained.
- Search, county/site selection, zoom/reset, time control, sources, exports, dismissal and mobile layout work. The initial viewport is the research surface.
- Build and meaningful validation pass; private deployment reaches terminal success. Browser QA limitations, if any, are stated.
- Release notes distinguish implemented software, verified data coverage and unresolved research. GitHub remains untouched until feedback and repository handoff.

## 11. Expansion boundaries

Do not add global coverage, predictive discovery rankings, automated claims of novelty, publication generation, crowd submissions, fieldwork instructions or a reusable skill in this MVP. After the county workflow and protocol are reviewed, expand geological sampling geographically, seek independently dated horizons, audit archaeological investigation records and document bounded reuse searches. Statistical comparison needs an explicit sampling design and effort denominators before inference. The eventual world map uses the same evidence contracts rather than inheriting a universal archaeological floor.

## 12. Release implementation record

The initial execution produced 171 county objects (83 Michigan, 88 Ohio), seven inherited geological cores with 226 logged intervals, eight public archaeological records (seven mapped, Norton county-only), 29 source-register entries and three source-backed geological research threads. Six archaeological records have normalized calendar ranges; two remain undated. Three additional geological studies remain candidates with documented blockers. No geological chronology was admitted and no investigation-depth comparison is available.

The mobile legend is collapsed initially and expands on request. County evidence is an on-demand nonmodal sheet, allowing the time control to remain usable on desktop. Archaeological dates retain the scope of the source statement (construction, broad cultural attribution, or historical operation), rather than implying continuous residence. Modern relief is georeferenced in Web Mercator and includes a broader context image for pan/zoom.

The private review build is complete as an evidence-browser MVP. The geological reconstruction objective remains data-blocked, and is disclosed directly beside the timeline. Feedback implementation and the subsequent GitHub handoff are pending the user's next turn.

## 13. Data stewardship and maintenance

Keep acquisition snapshots immutable; correct normalized records through documented transformations and a new version. Record source IDs, retrieval dates and exclusions. Do not label the source bundle an exhaustive site inventory or statewide sampling frame. Refresh data through a reviewed offline import, never through silent runtime scraping. New county or core records must pass ID, geometry, source and chronology checks before publication.

Census boundary data and Esri relief keep their respective attribution and use conditions. Primary geological and archaeological reports remain linked rather than being relicensed by the application. The original application code has no new open-source license assigned in this release; select that with the user's GitHub handoff if required. Private review access remains owner-only; no public audience change is part of this task.

Rollback means redeploying a previously saved application version with its matching dataset. Forward updates retain source IDs and record the reason for changed interpretations. No automated updating, paid data subscription or ongoing compute service is required for this MVP.
