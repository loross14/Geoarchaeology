# Landscape Atlas — independent engineering and method review

Reviewed 6 September 2026. Inputs: `docs/MVP-SPEC.md` v0.1 and inherited `Michigan-Ohio-Core-Atlas.md`. This is a bounded consistency review of the supplied specification and pilot, not new geological research or a source-verification pass.

## Verdict

The specification preserves the mission: archaeological sites are visible references; geological sampling is independently selected; time relevance is evidence-gated; county boundaries organize observations; missing material and missing investigation are separate. The seven-core convenience pilot cannot establish a preserved-depth/excavation-depth gap or reconstruct historical landscape states. The release contract correctly allows an explicitly incomplete temporal layer. Do not describe the initial release as a completed palaeolandscape reconstruction.

The following clarifications are needed before claiming the implementation satisfies its own contract.

## Significant corrections

1. **Make county classification deterministic.** The inventory categories do not define what happens when a county contains both resolved and provisional records. Recommended rule: resolved count > 0 gives `record available`; unresolved associations are separately flagged in the panel; otherwise unresolved count > 0 gives `unresolved location association`; otherwise `no imported record`. Never count the provisional Sandusky association as resolved. The default inventory layer must remain unchanged when time changes.

2. **Define dated evidence support and conflicts separately.** If using a single colour legend, apply explicit precedence: documented relevant conflict > relevant regional evidence > relevant local evidence > unknown. A conflict must identify contradictory claims about the same phenomenon, relevant location and overlapping age interval. Different phenomena, geological layers or dates are not intrinsically conflicting. Preserve the component records in the panel. Regional support describes the cited evidence's scale; it does not automatically establish every location in a county. Require an explicit county linkage basis or intersecting source support geometry. Point-local evidence may colour a county only under the explicit legend `local evidence`, never a blanket surface claim.

3. **Give unresolved site chronology its own visible state.** The spec currently gives both a nonoverlapping dated site and an undated site a hollow marker, distinguishing them only in details. This hides a mission-critical distinction. Use three observable states, such as filled (overlap), hollow (dated outside interval), and hollow with a question mark (unresolved). Multiple disjoint occupation periods must remain separate; do not merge them into one continuous range. If no dated range overlaps but an additional unresolved period exists, the overall temporal state remains unresolved.

4. **Do not aggregate excavation depth into county-wide reach.** The county panel can list specific documented excavation measurements but cannot make their maximum the county's searched depth. Any comparison must have compatible spatial support, surface/elevation reference, method and stratigraphy. A deep borehole and a nearby shallow excavation do not alone establish a preserved, unexamined archaeological horizon. In this pilot the honest state is `comparison unavailable: investigation footprint/depth and horizon age/integrity not established`.

5. **Keep available fields from quietly acquiring stronger meanings.** Display the core's logged bottom, not a catalogue extent when contradicted. Record recovery, retained-specimen removal and natural erosional interpretation independently. Original collection purpose does not prove the record was never archaeologically reused. Dates of drilling, publication, discovery and excavation must never enter occupation or sediment-age filters.

## Acceptance cases

| Area | Input or action | Required result |
|---|---|---|
| Calendar normalization | 1 BCE; 1 CE; 1950 CE | 1950; 1949; 0 calendar BP, respectively |
| Unsupported ages | `10,000 radiocarbon BP` with no calibration; `2,000 years ago` without a reference basis | Original expression retained; normalized calendar range unresolved |
| Invalid range | Oldest = 1900, youngest = 2200 | Validation fails; no silent swapping that obscures source interpretation |
| Window boundaries | Window 2000–2500 BP; point at 2000 or 2500 | Both overlap under the specified inclusive rule |
| Window exclusion | Same window; point at 1999 or 2501 | No overlap |
| Broad dates | Dated range 1500–3000 BP | Overlap reported as possible temporal relevance, not exact occupation at the chosen year |
| Disjoint occupation | Periods 1000–1500 and 3000–3500 BP | No overlap at 2000–2500 BP; no envelope-filling |
| Mixed dating | Nonoverlapping dated period plus unresolved period | Unresolved overall state, with both original periods inspectable |
| Navigation bound | Source outside 0–30,000 BP | Record retained/exported and available in details; explicitly outside navigation window |
| Inventory stability | Change time with unchanged core inventory | Inventory county colours unchanged |
| Mixed inventory | One resolved core and one provisional association | `record available`, with provisional association warning and separate count |
| Missing geological ages | All seven inherited cores | No dated landscape classification derived from lithology, log depth or drilling year |
| Missing dated evidence | Select dated layer in unsupported interval | `Unknown / no supported dated record for this interval`, not a reconstructed surface or archaeological absence |
| Local support | Dated local record only | `Local evidence`; no invented radius or county-wide physical condition |
| Different phenomena | Coeval water evidence and burial evidence | Not automatically classified as contradiction |
| Source contradiction | Explicit conflicting claims at matching place/time | Conflict retained with both sources and the disputed field |
| Core C03082 | Open Guernsey evidence | 24.5-ft logged bottom; conflicting catalogue values retained; tentative paleosol near 13–16+ ft, age and human association unknown |
| Core C03051 | Open Sandusky evidence | Catalogue/log conflict visible; precise spatial comparisons blocked |
| Excavation depth absent | Open a county with sites but no source-backed depth | Unknown, never 0; no calculated geological-versus-archaeological depth gap |
| Deep investigation documented | Add qualifying evidence | Retained as comparison/control; removes an unsupported gap claim rather than being discarded |
| Provenance | Select observation or download normalized data | Source title, URL, locator when applicable, original wording/basis and quality flags survive |

## Function-over-form audit path

A user must be able to complete these three tasks in the actual browser:

1. Choose Guernsey; read the tentative geological observation, its original source, unknown age, working alternative and next discriminating check without encountering a discovery claim.
2. Move the time window; observe an actual dated site change state; distinguish undated sites; switch to dated geological evidence and see the explicit dating gap when applicable.
3. Choose an unsampled county; see `no imported records`, accessible site/evidence details if present, and no inferred historical absence.

The page should keep the map, time window and current legend visible while inspecting evidence. A Sources panel alone is insufficient provenance if the user cannot tell which source supports the specific observation being viewed. The release notes should enumerate verified records, unresolved dates, provisional joins and whether investigation-depth comparison is currently possible.

No additional product features are proposed. These checks tighten the existing MVP rather than expanding its scope.
