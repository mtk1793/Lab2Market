/* ═══════════════════════════════════════════════════════════════
   CAPSM PhD Proposal Dashboard — Main JavaScript Module
   Author: Mahmoud Kiasari, Dalhousie University
   Charts (Chart.js), Navigation, Interactivity, Live Updates,
   HIRL Framework, Full Customization/Settings Panel
   ═══════════════════════════════════════════════════════════════ */

// ─── LocalStorage Config Key ───
const CONFIG_KEY = 'capsm_dashboard_config';

// ─── Default Config ───
const DEFAULT_CONFIG = {
    author: 'Mahmoud Kiasari',
    affiliation: 'Dalhousie University',
    degree: 'PhD Candidate',
    title: 'CAPSM: Cognitive Adaptive Power System Management',
    subtitle: 'A Dual-Process Metacognitive Framework for Resilient Power Grid Control',
    year: 2026,
    s1_response_ms: 5,
    s2_response_ms: 50,
    fault_accuracy: 96.8,
    pinn_compliance: 99.8,
    qirl_speedup: 2.0,
    max_violations: 0.2,
    base_mva: 100,
    base_kv: 230,
    frequency: 60,
    sim_time: 20,
    ev_fleet: 1000,
    ev_capacity_mw: 50,
    hirl_regions: 2,
    hirl_global_rate: 200,
    hirl_lr: 0.001,
    hirl_gamma: 0.99,
    hirl_epsilon: 0.01,
    tau_c: 0.7,
    tau_n: 2.0,
    tau_u: 0.3,
    dark_mode: true,
    show_live: true,
    auto_refresh: true,
    color_blue: '#2563eb',
    color_purple: '#8b5cf6',
    color_emerald: '#10b981',
    color_amber: '#f59e0b',
    fdi_start: 2.0,
    fdi_end: 5.0,
    dos_start: 8.0,
    dos_duration: 0.5,
    comm_delay: 1.5,
    notes: '',
};

// ─── Load Config from localStorage ───
function loadConfig() {
    try {
        const stored = localStorage.getItem(CONFIG_KEY);
        if (stored) {
            return { ...DEFAULT_CONFIG, ...JSON.parse(stored) };
        }
    } catch (e) { /* ignore parse errors */ }
    return { ...DEFAULT_CONFIG };
}

function saveConfigToStorage(cfg) {
    try {
        localStorage.setItem(CONFIG_KEY, JSON.stringify(cfg));
    } catch (e) { /* ignore quota errors */ }
}

let currentConfig = loadConfig();

// ─── Theme Colors (reactive to config) ───
const COLORS = {
    get blue()      { return currentConfig.color_blue || '#2563eb'; },
    get blueLight() { return lightenColor(currentConfig.color_blue || '#2563eb', 40); },
    get cyan()      { return '#06b6d4'; },
    get emerald()   { return currentConfig.color_emerald || '#10b981'; },
    get amber()     { return currentConfig.color_amber || '#f59e0b'; },
    get red()       { return '#ef4444'; },
    get purple()    { return currentConfig.color_purple || '#8b5cf6'; },
    get pink()      { return '#ec4899'; },
    text:       '#e8edf5',
    muted:      '#5a6d8a',
    grid:       'rgba(30, 58, 95, 0.3)',
    bg:         '#1a2332',
};

function lightenColor(hex, percent) {
    const num = parseInt(hex.replace('#', ''), 16);
    const amt = Math.round(2.55 * percent);
    const R = Math.min(255, (num >> 16) + amt);
    const G = Math.min(255, ((num >> 8) & 0x00FF) + amt);
    const B = Math.min(255, (num & 0x0000FF) + amt);
    return '#' + (0x1000000 + R * 0x10000 + G * 0x100 + B).toString(16).slice(1);
}

// Chart.js global defaults for dark theme
Chart.defaults.color = COLORS.muted;
Chart.defaults.borderColor = COLORS.grid;
Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.font.size = 11;
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.pointStyleWidth = 10;
Chart.defaults.plugins.legend.labels.padding = 16;
Chart.defaults.plugins.tooltip.backgroundColor = '#111827';
Chart.defaults.plugins.tooltip.borderColor = COLORS.grid;
Chart.defaults.plugins.tooltip.borderWidth = 1;
Chart.defaults.plugins.tooltip.padding = 10;
Chart.defaults.plugins.tooltip.cornerRadius = 8;

// ─── Navigation ───
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
        const page = item.getAttribute('data-page');
        if (!page) return;

        // Update active nav
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        item.classList.add('active');

        // Show page
        document.querySelectorAll('.section-page').forEach(p => p.classList.remove('active'));
        const target = document.getElementById('page-' + page);
        if (target) target.classList.add('active');

        // Update header
        const titles = {
            overview: 'CAPSM Dashboard — Overview',
            hypothesis: 'Central Hypothesis & Research Gaps',
            architecture: 'CAPSM Framework Architecture',
            system1: 'System-1: CNN-LSTM Reflexive Controller',
            system2: 'System-2: QIRL Deliberative Optimizer',
            hirl: 'HIRL: Hierarchical Integrated Reinforcement Learning',
            pinn: 'PINN Safety Layer',
            metacognition: 'Metacognitive Arbitration',
            topology: 'IEEE 9-Bus Topology',
            loadflow: 'Load Flow Analysis',
            facts: 'FACTS Devices',
            ev: 'EV/V2G Aggregator',
            performance: 'Performance Targets',
            cyber: 'Cyber-Attack Resilience',
            scaling: 'Test System Scaling',
            timeline: 'Research Timeline',
        };
        document.getElementById('page-title').textContent = titles[page] || 'CAPSM Dashboard';

        // Initialize charts for the page if not done
        initPageCharts(page);
    });
});

// ─── Chart Registry (avoid re-creating) ───
const chartInstances = {};

function getOrCreateChart(canvasId, config) {
    if (chartInstances[canvasId]) return chartInstances[canvasId];
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;
    chartInstances[canvasId] = new Chart(ctx, config);
    return chartInstances[canvasId];
}

function destroyChart(canvasId) {
    if (chartInstances[canvasId]) {
        chartInstances[canvasId].destroy();
        delete chartInstances[canvasId];
    }
}

// Page → canvas IDs mapping — needed so reinitPageCharts knows what to destroy
const PAGE_CHARTS = {
    overview:      ['chart-bus-voltages', 'chart-gen-dispatch', 'chart-gaps-radar'],
    system2:       ['chart-qirl-convergence'],
    hirl:          ['chart-hirl-convergence'],
    metacognition: ['chart-metacognition'],
    loadflow:      ['chart-loadflow-voltage', 'chart-loadflow-angle'],
    ev:            ['chart-ev-soc'],
    performance:   ['chart-performance-comparison'],
    scaling:       ['chart-scaling'],
};

// Destroy + recreate charts for a specific page
function reinitPageCharts(page) {
    // Destroy existing chart instances for this page first
    (PAGE_CHARTS[page] || []).forEach(id => destroyChart(id));
    initializedPages.delete(page);
    initPageCharts(page);
}

// Reinitialize all charts that have been visited — called after global settings save
function reinitAllInitializedCharts() {
    const pagesToReinit = [...initializedPages];
    initializedPages.clear();
    Object.keys(chartInstances).forEach(id => {
        chartInstances[id].destroy();
        delete chartInstances[id];
    });
    pagesToReinit.forEach(page => initPageCharts(page));
}

// ─── Initialize Charts per Page ───
const initializedPages = new Set();

function initPageCharts(page) {
    if (initializedPages.has(page)) return;
    initializedPages.add(page);

    switch (page) {
        case 'overview': initOverviewCharts(); break;
        case 'system2': initSystem2Charts(); break;
        case 'hirl': initHIRLCharts(); break;
        case 'metacognition': initMetacognitionChart(); break;
        case 'loadflow': initLoadFlowCharts(); break;
        case 'ev': initEVChart(); break;
        case 'performance': initPerformanceChart(); break;
        case 'scaling': initScalingChart(); break;
    }
}

// ─── Initialize overview on load ───
initPageCharts('overview');

// ═══════════════════════════════════════════
// OVERVIEW CHARTS
// ═══════════════════════════════════════════

function initOverviewCharts() {
    // Bus Voltage Bar Chart
    getOrCreateChart('chart-bus-voltages', {
        type: 'bar',
        data: {
            labels: ['Bus 1', 'Bus 2', 'Bus 3', 'Bus 4', 'Bus 5', 'Bus 6', 'Bus 7', 'Bus 8', 'Bus 9'],
            datasets: [{
                label: 'Voltage (pu)',
                data: [1.040, 1.025, 1.025, 1.026, 0.996, 1.013, 1.026, 1.016, 1.032],
                backgroundColor: [
                    COLORS.red, COLORS.red, COLORS.red,
                    COLORS.blue, COLORS.blue, COLORS.blue,
                    COLORS.blue, COLORS.blue, COLORS.blue
                ],
                borderColor: 'transparent',
                borderRadius: 6,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                annotation: {}
            },
            scales: {
                y: {
                    min: 0.95,
                    max: 1.08,
                    grid: { color: COLORS.grid },
                    ticks: { callback: v => v.toFixed(3) }
                },
                x: { grid: { display: false } }
            }
        }
    });

    // Generation Dispatch
    getOrCreateChart('chart-gen-dispatch', {
        type: 'bar',
        data: {
            labels: ['Gen 1 (Slack)', 'Gen 2 (PV)', 'Gen 3 (PV)'],
            datasets: [
                {
                    label: 'P (MW)',
                    data: [71.64, 163.0, 85.0],
                    backgroundColor: COLORS.blue,
                    borderRadius: 6,
                },
                {
                    label: 'Q (MVAR)',
                    data: [27.05, 6.65, -10.86],
                    backgroundColor: COLORS.purple,
                    borderRadius: 6,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                y: { grid: { color: COLORS.grid } },
                x: { grid: { display: false } }
            }
        }
    });

    // Radar Chart — Research Gap Coverage
    getOrCreateChart('chart-gaps-radar', {
        type: 'radar',
        data: {
            labels: [
                'G1: Dual-Speed',
                'G2: Sample Efficiency',
                'G3: Physics-Aware',
                'G4: Scalability',
                'G5: Cyber Resilience'
            ],
            datasets: [
                {
                    label: 'CAPSM Coverage',
                    data: [95, 88, 92, 78, 85],
                    borderColor: COLORS.blue,
                    backgroundColor: 'rgba(37, 99, 235, 0.15)',
                    pointBackgroundColor: COLORS.blue,
                    borderWidth: 2,
                },
                {
                    label: 'State-of-Art Baseline',
                    data: [45, 40, 35, 50, 30],
                    borderColor: COLORS.muted,
                    backgroundColor: 'rgba(90, 109, 138, 0.1)',
                    pointBackgroundColor: COLORS.muted,
                    borderWidth: 1,
                    borderDash: [4, 4],
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    grid: { color: COLORS.grid },
                    angleLines: { color: COLORS.grid },
                    pointLabels: { color: COLORS.text, font: { size: 10 } },
                    ticks: { display: false }
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// SYSTEM-2 CHARTS
// ═══════════════════════════════════════════

function initSystem2Charts() {
    // QIRL vs DQN Convergence
    const episodes = Array.from({length: 50}, (_, i) => (i + 1) * 20);
    const speedup = currentConfig.qirl_speedup || 2.0;
    const qirl_decay = Math.round(400 / speedup);
    const qirl_reward = episodes.map(e => -500 * Math.exp(-e / qirl_decay) + 100 + 5 * Math.random());
    const dqn_reward = episodes.map(e => -500 * Math.exp(-e / 400) + 80 + 8 * Math.random());
    const ppo_reward = episodes.map(e => -500 * Math.exp(-e / 350) + 90 + 6 * Math.random());

    getOrCreateChart('chart-qirl-convergence', {
        type: 'line',
        data: {
            labels: episodes,
            datasets: [
                {
                    label: 'QIRL (Proposed)',
                    data: qirl_reward,
                    borderColor: COLORS.purple,
                    backgroundColor: 'rgba(139, 92, 246, 0.1)',
                    fill: true,
                    tension: 0.4,
                    borderWidth: 2.5,
                    pointRadius: 0,
                },
                {
                    label: 'DQN Baseline',
                    data: dqn_reward,
                    borderColor: COLORS.muted,
                    borderDash: [6, 4],
                    tension: 0.4,
                    borderWidth: 1.5,
                    pointRadius: 0,
                },
                {
                    label: 'PPO Baseline',
                    data: ppo_reward,
                    borderColor: COLORS.amber,
                    borderDash: [3, 3],
                    tension: 0.4,
                    borderWidth: 1.5,
                    pointRadius: 0,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                x: {
                    title: { display: true, text: 'Episodes', color: COLORS.muted },
                    grid: { color: COLORS.grid }
                },
                y: {
                    title: { display: true, text: 'Cumulative Reward', color: COLORS.muted },
                    grid: { color: COLORS.grid }
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// METACOGNITION CHART
// ═══════════════════════════════════════════

function initMetacognitionChart() {
    const t = Array.from({length: 200}, (_, i) => (i * 0.1).toFixed(1));
    const confidence = t.map(v => 0.5 + 0.4 * Math.sin(2 * Math.PI * 0.03 * v) + 0.05 * Math.random());
    const urgency = t.map(v => {
        const base = 0.2 + 0.15 * Math.abs(Math.sin(2 * Math.PI * 0.07 * v));
        // Fault spike at t≈1s
        if (v >= 0.9 && v <= 1.5) return Math.min(1, base + 0.6);
        // DoS at t≈8s
        if (v >= 7.5 && v <= 9.0) return Math.min(1, base + 0.4);
        return base;
    });
    const mode = confidence.map((c, i) => (c > 0.7 && urgency[i] > 0.3) ? 1 : 0);

    getOrCreateChart('chart-metacognition', {
        type: 'line',
        data: {
            labels: t,
            datasets: [
                {
                    label: 'Confidence (Cₜ)',
                    data: confidence,
                    borderColor: COLORS.blue,
                    tension: 0.3,
                    borderWidth: 1.5,
                    pointRadius: 0,
                    yAxisID: 'y',
                },
                {
                    label: 'Urgency (Uₜ)',
                    data: urgency,
                    borderColor: COLORS.red,
                    tension: 0.3,
                    borderWidth: 1.5,
                    pointRadius: 0,
                    yAxisID: 'y',
                },
                {
                    label: 'Mode (1=S1, 0=S2)',
                    data: mode,
                    borderColor: COLORS.amber,
                    backgroundColor: 'rgba(245, 158, 11, 0.1)',
                    fill: true,
                    stepped: true,
                    borderWidth: 2,
                    pointRadius: 0,
                    yAxisID: 'y1',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
            plugins: { legend: { position: 'top' } },
            scales: {
                x: {
                    title: { display: true, text: 'Time (s)', color: COLORS.muted },
                    grid: { color: COLORS.grid },
                    ticks: { maxTicksLimit: 20 }
                },
                y: {
                    title: { display: true, text: 'Metric Value', color: COLORS.muted },
                    min: 0,
                    max: 1.1,
                    grid: { color: COLORS.grid },
                    position: 'left',
                },
                y1: {
                    title: { display: true, text: 'Mode', color: COLORS.amber },
                    min: -0.2,
                    max: 1.5,
                    grid: { display: false },
                    position: 'right',
                    ticks: {
                        callback: v => v === 1 ? 'S1' : v === 0 ? 'S2' : ''
                    }
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// LOAD FLOW CHARTS
// ═══════════════════════════════════════════

function initLoadFlowCharts() {
    const buses = ['Bus 1', 'Bus 2', 'Bus 3', 'Bus 4', 'Bus 5', 'Bus 6', 'Bus 7', 'Bus 8', 'Bus 9'];
    const voltages = [1.040, 1.025, 1.025, 1.026, 0.996, 1.013, 1.026, 1.016, 1.032];
    const angles = [0.0, 9.28, 4.665, -2.217, -3.989, -3.688, 3.72, 0.728, 1.967];

    getOrCreateChart('chart-loadflow-voltage', {
        type: 'line',
        data: {
            labels: buses,
            datasets: [{
                label: 'V (pu)',
                data: voltages,
                borderColor: COLORS.blue,
                backgroundColor: 'rgba(37, 99, 235, 0.15)',
                fill: true,
                tension: 0.3,
                pointBackgroundColor: COLORS.blue,
                pointRadius: 5,
                borderWidth: 2,
            }, {
                label: 'V_max (1.10 pu)',
                data: Array(9).fill(1.10),
                borderColor: COLORS.red,
                borderDash: [6, 4],
                borderWidth: 1,
                pointRadius: 0,
            }, {
                label: 'V_min (0.90 pu)',
                data: Array(9).fill(0.90),
                borderColor: COLORS.red,
                borderDash: [6, 4],
                borderWidth: 1,
                pointRadius: 0,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0.88, max: 1.12, grid: { color: COLORS.grid } },
                x: { grid: { display: false } }
            }
        }
    });

    getOrCreateChart('chart-loadflow-angle', {
        type: 'bar',
        data: {
            labels: buses,
            datasets: [{
                label: 'Angle (°)',
                data: angles,
                backgroundColor: angles.map(a => a >= 0 ? COLORS.cyan : COLORS.amber),
                borderRadius: 6,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: {
                    grid: { color: COLORS.grid },
                    title: { display: true, text: 'Angle (degrees)', color: COLORS.muted }
                },
                x: { grid: { display: false } }
            }
        }
    });
}

// ═══════════════════════════════════════════
// EV/V2G CHART
// ═══════════════════════════════════════════

function initEVChart() {
    const t = Array.from({length: 200}, (_, i) => (i * 0.1).toFixed(1));
    const soc = [];
    let s = 0.70;
    const capMW = (currentConfig.ev_capacity_mw || 50) * 1e6;
    for (let i = 0; i < 200; i++) {
        const dt = 0.1;
        const P = (0.6 - s) * capMW;
        const Pclamp = Math.max(-capMW, Math.min(capMW, P));
        s += -0.95 * Pclamp / (capMW * 3) * dt * 0.05;
        s = Math.max(0.20, Math.min(0.95, s));
        soc.push(s);
    }

    getOrCreateChart('chart-ev-soc', {
        type: 'line',
        data: {
            labels: t,
            datasets: [{
                label: 'SoC',
                data: soc,
                borderColor: COLORS.cyan,
                backgroundColor: 'rgba(6, 182, 212, 0.1)',
                fill: true,
                tension: 0.4,
                pointRadius: 0,
                borderWidth: 2,
            }, {
                label: 'SoC Max (0.95)',
                data: Array(200).fill(0.95),
                borderColor: COLORS.red,
                borderDash: [6, 4],
                borderWidth: 1,
                pointRadius: 0,
            }, {
                label: 'SoC Min (0.20)',
                data: Array(200).fill(0.20),
                borderColor: COLORS.red,
                borderDash: [6, 4],
                borderWidth: 1,
                pointRadius: 0,
            }, {
                label: 'SoC Target (0.60)',
                data: Array(200).fill(0.60),
                borderColor: COLORS.amber,
                borderDash: [3, 3],
                borderWidth: 1,
                pointRadius: 0,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                x: {
                    title: { display: true, text: 'Time (s)', color: COLORS.muted },
                    grid: { color: COLORS.grid },
                    ticks: { maxTicksLimit: 20 }
                },
                y: {
                    min: 0, max: 1,
                    title: { display: true, text: 'State of Charge (pu)', color: COLORS.muted },
                    grid: { color: COLORS.grid }
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// PERFORMANCE COMPARISON CHART
// ═══════════════════════════════════════════

function initPerformanceChart() {
    getOrCreateChart('chart-performance-comparison', {
        type: 'bar',
        data: {
            labels: ['Response Time\n(S1, ms)', 'Decision Cycle\n(S2, ms)', 'Constraint\nViolations (%)', 'Fault Detection\nAccuracy (%)', 'Convergence\nSpeed (×)'],
            datasets: [
                {
                    label: 'CAPSM (Target)',
                    data: [
                        currentConfig.s1_response_ms || 5,
                        currentConfig.s2_response_ms || 50,
                        currentConfig.max_violations || 0.2,
                        currentConfig.fault_accuracy || 96.8,
                        currentConfig.qirl_speedup || 2.0
                    ],
                    backgroundColor: COLORS.blue,
                    borderRadius: 6,
                },
                {
                    label: 'DQN Baseline',
                    data: [25, 200, 3.5, 88.0, 1.0],
                    backgroundColor: COLORS.muted,
                    borderRadius: 6,
                },
                {
                    label: 'PPO Baseline',
                    data: [18, 150, 2.1, 91.5, 1.3],
                    backgroundColor: COLORS.amber,
                    borderRadius: 6,
                },
                {
                    label: 'Traditional PID',
                    data: [2, 500, 5.0, 75.0, 0.5],
                    backgroundColor: 'rgba(90, 109, 138, 0.5)',
                    borderRadius: 6,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                y: { grid: { color: COLORS.grid } },
                x: { grid: { display: false } }
            }
        }
    });
}

// ═══════════════════════════════════════════
// SCALING CHART
// ═══════════════════════════════════════════

function initScalingChart() {
    getOrCreateChart('chart-scaling', {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Buses',
                    data: [
                        {x: 9, y: 3},
                        {x: 39, y: 10},
                        {x: 118, y: 54},
                        {x: 300, y: 69}
                    ],
                    backgroundColor: COLORS.blue,
                    pointRadius: 12,
                    pointHoverRadius: 16,
                },
                {
                    label: 'Lines',
                    data: [
                        {x: 9, y: 6},
                        {x: 39, y: 46},
                        {x: 118, y: 186},
                        {x: 300, y: 411}
                    ],
                    backgroundColor: COLORS.cyan,
                    pointRadius: 8,
                    pointHoverRadius: 12,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' },
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            const busNames = {9: 'IEEE 9-Bus', 39: 'IEEE 39-Bus', 118: 'IEEE 118-Bus', 300: 'IEEE 300-Bus'};
                            return `${busNames[ctx.raw.x] || ''}: ${ctx.dataset.label} = ${ctx.raw.y}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Number of Buses', color: COLORS.muted },
                    grid: { color: COLORS.grid },
                    type: 'logarithmic',
                },
                y: {
                    title: { display: true, text: 'Count', color: COLORS.muted },
                    grid: { color: COLORS.grid },
                    type: 'logarithmic',
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// HIRL CHARTS
// ═══════════════════════════════════════════

function initHIRLCharts() {
    const episodes = Array.from({length: 60}, (_, i) => (i + 1) * 5000);

    // HIRL regional convergence vs baselines
    const hirlReward = episodes.map(e => -400 * Math.exp(-e / 80000) + 90 + 4 * Math.random());
    const centralReward = episodes.map(e => -400 * Math.exp(-e / 200000) + 70 + 6 * Math.random());
    const indepReward = episodes.map(e => -400 * Math.exp(-e / 120000) + 75 + 5 * Math.random());
    const dqnReward = episodes.map(e => -400 * Math.exp(-e / 160000) + 60 + 8 * Math.random());

    getOrCreateChart('chart-hirl-convergence', {
        type: 'line',
        data: {
            labels: episodes.map(e => (e/1000) + 'k'),
            datasets: [
                {
                    label: 'HIRL (Proposed)',
                    data: hirlReward,
                    borderColor: COLORS.purple,
                    backgroundColor: 'rgba(139, 92, 246, 0.1)',
                    fill: true,
                    tension: 0.4,
                    borderWidth: 2.5,
                    pointRadius: 0,
                },
                {
                    label: 'Centralized RL',
                    data: centralReward,
                    borderColor: COLORS.muted,
                    borderDash: [6, 4],
                    tension: 0.4,
                    borderWidth: 1.5,
                    pointRadius: 0,
                },
                {
                    label: 'Independent Agents',
                    data: indepReward,
                    borderColor: COLORS.amber,
                    borderDash: [3, 3],
                    tension: 0.4,
                    borderWidth: 1.5,
                    pointRadius: 0,
                },
                {
                    label: 'DQN Baseline',
                    data: dqnReward,
                    borderColor: COLORS.red,
                    borderDash: [8, 4],
                    tension: 0.4,
                    borderWidth: 1.5,
                    pointRadius: 0,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: {
                x: {
                    title: { display: true, text: 'Training Episodes', color: COLORS.muted },
                    grid: { color: COLORS.grid },
                    ticks: { maxTicksLimit: 12 }
                },
                y: {
                    title: { display: true, text: 'Cumulative Reward (Regional Avg)', color: COLORS.muted },
                    grid: { color: COLORS.grid }
                }
            }
        }
    });
}

// ═══════════════════════════════════════════
// TOPOLOGY INTERACTIONS
// ═══════════════════════════════════════════

document.querySelectorAll('.bus-node').forEach(node => {
    node.addEventListener('mouseenter', function() {
        const id = this.id;
        const busData = {
            'node-gen1': 'Gen 1: V=1.040 pu, P=71.64 MW, Q=27.05 MVAR (Slack)',
            'node-gen2': 'Gen 2: V=1.025 pu, P=163.0 MW, Q=6.65 MVAR (PV)',
            'node-gen3': 'Gen 3: V=1.025 pu, P=85.0 MW, Q=-10.86 MVAR (PV)',
            'node-bus4': 'Bus 4: V=1.026 pu, θ=-2.217°',
            'node-bus5': 'Bus 5: V=0.996 pu, θ=-3.989°, Load=125+j50 MVA, SVC ±100 MVAR',
            'node-bus6': 'Bus 6: V=1.013 pu, θ=-3.688°, Load=90+j30 MVA',
            'node-bus7': 'Bus 7: V=1.026 pu, θ=3.720°',
            'node-bus8': 'Bus 8: V=1.016 pu, θ=0.728°, Load=100+j35 MVA, STATCOM ±50 MVAR, EV/V2G 50MW',
            'node-bus9': 'Bus 9: V=1.032 pu, θ=1.967°',
        };
        if (busData[id]) {
            this.setAttribute('title', busData[id]);
        }
    });
});

// ═══════════════════════════════════════════
// THEME TOGGLE
// ═══════════════════════════════════════════

function toggleTheme() {
    const isDark = document.body.classList.toggle('light-theme');
    currentConfig.dark_mode = !isDark;
    saveConfigToStorage(currentConfig);
    const el = document.getElementById('cfg-dark-mode');
    if (el) el.checked = currentConfig.dark_mode;
}

// ═══════════════════════════════════════════
// SETTINGS PANEL — Open / Close
// ═══════════════════════════════════════════

function openSettings() {
    document.getElementById('settings-panel').classList.add('open');
    document.getElementById('settings-overlay').classList.add('open');
    populateSettingsForm(currentConfig);
}

function closeSettings() {
    document.getElementById('settings-panel').classList.remove('open');
    document.getElementById('settings-overlay').classList.remove('open');
}

// Populate all settings form fields from config object
function populateSettingsForm(cfg) {
    document.querySelectorAll('[data-cfg]').forEach(el => {
        const key = el.getAttribute('data-cfg');
        if (cfg[key] !== undefined) {
            if (el.type === 'checkbox') {
                el.checked = cfg[key];
            } else {
                el.value = cfg[key];
            }
        }
    });
}

// Read all settings form fields into a config object
function readSettingsForm() {
    const cfg = {};
    document.querySelectorAll('[data-cfg]').forEach(el => {
        const key = el.getAttribute('data-cfg');
        if (el.type === 'checkbox') {
            cfg[key] = el.checked;
        } else if (el.type === 'number') {
            cfg[key] = parseFloat(el.value);
        } else {
            cfg[key] = el.value;
        }
    });
    return cfg;
}

// ═══════════════════════════════════════════
// SETTINGS — Save / Reset / Clear
// ═══════════════════════════════════════════

function saveSettings() {
    const newCfg = readSettingsForm();
    currentConfig = { ...currentConfig, ...newCfg };
    saveConfigToStorage(currentConfig);
    applyConfig(currentConfig);
    // Also sync to inline editors
    populateAllInlineEditors();
    showToast('Settings saved successfully!');
    // Also persist to server (optional, for export)
    fetch('/api/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentConfig)
    }).catch(() => {});
}

function resetSettings() {
    currentConfig = { ...DEFAULT_CONFIG };
    saveConfigToStorage(currentConfig);
    populateSettingsForm(currentConfig);
    populateAllInlineEditors();
    applyConfig(currentConfig);
    showToast('Settings reset to defaults');
}

function clearAll() {
    localStorage.removeItem(CONFIG_KEY);
    currentConfig = { ...DEFAULT_CONFIG };
    populateSettingsForm(currentConfig);
    populateAllInlineEditors();
    applyConfig(currentConfig);
    showToast('All customizations cleared');
}

function exportConfig() {
    const blob = new Blob([JSON.stringify(currentConfig, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'capsm_dashboard_config.json';
    a.click();
    URL.revokeObjectURL(url);
    showToast('Config exported as JSON');
}

function showToast(msg) {
    const toast = document.getElementById('settings-toast');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
}

// ═══════════════════════════════════════════
// APPLY CONFIG — Update Dashboard Content Dynamically
// ═══════════════════════════════════════════

function applyConfig(cfg) {
    // Update header
    const headerSubtext = document.querySelector('.header-left p');
    if (headerSubtext) {
        headerSubtext.textContent = `${cfg.author} • ${cfg.affiliation} • ${cfg.year}`;
    }

    // Update CSS custom properties for accent colors
    const root = document.documentElement;
    if (cfg.color_blue) {
        root.style.setProperty('--accent-blue', cfg.color_blue);
        root.style.setProperty('--border-glow', cfg.color_blue);
        root.style.setProperty('--accent-blue-light', lightenColor(cfg.color_blue, 40));
    }
    if (cfg.color_purple) {
        root.style.setProperty('--accent-purple', cfg.color_purple);
    }
    if (cfg.color_emerald) {
        root.style.setProperty('--accent-emerald', cfg.color_emerald);
    }
    if (cfg.color_amber) {
        root.style.setProperty('--accent-amber', cfg.color_amber);
    }

    // Dark/light mode
    if (cfg.dark_mode === false) {
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
    }

    // Live indicators
    if (cfg.show_live === false) {
        document.querySelectorAll('.live-indicator').forEach(el => el.style.display = 'none');
    } else {
        document.querySelectorAll('.live-indicator').forEach(el => el.style.display = '');
    }

    // Auto-refresh
    if (cfg.auto_refresh === false && liveInterval) {
        clearInterval(liveInterval);
        liveInterval = null;
    } else if (cfg.auto_refresh !== false && !liveInterval) {
        startLiveUpdates();
    }

    // Update all editable KPI values on overview page
    updateKPIValues(cfg);

    // Reinitialize charts so they pick up new config values
    reinitAllInitializedCharts();
}

function updateKPIValues(cfg) {
    // Find KPI cards and update values based on config
    const kpiMap = {
        'System-1 Response Time': `< ${cfg.s1_response_ms} ms`,
        'System-2 Decision Cycle': `< ${cfg.s2_response_ms} ms`,
        'PINN Constraint Compliance': `${cfg.pinn_compliance}%`,
        'Fault Detection Accuracy': `${cfg.fault_accuracy}%`,
        'QIRL Speedup vs DQN': `${cfg.qirl_speedup}×`,
    };
    document.querySelectorAll('.kpi-card').forEach(card => {
        const label = card.querySelector('.kpi-label');
        const value = card.querySelector('.kpi-value');
        if (label && value && kpiMap[label.textContent]) {
            value.textContent = kpiMap[label.textContent];
        }
    });
}

// Apply config on page load
applyConfig(currentConfig);

// ═══════════════════════════════════════════
// LIVE DATA UPDATES (from Flask API)
// ═══════════════════════════════════════════

let liveInterval = null;

async function fetchLiveData() {
    try {
        const [voltRes, freqRes, modeRes] = await Promise.all([
            fetch('/api/live/bus_voltages').then(r => r.json()).catch(() => null),
            fetch('/api/live/frequency').then(r => r.json()).catch(() => null),
            fetch('/api/live/capsm_mode').then(r => r.json()).catch(() => null),
        ]);

        // Update live indicators if elements exist
        if (voltRes) {
            const el = document.getElementById('live-voltage');
            if (el) el.textContent = voltRes.voltages.Bus_5?.toFixed(4) || '—';
            // Update bus voltage chart live
            const bvChart = chartInstances['chart-bus-voltages'];
            if (bvChart) {
                const busKeys = ['Bus_1','Bus_2','Bus_3','Bus_4','Bus_5','Bus_6','Bus_7','Bus_8','Bus_9'];
                bvChart.data.datasets[0].data = busKeys.map(k => voltRes.voltages[k] || 0);
                bvChart.update('none');
            }
        }
        if (freqRes) {
            const el = document.getElementById('live-frequency');
            if (el) el.textContent = freqRes.frequency?.toFixed(3) + ' Hz' || '—';
        }
        if (modeRes) {
            const el = document.getElementById('live-mode');
            if (el) el.textContent = modeRes.mode || '—';
        }
    } catch (e) {
        // Silent fail — API may not be running
    }
}

// Start live updates (every 2 seconds, only if server is running)
function startLiveUpdates() {
    if (liveInterval) return;
    liveInterval = setInterval(fetchLiveData, 2000);
}

// Check if server is running
fetch('/api/overview')
    .then(r => { if (r.ok) startLiveUpdates(); })
    .catch(() => { /* Static mode — no server */ });

// ═══════════════════════════════════════════
// ANIMATED COUNTERS
// ═══════════════════════════════════════════

function animateValue(el, start, end, duration) {
    const range = end - start;
    const startTime = performance.now();
    function update(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        el.textContent = (start + range * eased).toFixed(1);
        if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
}

// ═══════════════════════════════════════════
// PER-TAB INLINE EDITING — Edit Mode Toggle
// ═══════════════════════════════════════════

let editModeActive = false;

function toggleEditMode() {
    editModeActive = !editModeActive;
    document.body.classList.toggle('edit-mode', editModeActive);
    const btn = document.getElementById('edit-mode-btn');
    if (btn) btn.classList.toggle('active', editModeActive);

    if (editModeActive) {
        populateAllInlineEditors();
        showToast('Edit Mode ON — change values inline, see real-time updates');
    } else {
        showToast('Edit Mode OFF');
    }
}

// Populate all inline editor fields with current config values
function populateAllInlineEditors() {
    document.querySelectorAll('.tab-editor [data-cfg]').forEach(el => {
        const key = el.getAttribute('data-cfg');
        if (currentConfig[key] !== undefined) {
            if (el.type === 'checkbox') {
                el.checked = currentConfig[key];
            } else {
                el.value = currentConfig[key];
            }
        }
    });
}

// Save inline edits (persists to localStorage & server)
function saveInline() {
    // Read all inline editor fields
    document.querySelectorAll('.tab-editor [data-cfg]').forEach(el => {
        const key = el.getAttribute('data-cfg');
        if (el.type === 'checkbox') {
            currentConfig[key] = el.checked;
        } else if (el.type === 'number') {
            currentConfig[key] = parseFloat(el.value);
        } else {
            currentConfig[key] = el.value;
        }
    });

    saveConfigToStorage(currentConfig);
    applyConfig(currentConfig);

    // Also sync to global settings panel inputs
    populateSettingsForm(currentConfig);

    // Persist to server
    fetch('/api/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentConfig)
    }).catch(() => {});

    showToast('Changes saved!');
}

// ═══════════════════════════════════════════
// REAL-TIME INLINE EDITING — Live Preview
// ═══════════════════════════════════════════

// Listen for input events on all inline editor fields
document.addEventListener('input', function(e) {
    const el = e.target;
    if (!el.hasAttribute('data-cfg') || !el.hasAttribute('data-live')) return;

    const key = el.getAttribute('data-cfg');
    let value;
    if (el.type === 'checkbox') {
        value = el.checked;
    } else if (el.type === 'number') {
        value = parseFloat(el.value);
        if (isNaN(value)) return;
    } else {
        value = el.value;
    }

    // Update config in memory
    currentConfig[key] = value;

    // Visual feedback: mark field as changed
    el.classList.add('changed');
    setTimeout(() => el.classList.remove('changed'), 800);

    // Sync same data-cfg fields in other editors (e.g., s1_response_ms appears on multiple tabs)
    document.querySelectorAll(`.tab-editor [data-cfg="${key}"]`).forEach(other => {
        if (other !== el) {
            if (other.type === 'checkbox') other.checked = value;
            else other.value = value;
        }
    });

    // Also sync to global settings panel
    document.querySelectorAll(`#settings-panel [data-cfg="${key}"]`).forEach(other => {
        if (other.type === 'checkbox') other.checked = value;
        else other.value = value;
    });

    // Apply real-time live updates to dashboard content
    applyLiveInlineUpdate(key, value);
});

// Apply a single config change in real-time to visible dashboard content
function applyLiveInlineUpdate(key, value) {
    // Save to localStorage continuously for persistence
    saveConfigToStorage(currentConfig);

    // --- Header info ---
    if (key === 'author' || key === 'affiliation' || key === 'year') {
        const sub = document.querySelector('.header-left p');
        if (sub) sub.textContent = `${currentConfig.author} • ${currentConfig.affiliation} • ${currentConfig.year}`;
    }

    // --- KPI cards (overview + performance pages) ---
    const kpiMap = {
        s1_response_ms: { label: 'System-1 Response Time', fmt: v => `< ${v} ms` },
        s2_response_ms: { label: 'System-2 Decision Cycle', fmt: v => `< ${v} ms` },
        pinn_compliance: { label: 'PINN Constraint Compliance', fmt: v => `${v}%` },
        fault_accuracy: { label: 'Fault Detection Accuracy', fmt: v => `${v}%` },
        qirl_speedup: { label: 'QIRL Speedup vs DQN', fmt: v => `${v}×` },
        max_violations: { label: 'Constraint Violations', fmt: v => `< ${v}%` },
    };

    if (kpiMap[key]) {
        document.querySelectorAll('.kpi-card').forEach(card => {
            const label = card.querySelector('.kpi-label');
            const val = card.querySelector('.kpi-value');
            if (label && val && label.textContent === kpiMap[key].label) {
                val.textContent = kpiMap[key].fmt(value);
                flashElement(val);
            }
        });
    }

    // Also update PINN compliance labels across pages  
    if (key === 'pinn_compliance') {
        document.querySelectorAll('.kpi-card').forEach(card => {
            const label = card.querySelector('.kpi-label');
            const val = card.querySelector('.kpi-value');
            if (label && val && label.textContent === 'PINN Compliance Rate') {
                val.textContent = `> ${value}%`;
                flashElement(val);
            }
        });
    }

    // --- EV stats ---
    if (key === 'ev_fleet' || key === 'ev_capacity_mw') {
        const evStats = document.querySelectorAll('.ev-stat');
        evStats.forEach(stat => {
            const label = stat.querySelector('.label');
            const val = stat.querySelector('.value');
            if (!label || !val) return;
            if (key === 'ev_fleet' && label.textContent === 'EV Fleet Size') {
                val.textContent = Number(value).toLocaleString();
                flashElement(val);
            }
            if (key === 'ev_capacity_mw' && label.textContent === 'Total Capacity') {
                val.textContent = `${value} MW`;
                flashElement(val);
            }
        });
        // Update section description too
        const evDesc = document.querySelector('#page-ev .section-desc');
        if (evDesc) {
            evDesc.textContent = `Vehicle-to-Grid fleet at Bus 8 — ${Number(currentConfig.ev_fleet).toLocaleString()} EVs × ${Math.round(currentConfig.ev_capacity_mw * 1000 / currentConfig.ev_fleet)} kW = ${currentConfig.ev_capacity_mw} MW bidirectional capacity. Controlled by CAPSM System-2 QIRL for economic optimization.`;
        }
    }

    // --- Cyber attack timings ---
    if (['fdi_start', 'fdi_end', 'dos_start', 'dos_duration', 'comm_delay'].includes(key)) {
        updateCyberTimings();
    }

    // --- Metacognition thresholds ---
    if (['tau_c', 'tau_n', 'tau_u'].includes(key)) {
        updateMetacognitionThresholds();
    }

    // --- Topology description ---
    if (['base_mva', 'base_kv', 'frequency'].includes(key)) {
        const topoDesc = document.querySelector('#page-topology .section-desc');
        if (topoDesc) {
            topoDesc.textContent = `WSCC 3-generator, 9-bus reference system (Anderson & Fouad). Base: ${currentConfig.base_mva} MVA, ${currentConfig.base_kv} kV, ${currentConfig.frequency} Hz. Extended with FACTS (SVC Bus 5, STATCOM Bus 8) and EV/V2G aggregator at Bus 8.`;
        }
        const lfDesc = document.querySelector('#page-loadflow .section-desc');
        if (lfDesc) {
            lfDesc.innerHTML = `Steady-state AC power flow solution for the IEEE 9-Bus system (Anderson &amp; Fouad reference data). Total generation: 319.64 MW. System losses: 4.64 MW.`;
        }
    }

    // --- Accent colors (real-time theme) ---
    if (key.startsWith('color_')) {
        const root = document.documentElement;
        if (key === 'color_blue') {
            root.style.setProperty('--accent-blue', value);
            root.style.setProperty('--border-glow', value);
            root.style.setProperty('--accent-blue-light', lightenColor(value, 40));
        }
        if (key === 'color_purple') root.style.setProperty('--accent-purple', value);
        if (key === 'color_emerald') root.style.setProperty('--accent-emerald', value);
        if (key === 'color_amber') root.style.setProperty('--accent-amber', value);
    }

    // --- Charts that depend on numeric config — reinit when changed ---
    if (key === 'qirl_speedup' && initializedPages.has('system2')) {
        reinitPageCharts('system2');
    }
    if ((key === 'ev_capacity_mw' || key === 'ev_fleet') && initializedPages.has('ev')) {
        reinitPageCharts('ev');
    }
    if (['s1_response_ms', 's2_response_ms', 'max_violations', 'fault_accuracy', 'qirl_speedup'].includes(key) && initializedPages.has('performance')) {
        reinitPageCharts('performance');
    }

    // --- HIRL parameters in description ---
    if (key === 'hirl_regions') {
        // Update region count in hierarchy desc if visible
        const regDesc = document.querySelectorAll('.hirl-level .hirl-desc');
        if (regDesc.length >= 2) {
            // Regional description mentions zones
            flashElement(regDesc[1]);
        }
    }
}

function updateCyberTimings() {
    const blocks = document.querySelectorAll('.attack-block');
    blocks.forEach(block => {
        const timing = block.querySelector('.timing');
        if (!timing) return;
        if (block.classList.contains('fdi')) {
            timing.textContent = `t = ${currentConfig.fdi_start}s — ${currentConfig.fdi_end}s`;
            flashElement(timing);
        }
        if (block.classList.contains('dos')) {
            const dosEnd = (parseFloat(currentConfig.dos_start) + parseFloat(currentConfig.dos_duration)).toFixed(1);
            timing.textContent = `t = ${currentConfig.dos_start}s — ${dosEnd}s`;
            flashElement(timing);
        }
        if (block.classList.contains('delay')) {
            timing.textContent = `t = 12.0s — ${currentConfig.sim_time}s`;
            flashElement(timing);
            // Also update the delay amount text
            const delayText = block.querySelectorAll('.text-muted');
            delayText.forEach(el => {
                if (el.textContent.includes('Delay =')) {
                    el.innerHTML = `Target: Control loops<br>Delay = ${currentConfig.comm_delay} seconds`;
                    flashElement(el);
                }
            });
        }
    });
}

function updateMetacognitionThresholds() {
    // Update the metacognition cards with threshold values
    const cards = document.querySelectorAll('#page-metacognition .card');
    cards.forEach(card => {
        const muted = card.querySelectorAll('.text-muted');
        muted.forEach(el => {
            if (el.textContent.includes('τ_c =')) {
                el.textContent = `High confidence → trust current policy. Threshold: τ_c = ${currentConfig.tau_c}`;
                flashElement(el);
            }
            if (el.textContent.includes('τ_n =')) {
                el.textContent = `High novelty → unseen state, switch to System-2. Threshold: τ_n = ${currentConfig.tau_n}σ`;
                flashElement(el);
            }
            if (el.textContent.includes('τ_u =')) {
                el.textContent = `High urgency → trigger System-1 reflex. Threshold: τ_u = ${currentConfig.tau_u}`;
                flashElement(el);
            }
        });
    });
}

function flashElement(el) {
    el.classList.remove('value-updated');
    void el.offsetWidth; // force reflow
    el.classList.add('value-updated');
}

// ═══════════════════════════════════════════
// KEYBOARD SHORTCUTS
// ═══════════════════════════════════════════

document.addEventListener('keydown', (e) => {
    // Don't trigger shortcuts when typing in input fields
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

    const navItems = document.querySelectorAll('.nav-item[data-page]');
    const current = document.querySelector('.nav-item.active');
    const idx = Array.from(navItems).indexOf(current);

    if (e.key === 'ArrowDown' && idx < navItems.length - 1) {
        navItems[idx + 1].click();
        e.preventDefault();
    } else if (e.key === 'ArrowUp' && idx > 0) {
        navItems[idx - 1].click();
        e.preventDefault();
    } else if (e.key === 'e' || e.key === 'E') {
        toggleEditMode();
        e.preventDefault();
    } else if (e.key === 'Escape' && editModeActive) {
        toggleEditMode();
        e.preventDefault();
    }
});

console.log('%c CAPSM Dashboard ', 'background: #2563eb; color: white; font-size: 14px; font-weight: bold; padding: 4px 12px; border-radius: 4px;');
console.log('Mahmoud Kiasari • Dalhousie University • 2026');
console.log('HIRL: Hierarchical Integrated Reinforcement Learning');
console.log('Use ↑/↓ arrow keys to navigate | E to toggle Edit Mode | ⚙️ for global settings');
console.log('Edit Mode: Inline per-tab editing with real-time preview');
console.log('Config stored in localStorage key:', CONFIG_KEY);
