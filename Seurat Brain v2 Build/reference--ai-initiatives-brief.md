# Seurat AI Initiatives Brief
**Prepared for:** Security and Data Management Partner  
**Prepared by:** Nick Fisher, Seurat Group  
**Date:** March 6, 2026

## 1) Purpose
Seurat is building a practical AI operating layer that improves delivery speed, quality consistency, and institutional learning while maintaining client confidentiality.

The current strategy has two complementary tracks:
- **Track A (Immediate value):** workflow automations that remove repetitive analyst work and produce client-ready outputs.
- **Track B (Compounding value):** a curated institutional knowledge vault (`seurat-brain`) that captures reusable firm knowledge and supports context-aware AI collaboration.

This document summarizes the system design, operating model, and recommended controls for secure scale-up.

## 2) System Overview: Seurat Brain
`seurat-brain` is an Obsidian vault (primarily Markdown files) synced through Dropbox. It is intentionally lightweight compared with raw project storage and is designed as a curated knowledge layer, not a full replica of all source files.

### Core design principles
- **Curated over raw:** distilled notes, project briefs, handoffs, and reusable frameworks rather than full source dumps.
- **Mirrored structure:** client/project naming mirrors Dropbox project hierarchy for traceability.
- **Operational continuity:** each active project includes live status and next actions (`_handoff.md`).
- **Compounding intelligence:** cross-project themes, methods, and patterns are accumulated in shared intelligence/framework folders.

### Practical usage model
- Team members use Claude Cowork (and selectively Claude Code) pointed to `seurat-brain` for Seurat-specific context in daily work.
- AI skills and automations generate outputs such as meeting notes, survey test plans, and wireframe artifacts.
- Scheduled ingestion/hygiene tasks in `_automation/` keep the vault current and reduce drift.

## 3) Architecture (Conceptual)
1. **Source systems:** client materials, meeting outputs, project documents, Seurat process artifacts.
2. **Extraction and normalization layer:** periodic scripts convert relevant knowledge into structured Markdown notes and metadata.
3. **Knowledge vault (`seurat-brain`):** organized, linkable institutional memory (Clients, Intelligence, Skills, Outputs, etc.).
4. **AI interaction layer:** Claude Cowork/Code and Seurat workflow skills reference the vault for context-aware generation and decision support.
5. **Delivery layer:** final client outputs and internal operating artifacts.

## 4) Security and Data Management Controls (Recommended Baseline)
To make this architecture partner-ready, Seurat should formalize the following controls:

### Data scope and classification
- Define what is allowed in `seurat-brain` (approved summary knowledge) vs. prohibited (raw sensitive files unless explicitly approved).
- Tag notes by sensitivity tier (e.g., Internal, Client Confidential, Restricted).
- Create written inclusion/exclusion rules for ingestion jobs.

### Access control and identity
- Restrict Dropbox folder permissions to approved users/groups only.
- Enforce least-privilege access by role (leadership, delivery, operations).
- Require MFA and managed-device controls for vault access.

### Privacy and confidentiality
- Apply redaction/minimization policies for PII and sensitive client details.
- Store references/links to highly sensitive sources rather than full copied content when feasible.
- Maintain client-specific handling rules where contractual requirements differ.

### Auditability and integrity
- Keep automated run logs for ingestion/refresh jobs.
- Maintain routine vault health checks (broken links, missing critical docs, stale handoffs).
- Define owner accountability for remediation SLAs.

### AI usage governance
- Standardize approved AI tools and workspace configuration.
- Document “human-in-the-loop” requirements for client-facing outputs.
- Maintain prompt/output review standards for high-risk deliverables.

## 5) Current Value Delivered
Seurat is already seeing measurable value from automation-first workflows:
- Significant time reduction on repeatable production tasks (e.g., meeting notes, survey pipelines, document preparation).
- Faster turnaround with more consistent output quality.
- Better day-to-day execution throughput across active engagements.

This supports the current prioritization: continue shipping production tools while expanding knowledge compounding in parallel.

## 6) Near-Term Roadmap (90 Days)
### Phase 1: Governance hardening (Weeks 1-3)
- Approve data classification policy and ingestion guardrails.
- Finalize access model and ownership matrix.
- Define audit dashboard metrics and review cadence.

### Phase 2: Operational reliability (Weeks 4-8)
- Stabilize scheduled extraction/update jobs.
- Raise vault hygiene score (link integrity, required project docs, freshness).
- Implement exception handling for sensitive-content detection.

### Phase 3: Controlled scale (Weeks 9-12)
- Expand team usage with role-based onboarding.
- Track utilization and output quality KPIs.
- Publish quarterly insight synthesis from cross-project patterns and themes.

## 7) Decision Request for Security/Data Management Partner
Seurat requests alignment on:
- Classification and retention policy for vault content.
- Minimum technical controls for access, logging, and device posture.
- Approved operating model for AI-assisted work on client and internal materials.

With these controls in place, Seurat can scale a secure, high-leverage AI system that improves both immediate delivery efficiency and long-term institutional intelligence.
