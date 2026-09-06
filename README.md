# Landscape Atlas

An evidence browser for archaeological date ranges and independently selected geological cores in Michigan and Ohio. The map shows public archaeological reference locations. County colour separates imported core coverage from supported dated landscape evidence.

The initial dataset contains171 counties,7 cores,226 intervals,8 archaeological records (7 mapped),29 source entries and3 research threads. There are **no admitted geological age models**. The timeline filters archaeological date relevance; it does not yet reconstruct geological landscapes. Excavation-depth comparisons and archaeological non-reuse claims are unsupported.

Read [the MVP specification](docs/MVP-SPEC.md), [release notes](docs/RELEASE-NOTES.md) and [research log](docs/RESEARCH-LOG.md).

## Development

Requires Node22.13+ (Node22.18+ recommended for the built-in TypeScript test runner), npm and Python3. The standard Sites/Vinext starter is retained.

```sh
npm ci
python3 scripts/prepare-data.py
node --experimental-strip-types --test tests/evidence.test.mjs
npm run dev
npm run build
```

In ChatGPT Work, use the Sites skill's supervised preview and build lifecycle. Outside Work, the application uses the starter's normal development/build commands. No API keys, database or runtime data provider are needed for the map.

## Data flow

- `data/source-snapshots/`: reviewed normalized inputs plus the original inherited core pilot. Do not overwrite source history silently.
- `public/data/counties.geojson`: Census2024 cartographic county polygons, WGS84. The snapshot is the build input.
- `scripts/prepare-data.py`: deterministic projection, bundle assembly and document-copy step; Python standard library only.
- `public/data/map.json`: derived Web Mercator paths, preserving real county geometry.
- `public/data/evidence.json`: sources, cores, sites, candidate studies and testable research threads.
- `lib/evidence.ts`: chronology, temporal overlap and county classification.
- `app/page.tsx`: map, accessible search, time controls and source-linked evidence panels.
- `tests/evidence.test.mjs`: meaningful chronology, county membership, provenance, core-preservation and classification tests.

A data update must retain original age expressions and date scope. New dated geological records require independently verified chronology, uncertainty, local/regional support and source locators. Uncalibrated radiocarbonBP must not become calendarBP. A local core cannot establish a uniform county-wide surface.

The exported site records include approximate public visitor references only. Norton has no map coordinate and remains accessible through search/Kent County. The reference set is deliberately incomplete, not an archaeological-activity census.

## Review and repository handoff

The working build is published privately for the user's visual audit. The next feedback turn is to be implemented before pushing to a user-supplied GitHub repository. The Sites source remote is operational review hosting, not that future GitHub destination. No GitHub repository has been supplied or pushed.

Sources keep their own attribution and rights. Census boundaries are US federal cartographic data; Esri relief is attributed and not relicensed as original artwork. The new code has no open-source license assigned yet.
