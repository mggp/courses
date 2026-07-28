# Resources

> Broad sweep across all competency areas. Covers books, courses, articles, workshops, and practice resources. Ranked by relevance to the gap matrix. Time estimates are rough (total hours to complete).

---

## 1. Architecture Methodologies

### ADRs & Decision Records
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [ADR GitHub organization](https://github.com/adr) — templates, tools, tooling docs | Reference | 1h | Free | Official ADR format specs and examples |
| "Documenting Architecture Decisions" — Michael Nygard (original ADR blog post) | Article | 30m | Free | The original, short and essential |
| [ADR Examples by Spotify / AWS](https://github.com/joelparkerhenderson/architecture-decision-record) | Collection | 1h | Free | Real-world examples at multiple tiers |
| [Happy Path ADR workshop](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/examples) | Practice | 2h | Free | Write your first ADR from a scenario |

### Trade-off Analysis
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| "Software Architecture in Practice" — Bass, Clements, Kazman (4th ed.) | Book | 20h | Paid | Canonical text on architecture, quality attributes, trade-off analysis |
| "Documenting Software Architectures" — Clements et al. | Book | 15h | Paid | Views, stakeholders, documenting decisions |
| [ATAM (Architecture Trade-off Analysis Method)](https://www.sei.cmu.edu/our-work/atam-method/) — SEI | Method | 3h | Free | Structured trade-off evaluation |
| "Design It!" — Michael Keeling | Book | 10h | Paid | Practical, beginner-friendly architecture book |

### Quality Attributes / NFRs
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| "Software Architecture in Practice" (Ch. 4 — Quality Attributes) | Book chapter | 3h | Paid | Best NFR intro available |
| [ISO/IEC 25010 quality model](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) | Standard | 1h | Free | Industry-standard quality attribute taxonomy |
| AWS Well-Architected Framework — [Operational Excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html), [Security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html), [Reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html), [Performance Efficiency](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html), [Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html), [Sustainability](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/welcome.html) | Whitepapers | 8h | Free | Maps NFRs to AWS services — essential reference |

---

## 2. Architecture Patterns

### Foundational Pattern Knowledge
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| "Designing Data-Intensive Applications" — Martin Kleppmann | Book | 25h | Paid | Covers CQRS, Event Sourcing, partitioning, replication — masterpiece |
| "Building Microservices" — Sam Newman (2nd ed.) | Book | 20h | Paid | Microservices patterns, strangler fig, service boundaries |
| [Microservices.io patterns catalog](https://microservices.io/patterns/) — Chris Richardson | Catalog | 4h | Free | Browse all patterns: CQRS, Saga, Outbox, etc. |
| "Patterns of Enterprise Application Architecture" — Martin Fowler | Book | 15h | Paid | Classic reference, still highly relevant |

### Event-Driven & Async
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [AWS Event-Driven Architecture whitepaper](https://docs.aws.amazon.com/whitepapers/latest/event-driven-architecture/welcome.html) | Whitepaper | 3h | Free | Patterns with EventBridge, SQS, SNS |
| "Enterprise Integration Patterns" — Hohpe & Woolf | Book | 20h | Paid | Canonical messaging patterns |
| [Transactional Outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html) — Chris Richardson | Article | 30m | Free | With Debezium / Kafka or DynamoDB Streams |

### Resilience
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| "Building Resilient and Fault-Tolerant Applications" — AWS re:Invent talks | Videos | 3h | Free | Search YouTube for recent re:Invent sessions |
| [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) | Whitepaper | 2h | Free | DR strategies, RTO/RPO, backup |
| Circuit Breaker pattern — [Martin Fowler](https://martinfowler.com/bliki/CircuitBreaker.html) | Article | 30m | Free | Original write-up |
| Chaos Engineering — [Principles of Chaos](https://principlesofchaos.org/) | Article | 1h | Free | Core concepts |

---

## 3. Cloud Infrastructure (AWS)

### Networking (highest gap priority)
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [AWS VPC documentation / workshop](https://catalog.workshops.aws/networking/en-US) | Workshop | 6h | Free | Hands-on: VPCs, subnets, NAT, Transit Gateway |
| "AWS Networking Fundamentals" — Pluralsight / A Cloud Guru | Course | 8h | Paid | Structured video course |
| [AWS re:Invent networking sessions](https://www.youtube.com/@AWSEventsChannel/search?query=networking) — YouTube | Videos | 4h | Free | Search for latest VPC design talks |
| [AWS Well-Architected Networking Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-networking.html) | Whitepaper | 1h | Free | Best practices |

### Security / IAM
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [IAM Documentation — policies, roles, best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) | Docs | 4h | Free | Start with the user guide |
| [AWS Security Workshop](https://catalog.workshops.aws/security) | Workshop | 6h | Free | Hands-on IAM, KMS, Secrets Manager |
| "AWS Security" — Dylan Shields (O'Reilly) | Book | 10h | Paid | Practical, from basics to advanced |
| [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) | Whitepaper | 2h | Free | Framework-aligned |

### Compute & Storage — Deepening
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [ECS Workshop](https://ecs-workshop.aws/) | Workshop | 4h | Free | Hands-on ECS Fargate |
| [DynamoDB Advanced Patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html) | Docs | 3h | Free | Indexing, single-table design, streams |
| [S3 Workshop](https://s3-advanced-workshop.aws/) | Workshop | 4h | Free | Storage classes, lifecycle, performance |
| [Aurora Serverless Workshop](https://catalog.workshops.aws/aurora-serverless) | Workshop | 3h | Free | Database migration patterns |

### Observability
| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [AWS Observability Workshop](https://catalog.workshops.aws/observability) | Workshop | 6h | Free | CloudWatch, X-Ray, OpenTelemetry, Grafana |
| "Observability Engineering" — Majors, Fong, Mirza (O'Reilly) | Book | 12h | Paid | Modern observability principles |
| [AWS re:Invent observability talks](https://www.youtube.com/@AWSEventsChannel/search?query=observability) | Videos | 3h | Free | Latest patterns |

---

## 4. Influence Without Authority

| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| "Influence Without Authority" — Cohen & Bradford | Book | 8h | Paid | Classic framework, slightly dated but principles hold |
| [How to Write an RFC](https://philcalcado.com/2018/11/19/a_structured_rfc_process.html) — Phil Calcado | Article | 30m | Free | Practical RFC process for engineering orgs |
| "The Art of Writing Technical RFCs" — various articles | Collection | 2h | Free | Search for "technical RFC template" |
| [Amazon's 6-pager / PR/FAQ process](https://www.aboutamazon.com/news/company-news/writing-at-amazon) — public examples | Article | 1h | Free | Writing for stakeholder persuasion |
| "Articulating Design Decisions" — Tom Greever | Book | 6h | Paid | Communicating and defending decisions to stakeholders |

---

## 5. AWS Workshops & Practice Resources (Hands-On)

| Resource | Type | Time | Cost | Notes |
|---|---|---|---|---|
| [AWS Workshops catalog](https://catalog.workshops.aws/) | Portal | Variable | Free | Comprehensive workshop index |
| [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/) | Labs | Variable | Free | Hands-on WA framework labs |
| [Free AWS Digital Training](https://www.aws.training/) | Courses | Variable | Free | Official AWS training, some interactive |
| [AWS Skill Builder](https://explore.skillbuilder.aws/) | Portal | Variable | Freemium | Learning plans, exam prep |
| [Real AWS Architecture case studies](https://aws.amazon.com/solutions/case-studies/) | Case Studies | 3h | Free | Learn from production architectures |

---

## 6. Certifications (Optional Signal)

Not a goal of this plan, but useful for structured learning:

| Exam | Relevant For | Notes |
|---|---|---|
| [AWS Solutions Architect — Associate](https://aws.amazon.com/certification/certified-solutions-architect-associate/) | Broad AWS knowledge | Good structured baseline |
| [AWS Solutions Architect — Professional](https://aws.amazon.com/certification/certified-solutions-architect-professional/) | Advanced cross-service design | Closer to architect-level scope |
| [AWS Advanced Networking](https://aws.amazon.com/certification/certified-advanced-networking-specialty/) | Networking depth | Only if you decide to invest in networking specialty |

---

## Summary by Gap Priority

| Gap Priority | Top Recommendation | Estimated Time |
|---|---|---|
| Networking | AWS VPC Workshop (hands-on) | 6h |
| Security/IAM | AWS Security Workshop | 6h |
| Architecture Patterns | "Designing Data-Intensive Applications" + Microservices.io catalog | 29h |
| Architecture Methodologies | "Software Architecture in Practice" + ADR examples | 24h |
| Observability | AWS Observability Workshop | 6h |
| Influence | "Influence Without Authority" + RFC article | 9h |
