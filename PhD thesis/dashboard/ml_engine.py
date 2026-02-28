"""
═══════════════════════════════════════════════════════════════
CAPSM Machine Learning Engine
Author: Mahmoud Kiasari, Dalhousie University
═══════════════════════════════════════════════════════════════

ML models for the CAPSM PhD Dashboard:
  1. Fault Classification      — Random Forest + MLP (simulates CNN-LSTM)
  2. Cyber-Attack Anomaly Det. — Isolation Forest
  3. RL Convergence Prediction  — Gradient Boosting Regressor
  4. Metacognitive Mode Class.  — Gradient Boosting Classifier
  5. Voltage Stability Pred.    — MLP Regressor
  6. EV SoC Forecasting         — Gradient Boosting Regressor

All models are trained on synthetic IEEE 9-Bus data at startup.
"""

import numpy as np
from sklearn.ensemble import (
    RandomForestClassifier, IsolationForest,
    GradientBoostingRegressor, GradientBoostingClassifier,
)
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix
import warnings

warnings.filterwarnings("ignore")


class CAPSMMLEngine:
    """Machine Learning Engine for the CAPSM PhD Dashboard."""

    def __init__(self, seed=42):
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.models = {}
        self.scalers = {}
        self.metrics = {}
        self.fault_labels = []
        self.fault_importances = np.array([])
        self.fault_cm = None
        print("[ML Engine] Initializing CAPSM ML models …")
        self._train_all()
        print("[ML Engine] All models ready.\n")

    # ──────────────────────────────────────────────
    # Train all models
    # ──────────────────────────────────────────────
    def _train_all(self):
        self._train_fault_classifier()
        self._train_anomaly_detector()
        self._train_convergence_predictor()
        self._train_mode_classifier()
        self._train_voltage_predictor()
        self._train_soc_forecaster()

    # ═══ 1. Fault Classification ═══════════════════
    def _generate_fault_data(self, n=2000):
        X, y = [], []
        fault_types = ["Normal", "3-Phase", "Line-Ground", "Line-Line", "Loss-of-Gen"]
        for _ in range(n):
            ft = self.rng.choice(len(fault_types))
            v = 1.0 + self.rng.randn(9) * 0.02
            i_ = 0.5 + self.rng.randn(9) * 0.1
            f = 60.0 + self.rng.randn(9) * 0.05
            dv = self.rng.randn(9) * 0.01
            di = self.rng.randn(9) * 0.02
            df = self.rng.randn(9) * 0.005
            if ft == 1:
                v[4] -= 0.3 + self.rng.rand() * 0.2
                i_[4] += 2.0 + self.rng.rand()
                dv[4] = -0.5 + self.rng.randn() * 0.1
            elif ft == 2:
                v[3:5] -= 0.15 + self.rng.rand() * 0.1
                i_[3:5] += 0.8 + self.rng.rand() * 0.3
            elif ft == 3:
                v[6:8] -= 0.12 + self.rng.rand() * 0.08
                i_[6:8] += 0.6 + self.rng.rand() * 0.2
            elif ft == 4:
                v -= 0.04
                f -= 0.3 + self.rng.rand() * 0.2
                df -= 0.1
            X.append(np.concatenate([v, i_, f, dv, di, df]))
            y.append(ft)
        return np.array(X), np.array(y), fault_types

    def _train_fault_classifier(self):
        X, y, labels = self._generate_fault_data(3000)
        self.fault_labels = labels
        sc = StandardScaler()
        Xs = sc.fit_transform(X)
        Xtr, Xte, ytr, yte = train_test_split(Xs, y, test_size=0.2, random_state=self.seed)

        rf = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=self.seed)
        rf.fit(Xtr, ytr)
        rf_acc = accuracy_score(yte, rf.predict(Xte))

        mlp = MLPClassifier(hidden_layer_sizes=(128, 64, 32), max_iter=300, random_state=self.seed)
        mlp.fit(Xtr, ytr)
        mlp_acc = accuracy_score(yte, mlp.predict(Xte))

        self.fault_cm = confusion_matrix(yte, rf.predict(Xte))
        self.models["fault_rf"] = rf
        self.models["fault_mlp"] = mlp
        self.scalers["fault"] = sc
        self.fault_importances = rf.feature_importances_
        self.metrics["fault_rf_accuracy"] = round(rf_acc * 100, 1)
        self.metrics["fault_mlp_accuracy"] = round(mlp_acc * 100, 1)
        print(f"  [Fault]       RF={rf_acc:.3f}  MLP={mlp_acc:.3f}")

    def predict_fault(self, pmu_data, model="rf"):
        m = self.models[f"fault_{model}"]
        Xs = self.scalers["fault"].transform(pmu_data.reshape(1, -1))
        return self.fault_labels[m.predict(Xs)[0]], m.predict_proba(Xs)[0]

    # ═══ 2. Anomaly Detection (Cyber Attacks) ═════
    def _train_anomaly_detector(self):
        n = 1000
        normal = np.column_stack([
            1.0 + self.rng.randn(n, 9) * 0.02,
            60.0 + self.rng.randn(n, 9) * 0.05,
            self.rng.randn(n, 9) * 0.01,
        ])
        iso = IsolationForest(n_estimators=100, contamination=0.05, random_state=self.seed)
        iso.fit(normal)

        fdi = normal[:50].copy()
        fdi[:, 4] += self.rng.randn(50) * 0.3
        dos = np.zeros((20, 27))

        self.models["anomaly"] = iso
        self.metrics["anomaly_normal"] = round(float(iso.decision_function(normal[:100]).mean()), 3)
        self.metrics["anomaly_fdi"] = round(float(iso.decision_function(fdi).mean()), 3)
        self.metrics["anomaly_dos"] = round(float(iso.decision_function(dos).mean()), 3)
        print(f"  [Anomaly]     Normal={self.metrics['anomaly_normal']:.3f}  FDI={self.metrics['anomaly_fdi']:.3f}  DoS={self.metrics['anomaly_dos']:.3f}")

    def detect_anomaly(self, measurements):
        pred = self.models["anomaly"].predict(measurements.reshape(1, -1))[0]
        score = self.models["anomaly"].decision_function(measurements.reshape(1, -1))[0]
        return pred, float(score)

    # ═══ 3. RL Convergence Prediction ═════════════
    def _train_convergence_predictor(self):
        n = 500
        lr = self.rng.uniform(1e-4, 0.01, n)
        gamma = self.rng.uniform(0.9, 0.999, n)
        eps = self.rng.uniform(0.001, 0.1, n)
        agents = self.rng.randint(1, 5, n).astype(float)
        target = (50000 / (lr * 1000) * (1 / (1 - gamma)) * 0.01
                  + agents * 10000 - eps * 50000
                  + self.rng.randn(n) * 5000).clip(5000, 500000)
        X = np.column_stack([lr, gamma, eps, agents])
        sc = StandardScaler()
        Xs = sc.fit_transform(X)
        Xtr, Xte, ytr, yte = train_test_split(Xs, target, test_size=0.2, random_state=self.seed)
        gb = GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=self.seed)
        gb.fit(Xtr, ytr)
        r2 = gb.score(Xte, yte)
        self.models["convergence"] = gb
        self.scalers["convergence"] = sc
        self.metrics["convergence_r2"] = round(float(r2), 3)
        print(f"  [Convergence] R²={r2:.3f}")

    def predict_convergence(self, lr, gamma, epsilon, n_agents):
        X = np.array([[lr, gamma, epsilon, n_agents]])
        return max(1000, round(self.models["convergence"].predict(
            self.scalers["convergence"].transform(X))[0]))

    # ═══ 4. Metacognitive Mode Classification ═════
    def _train_mode_classifier(self):
        n = 2000
        c = self.rng.uniform(0, 1, n)
        nov = self.rng.uniform(0, 5, n)
        u = self.rng.uniform(0, 1, n)
        dv = self.rng.randn(n) * 0.1
        df = self.rng.randn(n) * 0.05
        mode = ((c > 0.7) & (u > 0.3)).astype(int)
        mode[nov > 2.0] = 0
        X = np.column_stack([c, nov, u, dv, df])
        sc = StandardScaler()
        Xs = sc.fit_transform(X)
        Xtr, Xte, ytr, yte = train_test_split(Xs, mode, test_size=0.2, random_state=self.seed)
        clf = GradientBoostingClassifier(n_estimators=80, max_depth=4, random_state=self.seed)
        clf.fit(Xtr, ytr)
        acc = accuracy_score(yte, clf.predict(Xte))
        self.models["mode"] = clf
        self.scalers["mode"] = sc
        self.metrics["mode_accuracy"] = round(acc * 100, 1)
        print(f"  [Mode]        Accuracy={acc:.3f}")

    def classify_mode(self, confidence, novelty, urgency, dv_dt=0, df_dt=0):
        X = np.array([[confidence, novelty, urgency, dv_dt, df_dt]])
        Xs = self.scalers["mode"].transform(X)
        return int(self.models["mode"].predict(Xs)[0]), self.models["mode"].predict_proba(Xs)[0].tolist()

    # ═══ 5. Voltage Stability Prediction ══════════
    def _train_voltage_predictor(self):
        n = 800
        lp = self.rng.uniform(50, 200, n)
        lq = self.rng.uniform(10, 80, n)
        gp = self.rng.uniform(200, 400, n)
        sq = self.rng.uniform(-100, 100, n)
        v = 1.04 - 3e-4 * lp - 2e-4 * lq + 5e-5 * gp + 1e-4 * sq + self.rng.randn(n) * 0.005
        X = np.column_stack([lp, lq, gp, sq])
        sc = StandardScaler()
        Xs = sc.fit_transform(X)
        Xtr, Xte, ytr, yte = train_test_split(Xs, v, test_size=0.2, random_state=self.seed)
        m = GradientBoostingRegressor(n_estimators=100, max_depth=4, random_state=self.seed)
        m.fit(Xtr, ytr)
        r2 = m.score(Xte, yte)
        self.models["voltage"] = m
        self.scalers["voltage"] = sc
        self.metrics["voltage_r2"] = round(float(r2), 3)
        print(f"  [Voltage]     R²={r2:.3f}")

    def predict_voltage(self, load_p, load_q, gen_p, svc_q):
        X = np.array([[load_p, load_q, gen_p, svc_q]])
        return float(self.models["voltage"].predict(self.scalers["voltage"].transform(X))[0])

    # ═══ 6. SoC Forecaster ════════════════════════
    def _train_soc_forecaster(self):
        n = 600
        soc0 = self.rng.uniform(0.2, 0.95, n)
        pw = self.rng.uniform(-50, 50, n)
        soc1 = np.clip(soc0 - 0.95 * pw / 150 * (1 / 3600), 0.2, 0.95)
        X = np.column_stack([soc0, pw])
        sc = StandardScaler()
        Xs = sc.fit_transform(X)
        Xtr, Xte, ytr, yte = train_test_split(Xs, soc1, test_size=0.2, random_state=self.seed)
        m = GradientBoostingRegressor(n_estimators=50, max_depth=3, random_state=self.seed)
        m.fit(Xtr, ytr)
        r2 = m.score(Xte, yte)
        self.models["soc"] = m
        self.scalers["soc"] = sc
        self.metrics["soc_r2"] = round(float(r2), 3)
        print(f"  [SoC]         R²={r2:.3f}")

    def predict_soc(self, current_soc, power_mw):
        X = np.array([[current_soc, power_mw]])
        return float(np.clip(self.models["soc"].predict(self.scalers["soc"].transform(X))[0], 0.2, 0.95))

    # ═══ Simulation helpers ═══════════════════════
    def simulate_qirl(self, lr=0.001, gamma=0.99, n_ep=1000):
        ep = np.arange(1, n_ep + 1)
        tau = 200 * lr * 1000
        qirl = -500 * np.exp(-ep / tau) + 100 + self.rng.randn(n_ep) * 3
        dqn = -500 * np.exp(-ep / (tau * 2)) + 80 + self.rng.randn(n_ep) * 5
        ppo = -500 * np.exp(-ep / (tau * 1.75)) + 90 + self.rng.randn(n_ep) * 4
        return ep, qirl, dqn, ppo

    def simulate_metacognition(self, tau_c=0.7, tau_u=0.3, dur=20.0, dt=0.1):
        n = int(dur / dt)
        t = np.arange(n) * dt
        c = 0.5 + 0.4 * np.sin(2 * np.pi * 0.03 * t) + self.rng.randn(n) * 0.05
        u = 0.2 + 0.15 * np.abs(np.sin(2 * np.pi * 0.07 * t))
        u[(t >= 0.9) & (t <= 1.5)] = np.minimum(1, u[(t >= 0.9) & (t <= 1.5)] + 0.6)
        u[(t >= 7.5) & (t <= 9.0)] = np.minimum(1, u[(t >= 7.5) & (t <= 9.0)] + 0.4)
        mode = ((c > tau_c) & (u > tau_u)).astype(int)
        return t, c, u, mode

    def simulate_ev_soc(self, cap_mw=50, soc0=0.7, dur=20.0):
        dt, n = 0.1, int(dur / 0.1)
        t = np.arange(n) * dt
        soc = np.zeros(n)
        soc[0] = soc0
        cap_mwh = cap_mw * 3
        for i in range(1, n):
            P = np.clip((0.6 - soc[i - 1]) * cap_mw * 1e6, -cap_mw * 1e6, cap_mw * 1e6)
            soc[i] = np.clip(soc[i - 1] - 0.95 * P / (cap_mwh * 1e6) * dt * 0.05, 0.20, 0.95)
        return t, soc

    def simulate_hirl(self, lr=0.001, gamma=0.99, n_regions=2, max_ep=300000):
        ep = np.arange(0, max_ep, 5000)
        hirl = -400 * np.exp(-ep / 80000) + 90 + self.rng.randn(len(ep)) * 4
        central = -400 * np.exp(-ep / 200000) + 70 + self.rng.randn(len(ep)) * 6
        indep = -400 * np.exp(-ep / 120000) + 75 + self.rng.randn(len(ep)) * 5
        dqn = -400 * np.exp(-ep / 160000) + 60 + self.rng.randn(len(ep)) * 8
        return ep, hirl, central, indep, dqn

    def get_feature_importance_data(self):
        names = []
        for ch in ["V", "I", "f", "dV/dt", "dI/dt", "df/dt"]:
            for b in range(1, 10):
                names.append(f"{ch}_B{b}")
        imp = self.fault_importances
        idx = np.argsort(imp)[::-1][:15]
        return [names[i] for i in idx], imp[idx].tolist()

    def get_all_metrics(self):
        return dict(self.metrics)
