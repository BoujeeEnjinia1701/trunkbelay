---
doc_id: TKB-MKT-001
title: TrunkBelay market and viability
project: TrunkBelay
doc_type: Market and viability
version: "0.1"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: First market and viability note (kit 1.9.1 upgrade)
---

# TrunkBelay market and viability

TrunkBelay is for coconut climbers who rescue each other, the training schemes that teach them and the rural fire crews who arrive later; it competes with improvised cloth and rope and, at a distance, with utility pole-top rescue kits that cost about USD 1,576 and are not made for palms. An open design matters because no one sells a palm rescue anchor, and because most of the kit's cost is certified rescue gear that a training scheme can buy in bulk. Prices and benchmarks are cited with the date they were checked. Method: STANDARDS section 23.

> **Safety:** TrunkBelay is not certified equipment and is not sold. Any route to wider use runs through the TRL 4 proof test, the dummy drill and a partner's training programme.

Table 1. Market segments.

| Segment | Target users and region | Competitive benchmark (cited price) | Estimated cost per unit (USD) | Value proposition |
| --- | --- | --- | --- | --- |
| Peer rescue by coconut climbers | Climber groups and labour banks in Kerala and Tamil Nadu first | Improvised cloth and rope (no cost, no anchor); fire crews with ladders and nets (TKB-PRB-001) | 828 per kit (BOM, single-kit prices); one kit per climber group | A rescue in minutes instead of a wait of 30 to 150 minutes head down |
| Climber training schemes | Friends of Coconut Tree training under the Coconut Development Board | No rescue kit or drill in current training (TKB-PRB-001) | 828, less group purchase of the rescue gear (not counted) | A standard kit and drill to teach in half a day (PR-010) |
| Fire and rescue services | Rural stations with palm rescues (Kasaragod, Kannur) | Utility pole-top rescue kit: Buckingham SuperSqueeze 488P, about USD 1,576, rated 350 lb, for smooth poles (as cited in TKB-PRB-001, checked 2026-09-30) | 828 | A light trunk anchor to secure a victim before ladders or nets are set |
| Bought rescue gear inside the kit | Any of the above | Auto-locking descender: Petzl I'D S, USD 421.20 (Haness Supply, checked 2026-10-25); Climbing Technology Sparrow 200R, GBP 179.95 (Skyland Equipment, checked 2026-10-25). Evacuation triangle: Petzl Pitagor, USD 92.90 on offer (Oliunid, checked 2026-10-25) | BOM carries USD 280 for the descender class and USD 140 for the triangle class | Specification by standard, not brand, lets a partner buy the cheapest certified device |
| Other single-stem palms | Toddy tappers, arecanut and date palm workers | None found | 828 | Same collar on trunks within 200 to 450 mm |

The BOM's USD 280 for the descender sits between the two cited devices; a branded I'D S would add about USD 141 and take the kit to about USD 969, over PR-009's USD 850. The triangle line (USD 140) is above the one cited offer; a cheaper certified triangle would take about USD 47 off. Neither is changed in the BOM: both are class prices from the TRL 3 session, to be replaced by quotes from the partner's supplier (TKB-DEC-001, item 3).

## Open route

- **Who builds it.** A fabrication shop with an AC TIG welder makes the frame (about USD 69 of the BOM, TIG welding included); everything else is bought to specification. A training scheme or a climbers' collective would hold the kits, one per group.
- **How it spreads.** Through the Friends of Coconut Tree training programme and fire service stations that have done palm rescues: a drill card, the build plan (TKB-BLD-001) and the open drawings let other districts and other palm crops copy it.
- **What keeps it open.** CERN-OHL-S-2.0 for the hardware and MIT for the scripts; the design keeps clear of the Cynch-Lok ratcheting cinch (PR-017); published with a DOI on Zenodo.
- **What it is not.** Not a product for sale and not certified equipment; any partner who wants a certified version faces EN 795-class testing at 12 kN (TKB-REG-001, G2).

## Sources

- Haness Supply. "Petzl D020AA00 I'D S Descender/Belay Device." https://www.hanessupply.com/petzl-d020aa00 (checked 2026-10-25).
- Skyland Equipment. "CT Sparrow 200 R Rescue Descender." https://skylandequipment.com/products/ct-sparrow-200 (checked 2026-10-25).
- Oliunid. "Petzl Pitagor evacuation triangle." https://www.oliunid.com/petzl-pitagor-evacuation-triangle (checked 2026-10-25).
- Buckingham Manufacturing. "SuperSqueeze Pole Top Rescue 488P." https://buckinghammfg.com/products/supersqueeze-pole-top-rescue-488p/ (as cited in TKB-PRB-001, checked 2026-09-30; not rechecked).
- TKB-PRB-001 for the reported rescues and the training scheme.
