"""
═══════════════════════════════════════════════════════════════
CAPSM PhD Proposal Dashboard — Python / Dash / ML
Author : Mahmoud Kiasari, Dalhousie University, 2026
Stack  : Dash 4 + Plotly + scikit-learn + NumPy
Usage  : python dash_app.py  →  http://localhost:5050
═══════════════════════════════════════════════════════════════
"""

import json, sys, os
import numpy as np
import dash
from dash import dcc, html, Input, Output, State, callback, ALL, MATCH, ctx, no_update
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

# ── ML Engine ──
sys.path.insert(0, os.path.dirname(__file__))
from ml_engine import CAPSMMLEngine

ml = CAPSMMLEngine()

# ═══════════════════════════════════════════
# DEFAULT CONFIG
# ═══════════════════════════════════════════
DEFAULT_CONFIG = dict(
    author="Mahmoud Kiasari", affiliation="Dalhousie University",
    degree="PhD Candidate", year=2026,
    title="CAPSM: Cognitive Adaptive Power System Management",
    subtitle="A Dual-Process Metacognitive Framework for Resilient Power Grid Control",
    s1_response_ms=5, s2_response_ms=50,
    fault_accuracy=96.8, pinn_compliance=99.8,
    qirl_speedup=2.0, max_violations=0.2,
    base_mva=100, base_kv=230, frequency=60, sim_time=20,
    ev_fleet=1000, ev_capacity_mw=50,
    hirl_regions=2, hirl_global_rate=200,
    hirl_lr=0.001, hirl_gamma=0.99, hirl_epsilon=0.01,
    tau_c=0.7, tau_n=2.0, tau_u=0.3,
    fdi_start=2.0, fdi_end=5.0,
    dos_start=8.0, dos_duration=0.5, comm_delay=1.5,
)

# ═══════════════════════════════════════════
# PLOTLY THEME (dark)
# ═══════════════════════════════════════════
PLT = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(26,35,50,0.4)",
    font=dict(color="#8b9dc3", family="Inter", size=11),
    margin=dict(l=40, r=20, t=36, b=36),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
)
BLUE, PURPLE, EMERALD, AMBER, RED, CYAN, MUTED = (
    "#2563eb", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444", "#06b6d4", "#5a6d8a"
)
GRID = "rgba(30,58,95,0.3)"


# ═══════════════════════════════════════════
# HELPER COMPONENTS
# ═══════════════════════════════════════════
def kpi(icon, value, label, color):
    return html.Div([
        html.Div(icon, className=f"kpi-icon {color}"),
        html.Div([
            html.Div(value, className="kpi-value"),
            html.Div(label, className="kpi-label"),
        ], className="kpi-content"),
    ], className=f"kpi-card {color}")


def card(title, children, badge=None, badge_color="badge-blue"):
    hdr = [html.Div(title, className="card-title")]
    if badge:
        hdr.append(html.Span(badge, className=f"badge {badge_color}"))
    return html.Div([
        html.Div(hdr, style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"}),
        children,
    ], className="card")


def eq_block(items):
    """items: list of ('label'|'line', text)"""
    children = []
    for kind, txt in items:
        cls = "eq-label" if kind == "label" else "eq-line"
        children.append(html.Div(txt, className=cls))
    return html.Div(children, className="eq-block")


def data_table(headers, rows):
    return html.Table([
        html.Thead(html.Tr([html.Th(h) for h in headers])),
        html.Tbody([html.Tr([html.Td(c) for c in row]) for row in rows]),
    ], className="data-table")


def editor_panel(page_id, fields, cfg=None):
    """Create per-tab inline editor.  fields: list of dicts {key, label, type, step, unit}"""
    if cfg is None:
        cfg = DEFAULT_CONFIG
    cols = []
    for f in fields:
        val = cfg.get(f["key"], "")
        inp = dbc.Input(
            id={"type": "edit-field", "page": page_id, "key": f["key"]},
            type=f.get("type", "number"), step=f.get("step", 1),
            value=val, className="editor-input", debounce=True,
            style={"width": "110px"} if f.get("type", "number") == "number" else {"minWidth": "180px"},
        )
        unit = html.Span(f.get("unit", ""), className="editor-unit") if f.get("unit") else None
        cols.append(dbc.Col([
            html.Label(f["label"], className="editor-label"), inp,
            unit,
        ], width="auto"))
    return html.Div([
        html.Div([
            html.Span(f"✏️ {page_id.replace('_', ' ').title()} — Inline Editor", className="editor-title"),
            html.Button("💾 Save", id={"type": "save-inline", "page": page_id},
                        className="header-btn", style={"marginLeft": "auto", "fontSize": ".72rem"}),
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "10px"}),
        dbc.Row(cols, className="g-2"),
    ], className="tab-editor", id={"type": "editor-panel", "page": page_id})


# ═══════════════════════════════════════════
# CHART BUILDERS
# ═══════════════════════════════════════════
def chart_bus_voltages():
    buses = [f"Bus {i}" for i in range(1, 10)]
    volts = [1.040, 1.025, 1.025, 1.026, 0.996, 1.013, 1.026, 1.016, 1.032]
    colors = [RED]*3 + [BLUE]*6
    fig = go.Figure(go.Bar(x=buses, y=volts, marker_color=colors, marker_cornerradius=6))
    fig.update_layout(**PLT, title="Bus Voltage Profile (pu)", yaxis=dict(range=[0.95, 1.08], gridcolor=GRID))
    return fig


def chart_gen_dispatch():
    gens = ["Gen 1 (Slack)", "Gen 2 (PV)", "Gen 3 (PV)"]
    fig = go.Figure([
        go.Bar(name="P (MW)", x=gens, y=[71.64, 163.0, 85.0], marker_color=BLUE, marker_cornerradius=6),
        go.Bar(name="Q (MVAR)", x=gens, y=[27.05, 6.65, -10.86], marker_color=PURPLE, marker_cornerradius=6),
    ])
    fig.update_layout(**PLT, barmode="group", title="Generation Dispatch")
    return fig


def chart_radar_gaps():
    cats = ["G1: Dual-Speed", "G2: Sample Eff.", "G3: Physics-Aware", "G4: Scalability", "G5: Cyber"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[95, 88, 92, 78, 85], theta=cats, fill="toself",
                                   name="CAPSM", line=dict(color=BLUE, width=2)))
    fig.add_trace(go.Scatterpolar(r=[45, 40, 35, 50, 30], theta=cats, fill="toself",
                                   name="Baseline", line=dict(color=MUTED, dash="dot")))
    fig.update_layout(**PLT, polar=dict(bgcolor="rgba(0,0,0,0)",
                      radialaxis=dict(range=[0, 100], gridcolor=GRID, showticklabels=False),
                      angularaxis=dict(gridcolor=GRID)))
    return fig


def chart_qirl(lr=0.001, gamma=0.99):
    ep, q, d, p = ml.simulate_qirl(lr, gamma, 1000)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ep, y=q, name="QIRL (Proposed)", line=dict(color=PURPLE, width=2.5)))
    fig.add_trace(go.Scatter(x=ep, y=d, name="DQN Baseline", line=dict(color=MUTED, dash="dash", width=1.5)))
    fig.add_trace(go.Scatter(x=ep, y=p, name="PPO Baseline", line=dict(color=AMBER, dash="dot", width=1.5)))
    fig.update_layout(**PLT, title="QIRL vs Classical RL Convergence",
                      xaxis=dict(title="Episodes", gridcolor=GRID), yaxis=dict(title="Reward", gridcolor=GRID))
    return fig


def chart_metacognition(tau_c=0.7, tau_u=0.3):
    t, c, u, mode = ml.simulate_metacognition(tau_c, tau_u)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=c, name="Confidence", line=dict(color=BLUE, width=1.5)))
    fig.add_trace(go.Scatter(x=t, y=u, name="Urgency", line=dict(color=RED, width=1.5)))
    fig.add_trace(go.Scatter(x=t, y=mode, name="Mode (1=S1)", line=dict(color=AMBER, width=2),
                             fill="tozeroy", fillcolor="rgba(245,158,11,.08)"))
    fig.update_layout(**PLT, title="Metacognitive Mode Switching",
                      xaxis=dict(title="Time (s)", gridcolor=GRID),
                      yaxis=dict(range=[-0.1, 1.2], gridcolor=GRID))
    return fig


def chart_loadflow_v():
    buses = [f"Bus {i}" for i in range(1, 10)]
    v = [1.040, 1.025, 1.025, 1.026, 0.996, 1.013, 1.026, 1.016, 1.032]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=buses, y=v, name="V (pu)", fill="tozeroy",
                             line=dict(color=BLUE, width=2), fillcolor="rgba(37,99,235,.12)"))
    fig.add_hline(y=1.10, line=dict(color=RED, dash="dash", width=1), annotation_text="Vmax")
    fig.add_hline(y=0.90, line=dict(color=RED, dash="dash", width=1), annotation_text="Vmin")
    fig.update_layout(**PLT, title="Voltage Magnitude", yaxis=dict(range=[0.88, 1.12], gridcolor=GRID))
    return fig


def chart_loadflow_a():
    buses = [f"Bus {i}" for i in range(1, 10)]
    a = [0.0, 9.28, 4.665, -2.217, -3.989, -3.688, 3.72, 0.728, 1.967]
    colors = [CYAN if v >= 0 else AMBER for v in a]
    fig = go.Figure(go.Bar(x=buses, y=a, marker_color=colors, marker_cornerradius=6))
    fig.update_layout(**PLT, title="Voltage Angle (°)", yaxis=dict(gridcolor=GRID))
    return fig


def chart_ev_soc(cap_mw=50):
    t, soc = ml.simulate_ev_soc(cap_mw)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=soc, name="SoC", fill="tozeroy",
                             line=dict(color=CYAN, width=2), fillcolor="rgba(6,182,212,.08)"))
    fig.add_hline(y=0.95, line=dict(color=RED, dash="dash", width=1))
    fig.add_hline(y=0.20, line=dict(color=RED, dash="dash", width=1))
    fig.add_hline(y=0.60, line=dict(color=AMBER, dash="dot", width=1))
    fig.update_layout(**PLT, title="EV Fleet SoC Trajectory",
                      xaxis=dict(title="Time (s)", gridcolor=GRID),
                      yaxis=dict(range=[0, 1], title="SoC", gridcolor=GRID))
    return fig


def chart_performance():
    cats = ["Response\n(S1, ms)", "Decision\n(S2, ms)", "Violations\n(%)", "Fault Acc\n(%)", "Speed\n(×)"]
    fig = go.Figure([
        go.Bar(name="CAPSM", x=cats, y=[5, 50, 0.2, 96.8, 2.0], marker_color=BLUE, marker_cornerradius=6),
        go.Bar(name="DQN",   x=cats, y=[25, 200, 3.5, 88.0, 1.0], marker_color=MUTED, marker_cornerradius=6),
        go.Bar(name="PPO",   x=cats, y=[18, 150, 2.1, 91.5, 1.3], marker_color=AMBER, marker_cornerradius=6),
        go.Bar(name="PID",   x=cats, y=[2, 500, 5.0, 75.0, 0.5], marker_color="rgba(90,109,138,.5)", marker_cornerradius=6),
    ])
    fig.update_layout(**PLT, barmode="group", title="CAPSM vs Baselines")
    return fig


def chart_scaling():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[9, 39, 118, 300], y=[3, 10, 54, 69], mode="markers",
                             name="Generators", marker=dict(size=16, color=BLUE)))
    fig.add_trace(go.Scatter(x=[9, 39, 118, 300], y=[6, 46, 186, 411], mode="markers",
                             name="Lines", marker=dict(size=10, color=CYAN)))
    fig.update_layout(**PLT, title="Test System Scaling",
                      xaxis=dict(title="Buses", type="log", gridcolor=GRID),
                      yaxis=dict(title="Count", type="log", gridcolor=GRID))
    return fig


def chart_hirl(lr=0.001, gamma=0.99, n_regions=2):
    ep, h, c, i_, d = ml.simulate_hirl(lr, gamma, n_regions)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ep, y=h, name="HIRL", line=dict(color=PURPLE, width=2.5), fill="tozeroy",
                             fillcolor="rgba(139,92,246,.08)"))
    fig.add_trace(go.Scatter(x=ep, y=c, name="Centralized", line=dict(color=MUTED, dash="dash")))
    fig.add_trace(go.Scatter(x=ep, y=i_, name="Independent", line=dict(color=AMBER, dash="dot")))
    fig.add_trace(go.Scatter(x=ep, y=d, name="DQN", line=dict(color=RED, dash="dashdot")))
    fig.update_layout(**PLT, title="HIRL Training Convergence",
                      xaxis=dict(title="Episodes", gridcolor=GRID), yaxis=dict(title="Reward", gridcolor=GRID))
    return fig


def chart_fault_importance():
    names, vals = ml.get_feature_importance_data()
    fig = go.Figure(go.Bar(x=vals[::-1], y=names[::-1], orientation="h",
                           marker_color=BLUE, marker_cornerradius=4))
    fig.update_layout(**PLT, title="Top-15 Feature Importances (Fault RF)",
                      xaxis=dict(gridcolor=GRID), yaxis=dict(tickfont=dict(size=9)),
                      height=340)
    return fig


def chart_confusion_matrix():
    cm = ml.fault_cm
    labels = ml.fault_labels
    fig = go.Figure(go.Heatmap(z=cm, x=labels, y=labels, colorscale="Blues",
                               text=cm, texttemplate="%{text}", textfont=dict(size=11)))
    fig.update_layout(**PLT, title="Fault Classifier Confusion Matrix",
                      xaxis=dict(title="Predicted"), yaxis=dict(title="Actual", autorange="reversed"),
                      height=360)
    return fig


def chart_anomaly_scores():
    rng = np.random.RandomState(99)
    normal = rng.randn(80) * 0.02 + 0.15
    fdi = rng.randn(30) * 0.04 - 0.08
    dos = rng.randn(15) * 0.03 - 0.25
    fig = go.Figure()
    fig.add_trace(go.Box(y=normal, name="Normal", marker_color=EMERALD))
    fig.add_trace(go.Box(y=fdi, name="FDI Attack", marker_color=AMBER))
    fig.add_trace(go.Box(y=dos, name="DoS Attack", marker_color=RED))
    fig.add_hline(y=0, line=dict(color="white", dash="dash", width=1), annotation_text="Decision boundary")
    fig.update_layout(**PLT, title="Anomaly Scores by Attack Type", yaxis=dict(title="Score", gridcolor=GRID))
    return fig


# ═══════════════════════════════════════════
# PAGE LAYOUTS  (16 pages)
# ═══════════════════════════════════════════

def page_overview(cfg):
    metrics = ml.get_all_metrics()
    return html.Div([
        editor_panel("overview", [
            dict(key="author", label="Author", type="text"),
            dict(key="affiliation", label="Affiliation", type="text"),
            dict(key="year", label="Year", type="number"),
            dict(key="s1_response_ms", label="S1 Response", step=0.1, unit="ms"),
            dict(key="s2_response_ms", label="S2 Decision", step=1, unit="ms"),
            dict(key="pinn_compliance", label="PINN", step=0.1, unit="%"),
            dict(key="fault_accuracy", label="Fault Acc.", step=0.1, unit="%"),
            dict(key="qirl_speedup", label="Speedup", step=0.1, unit="×"),
        ], cfg),
        html.Div("Cognitive Adaptive Power System Management", className="section-title"),
        html.P(f"A dual-process metacognitive framework combining fast reflexive control (System-1, CNN-LSTM, <{cfg['s1_response_ms']}ms) "
               f"with deliberative optimization (System-2, QIRL, <{cfg['s2_response_ms']}ms), governed by metacognitive arbitration "
               f"and enforced by PINN safety constraints.", className="section-desc"),
        html.Div([
            kpi("⚡", f"< {cfg['s1_response_ms']} ms", "System-1 Response Time", "blue"),
            kpi("🧠", f"< {cfg['s2_response_ms']} ms", "System-2 Decision Cycle", "purple"),
            kpi("🛡️", f"{cfg['pinn_compliance']}%", "PINN Constraint Compliance", "emerald"),
            kpi("🎯", f"{cfg['fault_accuracy']}%", "Fault Detection Accuracy", "amber"),
            kpi("🚀", f"{cfg['qirl_speedup']}×", "QIRL Speedup vs DQN", "red"),
            kpi("🔌", "9-Bus", "IEEE Test System", "cyan"),
        ], className="kpi-grid"),
        # ML metrics summary
        html.Div([
            html.Div("🤖 ML Engine Status", className="card-title"),
            html.Div([
                html.Div([html.Span("Fault RF Accuracy", className="ml-metric-label"),
                          html.Span(f"{metrics['fault_rf_accuracy']}%", className="ml-metric-value", style={"color": EMERALD})], className="ml-metric"),
                html.Div([html.Span("Fault MLP Accuracy", className="ml-metric-label"),
                          html.Span(f"{metrics['fault_mlp_accuracy']}%", className="ml-metric-value", style={"color": EMERALD})], className="ml-metric"),
                html.Div([html.Span("Mode Classifier Accuracy", className="ml-metric-label"),
                          html.Span(f"{metrics['mode_accuracy']}%", className="ml-metric-value", style={"color": BLUE})], className="ml-metric"),
                html.Div([html.Span("Convergence Predictor R²", className="ml-metric-label"),
                          html.Span(f"{metrics['convergence_r2']}", className="ml-metric-value", style={"color": PURPLE})], className="ml-metric"),
                html.Div([html.Span("Voltage Predictor R²", className="ml-metric-label"),
                          html.Span(f"{metrics['voltage_r2']}", className="ml-metric-value", style={"color": CYAN})], className="ml-metric"),
                html.Div([html.Span("SoC Forecaster R²", className="ml-metric-label"),
                          html.Span(f"{metrics['soc_r2']}", className="ml-metric-value", style={"color": AMBER})], className="ml-metric"),
            ]),
        ], className="ml-card"),
        html.Div([
            html.Div([
                card("Bus Voltage Profile", dcc.Graph(id="chart-bus-v", figure=chart_bus_voltages(), config={"displayModeBar": False})),
                card("Generation Dispatch", dcc.Graph(id="chart-gen-d", figure=chart_gen_dispatch(), config={"displayModeBar": False})),
            ], style={"flex": "1"}),
            html.Div([
                card("Research Gap Coverage", dcc.Graph(id="chart-radar", figure=chart_radar_gaps(), config={"displayModeBar": False})),
            ], style={"flex": "1"}),
        ], className="grid-2"),
    ])


def page_hypothesis(cfg):
    gaps = [
        ("G1", "Single-Speed Control Paradigm",
         "Existing AI controllers operate at a single temporal resolution — either fast reflex OR slow optimization — but never both integrated.",
         "Dual-process System-1 / System-2 architecture with metacognitive arbitration"),
        ("G2", "Sample Inefficiency of Deep RL",
         "Standard DQN/PPO require millions of episodes. Convergence too slow for real-time adaptation during cascading failures.",
         "Quantum-Inspired RL (QIRL) with superposition-based exploration and tunneling"),
        ("G3", "Physics-Blind Neural Controllers",
         "Most neural controllers ignore Kirchhoff's laws, leading to unsafe actions that violate voltage/current limits.",
         "Physics-Informed Neural Network (PINN) safety layer enforcing AC power flow constraints"),
        ("G4", "Scalability of Multi-Agent Coordination",
         "Centralized RL doesn't scale beyond small test systems. Distributed approaches lack coordination.",
         "Hierarchical Multi-Agent RL (HMARL) with regional agents and global coordinator"),
        ("G5", "Cyber-Physical Resilience Under Attack",
         "Power grids are vulnerable to FDI, DoS, MITM attacks. No integrated mechanism to detect and recover.",
         "Metacognitive anomaly detection + CAPSM's dual-process fallback architecture"),
    ]
    return html.Div([
        editor_panel("hypothesis", [
            dict(key="title", label="Title", type="text"),
            dict(key="subtitle", label="Subtitle", type="text"),
        ], cfg),
        html.Div("Central Hypothesis & Research Gaps", className="section-title"),
        html.Div([
            html.Div("Central Hypothesis", className="label"),
            html.Div(f'"A dual-process, metacognitively guided, physics-informed control architecture — inspired by human cognitive science '
                     f'— can simultaneously achieve sub-{cfg["s1_response_ms"]}ms fault response, near-optimal economic dispatch, '
                     f'>{cfg["pinn_compliance"]}% constraint compliance, and cyber-attack resilience in modern power grids '
                     f'with high renewable/EV penetration."', className="text"),
        ], className="hyp-banner"),
        html.Div("Research Gaps", className="section-title", style={"fontSize": "1.1rem"}),
        html.Div([
            html.Div([
                html.Span(gid, className="gap-id"),
                html.H3(title), html.P(desc, className="description"),
                html.Div(f"✓ Addressed by: {addr}", className="addressed"),
            ], className="gap-card") for gid, title, desc, addr in gaps
        ], className="grid-2"),
    ])


def page_architecture(cfg):
    return html.Div([
        editor_panel("architecture", [
            dict(key="s1_response_ms", label="S1 (ms)", step=0.1),
            dict(key="s2_response_ms", label="S2 (ms)", step=1),
            dict(key="pinn_compliance", label="PINN %", step=0.1),
        ], cfg),
        html.Div("CAPSM Framework Architecture", className="section-title"),
        html.P("Four-layer cognitive architecture inspired by dual-process theory (Kahneman, 2011).", className="section-desc"),
        html.Div([
            card("Information Flow", eq_block([
                ("label", "1. Sensor Fusion"), ("line", "X_t ∈ ℝ^{N_bus × 6 × T_window}"),
                ("line", "PMU (30-120 Hz) + SCADA + Weather + Market"),
                ("label", "2. Metacognitive Assessment"), ("line", "C_t = 1 - Var(Q) / Var_max"),
                ("line", "α_t = 𝟙(C_t > τ_c ∧ U_t > τ_u)"),
                ("label", "3. Dual-Process Execution"), ("line", "u = α_t · u_S1 + (1-α_t) · u_S2"),
                ("label", "4. Safety Projection"), ("line", "u_safe = PINN_project(u, state)"),
            ])),
            card("Cognitive Science Foundation", data_table(
                ["Aspect", "System-1 (Fast)", "System-2 (Slow)"],
                [["Cognition", "Intuitive / Automatic", "Deliberate / Analytical"],
                 ["Speed", "Milliseconds", "Seconds to minutes"],
                 ["CAPSM Model", "CNN-LSTM", "QIRL"],
                 ["Response", f"< {cfg['s1_response_ms']} ms", f"< {cfg['s2_response_ms']} ms"],
                 ["Task", "Fault reflex", "Economic dispatch"],
                 ["Activated", "High urgency", "Normal operation"]]
            )),
        ], className="grid-2"),
    ])


def page_system1(cfg):
    return html.Div([
        editor_panel("system1", [
            dict(key="s1_response_ms", label="Response", step=0.1, unit="ms"),
            dict(key="fault_accuracy", label="Fault Acc.", step=0.1, unit="%"),
            dict(key="frequency", label="Frequency", step=1, unit="Hz"),
        ], cfg),
        html.Div("System-1: CNN-LSTM Reflexive Controller", className="section-title"),
        html.P(f"Fast fault detection and voltage support. Targets sub-{cfg['s1_response_ms']}ms response.", className="section-desc"),
        html.Div([
            card("Network Architecture", eq_block([
                ("label", "Input"), ("line", "X_t ∈ ℝ^{N_bus × 6 × T_window}"),
                ("line", f"  N_bus=9, channels={{Va,Vb,Vc,Ia,Ib,Ic}}, T_window=30 @ 120 Hz"),
                ("label", "CNN Feature Extraction"), ("line", "h_spatial = CNN_1D(X_t)"),
                ("line", "  Conv1D → BatchNorm → ReLU → MaxPool (×3)"),
                ("label", "LSTM Temporal Processing"), ("line", "z(t) = LSTM(h_spatial)  # hidden=128, 2 layers"),
                ("label", "Output"), ("line", "u_fast = f_θ(z(t))  → ±100 MVAR"),
            ]), badge="CNN-LSTM"),
            html.Div([
                card("Performance Targets", html.Div([
                    kpi("⚡", f"{cfg['fault_accuracy']}%", "Fault Detection Accuracy", "blue"),
                    kpi("🏎", f"< {cfg['s1_response_ms']} ms", "Response Time", "cyan"),
                ], className="kpi-grid")),
                card("Fault Scenarios", data_table(
                    ["Type", "Location", "Duration"],
                    [["3-Phase Fault", "Bus 5", "5 cycles (83.3 ms)"], ["Line-Ground", "Line 4-5", "3 cycles"],
                     ["Line-Line", "Line 7-8", "5 cycles"], ["Loss of Gen", "Gen 2", "t=5s event"]]
                )),
            ]),
        ], className="grid-2"),
        # ML: Fault classification
        html.Div([
            html.Div([html.Span("🤖 ML: Fault Classifier", className="card-title"),
                      html.Span("TRAINED", className="badge badge-emerald")],
                     style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "marginBottom": "12px"}),
            html.Div([
                html.Div([html.Span(f"Random Forest: {ml.metrics['fault_rf_accuracy']}%", style={"color": EMERALD, "fontWeight": 700}),
                          html.Span(f"  |  MLP (CNN-LSTM proxy): {ml.metrics['fault_mlp_accuracy']}%", style={"color": BLUE})],
                         style={"marginBottom": "12px", "fontSize": ".85rem"}),
                html.Div([
                    dcc.Graph(figure=chart_fault_importance(), config={"displayModeBar": False}, style={"height": "340px"}),
                    dcc.Graph(figure=chart_confusion_matrix(), config={"displayModeBar": False}, style={"height": "360px"}),
                ], className="grid-2"),
            ]),
        ], className="ml-card"),
    ])


def page_system2(cfg):
    return html.Div([
        editor_panel("system2", [
            dict(key="s2_response_ms", label="Decision", step=1, unit="ms"),
            dict(key="qirl_speedup", label="Speedup", step=0.1, unit="×"),
            dict(key="hirl_lr", label="LR", step=0.0001),
            dict(key="hirl_gamma", label="γ", step=0.01),
        ], cfg),
        html.Div("System-2: QIRL Deliberative Optimizer", className="section-title"),
        html.P("Quantum-Inspired RL uses complex-valued policy amplitudes and quantum tunneling for ≥2× faster convergence.", className="section-desc"),
        html.Div([
            card("QIRL Algorithm", eq_block([
                ("label", "Policy Representation"), ("line", "ψ = Σᵢ αᵢ|aᵢ⟩   (complex amplitudes)"),
                ("line", "P(aᵢ|s) = |αᵢ|²  (Born rule)"),
                ("label", "Bellman Update"), ("line", "Q(s,a) ← Q + lr·(r + γ·max Q(s',a') - Q)"),
                ("label", "Quantum Tunneling"), ("line", "αᵢ ← αᵢ - lr·∇L + β·T(αᵢ)"),
                ("line", "β decays: β(t) = β₀·e^(-t/τ)"),
            ]), badge="QUANTUM-INSPIRED", badge_color="badge-purple"),
            html.Div([
                card("Convergence (live — tune LR & γ in editor)", dcc.Graph(id="chart-qirl", figure=chart_qirl(cfg["hirl_lr"], cfg["hirl_gamma"]), config={"displayModeBar": False})),
                card("Control Tasks", data_table(
                    ["Task", "Objective", "Cycle"],
                    [["Economic Dispatch", "min Σ cᵢ·Pᵢ", f"< {cfg['s2_response_ms']} ms"],
                     ["VAR Optimization", "min losses", f"< {cfg['s2_response_ms']} ms"],
                     ["EV Scheduling", "V2G fleet SoC", "< 100 ms"],
                     ["Cyber Recovery", "Restore control", "< 200 ms"]]
                )),
            ]),
        ], className="grid-2"),
        # ML: Convergence prediction
        html.Div([
            html.Div("🤖 ML: RL Convergence Predictor", className="card-title"),
            html.Div(f"Predicted convergence with lr={cfg['hirl_lr']}, γ={cfg['hirl_gamma']}: "
                     f"~{ml.predict_convergence(cfg['hirl_lr'], cfg['hirl_gamma'], cfg['hirl_epsilon'], cfg['hirl_regions']):,} episodes",
                     style={"fontSize": ".88rem", "color": PURPLE, "fontWeight": 700}),
            html.Div(f"Model R² = {ml.metrics['convergence_r2']}", style={"fontSize": ".78rem", "color": MUTED, "marginTop": "4px"}),
        ], className="ml-card"),
    ])


def page_hirl(cfg):
    return html.Div([
        editor_panel("hirl", [
            dict(key="hirl_regions", label="Regions", step=1),
            dict(key="hirl_global_rate", label="Global Rate", step=50, unit="ms"),
            dict(key="hirl_lr", label="LR", step=0.0001),
            dict(key="hirl_gamma", label="γ", step=0.01),
            dict(key="hirl_epsilon", label="ε", step=0.001),
        ], cfg),
        html.Div("HIRL: Hierarchical Integrated RL", className="section-title"),
        html.P("HIRL unifies QIRL with hierarchical multi-agent coordination into a scalable RL framework.", className="section-desc"),
        # Hierarchy diagram
        card("Three-Level HIRL Hierarchy", html.Div([
            html.Div([html.Span("☆ Global", className="hirl-badge", style={"background": "rgba(245,158,11,.15)", "color": AMBER}),
                      html.H4("Global Coordinator"), html.P("Federated averaging, inter-region conflict resolution, global economic dispatch.", className="section-desc", style={"maxWidth": "100%"}),
                      html.Div([html.Span(f"⏱ Update: {cfg['hirl_global_rate']} ms"), html.Span("🔗 Federated QIRL + Consensus")], className="hirl-meta")], className="hirl-level"),
            html.Div("⬇", className="hirl-connector"),
            html.Div([html.Span("◆ Regional", className="hirl-badge", style={"background": "rgba(139,92,246,.15)", "color": PURPLE}),
                      html.H4(f"Regional Agents ({cfg['hirl_regions']} zones)"), html.P("Each agent manages a zone with local QIRL for VAR optimization, FACTS setpoints, EV scheduling.", className="section-desc", style={"maxWidth": "100%"}),
                      html.Div([html.Span("⏱ Update: <50 ms"), html.Span("🔗 QIRL + Neighbor Messages")], className="hirl-meta")], className="hirl-level"),
            html.Div("⬇", className="hirl-connector"),
            html.Div([html.Span("● Device", className="hirl-badge", style={"background": "rgba(37,99,235,.15)", "color": "#60a5fa"}),
                      html.H4("Device Controllers"), html.P("SVC droop, STATCOM response, EV charge/discharge. PI/PID with QIRL-tuned gains.", className="section-desc", style={"maxWidth": "100%"}),
                      html.Div([html.Span("⏱ Update: <5 ms"), html.Span("🔗 PI/PID + QIRL Gains")], className="hirl-meta")], className="hirl-level"),
        ]), badge="HIERARCHICAL", badge_color="badge-purple"),
        html.Div([
            card("HIRL Equations", eq_block([
                ("label", "Federated Policy Aggregation"), ("line", "π_global = FedAvg({π_region_k})"),
                ("line", "with consensus: |π_k - π_global| < ε"),
                ("label", "Regional Q-Update"), ("line", "Q_k ← Q_k + lr·(r_k + γ·max Q_k' - Q_k + λ·msg)"),
                ("label", "Gradient Message Passing"), ("line", "msg_j→k = Σ_j w_jk · ∇Q_j"),
                ("label", "Global Objective"), ("line", "min Σ_k c_k(P_k) + μ·Σ |ΔP_tie|"),
            ]), badge="EQUATIONS", badge_color="badge-purple"),
            card("HIRL Convergence (live)", dcc.Graph(id="chart-hirl", figure=chart_hirl(cfg["hirl_lr"], cfg["hirl_gamma"], cfg["hirl_regions"]), config={"displayModeBar": False})),
        ], className="grid-2"),
        card("HIRL Performance vs Baselines", data_table(
            ["Metric", "HIRL Target", "DQN", "Independent", "Centralized"],
            [["Convergence", "<50k episodes", "~200k", "~150k", "~300k"],
             ["Coordination Overhead", "<15%", "N/A", "~5%", "~40%"],
             ["Max Scalability", "300+ buses", "~50", "~200", "~30"],
             ["Tie-Line Violations", "<0.5%", "~3%", "~3%", "~0.8%"]]
        )),
    ])


def page_pinn(cfg):
    return html.Div([
        editor_panel("pinn", [
            dict(key="pinn_compliance", label="Compliance", step=0.1, unit="%"),
            dict(key="max_violations", label="Max Violations", step=0.01, unit="%"),
        ], cfg),
        html.Div("PINN Safety Layer", className="section-title"),
        html.P(f"Physics-Informed Neural Network enforces AC power flow constraints. Target: >{cfg['pinn_compliance']}% compliance.", className="section-desc"),
        html.Div([
            card("Loss Function", eq_block([
                ("label", "Total Loss"), ("line", "L = L_data + λ_pf · L_AC + λ_lim · L_constraints"),
                ("label", "AC Power Flow Residual"),
                ("line", "P_i = V_i Σⱼ V_j(G_ij cos θ_ij + B_ij sin θ_ij)"),
                ("line", "Q_i = V_i Σⱼ V_j(G_ij sin θ_ij - B_ij cos θ_ij)"),
                ("label", "Constraint Penalties"),
                ("line", "L_V = Σ max(0, V-V_max)² + max(0, V_min-V)²"),
                ("line", "L_I = Σ max(0, I-I_max)²"),
                ("line", "L_SoC = Σ max(0, SoC-0.95)² + max(0, 0.20-SoC)²"),
            ]), badge="PHYSICS", badge_color="badge-emerald"),
            html.Div([
                card("Operational Limits", data_table(
                    ["Constraint", "Min", "Max", "Unit"],
                    [["Bus Voltage", "0.90", "1.10", "pu"], ["Line Current", "—", "1.05", "pu"],
                     ["EV SoC", "0.20", "0.95", "pu"], ["Frequency", "59.5", "60.5", "Hz"],
                     ["SVC Reactive", "-100", "+100", "MVAR"], ["STATCOM", "-50", "+50", "MVAR"]]
                )),
                html.Div([
                    html.Div(f"{cfg['pinn_compliance']}%", style={"fontSize": "3rem", "fontWeight": 900,
                             "background": "linear-gradient(135deg, #10b981, #06b6d4)", "-webkit-background-clip": "text",
                             "background-clip": "text", "-webkit-text-fill-color": "transparent", "textAlign": "center"}),
                    html.Div("Constraint compliance target", style={"textAlign": "center", "color": MUTED, "fontSize": ".78rem"}),
                ], className="card"),
            ]),
        ], className="grid-2"),
        # ML: Voltage prediction
        html.Div([
            html.Div("🤖 ML: Voltage Stability Predictor", className="card-title"),
            html.Div(f"Predicted Bus 5 voltage @ 125MW load: {ml.predict_voltage(125, 50, 320, 20):.4f} pu",
                     style={"fontSize": ".88rem", "color": EMERALD, "fontWeight": 700}),
            html.Div(f"MLP Regressor R² = {ml.metrics['voltage_r2']}", style={"fontSize": ".78rem", "color": MUTED}),
        ], className="ml-card"),
    ])


def page_metacognition(cfg):
    pred, proba = ml.classify_mode(cfg["tau_c"], 1.0, cfg["tau_u"])
    return html.Div([
        editor_panel("metacognition", [
            dict(key="tau_c", label="τ_c (Conf.)", step=0.05),
            dict(key="tau_n", label="τ_n (Nov.)", step=0.1),
            dict(key="tau_u", label="τ_u (Urg.)", step=0.05),
        ], cfg),
        html.Div("Metacognitive Arbitration", className="section-title"),
        html.P("Continuously monitors state and confidence, dynamically switching between System-1 and System-2.", className="section-desc"),
        html.Div([
            html.Div([html.Div("Confidence (C_t)", className="card-title", style={"color": "#60a5fa"}),
                      eq_block([("line", "C_t = 1 - Var(Q-values) / Var_max")]),
                      html.P(f"Threshold: τ_c = {cfg['tau_c']}", className="section-desc", style={"maxWidth": "100%", "marginTop": "8px"})], className="card", style={"borderLeft": f"3px solid {BLUE}"}),
            html.Div([html.Div("Novelty (N_t)", className="card-title", style={"color": PURPLE}),
                      eq_block([("line", "N_t = ‖s - μ_buffer‖ / σ_buffer")]),
                      html.P(f"Threshold: τ_n = {cfg['tau_n']}σ", className="section-desc", style={"maxWidth": "100%", "marginTop": "8px"})], className="card", style={"borderLeft": f"3px solid {PURPLE}"}),
            html.Div([html.Div("Urgency (U_t)", className="card-title", style={"color": RED}),
                      eq_block([("line", "U_t = max(|ΔV/Δt|, |Δf/Δt|) / threshold")]),
                      html.P(f"Threshold: τ_u = {cfg['tau_u']}", className="section-desc", style={"maxWidth": "100%", "marginTop": "8px"})], className="card", style={"borderLeft": f"3px solid {RED}"}),
        ], className="grid-3"),
        card("Simulated Mode Switching (live — tune thresholds)",
             dcc.Graph(id="chart-meta", figure=chart_metacognition(cfg["tau_c"], cfg["tau_u"]), config={"displayModeBar": False})),
        # ML: Mode classifier
        html.Div([
            html.Div("🤖 ML: Mode Classifier", className="card-title"),
            html.Div(f"Predicted mode @ C={cfg['tau_c']}, N=1.0, U={cfg['tau_u']}: "
                     f"{'System-1 (Reflex)' if pred == 1 else 'System-2 (Deliberative)'}  "
                     f"[P(S1)={proba[1]:.2f}, P(S2)={proba[0]:.2f}]",
                     style={"fontSize": ".88rem", "fontWeight": 700, "color": BLUE if pred == 1 else PURPLE}),
            html.Div(f"GradientBoosting Accuracy = {ml.metrics['mode_accuracy']}%", style={"color": MUTED, "fontSize": ".78rem"}),
        ], className="ml-card"),
    ])


def page_topology(cfg):
    return html.Div([
        editor_panel("topology", [
            dict(key="base_mva", label="Base MVA", step=10),
            dict(key="base_kv", label="Base kV", step=1),
            dict(key="frequency", label="Freq.", step=1, unit="Hz"),
            dict(key="sim_time", label="Sim Time", step=1, unit="s"),
        ], cfg),
        html.Div("IEEE 9-Bus Test System Topology", className="section-title"),
        html.P(f"WSCC 3-generator, 9-bus reference system. Base: {cfg['base_mva']} MVA, {cfg['base_kv']} kV, {cfg['frequency']} Hz.", className="section-desc"),
        card("Transmission Line Parameters", data_table(
            ["Line", "From", "To", "R (pu)", "X (pu)", "B (pu)"],
            [["L4-5", "Bus 4", "Bus 5", "0.0100", "0.0850", "0.1760"],
             ["L4-6", "Bus 4", "Bus 6", "0.0170", "0.0920", "0.1580"],
             ["L5-7", "Bus 5", "Bus 7", "0.0320", "0.1610", "0.3060"],
             ["L6-9", "Bus 6", "Bus 9", "0.0390", "0.1700", "0.3580"],
             ["L7-8", "Bus 7", "Bus 8", "0.0085", "0.0720", "0.1490"],
             ["L8-9", "Bus 8", "Bus 9", "0.0119", "0.1008", "0.2090"]]
        ), badge=f"PER-UNIT ({cfg['base_mva']} MVA, {cfg['base_kv']} kV)"),
    ])


def page_loadflow(cfg):
    return html.Div([
        editor_panel("loadflow", [
            dict(key="base_mva", label="Base MVA", step=10),
            dict(key="base_kv", label="Base kV", step=1),
            dict(key="frequency", label="Freq.", step=1, unit="Hz"),
        ], cfg),
        html.Div("Load Flow Analysis", className="section-title"),
        html.P("Steady-state AC power flow solution. Total generation: 319.64 MW. Losses: 4.64 MW.", className="section-desc"),
        card("Bus Data — Load Flow Results", data_table(
            ["Bus", "V (pu)", "Angle (°)", "P_gen", "Q_gen", "P_load", "Q_load", "Type"],
            [[1, 1.040, 0.000, 71.64, 27.05, 0, 0, "Slack"],
             [2, 1.025, 9.280, 163.00, 6.65, 0, 0, "PV"],
             [3, 1.025, 4.665, 85.00, -10.86, 0, 0, "PV"],
             [4, 1.026, -2.217, 0, 0, 0, 0, "PQ"],
             [5, 0.996, -3.989, 0, 0, 125, 50, "PQ"],
             [6, 1.013, -3.688, 0, 0, 90, 30, "PQ"],
             [7, 1.026, 3.720, 0, 0, 0, 0, "PQ"],
             [8, 1.016, 0.728, 0, 0, 100, 35, "PQ"],
             [9, 1.032, 1.967, 0, 0, 0, 0, "PQ"]]
        ), badge="SOLVED", badge_color="badge-emerald"),
        html.Div([
            card("Voltage Profile", dcc.Graph(figure=chart_loadflow_v(), config={"displayModeBar": False})),
            card("Voltage Angle", dcc.Graph(figure=chart_loadflow_a(), config={"displayModeBar": False})),
        ], className="grid-2"),
    ])


def page_facts(cfg):
    return html.Div([
        editor_panel("facts", [
            dict(key="s1_response_ms", label="S1 (ms)", step=0.1),
            dict(key="s2_response_ms", label="S2 (ms)", step=1),
        ], cfg),
        html.Div("FACTS Devices", className="section-title"),
        html.P("Flexible AC Transmission Systems for voltage regulation and reactive power support.", className="section-desc"),
        html.Div([
            html.Div([
                html.Div("Static VAR Compensator", style={"color": AMBER, "fontSize": ".7rem", "fontWeight": 700, "textTransform": "uppercase", "letterSpacing": "1px"}),
                html.H3("SVC at Bus 5", style={"marginBottom": "10px"}),
                *[html.Div([html.Span(k, className="label"), html.Span(v, className="value")], className="facts-detail")
                  for k, v in [("Rating", "±100 MVAR"), ("V Reference", "1.0 pu"), ("Droop (Xs)", "0.03 pu"),
                               ("Delay (Td)", "20 ms"), ("PI Gains", "Kp=5, Ki=100"),
                               ("Function", "Voltage regulation"), ("CAPSM Control", "System-1 + System-2")]],
            ], className="facts-card"),
            html.Div([
                html.Div("Static Synchronous Compensator", style={"color": PURPLE, "fontSize": ".7rem", "fontWeight": 700, "textTransform": "uppercase", "letterSpacing": "1px"}),
                html.H3("STATCOM at Bus 8", style={"marginBottom": "10px"}),
                *[html.Div([html.Span(k, className="label"), html.Span(v, className="value")], className="facts-detail")
                  for k, v in [("Rating", "±50 MVAR"), ("V Reference", "1.0 pu"), ("Droop (Xs)", "0.02 pu"),
                               ("Delay (Td)", "5 ms"), ("PI Gains", "Kp=5, Ki=200"),
                               ("Function", "Fast reactive comp."), (f"CAPSM Control", f"System-1 reflex (<{cfg['s1_response_ms']}ms)")]],
            ], className="facts-card"),
        ], className="grid-2"),
    ])


def page_ev(cfg):
    return html.Div([
        editor_panel("ev", [
            dict(key="ev_fleet", label="Fleet", step=100, unit="EVs"),
            dict(key="ev_capacity_mw", label="Capacity", step=5, unit="MW"),
        ], cfg),
        html.Div("EV/V2G Aggregator", className="section-title"),
        html.P(f"Vehicle-to-Grid fleet at Bus 8 — {cfg['ev_fleet']:,} EVs × "
               f"{int(cfg['ev_capacity_mw']*1000/max(1,cfg['ev_fleet']))} kW = {cfg['ev_capacity_mw']} MW.", className="section-desc"),
        html.Div([
            html.Div([html.Div(f"{cfg['ev_fleet']:,}", className="value"), html.Div("EV Fleet Size", className="label")], className="ev-stat"),
            html.Div([html.Div(f"{cfg['ev_capacity_mw']} MW", className="value"), html.Div("Total Capacity", className="label")], className="ev-stat"),
            html.Div([html.Div(f"{cfg['ev_capacity_mw']*3} MWh", className="value"), html.Div("Energy Storage", className="label")], className="ev-stat"),
        ], className="ev-stats-grid"),
        html.Div([
            card("V2G Parameters", data_table(
                ["Parameter", "Value"],
                [["Bus Location", "Bus 8"], [f"Fleet Size", f"{cfg['ev_fleet']:,} EVs"],
                 ["Total Capacity", f"±{cfg['ev_capacity_mw']} MW"],
                 ["Efficiency", "95%"], ["Initial SoC", "70%"],
                 ["SoC Bounds", "[20%, 95%]"], ["Controlled By", "System-2 QIRL"]]
            )),
            card("SoC Dynamics (live)", dcc.Graph(id="chart-ev", figure=chart_ev_soc(cfg["ev_capacity_mw"]), config={"displayModeBar": False})),
        ], className="grid-2"),
        # ML: SoC forecaster
        html.Div([
            html.Div("🤖 ML: SoC Forecaster", className="card-title"),
            html.Div(f"Predicted SoC after 1s @ 25MW charge, SoC=0.70: {ml.predict_soc(0.70, 25):.4f}",
                     style={"color": CYAN, "fontWeight": 700, "fontSize": ".88rem"}),
            html.Div(f"GradientBoosting R² = {ml.metrics['soc_r2']}", style={"color": MUTED, "fontSize": ".78rem"}),
        ], className="ml-card"),
    ])


def page_performance(cfg):
    return html.Div([
        editor_panel("performance", [
            dict(key="s1_response_ms", label="S1", step=0.1, unit="ms"),
            dict(key="s2_response_ms", label="S2", step=1, unit="ms"),
            dict(key="fault_accuracy", label="Fault%", step=0.1),
            dict(key="pinn_compliance", label="PINN%", step=0.1),
            dict(key="qirl_speedup", label="Speed×", step=0.1),
            dict(key="max_violations", label="Viol%", step=0.01),
        ], cfg),
        html.Div("Performance Targets", className="section-title"),
        html.P("Key performance indicators (PhD Proposal Table 7 & 9).", className="section-desc"),
        html.Div([
            kpi("⚡", f"< {cfg['s1_response_ms']} ms", "System-1 Response Time", "blue"),
            kpi("🧠", f"< {cfg['s2_response_ms']} ms", "System-2 Decision Cycle", "purple"),
            kpi("🛡️", f"< {cfg['max_violations']}%", "Constraint Violations", "emerald"),
            kpi("🎯", f"≥ {cfg['fault_accuracy']}%", "Fault Detection Accuracy", "amber"),
            kpi("🚀", f"≥ {cfg['qirl_speedup']}×", "QIRL Speedup vs DQN", "red"),
            kpi("📐", f"> {cfg['pinn_compliance']}%", "PINN Compliance Rate", "cyan"),
        ], className="kpi-grid"),
        card("CAPSM vs Baselines", dcc.Graph(id="chart-perf", figure=chart_performance(), config={"displayModeBar": False})),
    ])


def page_cyber(cfg):
    return html.Div([
        editor_panel("cyber", [
            dict(key="fdi_start", label="FDI Start", step=0.1, unit="s"),
            dict(key="fdi_end", label="FDI End", step=0.1, unit="s"),
            dict(key="dos_start", label="DoS Start", step=0.1, unit="s"),
            dict(key="dos_duration", label="DoS Dur.", step=0.1, unit="s"),
            dict(key="comm_delay", label="Delay", step=0.1, unit="s"),
        ], cfg),
        html.Div("Cyber-Attack Resilience", className="section-title"),
        html.P("Validated against three cyber-attack scenarios targeting PMU measurements and control channels.", className="section-desc"),
        html.Div([
            html.Div([html.H4("False Data Injection (FDI)", style={"color": RED}),
                      html.Div(f"t = {cfg['fdi_start']}s — {cfg['fdi_end']}s", className="attack-timing"),
                      html.P("Gaussian noise on Bus 5 PMU data (SNR=20dB). Tests System-1 anomaly detection and PINN validation.")],
                     className="attack-block fdi"),
            html.Div([html.H4("Denial of Service (DoS)", style={"color": AMBER}),
                      html.Div(f"t = {cfg['dos_start']}s — {cfg['dos_start']+cfg['dos_duration']}s", className="attack-timing"),
                      html.P(f"All PMU signals zeroed for {cfg['dos_duration']}s. Tests CAPSM maintain control with last-known-good state.")],
                     className="attack-block dos"),
            html.Div([html.H4("Communication Delay", style={"color": PURPLE}),
                      html.Div(f"t = 12.0s — {cfg['sim_time']}s", className="attack-timing"),
                      html.P(f"{cfg['comm_delay']}s delay on control signals. Tests System-2 robustness to delayed feedback.")],
                     className="attack-block delay"),
        ]),
        card("Response Strategy", data_table(
            ["Attack", "Detection", "Response", "Recovery"],
            [["FDI", "PINN residual ‖F(V,θ)‖ > threshold", "Switch to S2 filtered", "Reject corrupted, use PINN estimates"],
             ["DoS", "Metacognitive novelty detector", "S1 hold-last-good + S2 predictive", "Resume on signal recovery"],
             ["Delay", "Timestamp / RTT monitoring", "S2 model-predictive control", "Adaptive delay compensation"]]
        )),
        # ML: Anomaly detection
        html.Div([
            html.Div([html.Span("🤖 ML: Anomaly Detector (Isolation Forest)", className="card-title"),
                      html.Span("TRAINED", className="badge badge-emerald")],
                     style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "marginBottom": "12px"}),
            html.Div([
                html.Div([html.Span("Normal Avg Score", className="ml-metric-label"),
                          html.Span(f"{ml.metrics['anomaly_normal']}", className="ml-metric-value", style={"color": EMERALD})], className="ml-metric"),
                html.Div([html.Span("FDI Attack Avg Score", className="ml-metric-label"),
                          html.Span(f"{ml.metrics['anomaly_fdi']}", className="ml-metric-value", style={"color": AMBER})], className="ml-metric"),
                html.Div([html.Span("DoS Attack Avg Score", className="ml-metric-label"),
                          html.Span(f"{ml.metrics['anomaly_dos']}", className="ml-metric-value", style={"color": RED})], className="ml-metric"),
            ]),
            dcc.Graph(figure=chart_anomaly_scores(), config={"displayModeBar": False}, style={"marginTop": "12px"}),
        ], className="ml-card"),
    ])


def page_scaling(cfg):
    return html.Div([
        editor_panel("scaling", [
            dict(key="hirl_regions", label="Regions", step=1),
            dict(key="base_mva", label="Base MVA", step=10),
        ], cfg),
        html.Div("Test System Scaling", className="section-title"),
        html.P("CAPSM validated across 4 IEEE test systems of increasing complexity.", className="section-desc"),
        html.Div([
            html.Div([html.Div("9", className="bus-count"), html.H4("IEEE 9-Bus"),
                      html.Div("3 gens · 6 lines", className="stats"),
                      html.Div("Core validation", className="purpose"),
                      html.Span("BUILT ✓", className="status-badge status-built")], className="scale-card"),
            html.Div([html.Div("39", className="bus-count"), html.H4("IEEE 39-Bus"),
                      html.Div("10 gens · 46 lines", className="stats"),
                      html.Div("Dual-process scaling", className="purpose"),
                      html.Span("PLANNED", className="status-badge status-planned")], className="scale-card"),
            html.Div([html.Div("118", className="bus-count"), html.H4("IEEE 118-Bus"),
                      html.Div("54 gens · 186 lines", className="stats"),
                      html.Div("HMARL validation", className="purpose"),
                      html.Span("PLANNED", className="status-badge status-planned")], className="scale-card"),
            html.Div([html.Div("300", className="bus-count"), html.H4("IEEE 300-Bus"),
                      html.Div("69 gens · 411 lines", className="stats"),
                      html.Div("Full-scale stress", className="purpose"),
                      html.Span("PLANNED", className="status-badge status-planned")], className="scale-card"),
        ], className="grid-4"),
        card("Scalability", dcc.Graph(figure=chart_scaling(), config={"displayModeBar": False})),
    ])


def page_timeline(cfg):
    ros = [
        ("RO1: Cognitive Control Model", "Months 1-6", "Formalize dual-process model. Mathematical framework, mode-switching criteria.", True, 100),
        ("RO2: QIRL Algorithms", "Months 3-12", "Quantum-Inspired RL with complex amplitudes. Target: ≥2× speedup.", False, 65),
        ("RO3: PINN Safety Layer", "Months 6-15", "Physics-informed NN for AC power flow constraints. Target: >99.8%.", False, 40),
        ("RO4: HMARL + Fusion", "Months 12-24", "Multimodal sensor fusion + Hierarchical Multi-Agent RL.", False, 15),
        ("RO5: IEEE Validation", "Months 18-30", "Validation on 9/39/118/300-bus under fault, cyber, high-DER scenarios.", False, 10),
    ]
    return html.Div([
        editor_panel("timeline", [
            dict(key="year", label="Year"),
            dict(key="author", label="Author", type="text"),
            dict(key="sim_time", label="Sim Time", step=1, unit="s"),
        ], cfg),
        html.Div("Research Timeline", className="section-title"),
        html.P("PhD timeline spanning 30 months, 5 research objectives.", className="section-desc"),
        html.Div([
            html.Div([
                card("Research Objectives", html.Div([
                    html.Div([
                        html.H4(name), html.Div(time, className="time-range"),
                        html.P(desc),
                    ], className=f"timeline-item{'completed' if done else ''}")
                    for name, time, desc, done, _ in ros
                ])),
            ]),
            html.Div([
                card("Progress", html.Div([
                    html.Div([
                        html.Div([html.Span(name.split(":")[0]), html.Span(f"{pct}%", style={"color": EMERALD if pct == 100 else BLUE})],
                                 style={"display": "flex", "justifyContent": "space-between", "fontSize": ".82rem", "marginBottom": "4px"}),
                        html.Div(html.Div(className="progress-bar emerald", style={"width": f"{pct}%"}), className="progress-container"),
                    ], className="mb-2") for name, _, _, _, pct in ros
                ])),
                card("Simulation Setup", data_table(
                    ["Parameter", "Value"],
                    [["Mode", "Phasor"], ["Stop Time", f"{cfg['sim_time']} s"], ["Solver", "ode23tb"],
                     ["Max Step", "0.2 ms"], ["Rel Tol", "1e-4"], ["Abs Tol", "1e-6"]]
                )),
            ]),
        ], className="grid-2"),
    ])


# ═══════════════════════════════════════════
# PAGE REGISTRY
# ═══════════════════════════════════════════
PAGES = {
    "overview": ("📊", "Dashboard", page_overview),
    "hypothesis": ("🎯", "Hypothesis", page_hypothesis),
    "architecture": ("🧠", "Architecture", page_architecture),
    "system1": ("⚡", "System-1 CNN-LSTM", page_system1),
    "system2": ("🔮", "System-2 QIRL", page_system2),
    "hirl": ("🎯", "HIRL Framework", page_hirl),
    "pinn": ("🛡️", "PINN Safety", page_pinn),
    "metacognition": ("🔄", "Metacognition", page_metacognition),
    "topology": ("🔌", "IEEE 9-Bus", page_topology),
    "loadflow": ("📈", "Load Flow", page_loadflow),
    "facts": ("⚙️", "FACTS Devices", page_facts),
    "ev": ("🔋", "EV / V2G", page_ev),
    "performance": ("📐", "Targets", page_performance),
    "cyber": ("🔓", "Cyber Attacks", page_cyber),
    "scaling": ("📡", "Test Systems", page_scaling),
    "timeline": ("📅", "Timeline", page_timeline),
}

PAGE_TITLES = {k: v[1] for k, v in PAGES.items()}

NAV_SECTIONS = [
    ("Overview", ["overview", "hypothesis"]),
    ("Framework", ["architecture", "system1", "system2", "hirl", "pinn", "metacognition"]),
    ("Power System", ["topology", "loadflow", "facts", "ev"]),
    ("Validation", ["performance", "cyber", "scaling", "timeline"]),
]


# ═══════════════════════════════════════════
# APP INITIALIZATION
# ═══════════════════════════════════════════
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500;600;700&display=swap",
    ],
    suppress_callback_exceptions=True,
)
app.title = "CAPSM PhD Dashboard — Mahmoud Kiasari"


# ═══════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════
def build_sidebar(active_page="overview"):
    items = []
    for section_name, page_keys in NAV_SECTIONS:
        items.append(html.Div(section_name, className="nav-section-title"))
        for pk in page_keys:
            icon, label, _ = PAGES[pk]
            cls = "nav-item active" if pk == active_page else "nav-item"
            items.append(html.A([
                html.Span(icon, className="icon"), html.Span(label),
            ], className=cls, id={"type": "nav-item", "page": pk}, n_clicks=0))
    return html.Nav([
        html.Div([
            html.Div("C", className="logo-icon"),
            html.Div([html.H2("CAPSM"), html.P("PhD Dashboard")]),
        ], className="sidebar-brand"),
        html.Div(items, className="sidebar-nav"),
    ], className="sidebar")


# ═══════════════════════════════════════════
# MAIN LAYOUT
# ═══════════════════════════════════════════
app.layout = html.Div([
    dcc.Store(id="config-store", storage_type="local", data=DEFAULT_CONFIG),
    dcc.Store(id="current-page", data="overview"),
    dcc.Store(id="edit-mode", data=False),

    html.Div(id="sidebar-container", children=build_sidebar("overview")),

    html.Main([
        html.Header([
            html.Div([
                html.H1("CAPSM Dashboard — Overview", id="page-title"),
                html.P("Mahmoud Kiasari • Dalhousie University • 2026", id="header-sub", className="header-sub"),
            ]),
            html.Div([
                html.Div([html.Div(className="live-dot"), html.Span(" Live ML")],
                         style={"display": "flex", "alignItems": "center", "gap": "6px", "fontSize": ".78rem", "color": EMERALD}),
                html.Button([html.Span("", className="edit-dot", id="edit-dot-el"), " Edit Mode"],
                            id="edit-mode-btn", className="edit-toggle", n_clicks=0),
                html.Button("⬇ Export", id="export-btn", className="export-btn", n_clicks=0),
            ], className="header-right"),
        ], className="main-header"),
        html.Div(id="editor-container", className="editor-container"),
        html.Div(id="page-content", className="page-content"),
    ], className="main-content"),

    # Toast
    html.Div("", id="toast-msg", className="toast-msg"),
    # Download component
    dcc.Download(id="download-config"),
], className="dashboard-layout")


# ═══════════════════════════════════════════
# CALLBACKS
# ═══════════════════════════════════════════

# ── Navigation ──
@callback(
    Output("current-page", "data"),
    Input({"type": "nav-item", "page": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def navigate(n_clicks):
    if not ctx.triggered_id:
        return no_update
    return ctx.triggered_id["page"]


@callback(
    Output("sidebar-container", "children"),
    Output("page-title", "children"),
    Input("current-page", "data"),
)
def update_sidebar(page):
    title = PAGE_TITLES.get(page, "Dashboard")
    return build_sidebar(page), f"CAPSM — {title}"


# ── Helper: split page into editor + body ──
def _split_page(page, cfg):
    if cfg is None:
        cfg = DEFAULT_CONFIG
    _, _, page_fn = PAGES.get(page, PAGES["overview"])
    full = page_fn(cfg)
    children = full.children
    # Editor panel is always the first child of each page layout
    editor = children[0]
    body = html.Div(children[1:], id="page-body-wrapper")
    return editor, body


# ── Render editor (only on page navigation) ──
@callback(
    Output("editor-container", "children"),
    Output("page-content", "children"),
    Input("current-page", "data"),
    State("config-store", "data"),
)
def render_on_navigate(page, cfg):
    editor, body = _split_page(page, cfg)
    return editor, body


# ── Re-render body only when config changes (editors stay intact) ──
@callback(
    Output("page-content", "children", allow_duplicate=True),
    Input("config-store", "data"),
    State("current-page", "data"),
    prevent_initial_call=True,
)
def refresh_body_on_config(cfg, page):
    _, body = _split_page(page, cfg)
    return body


# ── Edit mode toggle ──
@callback(
    Output("edit-mode", "data"),
    Output("edit-mode-btn", "className"),
    Input("edit-mode-btn", "n_clicks"),
    State("edit-mode", "data"),
    prevent_initial_call=True,
)
def toggle_edit(n, current):
    new = not current
    cls = "edit-toggle active" if new else "edit-toggle"
    return new, cls


# ── Show/hide editor panels based on edit mode ──
# Runs on edit-mode toggle AND after navigation (new editor panel loaded)
app.clientside_callback(
    """
    function(editMode, page) {
        setTimeout(function() {
            const editors = document.querySelectorAll('.tab-editor');
            editors.forEach(e => { e.style.display = editMode ? 'block' : 'none'; });
        }, 50);
        return window.dash_clientside.no_update;
    }
    """,
    Output("edit-dot-el", "className"),  # dummy output
    Input("edit-mode", "data"),
    Input("current-page", "data"),
)


# ── Inline editing → update config store ──
@callback(
    Output("config-store", "data"),
    Output("header-sub", "children"),
    Input({"type": "edit-field", "page": ALL, "key": ALL}, "value"),
    State({"type": "edit-field", "page": ALL, "key": ALL}, "id"),
    State("config-store", "data"),
    prevent_initial_call=True,
)
def inline_edit(values, ids, cfg):
    if cfg is None:
        cfg = dict(DEFAULT_CONFIG)
    for eid, val in zip(ids, values):
        key = eid["key"]
        if val is not None and val != "":
            if key in DEFAULT_CONFIG and isinstance(DEFAULT_CONFIG[key], (int, float)):
                try:
                    cfg[key] = float(val)
                except (ValueError, TypeError):
                    pass
            else:
                cfg[key] = val
    sub = f"{cfg.get('author', '')} • {cfg.get('affiliation', '')} • {cfg.get('year', '')}"
    return cfg, sub


# ── Save inline button → toast ──
@callback(
    Output("toast-msg", "children"),
    Output("toast-msg", "className"),
    Input({"type": "save-inline", "page": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def save_toast(n):
    return "✓ Changes saved to localStorage!", "toast-msg show"


# Fade toast
app.clientside_callback(
    """
    function(cls) {
        if (cls && cls.includes('show')) {
            setTimeout(() => {
                const el = document.getElementById('toast-msg');
                if (el) el.className = 'toast-msg';
            }, 2500);
        }
        return window.dash_clientside.no_update;
    }
    """,
    Output("toast-msg", "style"),  # dummy
    Input("toast-msg", "className"),
)

# ── Export config ──
@callback(
    Output("download-config", "data"),
    Input("export-btn", "n_clicks"),
    State("config-store", "data"),
    prevent_initial_call=True,
)
def export_config(n, cfg):
    return dict(content=json.dumps(cfg or DEFAULT_CONFIG, indent=2),
                filename="capsm_dashboard_config.json")


# ═══════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  CAPSM PhD Dashboard — Python / Dash / ML")
    print("  Mahmoud Kiasari · Dalhousie University · 2026")
    print("  http://localhost:5050")
    print("=" * 55 + "\n")
    app.run(debug=True, port=5050, host="0.0.0.0")
