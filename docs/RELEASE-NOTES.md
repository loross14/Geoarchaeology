# Landscape Atlas — first browser review

6 September2026 · Research MVP0.1

## Delivered

- Full Michigan and Ohio county geometry:171 counties, including the Upper Peninsula.
- Seven geological cores with226 preserved logged intervals and source-quality flags.
- Eight sourced public archaeological records: Sanilac Petroglyphs, Fayette, Norton Mound Group, Mound City, Seip, Hopewell Mound Group, Hopeton and Fort Hill.
- Seven approximate public reference points. Norton remains county-only; no point is fabricated.
- Six records with calendar ranges and two with unresolved chronology. Date scopes remain explicit.
- Three geological research threads with alternative explanations, source links, missing evidence and next checks.
- Twenty-nine source-register entries; three additional geological studies retained as blocked candidates.
- Interactive map pan/zoom/reset, county/site search, temporal range filtering, deterministic county colours, on-demand evidence, source and dataset downloads, and responsive interface.

## Verification

Twelve automated evidence tests pass: historical-calendar conversion, inclusive overlap, unresolved and disjoint periods, site-time changes, inventory stability, undated geology exclusion, classification precedence, unique county/source joins, all seven public points inside their assigned counties, inherited interval/flag preservation, research-lead provenance and map projection alignment.

Browser checks used the actual working application. Desktop checks covered county selection directly from the map and via search, the Guernsey research thread, sourced chronology, keyboard time change (2 to5 overlapping site records), dated-evidence unknown state and the evidence sheet. A390×844 embedded viewport checked the responsive mobile layout and searchable county-only Norton record; this was viewport QA, not testing on a physical phone. The initially expanded mobile legend obscured Ohio and was corrected to collapse by default.

The production application build succeeds. The standalone whole-starter `tsc` command reports missing generated Cloudflare runtime types in untouched starter infrastructure; application code produced no reported TypeScript errors in that check. The framework build is the release gate; this limitation is retained rather than claiming a clean standalone typecheck.

## Research limitations

No geological age model passed admission. The geological timeline layer is explicitly unknown; no ice, flood or burial reconstruction is animated. The timeline changes archaeological date relevance only. The seven-core set is a convenience pilot, not statistically representative statewide coverage. Archaeological records are a curated public reference set, clustered in accessible published sources, not statewide site counts or research-effort measures.

No archaeological investigation depth or footprint comparison is established. Original purposes are geological, but prior archaeological reuse is unaudited. No archaeological floor, new occupation, historical absence or unexplored depth gap is claimed.

C03051 has an unresolved catalogue/log association. C03082 uses24.5ft logged bottom while retaining conflicting catalogue values and its tentative, undated paleosol interpretation. MGS recovery inconsistencies and duplicate-source handling remain documented.

## Next authorized stage

The user visually audits this private working build and supplies one further feedback turn. Implement that feedback, rerun affected checks, and update the review build. Push to GitHub only after the user supplies the destination repository. No GitHub publication has occurred.
