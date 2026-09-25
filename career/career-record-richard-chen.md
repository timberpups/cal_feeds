# Career Record — Richard Chen

**Product Manager · Rokt · August 2023 – October 2026**

> **Scope note.** This is a sanitized record of my own work, written for interviews,
> resumes and portfolio use. It deliberately excludes client and partner identities,
> absolute company financials, client-level performance data, internal quotes and
> colleague names, incident identifiers, and unreleased product strategy. What remains
> is my role, the problems I worked on, and the relative impact of my own programmes —
> the level of detail normally carried on a resume. See the final section for exactly
> what was removed.

---

## Snapshot

| | |
|---|---|
| **Title** | Product Manager (title of record throughout) |
| **Tenure** | Aug 2023 – Oct 2026 (3 years, 1 month) |
| **Org** | Ad platform product → Ads / Ads Success |
| **Locations** | Sydney (2023–2024) → New York (Aug 2024 onward) |
| **Team** | Final charter: six direct reports across data science, analytics and engineering |
| **Scope** | 12 major programmes across 13 quarters, 3 distinct product charters |

The formal title never changed. The scope roughly doubled with each charter.

---

## Three charters

### 1. ML product — Aug 2023 – Aug 2024 · Sydney
Scoping machine-learning problems for an ad network: defining target variables and
success criteria, and specifying the offline evaluation gates a model had to clear
before earning a live test.

### 2. Experimentation & measurement — Sep 2024 – Jul 2025 · New York
Built a new experimentation platform from concept to production release, serving
internal product teams and external advertising clients. Randomisation, statistical
power, stopping rules, and governance against overlapping-test contamination.

### 3. Bidding & ad-ranking platform — Sep 2025 – Sep 2026 · New York
Target-CPA, target-ROAS and multi-funnel bidding; bid construction, floors, caps and
safeguards; budget pacing treated as a control problem; and the proposal to change the
network's auction pricing mechanism. Six direct reports.

---

## The twelve programmes

### 1. Ad suppression: from static caps to model-driven relevance
**Owner / DRI · Sep 2023 – Jan 2025**

The network decided whether to show an ad at all using two blunt instruments — static
placement frequency caps and a minimum quality-score floor that had quietly lost
coverage over time. Nobody could say whether suppression created or destroyed value.

I wrote the founding document in my first fortnight, proposing a *dynamic reserve
quality score* evaluated per placement and per position, so a slot goes empty when no
candidate clears a value bar rather than firing on a fixed cadence. I chose positional
granularity over placement-only to give partners optionality, then carried the idea
through three product generations to network general availability, ending with
account-level defaults, fractional frequency capping, and a fallback pool so pinned
campaigns still serve when a slot would otherwise be suppressed.

**Outcome:** rolled from beta to the majority of network traffic, measured against a
universal no-suppression holdout: **+17% revenue per thousand impressions** and
**+15% conversions per impression**, both statistically significant, against an
accepted **−2.9%** revenue-per-transaction trade.

**Worth telling:** in January 2024 I paused my own rollout. The programme was shipping,
but its secondary hypothesis was unproven, and I stopped rather than keep scaling a tool
I couldn't defend. The reframe that came out of that pause is what eventually got it to
general availability.

---

### 2. Cart-conversion measurement and attribution
**Owner of the measurement · Jun 2024 – Sep 2025**

Our ads sit on partner checkout pages, so if they depress cart conversion the partner
loses money and blames us. Cart conversion was named the company's number-one focus
area, but the measurement underneath it couldn't support a decision: no per-placement
granularity, four disagreeing data sources, and no way to attribute a drop to a specific
advertiser or slot. Partners were pausing integrations on suspicion alone.

I rebuilt how the damage was measured and attributed, then fed it back into the auction.

**Outcome:** partners showing statistically significant negative impact fell from
roughly **11% to under 4%**.

**Worth telling:** asked directly by the CEO whether our suppression product could fix a
major partner's cart-conversion problem, I said no — because the objective function was
wrong. The internal metric and the partner's true conversion rate were not the same
thing, and optimising the first would not fix the second. That reframing is the piece of
product thinking I'm proudest of.

---

### 3. Experimentation platform
**Owner — concept to production · Jul 2024 – Jul 2025**

A single partner rarely had enough traffic to reach significance, and standing up one
design experiment cost up to 40 person-hours. Worse, overlapping experiments were
silently contaminating each other, so readouts became arguments.

I built the platform that pooled traffic across partners, with the statistical
foundations and anti-collision governance written down.

**Outcome:** experiment setup cut from **~7 days to ~1 day**, with contamination
governance that made readouts decisive instead of disputed.

---

### 4. Payments-surface supply
**Primary PM · Jan 2025 – Oct 2025**

Offers on the payment page — the most valuable and most sensitive real estate a partner
owns. Supply was small, every new integration carried cart-conversion risk, and account
managers were understandably cautious.

**Outcome:** grew the partner base **~80% in five months**; launched an SMB
digital-wallet line that reached a seven-figure annualised run-rate within two months;
named instrumental in a major airline's go-live.

---

### 5. Auction simulator and analysis tooling
**Sponsor, prioritiser, power user · Jun 2025 – Sep 2026**

Every bidding or ranking change faced the same question: what would this have done to
revenue, cost per acquisition and fill rate if we had shipped it? The only honest answers
came from live tests costing weeks and real money. An internal auction simulator existed,
but it was a notebook a handful of people occasionally ran — too slow and too fragile to
gate decisions on.

I found it, treated it as shared infrastructure rather than a side project, and sponsored
the work to make it usable.

**Outcome:** runtime cut from **40+ hours to 3–4**. It became the evidence substrate
under every major bidding decision that followed.

---

### 6. Audiences, targeting and eligibility
**Domain strategy owner · Oct 2025 – Aug 2026**

Two problems on different timescales. Structurally, the audience and lookalike stack was
a generation behind — narrow feature set, third-party cookie and mobile-ad-ID
deprecation closing in, and no way for an advertiser to forecast how much reach a given
bid would buy. Operationally, a major platform migration silently changed eligibility
semantics in production.

I wrote the re-architecture strategy, and became the central responder on the
production cluster — which included a **six-figure-impact incident**.

---

### 7. Budget pacing
**Originated the problem; set strategy · Nov 2025 – Jul 2026**

About one campaign in four burned its daily budget before 7pm, so the highest-intent
evening hours ran without it. I surfaced the problem space and set the control strategy,
treating pacing as a control problem rather than a scheduling one.

**Outcome:** became the **network-wide default in May 2026**, buying up to **+9 hours of
active spend per day at unchanged cost per acquisition**.

---

### 8. Value-Based Bidding
**Operating owner / co-DRI · Dec 2025 – Sep 2026**

We bid one flat target CPA per campaign — every customer priced the same, which is false
for almost every advertiser. Value-based bidding fixes that, but our version had been
hand-built for a single advertiser and didn't generalise. The commercial risk of leaving
it that way was compounding: one sophisticated advertiser could bid down on high-value
customers precisely because nobody else could bid up.

I took it from a pilot at 0.1% of traffic to full general availability, and built the
offline evaluation gate that decided which advertiser onboarded next.

**Outcome:** full GA holding target return on ad spend. The gate said **no more often
than yes** — several candidate advertisers were declined on label quality or volume
before they could fail in production.

---

### 9. Auction pricing mechanism proposal
**Author; presented to C-suite · Dec 2025 – Jul 2026**

My most ambitious piece of work, and the one I'm most honest about. I authored the case
to change the network's auction pricing mechanism, on the argument that our pricing made
us look systematically expensive for the same value delivered, and that our own model
error was being charged to advertisers.

Using the simulator, I showed that pairing the change with a pacing controller made it
spend-neutral, where the naive version caused a large spend decline. I presented it to
the Chief Technology, Product and Revenue Officers.

**Outcome:** it remains a proposal. I include it because authoring a credible case for
changing the core economics of a business, and getting it a C-suite hearing, is the work
— whether or not it shipped.

---

### 10. Advertiser retention
**Framed it; directed the analysis · Jan 2026 – Jul 2026**

We knew advertisers churned, but not why or what it cost. I asked the question properly
and directed the analysis.

**Outcome:** identified a measurable early-conversion threshold predicting roughly
**38% lower churn**. The go-to-market team credited the resulting programme in a
budget scale-up.

---

### 11. Multi-event (downstream) bidding
**Owner / DRI · Mar 2026 – Sep 2026**

We bid to the upstream conversion — a registration, a connected account, a signup.
Advertisers care about what happens next: the first deposit, the first purchase. I
designed the de-averaged bid that targets the downstream event.

I audited the first build and **paused my own programme** when I found the bidding
transform was broken, then relaunched it.

**Outcome:** **+15.6% downstream conversion rate at −11.9% cost per downstream event**,
on flat spend.

---

### 12. Window-native bidding
**Initiated and led end-to-end · Jun 2026 – Aug 2026**

An advertiser sets a target CPA against their own attribution window. Our auction wasn't
using that number directly — it ran it through a legacy ratio computed in an unrelated
pacing pipeline. I led its removal across four teams.

**Outcome:** advertiser target-CPA fidelity from **66% to 99.6%**; Stage 1 shipped to
**100% of traffic, behaviour-neutral, exactly as designed**.

---

## Themes worth leading with

**I stop my own programmes.** Twice — the suppression rollout in Jan 2024, and the
downstream bidding launch in 2026 — I paused work I owned and was being credited for,
because the evidence didn't support scaling it. Both shipped better afterwards.

**Measurement before optimisation.** The cart-conversion work and the tCPA-fidelity work
are the same instinct: before tuning the system, check that the number it optimises is
the number that matters.

**Tooling as leverage.** The auction simulator wasn't my product. Recognising that a
neglected internal tool was the bottleneck on every bidding decision — and sponsoring it
as shared infrastructure — unlocked more than any feature I shipped that year.

**Saying no with evidence.** The VBB onboarding gate existed to decline advertisers, and
usually did. Building the mechanism that tells you not to ship is harder than building
the thing that ships.

**Scope growth without title change.** Three charters, each roughly double the last,
ending with six direct reports and platform-level ownership — all under one title.

---

## What was removed from the source material, and why

This document was derived from a detailed internal retrospective. The following were
stripped before it left company systems:

- **Client and partner names** — every advertiser, partner and platform identity,
  replaced with category descriptors
- **Client-level performance data** — per-advertiser conversion, ROAS and CPA figures
- **Absolute company financials** — revenue figures, opportunity sizings, incident
  dollar impacts, partner counts and traffic-share percentages
- **Internal quotes and colleague names** — verbatim chat and email excerpts, and every
  named individual other than myself
- **Unreleased product strategy** — the specific auction mechanism proposed, and
  architectural direction not publicly announced
- **Internal identifiers** — incident, ticket and system references

Relative improvements attributable to my own programmes are retained, which is standard
resume practice. If a prospective employer wants more depth than this document carries,
the right answer is to walk them through the reasoning, not the numbers.

**Before using this externally, confirm with Rokt what you are permitted to cite.**
Employment agreements differ, and a two-minute check with your manager or People team
converts an assumption into permission.
