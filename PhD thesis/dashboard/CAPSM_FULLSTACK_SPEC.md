# CAPSM — Full-Stack Rebuild Specification

**Author:** Mahmoud Kiasari  
**Institution:** Dalhousie University, Department of Electrical & Computer Engineering  
**Degree:** PhD Candidate in Electrical Engineering  
**Title:** *CAPSM: Cognitive Adaptive Power System Management — A Dual-Process Metacognitive Framework for Resilient Power Grid Control*  
**Year:** 2026  

---

## Table of Contents

1. [Project Overview](#1-project-overview)  
2. [Research Foundation](#2-research-foundation)  
3. [Current Stack (to replace)](#3-current-stack-to-replace)  
4. [Recommended Full-Stack Architecture](#4-recommended-full-stack-architecture)  
5. [Data Models](#5-data-models)  
6. [API Specification — All Endpoints](#6-api-specification--all-endpoints)  
7. [Live Simulation Endpoints](#7-live-simulation-endpoints)  
8. [ML Engine](#8-ml-engine)  
9. [Frontend — 16 Dashboard Pages](#9-frontend--16-dashboard-pages)  
10. [Configuration System](#10-configuration-system)  
11. [IEEE 9-Bus Reference Data](#11-ieee-9-bus-reference-data)  
12. [Database Schema (proposed)](#12-database-schema-proposed)  
13. [WebSocket Events (proposed)](#13-websocket-events-proposed)  
14. [Charts & Visualizations Specification](#14-charts--visualizations-specification)  
15. [Performance Targets Reference Table](#15-performance-targets-reference-table)  
16. [Rebuild Checklist & Suggested Enhancements](#16-rebuild-checklist--suggested-enhancements)

---

## 1. Project Overview

CAPSM (Cognitive Adaptive Power System Management) is a PhD proposal dashboard that presents and simulates a novel AI framework for smart-grid control. The dashboard serves as an interactive knowledge base and live simulation environment for the PhD oral examination committee.

### What the dashboard does:
- Presents the research context: 5 research gaps, 5 objectives, central hypothesis
- Explains the CAPSM architecture: System-1 (reflexive CNN-LSTM), System-2 (QIRL deliberative), Metacognitive Arbitration, PINN Safety Layer, HIRL hierarchical RL
- Displays IEEE 9-bus power system topology, load flow data, FACTS devices, EV/V2G
- Live-polls simulated real-time data: bus voltages, frequency, CAPSM mode switching, EV SoC
- Allows user to tune ~40 simulation parameters via a settings panel
- All data served by a Flask backend; frontend is a single-page HTML/CSS/JS app

---

## 2. Research Foundation

### Central Hypothesis

> A dual-process, metacognitively guided cognitive architecture (CAPSM) that unifies quantum-inspired reinforcement learning (QIRL), physics-informed neural networks (PINNs), and hierarchical multi-agent RL (HMARL) will simultaneously achieve sub-5 ms fault response (System-1), optimal economic dispatch under uncertainty (System-2 QIRL), and guaranteed physics constraint satisfaction (PINNs), thereby outperforming any single-paradigm controller on resilience, efficiency, and scalability benchmarks across IEEE 9-bus through 300-bus test systems.

### 5 Research Gaps

| ID | Title | Problem | CAPSM Solution |
|----|-------|---------|----------------|
| G1 | Single-Speed Control | Existing controllers use one decision speed; grid events span 5 ms (faults) to 50 ms (optimization) | Dual-process System-1/System-2 with metacognitive switching |
| G2 | Sample Inefficiency of Deep RL | Standard deep RL needs ~500k episodes for convergence | QIRL uses quantum superposition amplitudes for 2× faster convergence |
| G3 | Physics-Blind Neural Controllers | Pure ML controllers violate AC power-flow equations | PINNs embed physical laws directly into loss function |
| G4 | Scalability of Multi-Agent RL | Independent agents cause coordination failures at 118+ buses | HMARL with federated policy aggregation (HIRL) |
| G5 | Cyber-Physical Resilience | No controller simultaneously handles FDI, DoS, and comm delays | Metacognitive anomaly detection with graceful degradation |

### 5 Research Objectives

| ID | Objective | Target | Timeline |
|----|-----------|--------|----------|
| RO1 | Cognitive Control Model | Formal dual-process cognitive model | Months 1–6 |
| RO2 | QIRL Algorithms | ≥2× faster convergence than DQN | Months 3–12 |
| RO3 | PINNs Safety Enforcement | >99.8% AC constraint compliance | Months 6–15 |
| RO4 | Multimodal Fusion + HMARL | Handle 118+ bus systems | Months 12–24 |
| RO5 | IEEE Test System Validation | 9-, 39-, 118-, 300-bus results | Months 18–30 |

---

## 3. Current Stack (to replace)

```
Backend:   Python 3.x + Flask 2.x
Frontend:  Single-file index.html (~2225 lines) + Chart.js 4.4.1 + vanilla JS (~1433 lines)
Styling:   Custom CSS (dark theme, CSS variables)
ML:        sklearn models trained at server startup (in-process)
Storage:   In-memory Python dict (USER_CONFIG) + localStorage on client
Hosting:   localhost:5050 (no deployment)
Live data: HTTP polling every 2 seconds from client JS
```

**Problems with current stack:**
- No database — config lost on restart
- No authentication
- No WebSocket — polling is inefficient for live data
- All logic in one 2225-line HTML file
- ML models re-train on every server start (~5-10 seconds delay)
- No real-time collaboration or sharing
- No export/report generation beyond JSON config export

---

## 4. Recommended Full-Stack Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  FRONTEND  (React + TypeScript + Vite)                       │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │ React Pages │  │ Recharts /   │  │  Zustand / Context │  │
│  │ (16 pages)  │  │ Chart.js     │  │  (config state)    │  │
│  └─────────────┘  └──────────────┘  └────────────────────┘  │
│       ↕ REST API + WebSocket                                 │
├─────────────────────────────────────────────────────────────┤
│  BACKEND  (FastAPI + Python 3.11)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ REST Routes  │  │ WebSocket    │  │ ML Engine         │  │
│  │ (proposal,   │  │ (live sim    │  │ (6 sklearn models │  │
│  │  config, ml) │  │  broadcast)  │  │  loaded at start) │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
│       ↕                                                      │
├─────────────────────────────────────────────────────────────┤
│  DATABASE  (PostgreSQL or SQLite for development)            │
│  ┌──────────────────────────────────────────────────────┐    │
│  │  users, sessions, configs, sim_logs, export_history │    │
│  └──────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### Recommended tech stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Frontend framework | React 18 + TypeScript | Component isolation, type safety |
| Build tool | Vite | Fast HMR, ESM native |
| UI components | shadcn/ui + Tailwind CSS | Matches existing dark theme |
| Charts | Recharts + D3 | React-native, better than Canvas Chart.js for React |
| State management | Zustand | Lightweight, persists to localStorage |
| Backend | FastAPI (Python 3.11) | Async, WebSocket native, auto OpenAPI docs |
| WebSocket | FastAPI WebSockets | Replace polling |
| Database | PostgreSQL (Supabase for hosted) | Persistent config, sim logs |
| ORM | SQLModel / SQLAlchemy | Type-safe queries |
| ML | scikit-learn (same models) | Keep working models, just persist |
| Serialization | Pydantic v2 | Same as FastAPI, full type safety |
| Auth (optional) | NextAuth or Clerk | If multi-user sharing needed |
| Deployment | Vercel (frontend) + Railway/Fly.io (backend) | Free tier sufficient |

---

## 5. Data Models

### 5.1 ProposalData (root object returned by `/api/proposal`)

```typescript
interface ProposalData {
  title: string;            // "CAPSM: Cognitive Adaptive Power System Management"
  subtitle: string;         // "A Dual-Process Metacognitive Framework..."
  author: string;           // "Mahmoud Kiasari"
  affiliation: string;      // "Dalhousie University, Department of E&CE"
  degree: string;           // "PhD Candidate"
  year: number;             // 2026
  supervisor: string;       // "PhD Oral Examination Proposal"
  central_hypothesis: string;
  research_gaps: ResearchGap[];          // 5 items
  research_objectives: ResearchObjective[]; // 5 items
  architecture: ArchitectureData;
  ieee9bus: IEEE9BusData;
  facts_devices: FACTSDevice[];
  ev_v2g: EVV2GData;
  performance_targets: PerformanceTarget[];
  cyber_attacks: CyberAttackScenario[];
  test_systems: TestSystem[];
  hirl: HIRLData;
  simulation: SimulationParams;
}
```

### 5.2 ResearchGap

```typescript
interface ResearchGap {
  id: string;               // "G1" .. "G5"
  title: string;
  problem: string;
  capsm_solution: string;
}
```

### 5.3 ResearchObjective

```typescript
interface ResearchObjective {
  id: string;               // "RO1" .. "RO5"
  title: string;
  target: string;
  timeline: string;         // "Months 1–6"
}
```

### 5.4 ArchitectureData

```typescript
interface ArchitectureData {
  system1: SystemSpec;
  system2: SystemSpec;
  metacognition: MetacognitionSpec;
  pinn: PINNSpec;
}

interface SystemSpec {
  name: string;
  model: string;
  response_time: string;     // "<5 ms"
  function: string;
  input: string;
  output: string;
  equations: string[];
  training: string;
  target_accuracy?: string;  // System-1
  target_speedup?: string;   // System-2
}

interface MetacognitionSpec {
  name: string;
  function: string;
  metrics: MetacogMetric[];
  decision_rule: string;
}

interface MetacogMetric {
  symbol: string;   // "Cₜ", "Nₜ", "Uₜ"
  name: string;     // "Confidence", "Novelty", "Urgency"
  formula: string;
  threshold: string;
}

interface PINNSpec {
  name: string;
  function: string;
  constraints: string[];
  loss_function: string;    // "L = L_data + λ_pf·L_AC + λ_lim·L_constraints"
  target_compliance: string; // ">99.8%"
}
```

### 5.5 IEEE9BusData

```typescript
interface IEEE9BusData {
  base: { S: string; V: string; f: string };
  buses: number;             // 9
  generators: Generator[];
  loads: Load[];
  lines: TransmissionLine[];
  transformers: Transformer[];
  load_flow: LoadFlowResult[];
}

interface Generator {
  bus: number;
  V_kV: number;
  V_pu: number;
  angle_deg: number;
  P_MW: number;
  Q_MVAR: number;
  type: "Slack" | "PV" | "PQ";
}

interface Load {
  bus: number;
  P_MW: number;
  Q_MVAR: number;
}

interface TransmissionLine {
  from: number;
  to: number;
  R_pu: number;
  X_pu: number;
  B_pu: number;             // shunt susceptance (charging)
}

interface Transformer {
  name: string;             // "T1", "T2", "T3"
  from_bus: number;
  to_bus: number;
  S_MVA: number;
  V1_kV: number;
  V2_kV: number;
  X_pu: number;
}

interface LoadFlowResult {
  bus: number;
  V_pu: number;
  angle: number;            // degrees
  Pgen: number;            // MW
  Qgen: number;            // MVAR
  Pload: number;           // MW
  Qload: number;           // MVAR
}
```

### 5.6 FACTSDevice

```typescript
interface FACTSDevice {
  type: "SVC" | "STATCOM";
  name: string;
  bus: number;
  rating: string;           // "±100 MVAR"
  function: string;
  Vref: number;             // 1.0 pu
  droop: number;            // 0.03
  response_time?: string;   // STATCOM only: "5 ms"
  controlled_by: string;
}
```

### 5.7 EVV2GData

```typescript
interface EVV2GData {
  bus: number;              // 8
  fleet_size: number;       // 1000 vehicles
  unit_capacity_kW: number; // 50 kW per vehicle
  total_capacity_MW: number; // 50 MW
  energy_capacity_MWh: number; // 150 MWh
  efficiency: number;       // 0.95
  initial_soc: number;      // 0.70
  soc_bounds: [number, number]; // [0.20, 0.95]
  controlled_by: string;
}
```

### 5.8 PerformanceTarget

```typescript
interface PerformanceTarget {
  metric: string;
  target: string;
  unit: string;
  value: number;
  icon: string;
}
```

### 5.9 CyberAttackScenario

```typescript
interface CyberAttackScenario {
  type: "FDI" | "DoS" | "Delay";
  name: string;
  timing: string;           // "t=2-5s"
  description: string;
  target: string;
}
```

### 5.10 TestSystem

```typescript
interface TestSystem {
  name: string;             // "IEEE 9-Bus"
  buses: number;
  generators: number;
  lines: number;
  purpose: string;
  status: "Built" | "Planned";
}
```

### 5.11 HIRLData

```typescript
interface HIRLData {
  name: string;
  purpose: string;
  key_innovation: string;
  hierarchy: HIRLLevel[];
  training_pipeline: TrainingStage[];
  equations: string[];
  performance_targets: HIRLTarget[];
  integration_with_capsm: {
    system1: string;
    system2: string;
    metacognition: string;
    pinn: string;
  };
}

interface HIRLLevel {
  level: "Global Coordinator" | "Regional Agents" | "Device Controllers";
  function: string;
  update_rate: string;
  algorithm: string;
}

interface TrainingStage {
  stage: number;
  name: string;
  method: string;
  duration: string;
}
```

### 5.12 SimulationParams

```typescript
interface SimulationParams {
  mode: "Phasor";
  stop_time: string;        // "20 s"
  solver: string;           // "ode23tb"
  max_step: string;         // "0.2 ms"
  fault: string;            // "3-phase at Bus 5, t=1.0–1.083s"
}
```

---

## 6. API Specification — All Endpoints

Base URL: `http://localhost:5050` (dev)

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | Serve index.html | HTML |
| GET | `/api/proposal` | **Full PROPOSAL_DATA object** | `ProposalData` |
| GET | `/api/overview` | Title, author, hypothesis summary | `OverviewDTO` |
| GET | `/api/gaps` | All 5 research gaps | `ResearchGap[]` |
| GET | `/api/objectives` | All 5 research objectives | `ResearchObjective[]` |
| GET | `/api/architecture` | System-1, System-2, Metacognition, PINN | `ArchitectureData` |
| GET | `/api/ieee9bus` | Full IEEE 9-bus parameters | `IEEE9BusData` |
| GET | `/api/performance` | 6 performance target KPIs | `PerformanceTarget[]` |
| GET | `/api/facts` | SVC (Bus 5) and STATCOM (Bus 8) | `FACTSDevice[]` |
| GET | `/api/ev` | EV/V2G fleet data | `EVV2GData` |
| GET | `/api/cyber` | FDI, DoS, Delay attack scenarios | `CyberAttackScenario[]` |
| GET | `/api/test_systems` | 9/39/118/300-bus scaling table | `TestSystem[]` |
| GET | `/api/simulation` | Simulation parameters | `SimulationParams` |
| GET | `/api/hirl` | Full HIRL framework data | `HIRLData` |
| GET | `/api/config` | Get current server-side config | `UserConfig` |
| POST | `/api/config` | Save user config (JSON body) | `{ status: "ok", config: UserConfig }` |

### OverviewDTO shape:
```json
{
  "title": "CAPSM: Cognitive Adaptive Power System Management",
  "subtitle": "A Dual-Process Metacognitive Framework for Resilient Power Grid Control",
  "author": "Mahmoud Kiasari",
  "affiliation": "Dalhousie University, Department of Electrical & Computer Engineering",
  "central_hypothesis": "A dual-process, metacognitively guided...",
  "num_gaps": 5,
  "num_objectives": 5
}
```

---

## 7. Live Simulation Endpoints

All live endpoints are polled every **2 seconds** by the frontend. In a rebuild, replace with WebSocket broadcast.

### GET `/api/live/bus_voltages`

Returns simulated real-time PMU bus voltages. Voltage = base_value + sinusoidal drift + Gaussian noise.

```json
{
  "timestamp": 1738000000.123,
  "voltages": {
    "Bus_1": 1.0412,
    "Bus_2": 1.0247,
    "Bus_3": 1.0252,
    "Bus_4": 1.0261,
    "Bus_5": 0.9963,
    "Bus_6": 1.0134,
    "Bus_7": 1.0259,
    "Bus_8": 1.0155,
    "Bus_9": 1.0318
  }
}
```

**Simulation formula:**
```python
noise = 0.005 * sin(2π × 0.1 × t + bus_index) + gaussian(0, 0.001)
voltage = base_voltage[bus] + noise
```

Base voltages (pu): Bus1=1.040, Bus2=1.025, Bus3=1.025, Bus4=1.026, Bus5=0.996, Bus6=1.013, Bus7=1.026, Bus8=1.016, Bus9=1.032

---

### GET `/api/live/frequency`

```json
{
  "timestamp": 1738000000.456,
  "frequency": 60.0134
}
```

Formula: `f = 60.0 + 0.02 × sin(2π × 0.05 × t) + gaussian(0, 0.005)`

---

### GET `/api/live/ev_soc`

```json
{
  "timestamp": 1738000000.789,
  "soc": 0.712,
  "power_MW": -5.6
}
```

Formula:
```python
soc = 0.70 + 0.15 × sin(2π × 0.02 × t)
soc = clamp(soc, 0.20, 0.95)
power_MW = (0.6 - soc) × 50  # negative = discharging (V2G)
```

---

### GET `/api/live/capsm_mode`

Returns current CAPSM operating mode and metacognitive state.

```json
{
  "timestamp": 1738000000.0,
  "mode": "System-1",
  "confidence": 0.823,
  "urgency": 0.451,
  "novelty": 0.312
}
```

**Mode decision rule:**
- `mode = "System-1"` if `confidence > 0.7 AND urgency > 0.3`
- `mode = "System-2"` otherwise

Formulas:
```python
confidence = 0.5 + 0.4 × sin(2π × 0.03 × t)
urgency = 0.3 + 0.3 × |sin(2π × 0.07 × t)|
novelty = uniform(0.1, 0.5)
```

---

### GET `/api/live/hirl`

Returns two regional HIRL agent metrics + global sync.

```json
{
  "timestamp": 1738000000.0,
  "regions": [
    {
      "name": "Zone A (Bus 4-5-7)",
      "reward": 76.34,
      "policy_loss": 0.2341,
      "episodes": 51203,
      "tie_violation": 0.287
    },
    {
      "name": "Zone B (Bus 6-8-9)",
      "reward": 80.12,
      "policy_loss": 0.1987,
      "episodes": 49800,
      "tie_violation": 0.312
    }
  ],
  "global_sync": 0.912
}
```

---

## 8. ML Engine

File: `ml_engine.py` — `CAPSMMLEngine` class

### 6 trained models

| # | Model | Algorithm | Input Features | Output | Metric |
|---|-------|-----------|----------------|--------|--------|
| 1 | Fault Classifier | Random Forest (n=100) + MLP (128-64-32) | 9-bus PMU: V, I, f, dV/dt, dI/dt, df/dt (54 features) | Fault type: Normal/3-Phase/Line-Ground/Line-Line/Loss-of-Gen | RF accuracy ~96%, MLP accuracy ~94% |
| 2 | Anomaly Detector | Isolation Forest (contamination=0.05) | 27 features: V(9), f(9), dV/dt(9) | Anomaly score (negative = attack) | FDI score < Normal score |
| 3 | Convergence Predictor | Gradient Boosting Regressor | lr, gamma, epsilon, n_agents | Episodes to converge | R² ≈ 0.85 |
| 4 | Mode Classifier | Gradient Boosting Classifier | confidence, novelty, urgency, dV/dt, df/dt | 0 = System-2, 1 = System-1 | Accuracy ~99% |
| 5 | Voltage Stability | Gradient Boosting Regressor | load_P, load_Q, gen_P, svc_Q | Voltage pu | R² ≈ 0.95 |
| 6 | SoC Forecaster | Gradient Boosting Regressor | current_soc, power_MW | next_soc | R² ≈ 0.99 |

All models trained on **synthetic IEEE 9-bus data** generated at startup. 3000 samples for fault classifier, 1000 for anomaly, 500–800 for others.

### Public API methods

```python
engine = CAPSMMLEngine(seed=42)

# Fault detection
label, probabilities = engine.predict_fault(pmu_data: np.ndarray, model="rf")

# Cyber anomaly detection
is_anomaly, score = engine.detect_anomaly(measurements: np.ndarray)
# is_anomaly: 1=normal, -1=anomaly

# RL convergence prediction
episodes = engine.predict_convergence(lr=0.001, gamma=0.99, epsilon=0.01, n_agents=2)

# Mode classification
mode_int, probabilities = engine.classify_mode(confidence, novelty, urgency, dv_dt=0, df_dt=0)
# mode_int: 1=System-1, 0=System-2

# Voltage prediction
voltage_pu = engine.predict_voltage(load_p, load_q, gen_p, svc_q)

# SoC forecasting
next_soc = engine.predict_soc(current_soc, power_mw)

# Simulation helpers (return numpy arrays for chart rendering)
ep, qirl, dqn, ppo = engine.simulate_qirl(lr=0.001, gamma=0.99, n_ep=1000)
t, conf, urgency, mode = engine.simulate_metacognition(tau_c=0.7, tau_u=0.3, dur=20.0)
t, soc = engine.simulate_ev_soc(cap_mw=50, soc0=0.7, dur=20.0)
ep, hirl, central, indep, dqn = engine.simulate_hirl(lr=0.001, gamma=0.99, n_regions=2, max_ep=300000)

# Feature importance (top-15 for fault classifier)
names, importances = engine.get_feature_importance_data()

# All training metrics
metrics_dict = engine.get_all_metrics()
```

### Recommended ML API endpoints (add to full-stack rebuild)

```
POST /api/ml/predict_fault        { pmu_data: float[54] } → { label, probabilities }
POST /api/ml/detect_anomaly       { measurements: float[27] } → { is_anomaly, score }
POST /api/ml/predict_convergence  { lr, gamma, epsilon, n_agents } → { episodes }
POST /api/ml/classify_mode        { confidence, novelty, urgency } → { mode, probabilities }
POST /api/ml/predict_voltage      { load_p, load_q, gen_p, svc_q } → { voltage_pu }
POST /api/ml/predict_soc          { current_soc, power_mw } → { next_soc }
GET  /api/ml/metrics              → { fault_rf_accuracy, convergence_r2, ... }
GET  /api/ml/feature_importance   → { names: string[], values: float[] }

# Simulation data for charts (replaces hardcoded chart data):
POST /api/ml/simulate/qirl        { lr, gamma, n_ep } → { episodes[], qirl[], dqn[], ppo[] }
POST /api/ml/simulate/metacog     { tau_c, tau_u, dur } → { t[], confidence[], urgency[], mode[] }
POST /api/ml/simulate/ev_soc      { cap_mw, soc0, dur } → { t[], soc[] }
POST /api/ml/simulate/hirl        { lr, gamma, n_regions } → { episodes[], hirl[], central[], indep[], dqn[] }
```

---

## 9. Frontend — 16 Dashboard Pages

Each page is accessible via sidebar navigation. The page ID is used in `data-page` attributes.

### Navigation Structure

```
Overview
├── overview     — Dashboard Overview
└── hypothesis   — Hypothesis & Gaps

Framework
├── architecture  — CAPSM Framework Architecture
├── system1      — System-1 CNN-LSTM
├── system2      — System-2 QIRL
├── hirl         — HIRL Framework
├── pinn         — PINN Safety Layer
└── metacognition — Metacognitive Arbitration

Power System
├── topology     — IEEE 9-Bus Topology
├── loadflow     — Load Flow Analysis
├── facts        — FACTS Devices
└── ev           — EV / V2G

Validation
├── performance  — Performance Targets
├── cyber        — Cyber Attacks
├── scaling      — Test Systems
└── timeline     — Research Timeline
```

---

### Page 1: `overview` — Dashboard Overview

**Purpose:** Landing page with KPI cards and live charts.

**KPI Cards (6, read from `/api/performance`):**
- System-1 Response: `<5 ms`
- System-2 Decision: `<50 ms`
- Constraint Violations: `<0.2%`
- Fault Detection: `≥96.8%`
- QIRL Speedup: `≥2×`
- PINN Compliance: `>99.8%`

**Charts:**
1. **Bus Voltage Bar Chart** — 9 bars, live-updated every 2s from `/api/live/bus_voltages`. X-axis: Bus 1–9. Y-axis: voltage (pu). Red dashed lines at 0.90 and 1.10 (limits).
2. **Generator Dispatch Bar Chart** — Static. Gen1=71.64 MW, Gen2=163.0 MW, Gen3=85.0 MW + corresponding MVAR values.
3. **Research Gap Radar** — Hexagonal radar chart showing severity score for each gap G1–G5.

---

### Page 2: `hypothesis` — Central Hypothesis & Research Gaps

**Purpose:** Full hypothesis text + 5 research gap cards.

**Content:**
- Central hypothesis in a styled quote block
- 5 cards, one per gap (G1–G5), each shows: ID badge, title, problem statement, CAPSM solution
- No live charts — static content from `/api/gaps`

---

### Page 3: `architecture` — CAPSM Framework Architecture

**Purpose:** Visual explanation of the 4-layer CAPSM architecture.

**Content:**
- Layered block diagram (SVG or CSS-grid based):
  - Layer 1: PMU Inputs (Bus 1–9, voltage/current/frequency)
  - Layer 2: System-1 CNN-LSTM (reflexive, <5 ms)
  - Layer 3: System-2 QIRL (deliberative, <50 ms)
  - Layer 4: Metacognitive Arbitration (confidence/urgency/novelty)
  - Layer 5: PINN Safety Filter (physics constraints)
  - Layer 6: FACTS/EV/Generator output commands
- Equations displayed alongside each component
- Data from `/api/architecture`

---

### Page 4: `system1` — System-1: CNN-LSTM Reflexive Controller

**Purpose:** Technical deep-dive into System-1.

**Content:**
- Model: CNN-LSTM Neural Network
- Input: PMU measurements (V, I, θ, f) at 30–120 Hz from all 9 buses
- Input tensor shape: `X_t ∈ ℝ^{N_bus × 6 × T_window}`
- Equations: `z(t) = LSTM(CNN(X_t))`, `u_fast = f_θ(z(t))`
- Output: Reactive power injection commands to FACTS devices
- Response time: `<5 ms`
- Training: Supervised pre-training on historical fault data, then online fine-tuning
- Accuracy target: `≥96.8%`
- Confusion matrix visualization (5×5: Normal/3-Phase/Line-Ground/Line-Line/Loss-of-Gen)
- Feature importance bar chart (top 15 PMU channels from ml_engine)

---

### Page 5: `system2` — System-2: QIRL Deliberative Optimizer

**Purpose:** QIRL algorithm explanation + convergence comparison.

**Content:**
- Model: Quantum-Inspired Reinforcement Learning (QIRL)
- Equations:
  - `ψ = Σᵢ αᵢ|aᵢ⟩` (complex-valued policy amplitudes)
  - `P(aᵢ|s) = |αᵢ|²` (Born rule probability)
  - `Q(s,a) ← Q(s,a) + lr·(r + γ·max Q(s',a') - Q(s,a))`
  - `αᵢ ← αᵢ - lr·∇L + β·T(αᵢ)` (tunneling operator)
- **Convergence Chart** (live line chart):
  - X-axis: Episodes (0–1000)
  - Y-axis: Cumulative Reward
  - 3 lines: QIRL (blue), DQN (gray), PPO (purple)
  - Generated by `engine.simulate_qirl(lr, gamma, n_ep)`
  - Re-runs with new config when `s2_response_ms`, `qirl_speedup` settings change

---

### Page 6: `hirl` — HIRL Framework

**Purpose:** Hierarchical Integrated RL — 3-level hierarchy explanation + live charts.

**Content:**
- 3-tier architecture diagram:
  - Level 1: Global Coordinator (100–500 ms, federated QIRL)
  - Level 2: Regional Agents — Zone A (Bus 4-5-7), Zone B (Bus 6-8-9) (<50 ms, QIRL)
  - Level 3: Device Controllers (<5 ms, PI/PID)
- Training pipeline (4 stages with episode counts)
- 5 key equations (federated averaging, neighbor gradient sharing, global objective)
- **HIRL Convergence Chart** (line chart):
  - X-axis: Episodes (0–300k)
  - Y-axis: Reward
  - 4 lines: HIRL, Centralized, Independent agents, DQN
  - Re-computed via `engine.simulate_hirl()`
- **Live HIRL Metrics** (polled from `/api/live/hirl` every 2s):
  - Region rewards (two gauges or numbers)
  - Policy loss (line chart trailing 30 samples)
  - Global sync score

---

### Page 7: `pinn` — PINN Safety Layer

**Purpose:** Physics-Informed Neural Network constraint enforcement.

**Content:**
- Function: Enforces AC power-flow physics on all control outputs
- 5 constraints with equations:
  1. AC Power Flow (active): `P_i = V_i Σ V_j(G_ij cos θ_ij + B_ij sin θ_ij)`
  2. AC Power Flow (reactive): `Q_i = V_i Σ V_j(G_ij sin θ_ij - B_ij cos θ_ij)`
  3. Voltage limits: `0.90 ≤ V ≤ 1.10 pu`
  4. Current thermal: `I ≤ I_max per line rating`
  5. SoC bounds: `0.20 ≤ SoC ≤ 0.95`
- Loss function: `L = L_data + λ_pf·L_AC + λ_lim·L_constraints`
- Compliance target: `>99.8%`
- Static compliance gauge card

---

### Page 8: `metacognition` — Metacognitive Arbitration

**Purpose:** Shows CAPSM mode switching logic + live confidence/urgency plots.

**Content:**
- 3 metacognitive metrics:
  - Confidence `Cₜ = 1 - Var(Q-values) / Var_max` (threshold τ_c = 0.7)
  - Novelty `Nₜ = ‖s - μ_buffer‖ / σ_buffer` (threshold τ_n = 2.0σ)
  - Urgency `Uₜ = max(|ΔV/Δt|, |Δf/Δt|) / threshold` (threshold τ_u = 0.3)
- Decision rule: `α_t = 1 (System-1)` if `C_t > τ_c AND U_t > τ_u`; else `α_t = 0 (System-2)`
- **Live Time-Series Chart** (polled from `/api/live/capsm_mode` every 2s):
  - 3 lines: Confidence (green), Urgency (amber), Novelty (purple)
  - 30-point rolling window
  - Mode indicator badge: "System-1 ACTIVE" or "System-2 ACTIVE" based on current values
- **Simulation Plot** (generated once via `engine.simulate_metacognition(tau_c, tau_u)`):
  - Shows 20-second simulation with fault at t=1.0–1.5s (urgency spike) and cyber attack at t=7.5–9s

---

### Page 9: `topology` — IEEE 9-Bus Topology

**Purpose:** Interactive one-line diagram of the IEEE 9-bus WSCC test system.

**Content:**
- SVG-based one-line diagram showing:
  - 9 buses as labeled nodes
  - 6 transmission lines with R/X/B parameters (on hover)
  - 3 transformers (T1: Bus1→4, T2: Bus2→7, T3: Bus3→9)
  - 3 generators (Bus 1 slack, Bus 2/3 PV)
  - 3 loads (Bus 5: 125+j50 MVA, Bus 6: 90+j30 MVA, Bus 8: 100+j35 MVA)
  - SVC at Bus 5 (±100 MVAR), STATCOM at Bus 8 (±50 MVAR)
  - EV/V2G aggregator at Bus 8 (50 MW / 150 MWh)
- Bus nodes **color-coded** by voltage level (live from `/api/live/bus_voltages`)
- Hover tooltip on each element showing parameters
- Data from `/api/ieee9bus`

---

### Page 10: `loadflow` — Load Flow Analysis

**Purpose:** Load flow results table + visualizations.

**Content:**
- Data table: 9 rows × columns: Bus, Type, V (pu), Angle (°), P_gen (MW), Q_gen (MVAR), P_load (MW), Q_load (MVAR)
- **Voltage Profile Line Chart**:
  - X-axis: Bus 1–9
  - Y-axis: Voltage (pu)
  - Reference lines at 0.90 and 1.10 pu
- **Voltage Angle Bar Chart**:
  - X-axis: Bus 1–9
  - Y-axis: Angle (degrees)
- Generation summary: Total generation = 319.64 MW, System losses = 4.64 MW
- Data from `/api/ieee9bus` → `load_flow` array

---

### Page 11: `facts` — FACTS Devices

**Purpose:** Static reference page for FACTS devices.

**Content:**
- **SVC (Static VAR Compensator)** at Bus 5:
  - Rating: ±100 MVAR
  - Vref = 1.0 pu, droop = 0.03
  - Controlled by System-1 (fast) / System-2 (optimization)
- **STATCOM** at Bus 8:
  - Rating: ±50 MVAR
  - Vref = 1.0 pu, droop = 0.02
  - Response time: 5 ms (matches System-1 <5 ms target)
  - Controlled by System-1 reflex actions
- Control architecture diagram showing how CAPSM interfaces with FACTS
- Data from `/api/facts`

---

### Page 12: `ev` — EV / V2G Aggregator

**Purpose:** EV fleet management and Vehicle-to-Grid (V2G) explanation + live SoC.

**Content:**
- Fleet: 1000 EVs at Bus 8
- Capacity: 50 MW / 150 MWh total
- SoC bounds: 20%–95%
- Efficiency: 95%
- Controlled by System-2 QIRL (economic optimization)
- **SoC Trajectory Chart** (simulation from `engine.simulate_ev_soc()`):
  - X-axis: Time (0–20s)
  - Y-axis: SoC (0–1) with dashed lines at 0.20 and 0.95 limits
  - Single line: fleet average SoC over time
- **Live SoC Badge** (from `/api/live/ev_soc` every 2s):
  - Current SoC: `71.2%`
  - Current power: `−5.6 MW` (negative = V2G discharging)
- Data from `/api/ev`

---

### Page 13: `performance` — Performance Targets

**Purpose:** CAPSM vs baseline comparison — the core validation metrics.

**Content:**
- 6 KPI cards (same as overview)
- **CAPSM vs Baselines Bar Chart** (grouped bars):
  - X-axis: Metric categories (Response Time, Accuracy, Speedup, Compliance)
  - Y-axis: Normalized score
  - 3 groups: CAPSM (emerald), DQN baseline (gray), Rule-based baseline (blue)
- **Targets Table**:

| Metric | CAPSM Target | DQN Baseline | Rule-Based | Unit |
|--------|-------------|--------------|-----------|------|
| System-1 Response | <5 | ~20 | ~10 | ms |
| System-2 Decision | <50 | ~500 | N/A | ms |
| Fault Detection | ≥96.8% | ~82% | ~75% | % |
| QIRL Convergence Speedup | ≥2× | 1× (baseline) | N/A | × |
| PINN Compliance | >99.8% | ~85% | ~70% | % |
| Constraint Violations | <0.2% | ~5% | ~8% | % |

- Data from `/api/performance`

---

### Page 14: `cyber` — Cyber-Attack Resilience

**Purpose:** Shows 3 cyber attack scenarios and CAPSM's detection/recovery.

**Content:**
- 3 attack cards:
  1. **FDI (False Data Injection)** at t=2–5s: Gaussian noise on Bus 5 PMU (SNR=20 dB). Target: PMU measurements.
  2. **DoS (Denial of Service)** at t=8–8.5s: All PMU signals zeroed (total blackout). Target: Communication channels.
  3. **Communication Delay** at t=12–20s: 1.5s delay on control signals. Target: Control loops.
- Metacognitive response: novelty spike → System-2 deliberation + anomaly flag
- Isolation Forest score visualization for FDI vs Normal vs DoS
- Static attack timeline chart (Gantt-style, t=0–20s)
- Data from `/api/cyber`

---

### Page 15: `scaling` — Test System Scaling

**Purpose:** Shows CAPSM scalability across IEEE test systems.

**Content:**
- **Scaling Table**:

| System | Buses | Generators | Lines | Purpose | Status |
|--------|-------|-----------|-------|---------|--------|
| IEEE 9-Bus | 9 | 3 | 6 | Core validation | Built |
| IEEE 39-Bus | 39 | 10 | 46 | Gap 1 — dual-process scaling | Planned |
| IEEE 118-Bus | 118 | 54 | 186 | Gap 4 — HMARL coordination | Planned |
| IEEE 300-Bus | 300 | 69 | 411 | Full-scale CAPSM stress test | Planned |

- **Log-scale Scatter Chart** (buses vs complexity):
  - X-axis: Number of buses (log scale: 9, 39, 118, 300)
  - Y-axis: Complexity / estimated training episodes
  - Bubble size: number of generators
  - Color: Built (green) vs Planned (gray)
- Data from `/api/test_systems`

---

### Page 16: `timeline` — Research Timeline

**Purpose:** Gantt-style project timeline showing 30-month PhD plan.

**Content:**
- 5 horizontal bars (one per research objective):
  - RO1: Months 1–6 (cognitive model)
  - RO2: Months 3–12 (QIRL)
  - RO3: Months 6–15 (PINNs)
  - RO4: Months 12–24 (HMARL)
  - RO5: Months 18–30 (validation)
- Current month indicator (vertical line at current progress)
- Milestone markers at key deliverable points
- Milestone examples: "IEEE 9-bus sim ready" (Month 6), "First QIRL results" (Month 12), "HMARL paper submitted" (Month 18), "Thesis defense" (Month 30)

---

## 10. Configuration System

### All ~40 config keys with defaults

```typescript
interface UserConfig {
  // System-1 parameters
  s1_response_ms: number;        // default: 5     — Target response time for System-1 (ms)
  fault_accuracy: number;        // default: 96.8  — Fault detection accuracy % target

  // System-2 / QIRL parameters
  s2_response_ms: number;        // default: 50    — Decision cycle target (ms)
  qirl_speedup: number;          // default: 2.0   — QIRL vs DQN speedup multiplier

  // PINN parameters
  pinn_compliance: number;       // default: 99.8  — Constraint compliance % target
  max_violations: number;        // default: 0.2   — Max constraint violation %

  // IEEE 9-bus base parameters
  base_mva: number;              // default: 100   — System base MVA
  base_kv: number;               // default: 230   — Base voltage kV
  frequency: number;             // default: 60    — System frequency Hz

  // Simulation parameters
  sim_time: number;              // default: 20    — Simulation duration (seconds)

  // EV/V2G parameters
  ev_fleet: number;              // default: 1000  — Number of EVs
  ev_capacity_mw: number;        // default: 50    — Total EV fleet capacity MW

  // HIRL parameters
  hirl_regions: number;          // default: 2     — Number of HIRL regions
  hirl_global_rate: number;      // default: 200   — Global coordinator update ms
  hirl_lr: number;               // default: 0.001 — HIRL learning rate
  hirl_gamma: number;            // default: 0.99  — Discount factor

  // Metacognition thresholds
  tau_c: number;                 // default: 0.7   — Confidence threshold (System-1 trigger)
  tau_n: number;                 // default: 2.0   — Novelty threshold (std deviations)
  tau_u: number;                 // default: 0.3   — Urgency threshold

  // Cyber attack timing (for simulation)
  fdi_start: number;             // default: 5.0
  fdi_end: number;               // default: 8.0
  dos_start: number;             // default: 10.0
  dos_duration: number;          // default: 2.0
  comm_delay: number;            // default: 0.5   — Communication delay (seconds)

  // Dashboard appearance
  color_blue: string;            // default: "#3b82f6"
  color_purple: string;          // default: "#8b5cf6"
  color_emerald: string;         // default: "#10b981"
  color_amber: string;           // default: "#f59e0b"
  dark_mode: boolean;            // default: true
  auto_refresh: boolean;         // default: true  — Enable live polling
  show_live: boolean;            // default: true  — Show live indicator

  // Editable metadata (inline edit mode)
  author: string;                // default: "Mahmoud Kiasari"
  affiliation: string;           // default: "Dalhousie University, ECE"
  year: number;                  // default: 2026
}
```

### Storage behavior

1. **On load:** Read from `localStorage['capsm_dashboard_config']`; fall back to `DEFAULT_CONFIG`
2. **On save:** Write to `localStorage` AND `POST /api/config` (server-side persistence, lost on restart)
3. **On export:** Download `capsm_config.json` with current config
4. **On import:** Accept JSON file, validate keys, apply to state
5. **On reset:** Restore all values to `DEFAULT_CONFIG`

### Settings panel (UI)

The settings panel (`openSettings()`) uses a modal with:
- Sliders for numeric values (with min/max bounds and step)
- Color pickers for theme colors
- Toggles for boolean flags
- Text inputs for `author`, `affiliation`, `year` (inline edit mode)

Every change triggers immediate chart re-initialization (`reinitPageCharts()`) for the current page.

### Full-stack config recommendations

In the rebuild, store config in PostgreSQL `user_configs` table with:
- `user_id` (or session_id for anonymous)
- `config_json` (JSONB)
- `created_at`, `updated_at`
- Named presets (e.g., "Default IEEE 9-Bus", "High-Performance Mode")

---

## 11. IEEE 9-Bus Reference Data

### Complete Bus Data

| Bus | Type | V (pu) | Angle (°) | P_gen (MW) | Q_gen (MVAR) | P_load (MW) | Q_load (MVAR) |
|-----|------|--------|----------|-----------|-------------|------------|--------------|
| 1 | Slack | 1.040 | 0.000 | 71.64 | 27.05 | 0 | 0 |
| 2 | PV | 1.025 | 9.280 | 163.00 | 6.65 | 0 | 0 |
| 3 | PV | 1.025 | 4.665 | 85.00 | -10.86 | 0 | 0 |
| 4 | PQ | 1.026 | -2.217 | 0 | 0 | 0 | 0 |
| 5 | PQ | 0.996 | -3.989 | 0 | 0 | 125 | 50 |
| 6 | PQ | 1.013 | -3.688 | 0 | 0 | 90 | 30 |
| 7 | PQ | 1.026 | 3.720 | 0 | 0 | 0 | 0 |
| 8 | PQ | 1.016 | 0.728 | 0 | 0 | 100 | 35 |
| 9 | PQ | 1.032 | 1.967 | 0 | 0 | 0 | 0 |

**System totals:** Generation = 319.64 MW | Losses = 4.64 MW | Total load = 315.0 MW

### Transmission Lines (6)

| From | To | R (pu) | X (pu) | B (pu) |
|------|----|--------|--------|--------|
| 4 | 5 | 0.010 | 0.085 | 0.176 |
| 4 | 6 | 0.017 | 0.092 | 0.158 |
| 5 | 7 | 0.032 | 0.161 | 0.306 |
| 6 | 9 | 0.039 | 0.170 | 0.358 |
| 7 | 8 | 0.0085 | 0.072 | 0.149 |
| 8 | 9 | 0.0119 | 0.1008 | 0.209 |

### Transformers (3)

| ID | From Bus | To Bus | MVA | V1 (kV) | V2 (kV) | X (pu) |
|----|----------|--------|-----|---------|---------|--------|
| T1 | 1 | 4 | 247.5 | 16.5 | 230 | 0.0576 |
| T2 | 2 | 7 | 192.0 | 18.0 | 230 | 0.0625 |
| T3 | 3 | 9 | 128.0 | 13.8 | 230 | 0.0586 |

### FACTS Devices

| Device | Bus | Rating | Vref (pu) | Droop | Response |
|--------|-----|--------|-----------|-------|----------|
| SVC | 5 | ±100 MVAR | 1.0 | 0.03 | ~50 ms (System-2) |
| STATCOM | 8 | ±50 MVAR | 1.0 | 0.02 | 5 ms (System-1) |

### EV/V2G at Bus 8

| Parameter | Value |
|-----------|-------|
| Fleet size | 1000 vehicles |
| Unit capacity | 50 kW/vehicle |
| Total capacity | 50 MW |
| Energy capacity | 150 MWh |
| Efficiency | 95% |
| Initial SoC | 70% |
| SoC bounds | 20%–95% |

### Fault Scenario (default simulation)

- **Type:** 3-phase short circuit at Bus 5
- **Duration:** t = 1.0–1.083 s (5 cycles at 60 Hz)
- **Solver:** ode23tb (Matlab Power Systems Toolbox)
- **Mode:** Phasor simulation
- **Total time:** 20 s
- **Max step:** 0.2 ms

---

## 12. Database Schema (proposed)

```sql
-- User sessions (anonymous by config hash, or authenticated)
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT now(),
    last_seen TIMESTAMPTZ DEFAULT now()
);

-- User configurations
CREATE TABLE user_configs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id),
    name VARCHAR(100) DEFAULT 'Default',
    config_json JSONB NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- Simulation run logs
CREATE TABLE sim_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id),
    timestamp TIMESTAMPTZ DEFAULT now(),
    endpoint VARCHAR(50),   -- 'bus_voltages', 'capsm_mode', etc.
    data_json JSONB,
    config_snapshot JSONB   -- what config was active when this was polled
);

-- ML prediction logs
CREATE TABLE ml_predictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id),
    timestamp TIMESTAMPTZ DEFAULT now(),
    model_name VARCHAR(50),  -- 'fault_rf', 'mode', 'voltage', etc.
    input_json JSONB,
    output_json JSONB,
    latency_ms INTEGER
);

-- Export history
CREATE TABLE exports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id),
    timestamp TIMESTAMPTZ DEFAULT now(),
    export_type VARCHAR(20),  -- 'json', 'pdf', 'csv'
    filename VARCHAR(200)
);
```

---

## 13. WebSocket Events (proposed)

Replace HTTP polling (`setInterval` every 2s) with WebSocket for live data.

### WebSocket endpoint: `ws://localhost:8000/ws/live`

### Server → Client events (broadcast every 2s)

```typescript
// All events have this shape:
interface WSMessage {
  event: string;
  timestamp: number;
  data: unknown;
}

// Event: "bus_voltages"
{ event: "bus_voltages", timestamp: 1738000000, data: {
  Bus_1: 1.0412, Bus_2: 1.0247, ..., Bus_9: 1.0318
}}

// Event: "frequency"
{ event: "frequency", timestamp: 1738000000, data: { frequency: 60.0134 }}

// Event: "ev_soc"
{ event: "ev_soc", timestamp: 1738000000, data: { soc: 0.712, power_MW: -5.6 }}

// Event: "capsm_mode"
{ event: "capsm_mode", timestamp: 1738000000, data: {
  mode: "System-1", confidence: 0.823, urgency: 0.451, novelty: 0.312
}}

// Event: "hirl"
{ event: "hirl", timestamp: 1738000000, data: {
  regions: [{name, reward, policy_loss, episodes, tie_violation}, ...],
  global_sync: 0.912
}}
```

### Client → Server events

```typescript
// Subscribe to specific data streams
{ event: "subscribe", streams: ["bus_voltages", "capsm_mode"] }

// Unsubscribe
{ event: "unsubscribe", streams: ["hirl"] }

// Pause/resume live data
{ event: "pause" }
{ event: "resume" }
```

---

## 14. Charts & Visualizations Specification

### Chart 1: Bus Voltage Bar Chart (Overview + Loadflow)
- **Type:** Vertical bar chart
- **Library:** Chart.js (current) / Recharts BarChart (rebuild)
- **X-axis:** Bus labels "Bus 1" … "Bus 9"
- **Y-axis:** Voltage (pu), range 0.85–1.15
- **Reference lines:** Dashed red at 0.90 and 1.10 pu
- **Live update:** Yes — every 2s via WebSocket `bus_voltages` event
- **Colors:** Blue for normal (within limits), amber at 0.95–0.90, red below 0.90 or above 1.10

### Chart 2: Generator Dispatch Bar (Overview)
- **Type:** Grouped bar (P_MW and Q_MVAR side by side)
- **Static data:** Gen1={71.64 MW, 27.05 MVAR}, Gen2={163.0 MW, 6.65 MVAR}, Gen3={85.0 MW, -10.86 MVAR}
- **Colors:** Blue (P), Purple (Q)

### Chart 3: Research Gap Radar (Overview)
- **Type:** Radar / spider chart
- **Labels:** G1–G5 (5 axes)
- **Datasets:** Two series — "Problem Severity" and "CAPSM Coverage"
- **Fill:** Semi-transparent

### Chart 4: QIRL Convergence (System-2)
- **Type:** Line chart
- **Data source:** `engine.simulate_qirl(lr, gamma, n_ep)` — re-run when config changes
- **X:** Episodes (0–1000), **Y:** Cumulative Reward (−500 to 100)
- **Lines:** QIRL (emerald), DQN (gray), PPO (purple)
- **Annotation:** Arrow showing "≥2× faster" at convergence crossover point

### Chart 5: Metacognition Time Series (Metacognition)
- **Type:** Multi-line chart with mode-switch background shading
- **Data source:** Live (`/api/live/capsm_mode`) + initial sim from `engine.simulate_metacognition()`
- **Lines:** Confidence (green), Urgency (amber), Novelty (purple)
- **Background shading:** Green when System-1 active, blue when System-2
- **Reference lines:** tau_c=0.7 (dashed green), tau_u=0.3 (dashed amber)

### Chart 6: EV SoC Trajectory (EV page)
- **Type:** Line chart
- **Data source:** `engine.simulate_ev_soc(cap_mw, soc0, dur)`
- **X:** Time (0–20s), **Y:** SoC (0–1)
- **Reference lines:** Dashed at 0.20 (min) and 0.95 (max)
- **Live badge:** Current SoC from `/api/live/ev_soc`

### Chart 7: HIRL Convergence (HIRL page)
- **Type:** Line chart
- **Data source:** `engine.simulate_hirl(lr, gamma, n_regions)`
- **X:** Episodes (0–300k), **Y:** Reward (−400 to 100)
- **Lines:** HIRL (emerald), Centralized (blue), Independent (amber), DQN (gray)

### Chart 8: Voltage Profile Line (Loadflow)
- **Type:** Line chart with area fill
- **X:** Bus 1–9, **Y:** Voltage pu
- **Same reference lines as Chart 1**

### Chart 9: Voltage Angle Bar (Loadflow)
- **Type:** Horizontal bar chart
- **X:** Angle in degrees, **Y:** Bus labels
- **Blue for positive angles, purple for negative**

### Chart 10: Test System Scaling Scatter (Scaling page)
- **Type:** Bubble/scatter chart with log-scale X-axis
- **X:** Number of buses (log: 9, 39, 118, 300)
- **Y:** Estimated training complexity (episodes)
- **Bubble size:** Number of generators
- **Color:** Green (Built), Gray (Planned)

### Chart 11: Performance Comparison Bar (Performance page)
- **Type:** Grouped horizontal bar chart
- **Groups:** CAPSM (emerald), DQN (gray), Rule-based (blue)
- **Categories:** 6 performance metrics normalized 0–100%

---

## 15. Performance Targets Reference Table

| Metric | CAPSM Target | Value | Unit | DQN Baseline | Rule-Based |
|--------|-------------|-------|------|-------------|-----------|
| System-1 Response Time | <5 | 5 | ms | ~20 ms | ~10 ms |
| System-2 Decision Cycle | <50 | 50 | ms | ~500 ms | N/A |
| Constraint Violations | <0.2% | 0.2 | % | ~5% | ~8% |
| Fault Detection Accuracy | ≥96.8% | 96.8 | % | ~82% | ~75% |
| QIRL Speedup vs DQN | ≥2× | 2.0 | × | 1× | N/A |
| PINN Compliance | >99.8% | 99.8 | % | ~85% | ~70% |
| HIRL Tie-Line Violation | <0.5% | 0.5 | % | ~3% | — |
| HIRL Global Coord Overhead | <15% | 15 | % | ~40% | — |
| Scalability | 300+ buses | 300 | buses | ~50 | — |
| HIRL Regional Convergence | <50k episodes | 50000 | eps | ~200k | — |

---

## 16. Rebuild Checklist & Suggested Enhancements

### Core rebuild (must-have)

- [ ] React + TypeScript project scaffold (Vite)
- [ ] FastAPI backend with all 16 REST endpoints from §6
- [ ] WebSocket server broadcasting 5 live data streams from §7
- [ ] All 16 page components matching §9 descriptions
- [ ] Config system with Zustand store persisting to localStorage + DB
- [ ] ML Engine exposed via REST API (§8 ML endpoints)
- [ ] PostgreSQL schema from §12
- [ ] All 11 chart components from §14
- [ ] Dark/light theme toggle
- [ ] Settings modal with all ~40 config keys
- [ ] Export to JSON + PDF
- [ ] Inline edit mode for text content (author, hypothesis, gaps)

### Suggested enhancements (new features)

- [ ] **Authentication:** User login so multiple researchers can save their own configs and simulation results
- [ ] **Named simulation presets:** Save/load/share config presets (e.g., "Fault scenario", "Cyber attack demo")
- [ ] **Simulation playback:** Record a 20s simulation run and replay it (currently everything is live only)
- [ ] **Real QIRL training:** Replace `simulate_qirl()` with actual QIRL training loop (async, shows live training progress)
- [ ] **Export to PDF/LaTeX:** Generate proposal section PDFs with live chart snapshots, for thesis documentation
- [ ] **IEEE bus selector:** Switch between 9-bus, 39-bus topology views
- [ ] **Comparison mode:** Side-by-side view of two different config setups
- [ ] **Annotation system:** Researchers can add text notes to any chart data point
- [ ] **Collaboration mode:** Real-time multi-user view (multiple tabs/browsers see same live data)
- [ ] **Mobile responsive:** Currently desktop-only layout
- [ ] **PyPSA integration:** Real power flow solver instead of hardcoded IEEE 9-bus data
- [ ] **Metrics history:** Log all live polling results to DB for trend analysis over sessions
- [ ] **Notification system:** Alert when any bus voltage leaves normal bounds

### Key files to create in rebuild

```
frontend/
├── src/
│   ├── components/
│   │   ├── charts/           (11 chart components)
│   │   ├── pages/            (16 page components)
│   │   ├── layout/           (Sidebar, Header, SettingsModal)
│   │   └── ui/               (KPICard, Badge, Gauge, etc.)
│   ├── stores/
│   │   ├── configStore.ts    (Zustand config store)
│   │   └── liveStore.ts      (WebSocket live data store)
│   ├── hooks/
│   │   ├── useWebSocket.ts
│   │   └── useConfig.ts
│   ├── lib/
│   │   └── api.ts            (typed API client)
│   └── types/
│       └── capsm.ts          (all interfaces from §5)

backend/
├── app/
│   ├── main.py               (FastAPI app, CORS, WebSocket)
│   ├── routes/
│   │   ├── proposal.py       (all /api/* endpoints)
│   │   ├── live.py           (live simulation endpoints)
│   │   └── ml.py             (ML prediction endpoints)
│   ├── models/
│   │   └── schemas.py        (Pydantic models)
│   ├── database/
│   │   ├── connection.py
│   │   └── crud.py
│   ├── ml/
│   │   └── engine.py         (CAPSMMLEngine class, unchanged)
│   └── data/
│       └── proposal_data.py  (PROPOSAL_DATA dict, unchanged)
```

---

*This document was generated from the CAPSM PhD Dashboard codebase.*  
*Source files: `server.py` (545 lines), `index.html` (2225 lines), `js/main.js` (1433 lines), `ml_engine.py` (400 lines)*  
*Dashboard: http://localhost:5050*
