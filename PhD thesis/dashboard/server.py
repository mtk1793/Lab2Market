"""
CAPSM PhD Proposal Dashboard — Full-Stack Backend
Author: Mahmoud Kiasari, PhD Candidate, Dalhousie University
Date: February 2026

Flask server providing:
  - Static file serving for the dashboard frontend
  - REST API endpoints for proposal data
  - Real-time simulation data stubs (for future Simulink integration)

Usage:
  cd "PhD thesis/dashboard"
  pip install flask flask-cors
  python server.py
  → Open http://localhost:5050
"""

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import json
import os
import math
import random
from datetime import datetime

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

# ─────────────────────────────────────────────────────────────
# DATA: Complete PhD Proposal Content (structured)
# ─────────────────────────────────────────────────────────────

PROPOSAL_DATA = {
    "title": "CAPSM: Cognitive Adaptive Power System Management",
    "subtitle": "A Dual-Process Metacognitive Framework for Resilient Power Grid Control",
    "author": "Mahmoud Kiasari",
    "affiliation": "Dalhousie University, Department of Electrical & Computer Engineering",
    "degree": "PhD Candidate",
    "year": 2026,
    "supervisor": "PhD Oral Examination Proposal",

    # ── Research Gaps ──
    "research_gaps": [
        {
            "id": "G1",
            "title": "Single-Speed Control Paradigm",
            "description": "Existing AI controllers operate at a single temporal resolution — either fast reflex OR slow optimization — but never both integrated. No architecture combines sub-5 ms fault response with multi-minute economic optimization in a unified cognitive framework.",
            "addressed_by": "Dual-process System-1 / System-2 architecture with metacognitive arbitration"
        },
        {
            "id": "G2",
            "title": "Sample Inefficiency of Deep RL in Power Systems",
            "description": "Standard DQN/PPO require millions of episodes to converge in high-dimensional grid environments. Convergence is too slow for real-time adaptation during cascading failures or topology changes.",
            "addressed_by": "Quantum-Inspired Reinforcement Learning (QIRL) with superposition-based exploration and tunneling"
        },
        {
            "id": "G3",
            "title": "Physics-Blind Neural Controllers",
            "description": "Most neural network controllers ignore fundamental power system physics (Kirchhoff's laws, AC power flow equations). This leads to unsafe control actions that violate voltage, current, and thermal limits.",
            "addressed_by": "Physics-Informed Neural Network (PINN) safety layer enforcing AC power flow constraints"
        },
        {
            "id": "G4",
            "title": "Scalability of Multi-Agent Coordination",
            "description": "Centralized RL does not scale beyond small test systems. Distributed approaches lack coordination, leading to oscillatory or conflicting control actions across regions.",
            "addressed_by": "Hierarchical Multi-Agent RL (HMARL) with regional agents and global coordinator"
        },
        {
            "id": "G5",
            "title": "Cyber-Physical Resilience Under Attack",
            "description": "Power grid control systems are increasingly vulnerable to cyber attacks (FDI, DoS, man-in-the-middle). Existing controllers have no integrated mechanism to detect and recover from coordinated cyber-physical attacks.",
            "addressed_by": "Metacognitive anomaly detection + CAPSM's dual-process fallback architecture"
        }
    ],

    # ── Central Hypothesis ──
    "central_hypothesis": "A dual-process, metacognitively guided, physics-informed control architecture — inspired by human cognitive science — can simultaneously achieve sub-5ms fault response, near-optimal economic dispatch, >99.8% constraint compliance, and cyber-attack resilience in modern power grids with high renewable/EV penetration.",

    # ── Research Objectives ──
    "research_objectives": [
        {
            "id": "RO1",
            "title": "Cognitive Control Model",
            "description": "Design and formalize a dual-process cognitive control model (System-1 reflexive + System-2 deliberative) with metacognitive arbitration for power system management.",
            "deliverable": "Mathematical framework, arbitration equations, mode-switching criteria",
            "timeline": "Months 1-6"
        },
        {
            "id": "RO2",
            "title": "QIRL Algorithms",
            "description": "Develop Quantum-Inspired Reinforcement Learning algorithms that achieve ≥2× faster convergence than DQN while maintaining stability in high-dimensional grid state spaces.",
            "deliverable": "QIRL policy with complex-valued amplitudes, tunneling operator, convergence proofs",
            "timeline": "Months 3-12"
        },
        {
            "id": "RO3",
            "title": "PINNs for Safety Enforcement",
            "description": "Integrate Physics-Informed Neural Networks as a real-time safety layer that enforces AC power flow equations (Kirchhoff's laws) and operational constraints with >99.8% compliance.",
            "deliverable": "PINN architecture, loss functions, real-time inference pipeline",
            "timeline": "Months 6-15"
        },
        {
            "id": "RO4",
            "title": "Multimodal Fusion + HMARL",
            "description": "Combine multimodal sensor fusion (PMU, SCADA, weather, market) with Hierarchical Multi-Agent RL for scalable control across 118+ bus systems.",
            "deliverable": "HMARL training framework, regional agent design, coordination protocol",
            "timeline": "Months 12-24"
        },
        {
            "id": "RO5",
            "title": "IEEE Test System Validation",
            "description": "Validate the complete CAPSM framework on IEEE 9-, 39-, 118-, and 300-bus test systems under fault, cyber-attack, and high-DER scenarios.",
            "deliverable": "Comprehensive simulation results, comparison with state-of-the-art controllers",
            "timeline": "Months 18-30"
        }
    ],

    # ── CAPSM Architecture Layers ──
    "architecture": {
        "system1": {
            "name": "System-1: Reflexive Controller",
            "model": "CNN-LSTM Neural Network",
            "response_time": "<5 ms",
            "function": "Fast fault detection, voltage dip response, protective relay coordination",
            "input": "PMU measurements (V, I, θ, f) at 30-120 Hz from all buses",
            "output": "Reactive power injection commands to FACTS devices",
            "equations": [
                "z(t) = LSTM(CNN(X_t))",
                "u_fast = f_θ(z(t))",
                "X_t ∈ ℝ^{N_bus × 6 × T_window}"
            ],
            "training": "Supervised pre-training on historical fault data, then online fine-tuning",
            "target_accuracy": "≥96.8% fault detection"
        },
        "system2": {
            "name": "System-2: Deliberative Optimizer",
            "model": "Quantum-Inspired Reinforcement Learning (QIRL)",
            "response_time": "<50 ms",
            "function": "Economic dispatch, VAR optimization, EV/V2G scheduling, cyber recovery",
            "input": "Grid state estimates, market prices, renewable forecasts, EV SoC",
            "output": "Generator dispatch, EV charging schedules, FACTS setpoints",
            "equations": [
                "ψ = Σᵢ αᵢ|aᵢ⟩  (complex-valued policy amplitudes)",
                "P(aᵢ|s) = |αᵢ|²  (Born rule probability)",
                "Q(s,a) ← Q(s,a) + lr·(r + γ·max Q(s',a') - Q(s,a))",
                "αᵢ ← αᵢ - lr·∇L + β·T(αᵢ)  (tunneling operator)"
            ],
            "target_speedup": "≥2× faster convergence vs DQN"
        },
        "metacognition": {
            "name": "Metacognitive Arbitration",
            "function": "Dynamically switches between System-1 and System-2 based on situation assessment",
            "metrics": [
                {"symbol": "Cₜ", "name": "Confidence", "formula": "1 - Var(Q-values) / Var_max", "threshold": "τ_c = 0.7"},
                {"symbol": "Nₜ", "name": "Novelty", "formula": "‖s - μ_buffer‖ / σ_buffer", "threshold": "τ_n = 2.0σ"},
                {"symbol": "Uₜ", "name": "Urgency", "formula": "max(|ΔV/Δt|, |Δf/Δt|) / threshold", "threshold": "τ_u = 0.3"}
            ],
            "decision_rule": "α_t = 1 (System-1) if C_t > τ_c AND U_t > τ_u; else α_t = 0 (System-2)"
        },
        "pinn": {
            "name": "PINN Safety Layer",
            "function": "Physics-informed constraint enforcement on all control actions",
            "constraints": [
                "AC Power Flow: P_i = V_i Σ V_j(G_ij cos θ_ij + B_ij sin θ_ij)",
                "Q_i = V_i Σ V_j(G_ij sin θ_ij - B_ij cos θ_ij)",
                "Voltage limits: 0.90 ≤ V ≤ 1.10 pu",
                "Current thermal: I ≤ I_max per line rating",
                "SoC bounds: 0.20 ≤ SoC ≤ 0.95"
            ],
            "loss_function": "L = L_data + λ_pf·L_AC + λ_lim·L_constraints",
            "target_compliance": ">99.8%"
        }
    },

    # ── IEEE 9-Bus System Parameters ──
    "ieee9bus": {
        "base": {"S": "100 MVA", "V": "230 kV", "f": "60 Hz"},
        "buses": 9,
        "generators": [
            {"bus": 1, "V_kV": 16.5, "V_pu": 1.040, "angle_deg": 0.0, "P_MW": 71.64, "Q_MVAR": 27.05, "type": "Slack"},
            {"bus": 2, "V_kV": 18.0, "V_pu": 1.025, "angle_deg": 9.28, "P_MW": 163.0, "Q_MVAR": 6.65, "type": "PV"},
            {"bus": 3, "V_kV": 13.8, "V_pu": 1.025, "angle_deg": 4.665, "P_MW": 85.0, "Q_MVAR": -10.86, "type": "PV"}
        ],
        "loads": [
            {"bus": 5, "P_MW": 125, "Q_MVAR": 50},
            {"bus": 6, "P_MW": 90, "Q_MVAR": 30},
            {"bus": 8, "P_MW": 100, "Q_MVAR": 35}
        ],
        "lines": [
            {"from": 4, "to": 5, "R_pu": 0.010, "X_pu": 0.085, "B_pu": 0.176},
            {"from": 4, "to": 6, "R_pu": 0.017, "X_pu": 0.092, "B_pu": 0.158},
            {"from": 5, "to": 7, "R_pu": 0.032, "X_pu": 0.161, "B_pu": 0.306},
            {"from": 6, "to": 9, "R_pu": 0.039, "X_pu": 0.170, "B_pu": 0.358},
            {"from": 7, "to": 8, "R_pu": 0.0085, "X_pu": 0.072, "B_pu": 0.149},
            {"from": 8, "to": 9, "R_pu": 0.0119, "X_pu": 0.1008, "B_pu": 0.209}
        ],
        "transformers": [
            {"name": "T1", "from_bus": 1, "to_bus": 4, "S_MVA": 247.5, "V1_kV": 16.5, "V2_kV": 230, "X_pu": 0.0576},
            {"name": "T2", "from_bus": 2, "to_bus": 7, "S_MVA": 192.0, "V1_kV": 18.0, "V2_kV": 230, "X_pu": 0.0625},
            {"name": "T3", "from_bus": 3, "to_bus": 9, "S_MVA": 128.0, "V1_kV": 13.8, "V2_kV": 230, "X_pu": 0.0586}
        ],
        "load_flow": [
            {"bus": 1, "V_pu": 1.040, "angle": 0.0, "Pgen": 71.64, "Qgen": 27.05, "Pload": 0, "Qload": 0},
            {"bus": 2, "V_pu": 1.025, "angle": 9.28, "Pgen": 163.0, "Qgen": 6.65, "Pload": 0, "Qload": 0},
            {"bus": 3, "V_pu": 1.025, "angle": 4.665, "Pgen": 85.0, "Qgen": -10.86, "Pload": 0, "Qload": 0},
            {"bus": 4, "V_pu": 1.026, "angle": -2.217, "Pgen": 0, "Qgen": 0, "Pload": 0, "Qload": 0},
            {"bus": 5, "V_pu": 0.996, "angle": -3.989, "Pgen": 0, "Qgen": 0, "Pload": 125, "Qload": 50},
            {"bus": 6, "V_pu": 1.013, "angle": -3.688, "Pgen": 0, "Qgen": 0, "Pload": 90, "Qload": 30},
            {"bus": 7, "V_pu": 1.026, "angle": 3.72, "Pgen": 0, "Qgen": 0, "Pload": 0, "Qload": 0},
            {"bus": 8, "V_pu": 1.016, "angle": 0.728, "Pgen": 0, "Qgen": 0, "Pload": 100, "Qload": 35},
            {"bus": 9, "V_pu": 1.032, "angle": 1.967, "Pgen": 0, "Qgen": 0, "Pload": 0, "Qload": 0}
        ]
    },

    # ── FACTS Devices ──
    "facts_devices": [
        {
            "type": "SVC",
            "name": "SVC (Phasor Type)",
            "bus": 5,
            "rating": "±100 MVAR",
            "function": "Voltage regulation, reactive power support",
            "Vref": 1.0,
            "droop": 0.03,
            "controlled_by": "System-1 (fast) / System-2 (optimization)"
        },
        {
            "type": "STATCOM",
            "name": "STATCOM (Phasor Type)",
            "bus": 8,
            "rating": "±50 MVAR",
            "function": "Fast reactive compensation, power quality",
            "Vref": 1.0,
            "droop": 0.02,
            "response_time": "5 ms",
            "controlled_by": "System-1 reflex actions (matches <5 ms target)"
        }
    ],

    # ── EV/V2G System ──
    "ev_v2g": {
        "bus": 8,
        "fleet_size": 1000,
        "unit_capacity_kW": 50,
        "total_capacity_MW": 50,
        "energy_capacity_MWh": 150,
        "efficiency": 0.95,
        "initial_soc": 0.70,
        "soc_bounds": [0.20, 0.95],
        "controlled_by": "System-2 QIRL (economic optimization)"
    },

    # ── Performance Targets ──
    "performance_targets": [
        {"metric": "System-1 Response Time", "target": "<5 ms", "unit": "ms", "value": 5, "icon": "⚡"},
        {"metric": "System-2 Decision Cycle", "target": "<50 ms", "unit": "ms", "value": 50, "icon": "🧠"},
        {"metric": "Constraint Violations", "target": "<0.2%", "unit": "%", "value": 0.2, "icon": "🛡️"},
        {"metric": "Fault Detection Accuracy", "target": "≥96.8%", "unit": "%", "value": 96.8, "icon": "🎯"},
        {"metric": "QIRL Speedup vs DQN", "target": "≥2×", "unit": "×", "value": 2.0, "icon": "🚀"},
        {"metric": "PINN Compliance", "target": ">99.8%", "unit": "%", "value": 99.8, "icon": "📐"}
    ],

    # ── Cyber-Attack Scenarios ──
    "cyber_attacks": [
        {"type": "FDI", "name": "False Data Injection", "timing": "t=2-5s", "description": "Gaussian noise injected on Bus 5 PMU data (SNR=20 dB)", "target": "PMU measurements"},
        {"type": "DoS", "name": "Denial of Service", "timing": "t=8-8.5s", "description": "All PMU signals zeroed out — complete communication blackout", "target": "Communication channels"},
        {"type": "Delay", "name": "Communication Delay", "timing": "t=12-20s", "description": "1.5s communication delay on control signals", "target": "Control loops"}
    ],

    # ── Test Systems Scaling ──
    "test_systems": [
        {"name": "IEEE 9-Bus", "buses": 9, "generators": 3, "lines": 6, "purpose": "Core validation, System-1/System-2 integration", "status": "Built"},
        {"name": "IEEE 39-Bus", "buses": 39, "generators": 10, "lines": 46, "purpose": "Gap 1 validation — dual-process scaling", "status": "Planned"},
        {"name": "IEEE 118-Bus", "buses": 118, "generators": 54, "lines": 186, "purpose": "Gap 4 — HMARL multi-agent coordination", "status": "Planned"},
        {"name": "IEEE 300-Bus", "buses": 300, "generators": 69, "lines": 411, "purpose": "Full-scale CAPSM stress testing", "status": "Planned"}
    ],

    # ── HIRL: Hierarchical Integrated Reinforcement Learning ──
    "hirl": {
        "name": "Hierarchical Integrated Reinforcement Learning (HIRL)",
        "purpose": "Unifies QIRL's quantum-inspired exploration with hierarchical multi-agent coordination (HMARL) into a single scalable RL framework that operates across multiple temporal and spatial resolutions.",
        "key_innovation": "HIRL bridges System-2's QIRL optimizer with the HMARL scalability layer, creating a two-tier hierarchy where regional agents use QIRL policies locally and a global coordinator merges strategies using federated policy aggregation.",
        "hierarchy": [
            {
                "level": "Global Coordinator",
                "function": "Aggregates regional QIRL policies via federated averaging, resolves inter-region power flow conflicts, and dispatches global objectives (full-system economic dispatch, frequency regulation)",
                "update_rate": "100-500 ms",
                "algorithm": "Federated QIRL with consensus constraint"
            },
            {
                "level": "Regional Agents",
                "function": "Each agent manages a zone (e.g., Bus 4-5-7 zone, Bus 6-8-9 zone). Executes local QIRL for VAR optimization, FACTS setpoints, and EV scheduling within its zone.",
                "update_rate": "<50 ms",
                "algorithm": "QIRL with local state observation + neighbor message passing"
            },
            {
                "level": "Device Controllers",
                "function": "Low-level actuator control (SVC droop, STATCOM response, EV charge/discharge rate). Fed by regional agent commands.",
                "update_rate": "<5 ms",
                "algorithm": "PI/PID with QIRL-tuned gains"
            }
        ],
        "training_pipeline": [
            {"stage": 1, "name": "Pre-training", "method": "Supervised learning on historical grid data + physics-guided curriculum", "duration": "~50k episodes"},
            {"stage": 2, "name": "Single-Agent QIRL", "method": "Train QIRL on IEEE 9-bus (single agent, full observability)", "duration": "~100k episodes"},
            {"stage": 3, "name": "Multi-Agent HIRL", "method": "Deploy regional agents on IEEE 39/118-bus with federated coordination", "duration": "~200k episodes"},
            {"stage": 4, "name": "Transfer + Fine-tune", "method": "Transfer learned policies to IEEE 300-bus, fine-tune with online learning", "duration": "~50k episodes"}
        ],
        "equations": [
            "π_global = FedAvg({π_region_k}) with consensus: |π_k - π_global| < ε",
            "Q_k(s_k, a_k) ← Q_k + lr·(r_k + γ·max Q_k(s_k', a_k') - Q_k + λ·msg_neighbors)",
            "msg_j→k = Σ_j w_jk · ∇Q_j(s_j, a_j)  (neighbor gradient sharing)",
            "π_region_k: ψ_k = Σᵢ α_ki|a_ki⟩  (local QIRL policy per region)",
            "Global objective: min Σ_k c_k(P_k) + μ·Σ_{(j,k)} |ΔP_tie_{jk}|"
        ],
        "performance_targets": [
            {"metric": "Regional Convergence", "target": "<50k episodes", "baseline": "~200k (DQN)"},
            {"metric": "Global Coordination Overhead", "target": "<15%", "baseline": "~40% (centralized)"},
            {"metric": "Scalability (buses)", "target": "300+", "baseline": "~50 (DQN)"},
            {"metric": "Tie-Line Violation Rate", "target": "<0.5%", "baseline": "~3% (independent)"}
        ],
        "integration_with_capsm": {
            "system1": "Device controllers receive fast reflex commands from System-1 CNN-LSTM when urgency is high",
            "system2": "Regional agents ARE the System-2 QIRL instances, operating in deliberative mode",
            "metacognition": "Global coordinator uses metacognitive confidence to decide centralized vs distributed mode",
            "pinn": "Each regional agent's output passes through local PINN safety check before actuation"
        }
    },

    # ── Simulation Parameters ──
    "simulation": {
        "mode": "Phasor",
        "stop_time": "20 s",
        "solver": "ode23tb",
        "max_step": "0.2 ms",
        "fault": "3-phase fault at Bus 5, t=1.0-1.083s (5 cycles)"
    }
}


# ─────────────────────────────────────────────────────────────
# ROUTES: Static Files
# ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory("css", filename)


@app.route("/js/<path:filename>")
def js(filename):
    return send_from_directory("js", filename)


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory("assets", filename)


# ─────────────────────────────────────────────────────────────
# API ROUTES: Proposal Data
# ─────────────────────────────────────────────────────────────

@app.route("/api/proposal")
def api_proposal():
    """Full proposal data."""
    return jsonify(PROPOSAL_DATA)


@app.route("/api/overview")
def api_overview():
    """High-level overview."""
    return jsonify({
        "title": PROPOSAL_DATA["title"],
        "subtitle": PROPOSAL_DATA["subtitle"],
        "author": PROPOSAL_DATA["author"],
        "affiliation": PROPOSAL_DATA["affiliation"],
        "central_hypothesis": PROPOSAL_DATA["central_hypothesis"],
        "num_gaps": len(PROPOSAL_DATA["research_gaps"]),
        "num_objectives": len(PROPOSAL_DATA["research_objectives"]),
    })


@app.route("/api/gaps")
def api_gaps():
    return jsonify(PROPOSAL_DATA["research_gaps"])


@app.route("/api/objectives")
def api_objectives():
    return jsonify(PROPOSAL_DATA["research_objectives"])


@app.route("/api/architecture")
def api_architecture():
    return jsonify(PROPOSAL_DATA["architecture"])


@app.route("/api/ieee9bus")
def api_ieee9bus():
    return jsonify(PROPOSAL_DATA["ieee9bus"])


@app.route("/api/performance")
def api_performance():
    return jsonify(PROPOSAL_DATA["performance_targets"])


@app.route("/api/facts")
def api_facts():
    return jsonify(PROPOSAL_DATA["facts_devices"])


@app.route("/api/ev")
def api_ev():
    return jsonify(PROPOSAL_DATA["ev_v2g"])


@app.route("/api/cyber")
def api_cyber():
    return jsonify(PROPOSAL_DATA["cyber_attacks"])


@app.route("/api/test_systems")
def api_test_systems():
    return jsonify(PROPOSAL_DATA["test_systems"])


@app.route("/api/simulation")
def api_simulation():
    return jsonify(PROPOSAL_DATA["simulation"])


@app.route("/api/hirl")
def api_hirl():
    return jsonify(PROPOSAL_DATA["hirl"])


# ─────────────────────────────────────────────────────────────
# API: Simulated Real-Time Data (for live dashboard demo)
# ─────────────────────────────────────────────────────────────

@app.route("/api/live/bus_voltages")
def api_live_bus_voltages():
    """Simulate real-time bus voltage readings."""
    base_voltages = {1: 1.04, 2: 1.025, 3: 1.025, 4: 1.026, 5: 0.996, 6: 1.013, 7: 1.026, 8: 1.016, 9: 1.032}
    t = datetime.now().timestamp()
    voltages = {}
    for bus, v in base_voltages.items():
        noise = 0.005 * math.sin(2 * math.pi * 0.1 * t + bus) + random.gauss(0, 0.001)
        voltages[f"Bus_{bus}"] = round(v + noise, 4)
    return jsonify({"timestamp": t, "voltages": voltages})


@app.route("/api/live/frequency")
def api_live_frequency():
    """Simulate real-time system frequency."""
    t = datetime.now().timestamp()
    f = 60.0 + 0.02 * math.sin(2 * math.pi * 0.05 * t) + random.gauss(0, 0.005)
    return jsonify({"timestamp": t, "frequency": round(f, 4)})


@app.route("/api/live/ev_soc")
def api_live_ev_soc():
    """Simulate EV fleet SoC over time."""
    t = datetime.now().timestamp()
    soc = 0.70 + 0.15 * math.sin(2 * math.pi * 0.02 * t)
    soc = max(0.20, min(0.95, soc))
    return jsonify({"timestamp": t, "soc": round(soc, 3), "power_MW": round((0.6 - soc) * 50, 1)})


@app.route("/api/live/capsm_mode")
def api_live_capsm_mode():
    """Simulate CAPSM mode switching."""
    t = datetime.now().timestamp()
    confidence = 0.5 + 0.4 * math.sin(2 * math.pi * 0.03 * t)
    urgency = 0.3 + 0.3 * abs(math.sin(2 * math.pi * 0.07 * t))
    mode = "System-1" if (confidence > 0.7 and urgency > 0.3) else "System-2"
    return jsonify({
        "timestamp": t,
        "mode": mode,
        "confidence": round(confidence, 3),
        "urgency": round(urgency, 3),
        "novelty": round(random.uniform(0.1, 0.5), 3)
    })


@app.route("/api/live/hirl")
def api_live_hirl():
    """Simulate HIRL regional agent metrics."""
    t = datetime.now().timestamp()
    regions = []
    for k, name in enumerate(["Zone A (Bus 4-5-7)", "Zone B (Bus 6-8-9)"]):
        reward = 60 + 30 * math.sin(2 * math.pi * 0.02 * t + k) + random.gauss(0, 3)
        loss = max(0, 0.5 - 0.3 * math.sin(2 * math.pi * 0.015 * t + k) + random.gauss(0, 0.05))
        regions.append({
            "name": name,
            "reward": round(reward, 2),
            "policy_loss": round(loss, 4),
            "episodes": int(50000 + 1000 * math.sin(2 * math.pi * 0.01 * t + k)),
            "tie_violation": round(max(0, 0.3 + 0.2 * math.sin(2 * math.pi * 0.04 * t) + random.gauss(0, 0.05)), 3)
        })
    global_sync = round(0.85 + 0.1 * math.sin(2 * math.pi * 0.025 * t) + random.gauss(0, 0.02), 3)
    return jsonify({"timestamp": t, "regions": regions, "global_sync": global_sync})


# ─────────────────────────────────────────────────────────────
# API: User Configuration (localStorage-backed on frontend,
#       this endpoint allows persist/export of config)
# ─────────────────────────────────────────────────────────────

USER_CONFIG = {}

@app.route("/api/config", methods=["GET"])
def api_config_get():
    return jsonify(USER_CONFIG)


@app.route("/api/config", methods=["POST"])
def api_config_save():
    global USER_CONFIG
    data = request.get_json(force=True)
    if data:
        USER_CONFIG.update(data)
    return jsonify({"status": "ok", "config": USER_CONFIG})


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  CAPSM PhD Proposal Dashboard")
    print("  Mahmoud Kiasari — Dalhousie University")
    print("=" * 60)
    print(f"  → http://localhost:5050")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5050, debug=True)
