# Phase 1 — Foundations

> Build fundamental architecture vocabulary and decision-making methodology. Address the highest-priority gaps (networking, security) at a basics level.

## Duration

**5 weeks / ~60 hours** (12h/wk average)

## Weekly Breakdown

### Week 1 — NFRs & Quality Attributes
- Read *Software Architecture in Practice* Ch. 4 (quality attributes)
- Read ISO 25010 quality model summary
- Skim all 6 AWS Well-Architected Pillar whitepapers (intro sections only)
- **Exercise**: Write down the NFRs that apply to your production system. List at least 5 quality attributes (availability, latency, durability, security, cost, etc.) and rate the current system 1–5 on each.
- **Hours**: 12

### Week 2 — ADR Format + Trade-off Intro
- Read Michael Nygard's original ADR article
- Browse ADR examples from GitHub (spotify, AWS, joelparkerhenderson)
- Read *Design It!* selected chapters on trade-off analysis
- Read ATAM method overview
- **AI session (1h)**: AI reviews ADR format understanding. You explain the template back; AI checks for gaps.
- **Exercise**: Find 3 decisions your team made recently. Write each decision as a single-line ADR (Title + Decision only).
- **Hours**: 12

### Week 3 — Networking Workshop
- Complete AWS VPC workshop (catalog.workshops.aws/networking)
- Hands-on: VPCs, subnets, public/private, NAT gateways, security groups, NACLs
- **Exercise**: Sketch the network topology of your production system. Identify what's in each subnet, what traffic flows between them, and where the security boundaries are.
- **Hours**: 12

### Week 4 — Security Workshop
- Complete AWS Security workshop (catalog.workshops.aws/security)
- Hands-on: IAM policies, roles, KMS basics, Secrets Manager
- **Exercise**: Audit one IAM policy in your production system. Write a 1-paragraph analysis: what does it allow, what should it restrict, and how would you improve it?
- **Hours**: 12

### Week 5 — Practice ADRs + Phase Close
- Write 2 practice Tier 0 ADRs (use generic scenarios or small decisions from your system)
- For each ADR, write a 3-sentence executive summary for a non-technical stakeholder
- **AI session (1h)**: Format review — AI checks template compliance
- Flex: catch any overflow from weeks 1–4
- **Hours**: 12 (8h ADR + 4h flex)

## Lead Mode Deliverable
2 practice ADRs (Tier 0) written in correct format, with executive summaries.

## Contribute Mode Deliverable
A personal reference document: "NFRs of my system" — a written analysis of 5+ quality attributes for your production system, including current ratings.

## Influence Component
Writing for an audience — practice ADRs must be written for a technical lead who has no context. Executive summaries target non-technical stakeholders.

## Checkpoint Gate
Can write a correct ADR using the template. Can explain quality attributes and basic trade-off concepts in your own words.

## Deferral Markers
- Drop IAM/Security workshop → replace with docs-only reading (−4h)
- Drop one practice ADR (−4h)
- Skip ATAM deep dive, keep just the concept (−3h)
- Final fallback: Week 5 flex absorbs up to 4h of overflow
