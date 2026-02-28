# CAPSM PhD Proposal Dashboard — Complete Guide

**Author:** Mahmoud Kiasari  
**Institution:** Dalhousie University, Department of Electrical & Computer Engineering  
**Dashboard URL (local):** http://localhost:5050  
**Topic:** Cognitive-Adaptive Power System Management (CAPSM) — A Dual-Process AI Framework for Modern Power Grids

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [How to Run the Dashboard](#2-how-to-run-the-dashboard)
3. [File Structure](#3-file-structure)
4. [All 16 Pages — Detailed Explanation](#4-all-16-pages--detailed-explanation)
   - [Overview](#41-overview-dashboard)
   - [Hypothesis](#42-hypothesis)
   - [Architecture](#43-architecture)
   - [System-1 CNN-LSTM](#44-system-1-cnn-lstm)
   - [System-2 QIRL](#45-system-2-qirl)
   - [HIRL Framework](#46-hirl-framework)
   - [PINN Safety](#47-pinn-safety)
   - [Metacognition](#48-metacognition)
   - [IEEE 9-Bus (Topology)](#49-ieee-9-bus-topology)
   - [Load Flow](#410-load-flow)
   - [FACTS Devices](#411-facts-devices)
   - [EV / V2G](#412-ev--v2g)
   - [Targets (Performance)](#413-targets-performance)
   - [Cyber Attacks](#414-cyber-attacks)
   - [Test Systems (Scaling)](#415-test-systems-scaling)
   - [Timeline](#416-timeline)
5. [ML Engine — 6 Models](#5-ml-engine--6-models)
6. [REST API Reference](#6-rest-api-reference)
7. [Interactive Features](#7-interactive-features)
8. [Source Files Explained](#8-source-files-explained)

---

## 1. Project Overview

The **CAPSM (Cognitive-Adaptive Power System Management)** dashboard is a PhD thesis proposal visualisation tool. It presents a research framework that proposes combining **dual-process AI** (inspired by Kahneman's System-1/System-2 cognitive model) with **physics-informed machine learning** to manage modern power grids in real time.

### Central Thesis Hypothesis

> _"A dual-process, metacognitively guided, physics-informed control architecture — inspired by human cognitive science — can simultaneously achieve sub-5ms fault response, near-optimal economic dispatch, >99.8% constraint compliance, and cyber-attack resilience in modern power grids with high renewable/EV penetration."_

### The 5 Research Gaps Being Addressed

| ID | Gap | Addressed By |
|----|-----|-------------|
| G1 | Latency vs. Accuracy Trade-off | System-1 CNN-LSTM fast inference |
| G2 | Quantum-Classical RL Integration | System-2 QIRL algorithm |
| G3 | Safety Guarantee Absence | PINN physics-based constraints |
| G4 | Multi-Agent Coordination | HIRL hierarchical architecture |
| G5 | Cyber-Attack Resilience | Anomaly detection + robust control |

---

## 2. How to Run the Dashboard

### Option A — Flask Static Server (Recommended)

This serves the `index.html` static frontend with a REST API backend.

```bash
# 1. Activate the virtual environment
source "/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/.venv/bin/activate"

# 2. Navigate to the dashboard folder
cd "/Users/admin/Library/CloudStorage/OneDrive-DalhousieUniversity/Google Drive/PhD/Lab2Market/PhD thesis/dashboard"

# 3. Start the server
python server.py

# 4. Open in browser
open http://localhost:5050
```

### Option B — Plotly/Dash App (Interactive Python)

This runs a fully Python-driven Plotly Dash application with live chart re-renders.

```bash
# Requirements (in addition to flask): dash, plotly, dash-bootstrap-components
pip install dash plotly dash-bootstrap-components

python dash_app.py

# Open in browser — Dash uses port 8050 by default, or 5050 if configured
open http://localhost:8050
```

### Stopping the Server

```bash
# Find and kill the process using port 5050
lsof -ti:5050 | xargs kill -9
```

---

## 3. File Structure

```
dashboard/
├── server.py           ← Flask backend (API + static file serving)
├── dash_app.py         ← Alternative: full Plotly/Dash Python app
├── ml_engine.py        ← CAPSMMLEngine — 6 sklearn ML models
├── index.html          ← Static HTML/JS frontend (2225 lines)
├── css/
│   └── dashboard.css   ← Dark-theme stylesheet
├── js/                 ← Chart.js charts, page routing, interactivity
└── assets/             ← Images, logos, diagrams
```

---

## 4. All 16 Pages — Detailed Explanation

The sidebar organises pages into **4 sections**: Overview, Framework, Power System, Validation.

---

### 4.1 Overview (Dashboard)

**What it shows:** The top-level KPI summary and live system status.

**KPI Cards (6 metrics):**

| Metric | Target | Component |
|--------|--------|-----------|
| S1 Response Time | < 5 ms | System-1 CNN-LSTM |
| S2 Dispatch Time | < 50 ms | System-2 QIRL |
| PINN Compliance | 99.8% | Physics constraints |
| Fault Classification | 96.8% | ML fault classifier |
| QIRL Improvement | 2× vs. DQN | Quantum RL algorithm |
| Test Grid | IEEE 9-Bus | Power system |

**Charts:**
- **Bus Voltage Profile** — real-time bar chart showing p.u. voltages for all 9 buses (with ±5% limits)
- **Generator Dispatch** — bar chart for G1/G2/G3 active power output
- **Gap Coverage Radar** — radar chart showing how well G1–G5 research gaps are addressed

**ML Engine Status Table:**  
Shows all 6 ML model types, their accuracy/R², and training status (Trained / Ready).

---

### 4.2 Hypothesis

**What it shows:** The intellectual foundation — the central hypothesis and the 5 literature gaps.

**Central Hypothesis Block:**  
Displays the full hypothesis as a styled quote (as listed in Section 1 above).

**5 Research Gap Cards (G1–G5):**  
Each card shows:
- Gap ID (e.g., G1)
- Short title (e.g., "Latency vs. Accuracy Trade-off")
- 1–2 sentence description of what is missing in current literature
- "Addressed by" field naming which CAPSM component solves it

**Purpose:** Justifies why the CAPSM framework is needed and what specific holes in existing research it fills.

---

### 4.3 Architecture

**What it shows:** The overall CAPSM system design as a formal architecture diagram.

**Architecture Layers (top to bottom):**

```
PMU Sensor Grid (IEEE 9-Bus)
         ↓
  Metacognition Layer
  (Confidence Cₜ / Novelty Nₜ / Urgency Uₜ)
      ↙           ↘
System-1          System-2
CNN-LSTM          QIRL
(fast, reactive)  (slow, deliberate)
      ↘           ↙
  PINN Safety Layer
  (AC Power Flow Constraints)
         ↓
  Grid Control Actions
```

**Tables & Diagrams:**
- SVG architecture diagram showing data flow
- Kahneman dual-process theory comparison (S1 = intuition, fast; S2 = reasoning, slow)
- Information flow equations

**Key Insight:** The cognitive science analogy — human intuitive reactions (S1) vs. deliberate thinking (S2) — is the philosophical core of CAPSM.

---

### 4.4 System-1 CNN-LSTM

**What it shows:** The fast-path fault detection and classification neural network.

**Network Architecture:**
```
Input: 9 buses × 6 features × 30 timesteps  →  [9, 6, 30] tensor
  Conv1D (32 filters, kernel=3) + ReLU
  Conv1D (64 filters, kernel=3) + ReLU
  MaxPooling1D
  LSTM (128 hidden units)
  Dense(64) + Dense(5)  →  fault class output
```

**6 Input Features per Bus:** Voltage magnitude, Voltage angle, Active power P, Reactive power Q, Frequency deviation, Rate of change of frequency (RoCoF)

**5 Fault Types:**
| Class | Description |
|-------|-------------|
| 0 | Normal operation |
| 1 | Single-phase to ground |
| 2 | Three-phase fault |
| 3 | Line overload |
| 4 | Generator trip |

**Performance Displays:**
- Gauge visualization: **96.8% accuracy**, **5 ms inference time**
- Feature importance bar chart (SHAP-style)
- Confusion matrix heatmap

**ML Models Used:** Random Forest + MLP Classifier (`fault_rf`, `fault_mlp` from `ml_engine.py`)

---

### 4.5 System-2 QIRL

**What it shows:** The slow-path optimal dispatch algorithm using Quantum-Inspired Reinforcement Learning.

**Key Equations Displayed:**

Quantum state policy (complex amplitude superposition):
$$\psi = \sum_i \alpha_i |a_i\rangle$$

Action probability (Born rule):
$$P(a_i) = |\alpha_i|^2$$

Bellman update with quantum tunneling:
$$Q(s,a) \leftarrow Q(s,a) + \eta[r + \gamma \max_{a'} Q(s',a') - Q(s,a)] + \mathcal{T}(s,a)$$

**QIRL vs. Classical RL Convergence Chart:**  
Line chart comparing episode convergence speed:
- QIRL: ~200 episodes to convergence
- DQN: ~350 episodes
- PPO: ~280 episodes

**Control Tasks Table:**
| Task | Method | Time Budget |
|------|--------|------------|
| Economic dispatch | QIRL | < 50 ms |
| EV V2G scheduling | QIRL | < 50 ms |
| FACTS control | QIRL | < 50 ms |

**ML Used:** Convergence predictor (`convergence` GradientBoostingRegressor, R² ~ 0.9)

---

### 4.6 HIRL Framework

**What it shows:** A 3-level Hierarchical Multi-Agent RL (HIRL) architecture for coordinating control across large grids.

**3-Level Hierarchy:**
```
Level 3: Global Coordinator
  — Grid-wide economic objective (total cost minimisation)
  
Level 2: Regional Agents (per zone)
  — Zone-level voltage/frequency regulation
  — Federated learning using local data only
  
Level 1: Device Controllers
  — Individual generator, load, FACTS, EV control
```

**Federated Averaging Equation:**
$$w_{global} = \frac{1}{N}\sum_{i=1}^{N} w_i$$

Where each regional agent i contributes local model weights wᵢ without sharing raw grid data (privacy-preserving).

**4-Stage Training Pipeline:**
1. Pre-train on IEEE 9-bus simulation data
2. Fine-tune regional agents with local grid data
3. Federated averaging to update global coordinator
4. Evaluate and iterate

**HIRL vs. Baselines:**
| Method | Reward | Convergence | Scalability |
|--------|--------|------------|-------------|
| HIRL | Highest | Fastest | Full grid |
| Centralised DQN | Medium | Slow | Limited |
| Independent Q | Low | Diverges | Poor |

---

### 4.7 PINN Safety

**What it shows:** How Physics-Informed Neural Networks enforce hard physical constraints on every control action.

**Loss Function (3-term):**
$$\mathcal{L} = \mathcal{L}_{data} + \lambda_{pf} \cdot \mathcal{L}_{AC} + \lambda_{lim} \cdot \mathcal{L}_{constraints}$$

- **L_data** — fit error against PMU measurements
- **L_AC** — violation of AC power flow equations
- **L_constraints** — soft penalties for operational limit violations

**AC Power Flow Equations:**
$$P_i = \sum_{j} |V_i||V_j|(G_{ij}\cos\theta_{ij} + B_{ij}\sin\theta_{ij})$$
$$Q_i = \sum_{j} |V_i||V_j|(G_{ij}\sin\theta_{ij} - B_{ij}\cos\theta_{ij})$$

**Operational Limits Table:**
| Variable | Lower Bound | Upper Bound |
|----------|------------|------------|
| Bus voltage | 0.90 p.u. | 1.10 p.u. |
| Line current | 0 A | I_max |
| EV SoC | 0.20 | 0.95 |
| System frequency | 59.5 Hz | 60.5 Hz |

**Compliance Target:** 99.8% of timesteps within all constraints.

**ML Used:** Voltage stability predictor (`voltage` MLPRegressor from `ml_engine.py`)

---

### 4.8 Metacognition

**What it shows:** The "brain" of CAPSM — a meta-controller that monitors system state and decides which subsystem (S1 or S2) should be in control at each timestep.

**3 Real-Time Metrics:**

| Metric | Symbol | Formula | Meaning |
|--------|--------|---------|---------|
| Confidence | Cₜ | softmax entropy of S1 output | How certain is System-1? |
| Novelty | Nₜ | distance from training distribution | How unfamiliar is the situation? |
| Urgency | Uₜ | rate of change of key grid variables | How fast is the situation evolving? |

**Decision Rule:**
$$\alpha_t = \begin{cases} S1 & \text{if } C_t > \theta_C \text{ and } N_t < \theta_N \\ S2 & \text{otherwise} \end{cases}$$

In words: Use the fast S1 path when it's confident and the situation is familiar. Escalate to S2 when uncertain or novel.

**Mode Switching Chart:**  
Time-series plot showing Cₜ / Nₜ / Uₜ over time alongside mode switches between S1 and S2.

**ML Used:** Mode classifier (`mode` GradientBoostingClassifier) predicting S1/S2 label from [Cₜ, Nₜ, Uₜ] triples.

---

### 4.9 IEEE 9-Bus (Topology)

**What it shows:** The physical power network used as the primary test case.

**Network Parameters:**
| Element | Count | Details |
|---------|-------|---------|
| Buses | 9 | Voltage nodes |
| Generators | 3 | Slack (Bus 1), PV (Bus 2, Bus 3) |
| Loads | 3 | Bus 5 (125 MW), Bus 6 (90 MW), Bus 8 (100 MW) |
| Transmission lines | 6 | With R, X, B parameters in p.u. |
| Transformers | 3 | Step-up transformers at each generator |

**Base Case:**
- Base MVA: 100 MVA
- Base voltage: 230 kV
- Frequency: 60 Hz

**Line Parameters (selected):**

| Line | From | To | R (p.u.) | X (p.u.) |
|------|------|----|----------|----------|
| L1 | Bus 4 | Bus 5 | 0.0100 | 0.0850 |
| L2 | Bus 4 | Bus 6 | 0.0170 | 0.0920 |
| L3 | Bus 5 | Bus 7 | 0.0320 | 0.1610 |
| L4 | Bus 6 | Bus 9 | 0.0390 | 0.1700 |
| L5 | Bus 7 | Bus 8 | 0.0085 | 0.0720 |
| L6 | Bus 8 | Bus 9 | 0.0119 | 0.1008 |

---

### 4.10 Load Flow

**What it shows:** Steady-state power flow solution for the 9-bus system.

**Bus Voltage Magnitude Chart:**  
Bar chart showing V_pu for all 9 buses — target is all within 0.95–1.05 p.u.

**Voltage Angle Chart:**  
Bar chart showing δ in degrees (Bus 1 = 0° reference, slack bus).

**Full Load Flow Results Table (9 rows):**
| Bus | V (p.u.) | δ (deg) | P_gen (MW) | Q_gen (MVAR) | P_load (MW) | Q_load (MVAR) |
|-----|----------|---------|-----------|-------------|------------|--------------|
| 1 (Slack) | 1.040 | 0.000 | 71.6 | 27.0 | 0 | 0 |
| 2 (PV) | 1.025 | 9.280 | 163.0 | 6.7 | 0 | 0 |
| 3 (PV) | 1.025 | 4.665 | 85.0 | -10.9 | 0 | 0 |
| 4–9 | varies | varies | 0 | 0 | varies | varies |

---

### 4.11 FACTS Devices

**What it shows:** Flexible AC Transmission System (FACTS) devices added to the 9-bus system for reactive power and voltage control.

**SVC (Static VAR Compensator) — Bus 5:**
| Parameter | Value |
|-----------|-------|
| Location | Bus 5 |
| Reactive range | ±100 MVAR |
| Droop setting | 0.03 |
| Voltage reference | 1.00 p.u. |
| Response time | 10 ms |
| Control mode | Voltage droop |

**STATCOM (Static Synchronous Compensator) — Bus 8:**
| Parameter | Value |
|-----------|-------|
| Location | Bus 8 |
| Reactive range | ±50 MVAR |
| Voltage reference | 1.00 p.u. |
| Response time | 5 ms |
| Control mode | Direct voltage control |

**Why FACTS?**  
Both devices are controlled by System-2 QIRL in real time, providing sub-cycle reactive compensation that classical controllers cannot achieve.

---

### 4.12 EV / V2G

**What it shows:** The EV fleet integration model and Vehicle-to-Grid (V2G) scheduling.

**Fleet Parameters:**
| Parameter | Value |
|-----------|-------|
| Fleet size | 1,000 EVs |
| Grid connection | Bus 8 |
| Total power capacity | 50 MW |
| Total energy capacity | 150 MWh |
| SoC lower bound | 0.20 (20%) |
| SoC upper bound | 0.95 (95%) |
| Scheduling algorithm | System-2 QIRL |
| Charging efficiency | 95% |
| Discharging efficiency | 93% |

**V2G Operation:**  
EVs can inject power back into the grid (V2G mode) during peak demand or grid faults, acting as a distributed storage bank controlled by QIRL.

**SoC Trajectory Chart:**  
Time-series showing fleet average SoC over 24 hours, with upper/lower safety limits as horizontal dashed lines.

**ML Used:** EV SoC Forecaster (`soc` GradientBoostingRegressor)

---

### 4.13 Targets (Performance)

**What it shows:** How CAPSM compares to baseline methods across 5 key performance metrics.

**Comparison Chart (Grouped Bar Chart):**  
4 controllers × 5 metrics:

| Metric | CAPSM | DQN | PPO | PID |
|--------|-------|-----|-----|-----|
| Fault response time | 5 ms | 45 ms | 38 ms | 120 ms |
| Constraint compliance | 99.8% | 94.1% | 95.3% | 98.2% |
| Economic efficiency | 97.5% | 91.0% | 92.4% | 78.0% |
| Cyber resilience | 96.2% | 61.0% | 58.0% | 22.0% |
| QIRL convergence improvement | 2.1× | 1.0× | 1.2× | N/A |

**Key Message:** CAPSM dominates on fault response (12× faster than PID), cyber resilience (4× better than PPO), and QIRL convergence speed.

---

### 4.14 Cyber Attacks

**What it shows:** How the CAPSM anomaly detection layer identifies and mitigates three types of cyber attacks.

**3 Attack Scenarios:**

| Scenario | Attack Type | Time Window | Target | Effect |
|----------|------------|------------|--------|--------|
| FDI | False Data Injection | t = 2–5 s | Bus 5 PMU | Adds Gaussian noise to measurements |
| DoS | Denial of Service | t = 8–8.5 s | All PMUs | Zeroes out all measurements (blackout) |
| Delay | Communication Delay | t = 12–20 s | All PMUs | 1.5 s measurement delay |

**Anomaly Score Box Plots:**  
Box plots comparing anomaly scores from the Isolation Forest detector across:
- Normal operation (low score)
- FDI attack (elevated score)
- DoS attack (highest score)

**Detection Performance:**  
The Isolation Forest (`anomaly` model in `ml_engine.py`) is trained to distinguish normal, FDI, and DoS patterns.

**Mitigation Strategy:**  
Under detected attacks, the Metacognition layer increases Nₜ (novelty) and Uₜ (urgency), forcing a switch to System-2 QIRL and activating backup state estimation from healthy PMUs.

---

### 4.15 Test Systems (Scaling)

**What it shows:** How CAPSM scales from the 9-bus test case to realistic large grids.

**4 Test Systems:**

| System | Buses | Status | Purpose |
|--------|-------|--------|---------|
| IEEE 9-Bus | 9 | ✅ Built | Development & validation |
| IEEE 39-Bus | 39 | 🔄 Planned | Regional grid |
| IEEE 118-Bus | 118 | 🔄 Planned | Transmission network |
| IEEE 300-Bus | 300 | 🔄 Planned | Large-scale realism test |

**Scatter Plot:**  
Shows bus count vs. computational time, the framework's scalability curve.

**Scaling Strategy:**  
The HIRL hierarchy is designed to scale: local agents handle device-level control, regional agents handle zone-level, and global coordinator handles grid-wide optimisation — avoiding exponential state-space growth.

---

### 4.16 Timeline

**What it shows:** The PhD research plan broken into 5 Research Objectives with deliverables and months.

**5 Research Objectives:**

| RO | Title | Months | Deliverable |
|----|-------|--------|-------------|
| RO1 | System-1 CNN-LSTM Design & IEEE 9-Bus Integration | 1–8 | Fault classification system, ≥95% accuracy |
| RO2 | System-2 QIRL Algorithm Development | 5–16 | QIRL algorithm, 2× convergence improvement |
| RO3 | PINN Safety Layer Integration | 9–20 | Physics-constrained controller, 99.8% compliance |
| RO4 | HIRL Multi-Agent Framework | 13–28 | Hierarchical coordination across 39/118 buses |
| RO5 | Metacognition + Full System Validation | 24–36 | Complete CAPSM system, journal submission |

**Layout:**  
Gantt-style display showing overlapping research phases, emphasising that RO phases build on each other with deliberate overlap for parallelism.

---

## 5. ML Engine — 6 Models

All models live in `ml_engine.py` inside the `CAPSMMLEngine` class. They are **trained at startup** on synthetic IEEE 9-bus data.

| # | Attribute | Algorithm | Input Features | Output | Accuracy |
|---|-----------|-----------|---------------|--------|----------|
| 1 | `fault_rf` | Random Forest (n=100) | [V, δ, P, Q, f, df/dt] × 9 buses | Fault class (0–4) | ~96–97% |
| 2 | `fault_mlp` | MLP Classifier (128,64) | Same as above | Fault class (0–4) | ~96% |
| 3 | `anomaly` | Isolation Forest | PMU reading arrays | normal / FDI / DoS | Unsupervised |
| 4 | `convergence` | Gradient Boosting Regressor | RL episode features | Convergence episodes | R² ~ 0.90 |
| 5 | `mode` | Gradient Boosting Classifier | [Cₜ, Nₜ, Uₜ] | S1 / S2 mode | ~92–95% |
| 6 | `voltage` | MLP Regressor (64,32) | Bus admittance + injection | Voltage stability metric | R² ~ 0.88 |
| 7 | `soc` | Gradient Boosting Regressor | [hour, demand, V2G flag, SoC_prev] | SoC at next step | R² ~ 0.92 |

### Key Simulation Methods

- **`simulate_qirl(n_episodes)`** — Generates synthetic QIRL convergence data comparing QIRL vs DQN vs PPO
- **`simulate_metacognition(n_steps)`** — Generates confidence/novelty/urgency time series with mode-switching events
- **`simulate_hirl(n_agents, n_steps)`** — Generates regional agent reward and loss trajectories
- **`simulate_ev_soc(n_steps)`** — Generates 24-hour EV SoC trajectory with V2G events

---

## 6. REST API Reference

Base URL: `http://localhost:5050`

### Data Endpoints

| Method | Endpoint | Returns |
|--------|----------|---------|
| GET | `/` | `index.html` static site |
| GET | `/api/proposal` | Full PhD proposal as structured JSON |
| GET | `/api/overview` | Title, author, hypothesis, key counts |
| GET | `/api/gaps` | Array of 5 research gap objects |
| GET | `/api/objectives` | Array of 5 research objectives |
| GET | `/api/architecture` | S1, S2, metacognition, PINN sub-details |
| GET | `/api/ieee9bus` | Buses, generators, loads, lines, transformers, load flow |
| GET | `/api/performance` | 6 KPI targets and values |
| GET | `/api/facts` | SVC + STATCOM parameters |
| GET | `/api/ev` | EV fleet parameters |
| GET | `/api/cyber` | 3 attack scenario definitions |
| GET | `/api/test_systems` | 4 test system rows with status |
| GET | `/api/simulation` | Current simulation state |
| GET | `/api/hirl` | HIRL hierarchy, equations, pipeline |

### Live Simulation Endpoints (Real-Time Data)

| Method | Endpoint | Returns |
|--------|----------|---------|
| GET | `/api/live/bus_voltages` | 9 bus voltages with sinusoidal noise |
| GET | `/api/live/frequency` | System frequency (60 ± 0.02 Hz) |
| GET | `/api/live/ev_soc` | EV fleet SoC trajectory |
| GET | `/api/live/capsm_mode` | Confidence, novelty, urgency + mode (S1/S2) |
| GET | `/api/live/hirl` | Regional agent reward/loss per step |

### Configuration Endpoints

| Method | Endpoint | Body | Returns |
|--------|----------|------|---------|
| POST | `/api/config` | JSON config object | `{"status": "saved"}` |
| GET | `/api/config` | — | Last saved config JSON |

### Example: Fetch Overview

```bash
curl -s http://localhost:5050/api/overview | python3 -m json.tool
```

### Example: Live Bus Voltages

```bash
watch -n 1 'curl -s http://localhost:5050/api/live/bus_voltages'
```

---

## 7. Interactive Features

### Edit Mode (Inline Parameter Editor)
- Each page has a **Edit Mode** toggle button (top-right of page area)
- Activating Edit Mode reveals a sidebar panel with all tunable parameters for that page
- Parameters include: thresholds (θ_C, θ_N, θ_U), KPI targets, fault thresholds, SoC limits, FACTS references
- Changes are reflected live in charts (on save)
- Settings persist across reloads via **browser `localStorage`**

### Theme Toggle
- Light / Dark mode toggle in the header
- Dark is default (research presentation optimised)

### Export Config Button
- Exports current page configuration as a JSON file download
- Useful for saving research parameter snapshots

### Live Indicator
- Green pulsing indicator in the header shows real-time data is being polled
- Live endpoints are called every 2 seconds via JavaScript intervals

### Sidebar Navigation
- Click any page name to switch views without page reload (single-page app behaviour)
- Current page is highlighted in the sidebar
- Section headers are collapsible

---

## 8. Source Files Explained

### `server.py` (545 lines)
The Flask web server. Responsibilities:
- Serve `index.html` as the root page
- Serve static assets (`/css/`, `/js/`, `/assets/`)
- Define all REST API routes using Flask `@app.route` decorators
- Store the complete `PROPOSAL_DATA` dictionary (the entire PhD proposal in JSON form)
- Implement live simulation endpoints (sinusoidal noise generation in Python)
- Handle configuration save/load (in-memory dict, not persisted to disk on restart)

Start command: `python server.py`  
Port: **5050**

---

### `dash_app.py` (1170 lines)
An alternative Plotly Dash Python application. Responsibilities:
- Defines `DEFAULT_CONFIG` — all tunable parameters in a Python dict
- Instantiates `CAPSMMLEngine` at startup to get real ML model results
- Contains 16 `page_*()` functions — each returns a Plotly Dash layout for that page
- Uses Dash `@app.callback` decorators to wire editor inputs to live chart re-renders
- `editor_panel()` function creates per-page parameter editors

The key difference from `index.html`: this version uses **real ML predictions** (from `ml_engine.py`) rather than hardcoded JSON data.

Start command: `python dash_app.py`  
Port: **8050** (Dash default) or **5050** if overridden

---

### `ml_engine.py` (293 lines)
The **CAPSMMLEngine** class. Responsibilities:
- At `__init__`: trains all 6 ML models on synthetic IEEE 9-bus data (takes ~2s)
- `_generate_fault_data()` — creates labelled synthetic PMU samples for 5 fault classes
- `_train_models()` — trains RF, MLP, IsolationForest, GB Regressor/Classifier, MLPRegressor
- `get_ml_results()` — returns accuracy/R² dict for all models (used in Overview page)
- `simulate_qirl()`, `simulate_metacognition()`, `simulate_hirl()`, `simulate_ev_soc()` — deterministic-with-noise simulation functions

Dependencies: `scikit-learn`, `numpy`, `pandas`

---

### `index.html` (2225 lines)
The static HTML frontend. Responsibilities:
- Defines the entire UI in a single file (no build step needed)
- Sidebar navigation using `<nav>` with JavaScript `showPage()` function
- Each page is a `<div id="page-*">` hidden/shown by JavaScript
- Uses **Chart.js** for all charts (canvas elements)
- Fetches data from the Flask API on page load
- Edit mode, theme toggle, export config — all implemented in embedded `<script>` tags
- Inline CSS styles supplemented by `css/dashboard.css`

No React, no Node.js, no build pipeline — just HTML + vanilla JavaScript + Chart.js.

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Start server | `python server.py` |
| Open dashboard | `open http://localhost:5050` |
| Stop server | `lsof -ti:5050 \| xargs kill -9` |
| View server logs | `cat /tmp/capsm.log` |
| Fetch all proposal data | `curl http://localhost:5050/api/proposal` |
| Live bus voltages | `curl http://localhost:5050/api/live/bus_voltages` |
| Run ML version | `python dash_app.py` |

---

*Dashboard Guide — CAPSM PhD Proposal — Mahmoud Kiasari — Dalhousie University*
