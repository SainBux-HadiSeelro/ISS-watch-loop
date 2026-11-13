# 📐 Specifications Index // ISS Watch Loop

This directory contains formal engineering and architectural specifications for the **ISS Watch Loop** telemetry system, designed in accordance with **Loop Engineering Concept 4: In-Session Loops**.

---

## 📑 Specification Documents

| Document | Identifier | Description |
| :--- | :--- | :--- |
| [**System Specification**](system-spec.md) | `SPEC-LOOP-004-ISS` | Autonomous agentic loop architecture, Perception-Action cycle, Finite State Machine (FSM), invariants, and fault-tolerance policies. |
| [**Telemetry & Schema Specification**](telemetry-schema.md) | `SCHEMA-LOOP-004-ISS` | Inbound oracle API contracts (`WhereTheISS.at`, `BigDataCloud`), JSON schemas, and append-only log format specifications. |

---

## 🎯 Compliance Checklist

- [x] **Zero External Runtime Dependencies:** Python Standard Library only (`urllib.request`, `json`, `time`, `pathlib`).
- [x] **Fault Containment:** Crash-free loop lifecycle with dual stream output (`iss_watch.log`, `iss_watch_err.log`).
- [x] **Dual Surface Support:** Headless autonomous daemon + reactive web HUD.
- [x] **Session-Bound Execution:** Fully compliant with In-Session Loop paradigms.
