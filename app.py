import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Geodesia Física · Taller Python",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# SESSION STATE — navegación
# ─────────────────────────────────────────────
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

:root {
    --bg:          #ffffff;
    --bg2:         #f7faf9;
    --panel:       #ffffff;
    --panel2:      #f2f7f5;
    --border:      #d7e4df;

    --accent:      #2fa88f;
    --accent2:     #56c7a7;
    --accent3:     #c93b3b;
    --gold:        #d4a81e;
    --purple:      #5f7f7a;

    --text:        #24343a;
    --text-dim:    #6b7f86;
    --text-bright: #102028;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Syne', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 70% 50% at 50% -10%, rgba(47,168,143,0.08) 0%, transparent 65%),
        radial-gradient(ellipse 50% 40% at 95% 85%, rgba(201,59,59,0.05) 0%, transparent 60%),
        linear-gradient(180deg, #ffffff 0%, #f8fbfa 100%);
}

[data-testid="stHeader"], header { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 2rem 3rem !important; max-width: 1400px !important; }

body::before {
    content: '';
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9999;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 3px,
        rgba(0,0,0,0.015) 3px,
        rgba(0,0,0,0.015) 6px
    );
}

/* HERO */
.hero-wrapper {
    position: relative;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: linear-gradient(135deg, #ffffff 0%, #f4fbf8 45%, #fffdf7 100%);
    padding: 3.5rem 3rem 3rem;
    margin-bottom: 2.5rem;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

.hero-wrapper::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 80px,
            rgba(47,168,143,0.04) 80px,
            rgba(47,168,143,0.04) 81px
        ),
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 80px,
            rgba(47,168,143,0.04) 80px,
            rgba(47,168,143,0.04) 81px
        );
    pointer-events: none;
}

.hero-wrapper::after {
    content: '';
    position: absolute;
    top: -60px;
    left: -60px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(86,199,167,0.16) 0%, transparent 70%);
    pointer-events: none;
}

.badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid rgba(47,168,143,0.30);
    background: rgba(47,168,143,0.08);
    padding: 0.3rem 0.8rem;
    border-radius: 4px;
    margin-bottom: 1.2rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.02em;
    margin: 0.4rem 0 1rem;
    color: var(--text-bright);
}

.hero-title span {
    background: linear-gradient(90deg, var(--accent) 0%, var(--gold) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.9rem;
    color: var(--text-dim);
    line-height: 1.7;
    max-width: 620px;
    margin-bottom: 2rem;
}

.hero-meta { display: flex; gap: 2rem; flex-wrap: wrap; }

.hero-meta-item {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-dim);
}

.hero-meta-item b {
    display: block;
    color: var(--accent);
    font-size: 0.85rem;
    letter-spacing: 0;
    text-transform: none;
    margin-top: 0.15rem;
}

.hero-globe {
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0.10;
    font-size: 9rem;
    pointer-events: none;
}

/* SECTION LABELS */
.sec-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.sec-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border) 0%, transparent 100%);
}

.sec-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-bright);
    margin-bottom: 0.4rem;
}

/* TARJETAS */
.mod-btn-card {
    position: relative;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.8rem 1.6rem 1.5rem;
    overflow: hidden;
    transition: all 0.25s ease;
    margin-bottom: 0.6rem;
    box-shadow: 0 6px 18px rgba(0,0,0,0.04);
}

.mod-btn-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.08);
}

.mod-btn-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
}

.mod-c1::before { background: linear-gradient(90deg, #2fa88f, #56c7a7); }
.mod-c2::before { background: linear-gradient(90deg, #56c7a7, #8ed8c3); }
.mod-c3::before { background: linear-gradient(90deg, #6f8f88, #2fa88f); }
.mod-c4::before { background: linear-gradient(90deg, #d4a81e, #c93b3b); }

.mod-c1:hover, .mod-c2:hover, .mod-c3:hover, .mod-c4:hover {
    border-color: rgba(47,168,143,0.35);
}

.mod-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.7rem;
    color: var(--accent);
}

.mod-icon {
    font-size: 2.2rem;
    margin-bottom: 0.6rem;
    display: block;
    line-height: 1;
}

.mod-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-bright);
    margin-bottom: 0.6rem;
    line-height: 1.25;
}

.mod-desc {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-dim);
    line-height: 1.65;
    margin-bottom: 1rem;
}

.mod-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-bottom: 1.3rem;
}

.mod-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.2rem 0.55rem;
    border-radius: 20px;
}

.tag-cyan   { color: #237e6f; border: 1px solid rgba(47,168,143,0.25); background: rgba(47,168,143,0.08); }
.tag-green  { color: #2f8f77; border: 1px solid rgba(86,199,167,0.25); background: rgba(86,199,167,0.10); }
.tag-purple { color: #5f7f7a; border: 1px solid rgba(95,127,122,0.20); background: rgba(95,127,122,0.08); }
.tag-gold   { color: #9a7a10; border: 1px solid rgba(212,168,30,0.25); background: rgba(212,168,30,0.10); }
.tag-orange { color: #b53d3d; border: 1px solid rgba(201,59,59,0.22); background: rgba(201,59,59,0.08); }

.mod-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.73rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    padding: 0.55rem 1.2rem;
    border-radius: 6px;
    border: 1px solid rgba(47,168,143,0.22);
    color: var(--accent);
    background: rgba(47,168,143,0.06);
}

/* BOTONES */
div[data-testid="stButton"] > button {
    width: 100%;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--panel2);
    color: var(--text-bright);
    padding: 0.75rem 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    transition: all 0.2s ease;
    position: static !important;
    inset: auto !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}

div[data-testid="stButton"] > button:hover {
    border-color: rgba(47,168,143,0.45);
    color: var(--accent);
    background: rgba(47,168,143,0.05);
}

div[data-testid="stButton"] > button:focus:not(:active) {
    border-color: rgba(47,168,143,0.55);
    color: var(--accent);
    box-shadow: 0 0 0 1px rgba(47,168,143,0.25);
}

/* CAJAS */
.formula-box {
    background: #fcfefd;
    border: 1px solid var(--border);
    border-left: 4px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 1.2rem 1.4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #1f6d5f;
    line-height: 1.9;
}

.formula-box .comment {
    color: var(--text-dim);
    font-size: 0.75rem;
}

.info-panel {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.4rem;
    box-shadow: 0 6px 16px rgba(0,0,0,0.03);
}

.info-panel-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-dim);
    margin-bottom: 1rem;
}

.timeline-item {
    display: flex;
    gap: 1rem;
    padding: 0.7rem 0;
    border-bottom: 1px solid #e8efec;
}
.timeline-item:last-child { border-bottom: none; }

.tl-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--accent);
    min-width: 24px;
    padding-top: 0.1rem;
}

.tl-text {
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: var(--text);
    line-height: 1.5;
}

.tl-text b {
    color: var(--text-bright);
    font-weight: 700;
}

.page-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 0.3rem;
}

.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--text-bright);
    line-height: 1.1;
}

.coming-soon-box {
    background: linear-gradient(180deg, #ffffff 0%, #f8fbfa 100%);
    border: 1px dashed var(--border);
    border-radius: 10px;
    padding: 5rem 2rem;
    text-align: center;
    margin-top: 1.5rem;
}

.cs-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    display: block;
}

.cs-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-bright);
    margin-bottom: 0.5rem;
}

.cs-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--text-dim);
    line-height: 1.7;
    max-width: 420px;
    margin: 0 auto;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #d7e4df 30%, #d7e4df 70%, transparent);
    margin: 2rem 0;
}

.stack-row {
    display: flex;
    gap: 0.8rem;
    flex-wrap: wrap;
    margin-top: 0.6rem;
}

.stack-chip {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 0.5rem 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--text);
}

.stack-chip-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
}

.footer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-align: center;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
}

[data-testid="stPlotlyChart"] {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    background: #ffffff;
}

h1,h2,h3,h4 { color: var(--text-bright) !important; }
p, li {
    color: var(--text) !important;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
}
hr { border-color: var(--border) !important; }

/* ── MODULE 1: EXTRA UI ─── */
.control-panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem;
    box-shadow: 0 6px 16px rgba(0,0,0,0.03);
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 1rem;
}

.metric-card {
    background: var(--panel2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.9rem 1rem;
}

.metric-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 0.35rem;
}

.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-bright);
    line-height: 1.2;
}

.step-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.1rem;
    margin-bottom: 1rem;
}

.step-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-bright);
    margin-bottom: 0.4rem;
}

.step-text {
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: var(--text);
    line-height: 1.7;
}

.soft-note {
    background: rgba(47,168,143,0.06);
    border: 1px solid rgba(47,168,143,0.18);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--text);
    line-height: 1.7;
}

.mod-table {
    width: 100%;
    border-collapse: collapse;
    overflow: hidden;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--panel);
    margin-top: 1rem;
}

.mod-table th,
.mod-table td {
    padding: 0.75rem 0.85rem;
    border-bottom: 1px solid var(--border);
    text-align: left;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text);
}

.mod-table th {
    background: var(--panel2);
    color: var(--text-bright);
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.mod-table tr:last-child td {
    border-bottom: none;
}  
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATOS DE MÓDULOS
# ─────────────────────────────────────────────
MODULES = [
    {
        "key": "mod1",
        "cls": "mod-c1",
        "num": "MÓDULO 01 · DEMOSTRACIÓN MATEMÁTICA",
        "icon": "⚡",
        "color": "#2fa88f",
        "title": "Gravedad interior\ny exterior",
        "desc": "Esfera de densidad constante: g(r) crece linealmente para r < R y decrece como 1/r² para r ≥ R.",
        "tags": [("g ∝ r", "tag-cyan"), ("g ∝ 1/r²", "tag-cyan"), ("r = R", "tag-cyan")],
        "subtemas": [
            "Ley de gravitación universal",
            "Superficie gaussiana esférica",
            "M(r) = (4/3)πρr³",
            "Función por tramos de g(r)",
            "Perfil radial interactivo"
        ],
    },
    {
        "key": "mod2",
        "cls": "mod-c2",
        "num": "MÓDULO 02 · DEMOSTRACIÓN MATEMÁTICA",
        "icon": "🫧",
        "color": "#56c7a7",
        "title": "Potencial del\ncascarón esférico",
        "desc": "Cascarón de radio R y masa M: V(r) = GM/R para r ≤ R y V(r) = GM/r para r > R; en el interior el campo es nulo.",
        "tags": [("V = cte interior", "tag-green"), ("V = GM/r", "tag-green"), ("g = 0", "tag-green")],
        "subtemas": [
            "Definición integral del potencial",
            "Densidad superficial σ",
            "Potencial interior constante",
            "Continuidad de V en r = R",
            "Comparación V(r) y g(r)"
        ],
    },
    {
        "key": "mod3",
        "cls": "mod-c3",
        "num": "MÓDULO 03 · DEMOSTRACIÓN MATEMÁTICA",
        "icon": "🌐",
        "color": "#5f7f7a",
        "title": "Potencial de la\nesfera homogénea",
        "desc": "Esfera sólida de densidad constante: V(r) es parabólico en el interior y newtoniano en el exterior.",
        "tags": [("V_int parabólico", "tag-purple"), ("V_ext = GM/r", "tag-purple"), ("ρ = cte", "tag-purple")],
        "subtemas": [
            "M = (4/3)πρR³",
            "Suma de cascarones esféricos",
            "V_int = GM(3R²-r²)/(2R³)",
            "Continuidad en r = R",
            "Relación entre V(r) y g(r)"
        ],
    },
    {
        "key": "mod4",
        "cls": "mod-c4",
        "num": "MÓDULO 04 · DEMOSTRACIÓN MATEMÁTICA",
        "icon": "🔩",
        "color": "#d4a81e",
        "title": "Anomalía gravimétrica\ndel cilindro vertical",
        "desc": "Atracción vertical sobre el eje del cilindro: Δg depende del radio R, el contraste de densidad Δρ y las profundidades z₁ y z₂.",
        "tags": [("Δρ", "tag-gold"), ("z₁, z₂, L", "tag-gold"), ("atracción vertical", "tag-orange")],
        "subtemas": [
            "Disco delgado elemental",
            "Integración entre z₁ y z₂",
            "z₂ = z₁ + L",
            "Δg sobre el eje (z = 0)",
            "Perfiles y sensibilidad paramétrica"
        ],
    },
]
# ─────────────────────────────────────────────
# MÓDULO 1 · FUNCIONES AUXILIARES
# ─────────────────────────────────────────────
def enclosed_mass(radius, M, R):
    radius = np.asarray(radius, dtype=float)
    return M * (np.minimum(radius, R) ** 3) / (R ** 3)


def gravity_piecewise(radius, M, R, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    g = np.zeros_like(radius, dtype=float)

    mask_positive = radius > 0
    mask_inside = mask_positive & (radius < R)
    mask_outside = mask_positive & ~mask_inside

    g[mask_inside] = G * M * radius[mask_inside] / (R ** 3)
    g[mask_outside] = G * M / (radius[mask_outside] ** 2)

    return g


def build_mod1_profile_figure(radius, gravity, R, r_probe, g_probe):
    inside = radius <= R
    outside = radius >= R

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=radius[inside] / 1e3,
        y=gravity[inside],
        fill="tozeroy",
        fillcolor="rgba(47,168,143,0.12)",
        line=dict(color="#2fa88f", width=3),
        name="Interior · g(r) = GMr/R³",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=radius[outside] / 1e3,
        y=gravity[outside],
        fill="tozeroy",
        fillcolor="rgba(212,168,30,0.10)",
        line=dict(color="#d4a81e", width=3),
        name="Exterior · g(r) = GM/r²",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_vline(
        x=R / 1e3,
        line=dict(color="#c93b3b", width=1.8, dash="dot"),
        annotation_text="r = R",
        annotation_font=dict(color="#c93b3b", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[r_probe / 1e3],
        y=[g_probe],
        mode="markers+text",
        marker=dict(size=10, color="#c93b3b"),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=380,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.56,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Distancia radial r (km)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="g(r) (m/s²)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )

    return fig


def build_mod1_normalized_figure(max_eta, eta_probe):
    eta = np.linspace(0.0, max_eta, 700)
    g_norm = np.zeros_like(eta)

    inside = eta < 1
    outside = eta >= 1

    g_norm[inside] = eta[inside]
    g_norm[outside] = 1 / (eta[outside] ** 2)

    g_probe_norm = eta_probe if eta_probe < 1 else 1 / (eta_probe ** 2)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=eta[inside],
        y=g_norm[inside],
        fill="tozeroy",
        fillcolor="rgba(47,168,143,0.12)",
        line=dict(color="#2fa88f", width=3),
        name="Interior · g/g(R) = r/R",
        hovertemplate="r/R = %{x:.3f}<br>g/g(R) = %{y:.3f}<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=eta[outside],
        y=g_norm[outside],
        fill="tozeroy",
        fillcolor="rgba(212,168,30,0.10)",
        line=dict(color="#d4a81e", width=3),
        name="Exterior · g/g(R) = 1/(r/R)²",
        hovertemplate="r/R = %{x:.3f}<br>g/g(R) = %{y:.3f}<extra></extra>"
    ))

    fig.add_vline(
        x=1.0,
        line=dict(color="#c93b3b", width=1.8, dash="dot"),
        annotation_text="r/R = 1",
        annotation_font=dict(color="#c93b3b", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[eta_probe],
        y=[g_probe_norm],
        mode="markers+text",
        marker=dict(size=10, color="#c93b3b"),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r/R = %{x:.3f}<br>g/g(R) = %{y:.3f}<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=320,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.42,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Radio adimensional r/R", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Gravedad adimensional g(r)/g(R)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )

    return fig
# ─────────────────────────────────────────────
# MÓDULO 2 · FUNCIONES AUXILIARES
# ─────────────────────────────────────────────
def shell_surface_density(M, R):
    return M / (4 * np.pi * R**2)


def shell_potential_piecewise(radius, M, R, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    V = np.empty_like(radius, dtype=float)

    inside = radius <= R
    outside = radius > R

    V[inside] = G * M / R
    V[outside] = G * M / radius[outside]

    return V


def shell_gravity_piecewise(radius, M, R, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    g = np.zeros_like(radius, dtype=float)

    outside = radius >= R
    positive = radius > 0

    mask = outside & positive
    g[mask] = G * M / (radius[mask] ** 2)

    return g


def build_mod2_shell_figure(R, r_probe):
    phi = np.linspace(0, np.pi, 90)
    theta = np.linspace(0, 2 * np.pi, 180)
    PHI, THETA = np.meshgrid(phi, theta)

    def sphere(a):
        x = a * np.sin(PHI) * np.cos(THETA)
        y = a * np.sin(PHI) * np.sin(THETA)
        z = a * np.cos(PHI)
        return x, y, z

    outer_scale = 1.0
    inner_scale = 0.80

    x1, y1, z1 = sphere(outer_scale)
    x2, y2, z2 = sphere(inner_scale)

    eta_probe = r_probe / R
    probe_scale = min(eta_probe, 1.85)

    # patrón visual para que el cascarón no se vea plano
    shell_pattern = (
        0.55
        + 0.25 * np.cos(2 * THETA) * np.sin(PHI) ** 2
        + 0.20 * np.cos(PHI)
    )

    fig = go.Figure()

    # Cascarón exterior con color más rico
    fig.add_trace(go.Surface(
        x=x1, y=y1, z=z1,
        surfacecolor=shell_pattern,
        cmin=shell_pattern.min(),
        cmax=shell_pattern.max(),
        colorscale=[
            [0.00, "#f7fffc"],
            [0.18, "#c8f3e6"],
            [0.38, "#56c7a7"],
            [0.58, "#2fa88f"],
            [0.78, "#d4a81e"],
            [1.00, "#c93b3b"],
        ],
        opacity=0.96,
        showscale=False,
        hoverinfo="skip",
        lighting=dict(ambient=0.55, diffuse=0.9, specular=0.55, roughness=0.25),
        lightposition=dict(x=2.0, y=1.6, z=1.8)
    ))

    # interior para dar sensación de hueco
    fig.add_trace(go.Surface(
        x=x2, y=y2, z=z2,
        surfacecolor=np.ones_like(x2),
        cmin=0, cmax=1,
        colorscale=[[0, "#ffffff"], [1, "#eefaf5"]],
        opacity=0.38,
        showscale=False,
        hoverinfo="skip",
        lighting=dict(ambient=0.8, diffuse=0.3, specular=0.15, roughness=0.8),
        lightposition=dict(x=-2.0, y=-1.2, z=1.0)
    ))

    # anillo ecuatorial
    t = np.linspace(0, 2 * np.pi, 500)
    fig.add_trace(go.Scatter3d(
        x=np.cos(t),
        y=np.sin(t),
        z=np.zeros_like(t),
        mode="lines",
        line=dict(color="#102028", width=5),
        opacity=0.35,
        hoverinfo="skip",
        showlegend=False
    ))

    # meridiano
    fig.add_trace(go.Scatter3d(
        x=np.sin(t),
        y=np.zeros_like(t),
        z=np.cos(t),
        mode="lines",
        line=dict(color="#ffffff", width=5),
        opacity=0.25,
        hoverinfo="skip",
        showlegend=False
    ))

    # radio hacia el punto de observación
    fig.add_trace(go.Scatter3d(
        x=[0.0, probe_scale],
        y=[0.0, 0.0],
        z=[0.0, 0.0],
        mode="lines+markers",
        line=dict(color="#c93b3b", width=8),
        marker=dict(
            size=[6, 8],
            color=["#102028", "#c93b3b"]
        ),
        hoverinfo="skip",
        showlegend=False
    ))

    boundary_label_x = 1.0 if probe_scale >= 1.0 else probe_scale * 0.90

    fig.add_trace(go.Scatter3d(
        x=[boundary_label_x, probe_scale],
        y=[0.0, 0.0],
        z=[0.0, 0.0],
        mode="text",
        text=["r = R", "P(r)"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        hoverinfo="skip",
        showlegend=False
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=390,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.65, y=1.25, z=0.90)),
            aspectmode="data"
        )
    )

    return fig

def build_mod2_potential_surface_figure(max_eta, eta_probe):
    x = np.linspace(-max_eta, max_eta, 220)
    y = np.linspace(-max_eta, max_eta, 220)
    X, Y = np.meshgrid(x, y)

    rho = np.sqrt(X**2 + Y**2)
    rho_safe = np.where(rho < 1e-6, 1e-6, rho)

    # Potencial normalizado: V/V(R)
    Z = np.where(rho <= 1.0, 1.0, 1.0 / rho_safe)

    V_probe_norm = 1.0 if eta_probe <= 1.0 else 1.0 / eta_probe

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=X,
        y=Y,
        z=Z,
        surfacecolor=Z,
        colorscale=[
            [0.00, "#102028"],
            [0.12, "#1d5d63"],
            [0.28, "#2fa88f"],
            [0.48, "#56c7a7"],
            [0.70, "#d4a81e"],
            [1.00, "#fff5cf"],
        ],
        showscale=True,
        colorbar=dict(
            title=dict(text="V / V(R)", font=dict(color="#6b7f86", size=11, family="JetBrains Mono")),
            tickfont=dict(color="#6b7f86", size=10, family="JetBrains Mono"),
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="#d7e4df",
            thickness=12,
            len=0.72
        ),
        contours={
            "z": {
                "show": True,
                "usecolormap": True,
                "project_z": True,
                "width": 1
            }
        },
        hovertemplate="x/R = %{x:.2f}<br>y/R = %{y:.2f}<br>V/V(R) = %{z:.3f}<extra></extra>"
    ))

    # círculo frontera rho = 1
    t = np.linspace(0, 2 * np.pi, 500)
    fig.add_trace(go.Scatter3d(
        x=np.cos(t),
        y=np.sin(t),
        z=np.ones_like(t),
        mode="lines",
        line=dict(color="#c93b3b", width=7),
        name="r = R",
        hoverinfo="skip"
    ))

    # punto de observación sobre el eje x
    fig.add_trace(go.Scatter3d(
        x=[eta_probe],
        y=[0.0],
        z=[V_probe_norm],
        mode="markers+text",
        marker=dict(size=8, color="#ffffff", line=dict(color="#102028", width=2)),
        text=["P(r)"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        name="Punto evaluado",
        hovertemplate="r/R = %{x:.2f}<br>V/V(R) = %{z:.3f}<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=10, b=0),
        height=420,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(
                title="x / R",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            yaxis=dict(
                title="y / R",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            zaxis=dict(
                title="V / V(R)",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            camera=dict(eye=dict(x=1.55, y=1.4, z=0.95)),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.52)
        )
    )

    return fig


def build_mod2_potential_figure(radius, potential, R, r_probe, V_probe):
    inside = radius <= R
    outside = radius >= R

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=radius[inside] / 1e3,
        y=potential[inside],
        fill="tozeroy",
        fillcolor="rgba(86,199,167,0.18)",
        line=dict(color="#2fa88f", width=3.5),
        name="Interior · V(r) = GM/R",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=radius[outside] / 1e3,
        y=potential[outside],
        fill="tozeroy",
        fillcolor="rgba(212,168,30,0.16)",
        line=dict(color="#d4a81e", width=3.5),
        name="Exterior · V(r) = GM/r",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.add_vline(
        x=R / 1e3,
        line=dict(color="#c93b3b", width=2.0, dash="dot"),
        annotation_text="r = R",
        annotation_font=dict(color="#c93b3b", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[r_probe / 1e3],
        y=[V_probe],
        mode="markers+text",
        marker=dict(size=10, color="#102028", line=dict(color="#ffffff", width=1.5)),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=350,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.48,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Distancia radial r (km)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Potencial V(r) (m²/s²)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )

    return fig


def build_mod2_gravity_figure(radius, gravity, R, r_probe, g_probe):
    inside = radius < R
    outside = radius >= R

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=radius[inside] / 1e3,
        y=gravity[inside],
        fill="tozeroy",
        fillcolor="rgba(95,127,122,0.10)",
        line=dict(color="#5f7f7a", width=3),
        name="Interior · g(r) = 0",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=radius[outside] / 1e3,
        y=gravity[outside],
        fill="tozeroy",
        fillcolor="rgba(201,59,59,0.08)",
        line=dict(color="#c93b3b", width=3),
        name="Exterior · g(r) = GM/r²",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_vline(
        x=R / 1e3,
        line=dict(color="#d4a81e", width=1.8, dash="dot"),
        annotation_text="r = R",
        annotation_font=dict(color="#d4a81e", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[r_probe / 1e3],
        y=[g_probe],
        mode="markers+text",
        marker=dict(size=10, color="#102028"),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=320,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.49,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Distancia radial r (km)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Campo g(r) (m/s²)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )

    return fig

# ─────────────────────────────────────────────
# MÓDULO 3 · FUNCIONES AUXILIARES
# ─────────────────────────────────────────────
def solid_sphere_mass_from_density(rho, R):
    return (4.0 / 3.0) * np.pi * rho * R**3


def solid_sphere_density_from_mass(M, R):
    return 3.0 * M / (4.0 * np.pi * R**3)


def solid_sphere_potential_piecewise(radius, M, R, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    V = np.empty_like(radius, dtype=float)

    inside = radius <= R
    outside = radius > R

    V[inside] = G * M * (3.0 * R**2 - radius[inside]**2) / (2.0 * R**3)
    V[outside] = G * M / radius[outside]

    return V


def solid_sphere_gravity_piecewise(radius, M, R, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    g = np.zeros_like(radius, dtype=float)

    positive = radius > 0
    inside = positive & (radius < R)
    outside = positive & ~inside

    g[inside] = G * M * radius[inside] / R**3
    g[outside] = G * M / radius[outside]**2

    return g


def build_mod3_sphere_figure(R, r_probe):
    phi = np.linspace(0, np.pi, 85)
    theta = np.linspace(0, 2 * np.pi, 180)
    PHI, THETA = np.meshgrid(phi, theta)

    def sphere(a):
        x = a * np.sin(PHI) * np.cos(THETA)
        y = a * np.sin(PHI) * np.sin(THETA)
        z = a * np.cos(PHI)
        return x, y, z

    x1, y1, z1 = sphere(1.0)
    x2, y2, z2 = sphere(0.72)

    eta_probe = r_probe / R
    probe_scale = min(eta_probe, 1.85)

    pattern = (
        0.50
        + 0.18 * np.cos(2 * THETA) * np.sin(PHI) ** 2
        + 0.32 * np.cos(PHI)
    )

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=x1, y=y1, z=z1,
        surfacecolor=pattern,
        cmin=pattern.min(),
        cmax=pattern.max(),
        colorscale=[
            [0.00, "#f7fffd"],
            [0.20, "#d4efe8"],
            [0.40, "#9ccdc4"],
            [0.60, "#5f7f7a"],
            [0.82, "#2fa88f"],
            [1.00, "#d4a81e"],
        ],
        opacity=0.98,
        showscale=False,
        hoverinfo="skip",
        lighting=dict(ambient=0.55, diffuse=0.95, specular=0.40, roughness=0.28),
        lightposition=dict(x=2.0, y=1.4, z=2.0)
    ))

    fig.add_trace(go.Surface(
        x=x2, y=y2, z=z2,
        surfacecolor=np.ones_like(x2),
        cmin=0, cmax=1,
        colorscale=[[0, "#f1fbf8"], [1, "#bfe5db"]],
        opacity=0.23,
        showscale=False,
        hoverinfo="skip"
    ))

    t = np.linspace(0, 2 * np.pi, 500)
    fig.add_trace(go.Scatter3d(
        x=np.cos(t),
        y=np.sin(t),
        z=np.zeros_like(t),
        mode="lines",
        line=dict(color="#102028", width=5),
        opacity=0.30,
        hoverinfo="skip",
        showlegend=False
    ))

    fig.add_trace(go.Scatter3d(
        x=[0.0, probe_scale],
        y=[0.0, 0.0],
        z=[0.0, 0.0],
        mode="lines+markers",
        line=dict(color="#c93b3b", width=8),
        marker=dict(size=[6, 8], color=["#102028", "#c93b3b"]),
        hoverinfo="skip",
        showlegend=False
    ))

    boundary_label_x = 1.0 if probe_scale >= 1.0 else probe_scale * 0.92

    fig.add_trace(go.Scatter3d(
        x=[boundary_label_x, probe_scale],
        y=[0.0, 0.0],
        z=[0.0, 0.0],
        mode="text",
        text=["r = R", "P(r)"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        hoverinfo="skip",
        showlegend=False
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=390,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.65, y=1.22, z=0.88)),
            aspectmode="data"
        )
    )
    return fig


def build_mod3_potential_surface_figure(max_eta, eta_probe):
    x = np.linspace(-max_eta, max_eta, 220)
    y = np.linspace(-max_eta, max_eta, 220)
    X, Y = np.meshgrid(x, y)

    rho = np.sqrt(X**2 + Y**2)
    rho_safe = np.where(rho < 1e-6, 1e-6, rho)

    Z = np.where(rho <= 1.0, (3.0 - rho**2) / 2.0, 1.0 / rho_safe)

    V_probe_norm = (3.0 - eta_probe**2) / 2.0 if eta_probe <= 1.0 else 1.0 / eta_probe

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=X,
        y=Y,
        z=Z,
        surfacecolor=Z,
        colorscale=[
            [0.00, "#102028"],
            [0.15, "#1a5660"],
            [0.32, "#5f7f7a"],
            [0.52, "#2fa88f"],
            [0.72, "#d4a81e"],
            [1.00, "#fff2c5"],
        ],
        showscale=True,
        colorbar=dict(
            title=dict(text="V / V(R)", font=dict(color="#6b7f86", size=11, family="JetBrains Mono")),
            tickfont=dict(color="#6b7f86", size=10, family="JetBrains Mono"),
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="#d7e4df",
            thickness=12,
            len=0.72
        ),
        contours={
            "z": {
                "show": True,
                "usecolormap": True,
                "project_z": True,
                "width": 1
            }
        },
        hovertemplate="x/R = %{x:.2f}<br>y/R = %{y:.2f}<br>V/V(R) = %{z:.3f}<extra></extra>"
    ))

    t = np.linspace(0, 2 * np.pi, 500)
    fig.add_trace(go.Scatter3d(
        x=np.cos(t),
        y=np.sin(t),
        z=np.ones_like(t),
        mode="lines",
        line=dict(color="#c93b3b", width=7),
        name="r = R",
        hoverinfo="skip"
    ))

    fig.add_trace(go.Scatter3d(
        x=[eta_probe],
        y=[0.0],
        z=[V_probe_norm],
        mode="markers+text",
        marker=dict(size=8, color="#ffffff", line=dict(color="#102028", width=2)),
        text=["P(r)"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        name="Punto evaluado",
        hovertemplate="r/R = %{x:.2f}<br>V/V(R) = %{z:.3f}<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=10, b=0),
        height=420,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(
                title="x / R",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            yaxis=dict(
                title="y / R",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            zaxis=dict(
                title="V / V(R)",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            camera=dict(eye=dict(x=1.55, y=1.42, z=0.95)),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.58)
        )
    )
    return fig


def build_mod3_potential_figure(radius, potential, R, r_probe, V_probe):
    inside = radius <= R
    outside = radius >= R

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=radius[inside] / 1e3,
        y=potential[inside],
        fill="tozeroy",
        fillcolor="rgba(95,127,122,0.16)",
        line=dict(color="#5f7f7a", width=3.5),
        name="Interior · V(r) parabólico",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=radius[outside] / 1e3,
        y=potential[outside],
        fill="tozeroy",
        fillcolor="rgba(212,168,30,0.14)",
        line=dict(color="#d4a81e", width=3.5),
        name="Exterior · V(r) = GM/r",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.add_vline(
        x=R / 1e3,
        line=dict(color="#c93b3b", width=2.0, dash="dot"),
        annotation_text="r = R",
        annotation_font=dict(color="#c93b3b", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[r_probe / 1e3],
        y=[V_probe],
        mode="markers+text",
        marker=dict(size=10, color="#102028", line=dict(color="#ffffff", width=1.5)),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r = %{x:.2f} km<br>V = %{y:.4f} m²/s²<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=350,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.48,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Distancia radial r (km)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Potencial V(r) (m²/s²)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )
    return fig


def build_mod3_gravity_figure(radius, gravity, R, r_probe, g_probe):
    inside = radius <= R
    outside = radius >= R

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=radius[inside] / 1e3,
        y=gravity[inside],
        fill="tozeroy",
        fillcolor="rgba(47,168,143,0.12)",
        line=dict(color="#2fa88f", width=3.2),
        name="Interior · g(r) = GMr/R³",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=radius[outside] / 1e3,
        y=gravity[outside],
        fill="tozeroy",
        fillcolor="rgba(201,59,59,0.08)",
        line=dict(color="#c93b3b", width=3.2),
        name="Exterior · g(r) = GM/r²",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.add_vline(
        x=R / 1e3,
        line=dict(color="#d4a81e", width=1.8, dash="dot"),
        annotation_text="r = R",
        annotation_font=dict(color="#d4a81e", size=10, family="JetBrains Mono"),
        annotation_position="top right"
    )

    fig.add_trace(go.Scatter(
        x=[r_probe / 1e3],
        y=[g_probe],
        mode="markers+text",
        marker=dict(size=10, color="#102028"),
        text=["P(r)"],
        textposition="top center",
        name="Punto evaluado",
        hovertemplate="r = %{x:.2f} km<br>g = %{y:.4f} m/s²<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=320,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.47,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Distancia radial r (km)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Campo g(r) (m/s²)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )
    return fig


# ─────────────────────────────────────────────
# MÓDULO 4 · FUNCIONES AUXILIARES
# ─────────────────────────────────────────────
def cylinder_vertical_anomaly(radius, z1, z2, delta_rho, G=6.67430e-11):
    radius = np.asarray(radius, dtype=float)
    z1 = np.asarray(z1, dtype=float)
    z2 = np.asarray(z2, dtype=float)
    return 2.0 * np.pi * G * delta_rho * (
        (z2 - z1) + np.sqrt(radius**2 + z1**2) - np.sqrt(radius**2 + z2**2)
    )


def cylinder_vertical_anomaly_from_length(radius, z1, length, delta_rho, G=6.67430e-11):
    z2 = z1 + length
    return cylinder_vertical_anomaly(radius, z1, z2, delta_rho, G)


def build_mod4_cylinder_figure(radius, z1, z2):
    theta = np.linspace(0, 2 * np.pi, 140)
    z = np.linspace(-z1, -z2, 80)
    THETA, Z = np.meshgrid(theta, z)

    X = radius * np.cos(THETA)
    Y = radius * np.sin(THETA)

    rmax = max(radius * 2.4, 1.0)

    plane_x = np.linspace(-rmax, rmax, 2)
    plane_y = np.linspace(-rmax, rmax, 2)
    PX, PY = np.meshgrid(plane_x, plane_y)
    PZ = np.zeros_like(PX)

    top_r = np.linspace(0, radius, 80)
    top_t = np.linspace(0, 2 * np.pi, 140)
    RR_top, TT_top = np.meshgrid(top_r, top_t)
    Xtop = RR_top * np.cos(TT_top)
    Ytop = RR_top * np.sin(TT_top)
    Ztop = np.full_like(Xtop, -z1)

    Xbot = RR_top * np.cos(TT_top)
    Ybot = RR_top * np.sin(TT_top)
    Zbot = np.full_like(Xbot, -z2)

    wall_pattern = 0.5 + 0.5 * np.cos(THETA)

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=PX, y=PY, z=PZ,
        surfacecolor=np.ones_like(PX),
        colorscale=[[0, "#f8fbfa"], [1, "#edf7f3"]],
        opacity=0.95,
        showscale=False,
        hoverinfo="skip"
    ))

    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        surfacecolor=wall_pattern,
        colorscale=[
            [0.00, "#fff4cf"],
            [0.25, "#f0d97f"],
            [0.50, "#d4a81e"],
            [0.75, "#c56f37"],
            [1.00, "#c93b3b"],
        ],
        opacity=0.96,
        showscale=False,
        hoverinfo="skip",
        lighting=dict(ambient=0.55, diffuse=0.95, specular=0.35, roughness=0.30),
        lightposition=dict(x=1.8, y=1.4, z=2.0)
    ))

    fig.add_trace(go.Surface(
        x=Xtop, y=Ytop, z=Ztop,
        surfacecolor=np.ones_like(Xtop),
        colorscale=[[0, "#ffe8b5"], [1, "#d4a81e"]],
        opacity=0.98,
        showscale=False,
        hoverinfo="skip"
    ))

    fig.add_trace(go.Surface(
        x=Xbot, y=Ybot, z=Zbot,
        surfacecolor=np.ones_like(Xbot),
        colorscale=[[0, "#f9d5c9"], [1, "#c93b3b"]],
        opacity=0.98,
        showscale=False,
        hoverinfo="skip"
    ))

    fig.add_trace(go.Scatter3d(
        x=[0.0, 0.0],
        y=[0.0, 0.0],
        z=[0.0, -z2],
        mode="lines",
        line=dict(color="#102028", width=7),
        hoverinfo="skip",
        showlegend=False
    ))

    fig.add_trace(go.Scatter3d(
        x=[0.0],
        y=[0.0],
        z=[0.0],
        mode="markers+text",
        marker=dict(size=8, color="#2fa88f"),
        text=["P(z=0)"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        hoverinfo="skip",
        showlegend=False
    ))

    fig.add_trace(go.Scatter3d(
        x=[radius * 1.15, radius * 1.15],
        y=[0.0, 0.0],
        z=[-z1, -z2],
        mode="text",
        text=["z₁", "z₂"],
        textposition="middle right",
        textfont=dict(size=12, color="#24343a"),
        hoverinfo="skip",
        showlegend=False
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=390,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.75, y=1.35, z=0.90)),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=max(0.5, z2 / max(radius, 1.0)))
        )
    )
    return fig


def build_mod4_sensitivity_surface_figure(radius, z1, length, delta_rho, G=6.67430e-11):
    r_vals = np.linspace(max(5.0, 0.25 * radius), 2.2 * radius, 120)
    z1_vals = np.linspace(max(5.0, 0.35 * z1), 2.2 * z1, 120)
    RR, ZZ1 = np.meshgrid(r_vals, z1_vals)
    ZZ2 = ZZ1 + length

    DG = cylinder_vertical_anomaly(RR, ZZ1, ZZ2, delta_rho, G) * 1e5  # mGal

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=RR,
        y=ZZ1,
        z=DG,
        surfacecolor=DG,
        colorscale=[
            [0.00, "#102028"],
            [0.18, "#1d5d63"],
            [0.38, "#2fa88f"],
            [0.60, "#d4a81e"],
            [0.82, "#e07a3f"],
            [1.00, "#c93b3b"],
        ],
        showscale=True,
        colorbar=dict(
            title=dict(text="Δg (mGal)", font=dict(color="#6b7f86", size=11, family="JetBrains Mono")),
            tickfont=dict(color="#6b7f86", size=10, family="JetBrains Mono"),
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="#d7e4df",
            thickness=12,
            len=0.72
        ),
        contours={
            "z": {
                "show": True,
                "usecolormap": True,
                "project_z": True,
                "width": 1
            }
        },
        hovertemplate="R = %{x:.1f} m<br>z₁ = %{y:.1f} m<br>Δg = %{z:.4f} mGal<extra></extra>"
    ))

    current_dg = cylinder_vertical_anomaly(radius, z1, z1 + length, delta_rho, G) * 1e5
    fig.add_trace(go.Scatter3d(
        x=[radius],
        y=[z1],
        z=[current_dg],
        mode="markers+text",
        marker=dict(size=8, color="#ffffff", line=dict(color="#102028", width=2)),
        text=["Caso actual"],
        textposition="top center",
        textfont=dict(size=12, color="#24343a"),
        hovertemplate="R = %{x:.1f} m<br>z₁ = %{y:.1f} m<br>Δg = %{z:.4f} mGal<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        margin=dict(l=0, r=0, t=10, b=0),
        height=420,
        scene=dict(
            bgcolor="rgba(255,255,255,0)",
            xaxis=dict(
                title="Radio R (m)",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            yaxis=dict(
                title="Profundidad z₁ (m)",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            zaxis=dict(
                title="Δg (mGal)",
                backgroundcolor="rgba(255,255,255,0)",
                gridcolor="#e2ece8",
                linecolor="#d7e4df",
                tickfont=dict(color="#6b7f86")
            ),
            camera=dict(eye=dict(x=1.60, y=1.35, z=0.90)),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.65)
        )
    )
    return fig


def build_mod4_radius_response_figure(radius, z1, z2, delta_rho, G=6.67430e-11):
    r_vals = np.linspace(max(5.0, 0.15 * radius), 2.5 * radius, 300)
    dg_vals = cylinder_vertical_anomaly(r_vals, z1, z2, delta_rho, G) * 1e5

    current_dg = cylinder_vertical_anomaly(radius, z1, z2, delta_rho, G) * 1e5

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=r_vals,
        y=dg_vals,
        fill="tozeroy",
        fillcolor="rgba(212,168,30,0.16)",
        line=dict(color="#d4a81e", width=3.5),
        name="Δg sobre el eje",
        hovertemplate="R = %{x:.2f} m<br>Δg = %{y:.4f} mGal<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=[radius],
        y=[current_dg],
        mode="markers+text",
        marker=dict(size=10, color="#c93b3b"),
        text=["Caso actual"],
        textposition="top center",
        name="Caso actual",
        hovertemplate="R = %{x:.2f} m<br>Δg = %{y:.4f} mGal<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=320,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.58,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Radio del cilindro R (m)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Δg (mGal)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )
    return fig


def build_mod4_depth_response_figure(radius, z1, length, delta_rho, G=6.67430e-11):
    z1_vals = np.linspace(max(5.0, 0.25 * z1), 2.5 * z1, 300)
    z2_vals = z1_vals + length
    dg_vals = cylinder_vertical_anomaly(radius, z1_vals, z2_vals, delta_rho, G) * 1e5

    current_dg = cylinder_vertical_anomaly(radius, z1, z1 + length, delta_rho, G) * 1e5

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=z1_vals,
        y=dg_vals,
        fill="tozeroy",
        fillcolor="rgba(47,168,143,0.14)",
        line=dict(color="#2fa88f", width=3.5),
        name="Δg sobre el eje",
        hovertemplate="z₁ = %{x:.2f} m<br>Δg = %{y:.4f} mGal<extra></extra>"
    ))

    fig.add_trace(go.Scatter(
        x=[z1],
        y=[current_dg],
        mode="markers+text",
        marker=dict(size=10, color="#102028"),
        text=["Caso actual"],
        textposition="top center",
        name="Caso actual",
        hovertemplate="z₁ = %{x:.2f} m<br>Δg = %{y:.4f} mGal<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,1)",
        height=320,
        margin=dict(l=55, r=20, t=20, b=55),
        font=dict(family="JetBrains Mono", color="#6b7f86", size=10),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#d7e4df",
            borderwidth=1,
            font=dict(color="#24343a", size=11),
            x=0.58,
            y=0.97
        ),
        xaxis=dict(
            title=dict(text="Profundidad del tope z₁ (m)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="Δg (mGal)", font=dict(color="#6b7f86", size=11)),
            gridcolor="#e2ece8",
            linecolor="#d7e4df",
            tickfont=dict(color="#6b7f86"),
            zeroline=False
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#ffffff",
            bordercolor="#d7e4df",
            font=dict(color="#24343a", family="JetBrains Mono", size=11)
        ),
    )
    return fig

def render_mod1():
    m = next(x for x in MODULES if x["key"] == "mod1")
    color = m["color"]

    if st.button("← Volver al inicio", key="btn_back_mod1", width="stretch"):
        st.session_state.pagina = "home"
        st.rerun()

    st.markdown(f"""
    <div style="border-left: 3px solid {color}; padding-left: 1.3rem; margin: 1.5rem 0 0.5rem;">
    <div class="page-num">{m['num']}</div>
    <div class="page-title">{m['icon']} &nbsp;{m['title'].replace(chr(10), ' ')}</div>
    </div>
    <p style="font-family:Space Mono,monospace; font-size:0.8rem; color:#6b7f86;
            line-height:1.7; max-width:850px; margin: 0.8rem 0 2rem; padding-left:1.3rem;">
    Modelo de esfera homogénea con densidad constante. Se estudia la gravedad para puntos
    interiores y exteriores, verificando que la expresión cambia en r = R pero el valor
    permanece continuo.
    </p>""", unsafe_allow_html=True)

    st.markdown(f'<div class="sec-label" style="color:{color};">SUBTEMAS</div>', unsafe_allow_html=True)
    cols_sub = st.columns(len(m["subtemas"]))
    for col, sub in zip(cols_sub, m["subtemas"]):
        col.markdown(f"""
    <div style="background:var(--panel); border:1px solid var(--border); border-top:2px solid {color};
        border-radius:8px; padding:1rem 0.8rem; font-family:'Space Mono',monospace;
        font-size:0.72rem; color:var(--text); line-height:1.5; text-align:center; min-height:70px;
        display:flex; align-items:center; justify-content:center;">
    {sub}
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Fundamento matemático",
        "Explorador interactivo",
        "Validación numérica"
    ])

    with tab1:
        col_a, col_b = st.columns([1.25, 1.0], gap="large")

        with col_a:
            st.markdown('<div class="sec-label">01 &nbsp; HIPÓTESIS DEL MODELO</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Supuestos usados en la demostración</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="soft-note">
            Se asume una esfera perfecta de radio <b>R</b>, masa total <b>M</b> y densidad constante <b>ρ</b>.
            La variable <b>r</b> representa la distancia desde el centro hasta el punto de observación P.
            El caso exterior usa toda la masa M; el caso interior solo usa la masa contenida M(r).
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-label">02 &nbsp; ECUACIONES BASE</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Definiciones del módulo 1</div>', unsafe_allow_html=True)

            st.latex(r"F = G\frac{m\,M}{r^2}")
            st.latex(r"g = \frac{F}{m}")
            st.latex(r"\oint_S \vec{g}\cdot d\vec{S} = -4\pi G\,M_{\mathrm{enc}}")
            st.latex(r"M = \frac{4}{3}\pi \rho R^3")
            st.latex(r"M(r) = \frac{4}{3}\pi \rho r^3 = M\frac{r^3}{R^3}")

        with col_b:
            st.markdown('<div class="sec-label">03 &nbsp; FUNCIÓN FINAL</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Expresión por tramos</div>', unsafe_allow_html=True)

            st.latex(r"""
            g(r)=
            \begin{cases}
            \dfrac{GMr}{R^3}, & 0 \le r < R \\
            \dfrac{GM}{r^2}, & r \ge R
            \end{cases}
            """)

            st.markdown("""
            <div class="soft-note">
            Interpretación física:
            <br>• En el <b>interior</b>, la gravedad crece linealmente desde el centro.
            <br>• En el <b>exterior</b>, la esfera se comporta como una masa puntual concentrada en el centro.
            <br>• En <b>r = R</b>, ambas expresiones entregan el mismo valor.
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            col_c, col_d = st.columns(2, gap="large")

        with col_c:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Exterior: r ≥ R</div>
            <div class="step-text">
                La superficie gaussiana de radio r encierra toda la masa M.
                Por simetría esférica, la magnitud de g es constante sobre la superficie,
                por lo que el resultado coincide con el de una masa puntual en el centro.
            </div>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"g(r)\,4\pi r^2 = 4\pi G M")
            st.latex(r"g(r)=\frac{GM}{r^2}")

        with col_d:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Interior: 0 ≤ r &lt; R</div>
            <div class="step-text">
                Solo contribuye la masa contenida dentro de la esfera de radio r.
                Como la densidad es constante, la masa encerrada es proporcional a r³.
                Al sustituir en la expresión gravitatoria, el resultado es lineal en r.
            </div>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"M(r)=M\frac{r^3}{R^3}")
            st.latex(r"g(r)=\frac{GM(r)}{r^2}=\frac{GMr}{R^3}")

    with tab2:
        st.markdown('<div class="sec-label">04 &nbsp; CONTROLES DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Ajusta parámetros y explora g(r)</div>', unsafe_allow_html=True)

        col_ctrl, col_plot = st.columns([1.0, 1.45], gap="large")

        with col_ctrl:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)

            mode = st.radio(
                "Modo de parametrización",
                ["Ingresar M y R", "Ingresar ρ y R"],
                key="mod1_param_mode",
                horizontal=True
            )

            if mode == "Ingresar M y R":
                M = st.number_input(
                    "Masa total  de la Tierra M (kg)",
                    min_value=1.0,
                    value=5.972e24,
                    step=1.0e23,
                    format="%.6e",
                    key="mod1_M"
                )
                R = st.number_input(
                    "Radio R de la Tierra(m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod1_R"
                )
                rho = 3 * M / (4 * np.pi * R**3)
            else:
                rho = st.number_input(
                    "Densidad constante ρ (kg/m³)",
                    min_value=1.0,
                    value=5515.0,
                    step=10.0,
                    format="%.3f",
                    key="mod1_rho"
                )
                R = st.number_input(
                    "Radio R de la Tierra (m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod1_R_from_rho"
                )
                M = (4 / 3) * np.pi * rho * R**3

            G = st.number_input(
                "Constante G (m³ kg⁻¹ s⁻²)",
                min_value=1e-20,
                value=6.67430e-11,
                step=1e-12,
                format="%.6e",
                key="mod1_G"
            )

            max_eta = st.slider(
                "Alcance radial máximo (r_max / R)",
                min_value=1.20,
                max_value=5.00,
                value=3.00,
                step=0.05,
                key="mod1_max_eta"
            )

            eta_probe = st.slider(
                "Punto de evaluación (r / R)",
                min_value=0.00,
                max_value=float(max_eta),
                value=1.00,
                step=0.01,
                key="mod1_eta_probe"
            )

            r_probe = eta_probe * R
            g_surface = G * M / R**2
            g_probe = float(gravity_piecewise(np.array([r_probe]), M, R, G)[0])

            region = "Interior" if r_probe < R else "Exterior / Superficie"
            m_enc_probe = float(enclosed_mass(np.array([r_probe]), M, R)[0])

            cards_html = f"""
            <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-label">Región actual</div>
                <div class="metric-value">{region}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">g(R) de la Tierra</div>
                <div class="metric-value">{g_surface:.5f} m/s²</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">r evaluado</div>
                <div class="metric-value">{r_probe/1e3:,.2f} km</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">g(r) en el punto evaluado</div>
                <div class="metric-value">{g_probe:.5f} m/s²</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">ρ derivada</div>
                <div class="metric-value">{rho:,.2f} kg/m³</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">M(r) contenida</div>
                <div class="metric-value">{m_enc_probe:.3e} kg</div>
            </div>
            </div>
            """
            st.markdown(cards_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_plot:
            radius = np.linspace(0.0, max_eta * R, 900)
            gravity = gravity_piecewise(radius, M, R, G)

            st.plotly_chart(
                build_mod1_profile_figure(radius, gravity, R, r_probe, g_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod1_normalized_figure(max_eta, eta_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

    with tab3:
        st.markdown('<div class="sec-label">05 &nbsp; VERIFICACIÓN DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Continuidad y valores característicos</div>', unsafe_allow_html=True)

        g_R_inside = G * M * R / R**3
        g_R_outside = G * M / R**2
        diff_R = abs(g_R_inside - g_R_outside)

        col_v1, col_v2 = st.columns([1.0, 1.1], gap="large")

        with col_v1:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Verificación en la superficie</div>
            <div class="step-text">
                La demostración exige que en r = R cambie la expresión,
                pero no el valor numérico. Ese principio de continuidad se comprueba aquí
                comparando la fórmula interior con la exterior justo en la superficie.
            </div>
            </div>
            """, unsafe_allow_html=True)

            st.latex(r"g_{\mathrm{int}}(R)=\frac{GMR}{R^3}=\frac{GM}{R^2}")
            st.latex(r"g_{\mathrm{ext}}(R)=\frac{GM}{R^2}")

            st.markdown(f"""
            <div class="soft-note">
            <b>Resultado numérico</b>
            <br>g<sub>int</sub>(R) = {g_R_inside:.8f} m/s²
            <br>g<sub>ext</sub>(R) = {g_R_outside:.8f} m/s²
            <br>|Δ| = {diff_R:.3e} m/s²
            </div>
            """, unsafe_allow_html=True)

        with col_v2:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Interpretación física</div>
            <div class="step-text">
                • En el centro, g(0) = 0.
                <br>• En el interior, g aumenta linealmente porque M(r) ∝ r³.
                <br>• En la superficie, g alcanza su máximo para este modelo.
                <br>• En el exterior, g decrece siguiendo una ley inversa al cuadrado.
            </div>
            </div>
            """, unsafe_allow_html=True)

        sample_etas = sorted(set([0.0, 0.25, 0.50, 0.75, 1.00, 1.50, 2.00, float(max_eta)]))
        rows_html = ""

        for eta in sample_etas:
            r_i = eta * R
            g_i = float(gravity_piecewise(np.array([r_i]), M, R, G)[0])
            region_i = "Interior" if eta < 1 else "Exterior / superficie"
            rows_html += (
                "<tr>"
                f"<td>{eta:.2f}</td>"
                f"<td>{r_i/1e3:,.2f}</td>"
                f"<td>{g_i:.6f}</td>"
                f"<td>{region_i}</td>"
                "</tr>"
            )

        st.markdown(f"""
            <table class="mod-table">
            <thead>
                <tr>
                <th>r/R</th>
                <th>r (km)</th>
                <th>g(r) (m/s²)</th>
                <th>Región</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
            </table>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
    MÓDULO 01 · GRAVEDAD INTERIOR Y EXTERIOR · ESFERA HOMOGÉNEA
    </div>
    """, unsafe_allow_html=True)

def render_mod2():
    m = next(x for x in MODULES if x["key"] == "mod2")
    color = m["color"]

    if st.button("← Volver al inicio", key="btn_back_mod2", width="stretch"):
        st.session_state.pagina = "home"
        st.rerun()

    st.markdown(f"""
    <div style="border-left: 3px solid {color}; padding-left: 1.3rem; margin: 1.5rem 0 0.5rem;">
    <div class="page-num">{m['num']}</div>
    <div class="page-title">{m['icon']} &nbsp;{m['title'].replace(chr(10), ' ')}</div>
    </div>
    <p style="font-family:Space Mono,monospace; font-size:0.8rem; color:#6b7f86;
            line-height:1.7; max-width:850px; margin: 0.8rem 0 2rem; padding-left:1.3rem;">
    Modelo de superficie esférica de radio R y masa total M distribuida uniformemente.
    El potencial es constante en el interior y newtoniano en el exterior.
    El módulo permite verificar visual y numéricamente la continuidad del potencial en r = R.
    </p>""", unsafe_allow_html=True)

    st.markdown(f'<div class="sec-label" style="color:{color};">SUBTEMAS</div>', unsafe_allow_html=True)
    cols_sub = st.columns(len(m["subtemas"]))
    for col, sub in zip(cols_sub, m["subtemas"]):
        col.markdown(f"""
        <div style="background:var(--panel); border:1px solid var(--border); border-top:2px solid {color};
            border-radius:8px; padding:1rem 0.8rem; font-family:'Space Mono',monospace;
            font-size:0.72rem; color:var(--text); line-height:1.5; text-align:center; min-height:70px;
            display:flex; align-items:center; justify-content:center;">
        {sub}
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Fundamento matemático",
        "Explorador interactivo",
        "Validación numérica"
    ])

    with tab1:
        col_a, col_b = st.columns([1.2, 1.0], gap="large")

        with col_a:
            st.markdown('<div class="sec-label">01 &nbsp; HIPÓTESIS DEL MODELO</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Cascarón esférico uniforme</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="soft-note">
            Se modela una <b>superficie esférica</b> de radio <b>R</b> y masa total <b>M</b>,
            con densidad superficial uniforme <b>σ</b>.
            El punto de observación <b>P</b> está a una distancia radial <b>r</b> del centro.
            En este módulo se usa la misma convención del documento:
            se representa el potencial con magnitud positiva.
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-label">02 &nbsp; ECUACIONES BASE</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Definiciones del módulo 2</div>', unsafe_allow_html=True)

            st.latex(r"\sigma=\frac{M}{4\pi R^2}")
            st.latex(r"V(P)=G\int_S \frac{dm}{l}")
            st.latex(r"dm=\sigma\,dS")

        with col_b:
            st.markdown('<div class="sec-label">03 &nbsp; FUNCIÓN FINAL</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Resultado por tramos</div>', unsafe_allow_html=True)

            st.latex(r"""
            V(r)=
            \begin{cases}
            \dfrac{GM}{R}, & 0 \le r \le R \\
            \dfrac{GM}{r}, & r > R
            \end{cases}
            """)

            st.latex(r"""
            g(r)=
            \begin{cases}
            0, & 0 \le r < R \\
            \dfrac{GM}{r^2}, & r \ge R
            \end{cases}
            """)

            st.markdown("""
            <div class="soft-note">
            Interpretación física:
            <br>• En el <b>interior</b>, el potencial es constante.
            <br>• Por eso, en el interior <b>g(r)=0</b>.
            <br>• En el <b>exterior</b>, el cascarón se comporta como una masa puntual en el centro.
            <br>• En <b>r = R</b>, el potencial es continuo.
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        col_c, col_d = st.columns(2, gap="large")

        with col_c:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Exterior: r &gt; R</div>
            <div class="step-text">
                La integración sobre toda la superficie del cascarón produce el mismo potencial
                que una masa puntual M ubicada en el centro. Por eso, fuera del cascarón
                se obtiene una ley newtoniana V(r)=GM/r.
            </div>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"V_{\mathrm{ext}}(r)=\frac{GM}{r}")

        with col_d:
            st.markdown("""
            <div class="step-card">
            <div class="step-title">Interior: 0 ≤ r ≤ R</div>
            <div class="step-text">
                Dentro del cascarón, los aportes de todos los elementos superficiales
                se compensan de forma que el potencial permanece constante en todo el espacio interior.
                Al ser constante, su gradiente es nulo y por eso no hay atracción gravitatoria neta.
            </div>
            </div>
            """, unsafe_allow_html=True)
            st.latex(r"V_{\mathrm{int}}(r)=\frac{GM}{R}")
            st.latex(r"g_{\mathrm{int}}(r)=0")

    with tab2:
        st.markdown('<div class="sec-label">04 &nbsp; CONTROLES DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Explora el potencial del cascarón esférico</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="soft-note">
        La visualización 3D del cascarón muestra la geometría de la distribución superficial de masa.
        La superficie 3D del potencial muestra el comportamiento radial del modelo:
        una <b>meseta interior</b> para r ≤ R y una caída <b>hiperbólica</b> para r > R.
        </div>
        """, unsafe_allow_html=True)
        col_ctrl, col_plot = st.columns([1.0, 1.45], gap="large")

        with col_ctrl:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)

            mode = st.radio(
                "Modo de parametrización",
                ["Ingresar M y R", "Ingresar σ y R"],
                key="mod2_param_mode",
                horizontal=True
            )

            if mode == "Ingresar M y R":
                M = st.number_input(
                    "Masa total M (kg)",
                    min_value=1.0,
                    value=5.972e24,
                    step=1.0e23,
                    format="%.6e",
                    key="mod2_M"
                )
                R = st.number_input(
                    "Radio R (m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod2_R"
                )
                sigma = shell_surface_density(M, R)
            else:
                sigma = st.number_input(
                    "Densidad superficial σ (kg/m²)",
                    min_value=1.0,
                    value=1.169e10,
                    step=1.0e8,
                    format="%.6e",
                    key="mod2_sigma"
                )
                R = st.number_input(
                    "Radio R (m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod2_R_from_sigma"
                )
                M = 4 * np.pi * R**2 * sigma

            G = st.number_input(
                "Constante G (m³ kg⁻¹ s⁻²)",
                min_value=1e-20,
                value=6.67430e-11,
                step=1e-12,
                format="%.6e",
                key="mod2_G"
            )

            max_eta = st.slider(
                "Alcance radial máximo (r_max / R)",
                min_value=1.20,
                max_value=5.00,
                value=3.00,
                step=0.05,
                key="mod2_max_eta"
            )

            eta_probe = st.slider(
                "Punto de evaluación (r / R)",
                min_value=0.00,
                max_value=float(max_eta),
                value=0.70,
                step=0.01,
                key="mod2_eta_probe"
            )

            r_probe = eta_probe * R
            V_surface = G * M / R
            V_probe = float(shell_potential_piecewise(np.array([r_probe]), M, R, G)[0])
            g_probe = float(shell_gravity_piecewise(np.array([r_probe]), M, R, G)[0])

            if eta_probe < 1:
                region = "Interior"
            elif np.isclose(eta_probe, 1.0):
                region = "Superficie"
            else:
                region = "Exterior"

            cards_html = f"""
            <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-label">Región actual</div>
                <div class="metric-value">{region}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">V(R)</div>
                <div class="metric-value">{V_surface:.5f} m²/s²</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">r evaluado</div>
                <div class="metric-value">{r_probe/1e3:,.2f} km</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">V(r)</div>
                <div class="metric-value">{V_probe:.5f} m²/s²</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">σ derivada</div>
                <div class="metric-value">{sigma:.3e} kg/m²</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">g(r)</div>
                <div class="metric-value">{g_probe:.5f} m/s²</div>
            </div>
            </div>
            """
            st.markdown(cards_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_plot:
            radius = np.linspace(0.0, max_eta * R, 900)
            potential = shell_potential_piecewise(radius, M, R, G)
            gravity = shell_gravity_piecewise(radius, M, R, G)

            st.plotly_chart(
                build_mod2_shell_figure(R, r_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod2_potential_surface_figure(max_eta, eta_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod2_potential_figure(radius, potential, R, r_probe, V_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod2_gravity_figure(radius, gravity, R, r_probe, g_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

    with tab3:
        st.markdown('<div class="sec-label">05 &nbsp; VERIFICACIÓN DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Continuidad del potencial y campo interior nulo</div>', unsafe_allow_html=True)

        V_R_inside = G * M / R
        V_R_outside = G * M / R
        diff_R = abs(V_R_inside - V_R_outside)

        V_025 = float(shell_potential_piecewise(np.array([0.25 * R]), M, R, G)[0])
        V_075 = float(shell_potential_piecewise(np.array([0.75 * R]), M, R, G)[0])
        g_025 = float(shell_gravity_piecewise(np.array([0.25 * R]), M, R, G)[0])
        g_075 = float(shell_gravity_piecewise(np.array([0.75 * R]), M, R, G)[0])

        col_v1, col_v2 = st.columns([1.0, 1.1], gap="large")

        with col_v1:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Chequeo en la superficie</div>'
                '<div class="step-text">'
                'El potencial cambia de expresión al cruzar r = R, '
                'pero no cambia de valor. Esa continuidad se verifica '
                'comparando la rama interior con la exterior en la superficie.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.latex(r"V_{\mathrm{int}}(R)=\frac{GM}{R}")
            st.latex(r"V_{\mathrm{ext}}(R)=\frac{GM}{R}")

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Resultado numérico</b><br>'
                f'V<sub>int</sub>(R) = {V_R_inside:.8f} m²/s²<br>'
                f'V<sub>ext</sub>(R) = {V_R_outside:.8f} m²/s²<br>'
                f'|Δ| = {diff_R:.3e} m²/s²'
                f'</div>',
                unsafe_allow_html=True
            )

        with col_v2:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Verificación interior</div>'
                '<div class="step-text">'
                'Si el documento es correcto, dos puntos distintos dentro del cascarón '
                'deben tener el mismo potencial y campo nulo. '
                'Aquí se comparan 0.25R y 0.75R.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Comparación interior</b><br>'
                f'V(0.25R) = {V_025:.8f} m²/s²<br>'
                f'V(0.75R) = {V_075:.8f} m²/s²<br>'
                f'g(0.25R) = {g_025:.8f} m/s²<br>'
                f'g(0.75R) = {g_075:.8f} m/s²'
                f'</div>',
                unsafe_allow_html=True
            )

        sample_etas = [0.0, 0.25, 0.50, 0.75, 1.00, 1.50, 2.00, float(max_eta)]
        sample_etas = sorted(set(sample_etas))

        rows_html = ""
        for eta in sample_etas:
            r_i = eta * R
            V_i = float(shell_potential_piecewise(np.array([r_i]), M, R, G)[0])
            g_i = float(shell_gravity_piecewise(np.array([r_i]), M, R, G)[0])

            if eta < 1:
                region_i = "Interior"
            elif np.isclose(eta, 1.0):
                region_i = "Superficie"
            else:
                region_i = "Exterior"

            rows_html += (
                "<tr>"
                f"<td>{eta:.2f}</td>"
                f"<td>{r_i/1e3:,.2f}</td>"
                f"<td>{V_i:.6f}</td>"
                f"<td>{g_i:.6f}</td>"
                f"<td>{region_i}</td>"
                "</tr>"
            )

        table_html = (
            '<table class="mod-table">'
            '<thead>'
            '<tr>'
            '<th>r/R</th>'
            '<th>r (km)</th>'
            '<th>V(r) (m²/s²)</th>'
            '<th>g(r) (m/s²)</th>'
            '<th>Región</th>'
            '</tr>'
            '</thead>'
            '<tbody>'
            f'{rows_html}'
            '</tbody>'
            '</table>'
        )

        st.markdown(table_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="footer">'
        'MÓDULO 02 · POTENCIAL DEL CASCARÓN ESFÉRICO'
        '</div>',
        unsafe_allow_html=True
    )

def render_mod3():
    m = next(x for x in MODULES if x["key"] == "mod3")
    color = m["color"]

    if st.button("← Volver al inicio", key="btn_back_mod3", width="stretch"):
        st.session_state.pagina = "home"
        st.rerun()

    st.markdown(f"""
<div style="border-left: 3px solid {color}; padding-left: 1.3rem; margin: 1.5rem 0 0.5rem;">
  <div class="page-num">{m['num']}</div>
  <div class="page-title">{m['icon']} &nbsp;{m['title'].replace(chr(10), ' ')}</div>
</div>
<p style="font-family:Space Mono,monospace; font-size:0.8rem; color:#6b7f86;
          line-height:1.7; max-width:850px; margin: 0.8rem 0 2rem; padding-left:1.3rem;">
  Esfera sólida de densidad constante. El potencial interior sigue una ley parabólica,
  mientras que en el exterior la esfera es equivalente a una masa puntual en el centro.
  El módulo permite verificar la continuidad en r = R y el máximo del potencial en el centro.
</p>""", unsafe_allow_html=True)

    st.markdown(f'<div class="sec-label" style="color:{color};">SUBTEMAS</div>', unsafe_allow_html=True)
    cols_sub = st.columns(len(m["subtemas"]))
    for col, sub in zip(cols_sub, m["subtemas"]):
        col.markdown(f"""
<div style="background:var(--panel); border:1px solid var(--border); border-top:2px solid {color};
     border-radius:8px; padding:1rem 0.8rem; font-family:'Space Mono',monospace;
     font-size:0.72rem; color:var(--text); line-height:1.5; text-align:center; min-height:70px;
     display:flex; align-items:center; justify-content:center;">
  {sub}
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Fundamento matemático",
        "Explorador interactivo",
        "Validación numérica"
    ])

    with tab1:
        col_a, col_b = st.columns([1.2, 1.0], gap="large")

        with col_a:
            st.markdown('<div class="sec-label">01 &nbsp; HIPÓTESIS DEL MODELO</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Esfera homogénea de densidad constante</div>', unsafe_allow_html=True)

            st.markdown("""
<div class="soft-note">
Se modela una <b>esfera sólida</b> de radio <b>R</b> y densidad constante <b>ρ</b>.
La masa total es <b>M = (4/3)πρR³</b>. Para un punto a distancia radial <b>r</b>,
el potencial interior se obtiene sumando las contribuciones de los cascarones interiores
y exteriores, tal como lo expone el documento.
</div>
""", unsafe_allow_html=True)

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-label">02 &nbsp; ECUACIONES BASE</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Definiciones del módulo 3</div>', unsafe_allow_html=True)

            st.latex(r"M=\frac{4}{3}\pi \rho R^3")
            st.latex(r"V(P)=\int dV")
            st.latex(r"V_{\mathrm{ext}}(r)=\frac{GM}{r}")
            st.latex(r"V_{\mathrm{int}}(r)=\frac{GM(3R^2-r^2)}{2R^3}")

        with col_b:
            st.markdown('<div class="sec-label">03 &nbsp; FUNCIÓN FINAL</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Potencial y campo por tramos</div>', unsafe_allow_html=True)

            st.latex(r"""
V(r)=
\begin{cases}
\dfrac{GM(3R^2-r^2)}{2R^3}, & 0 \le r \le R \\
\dfrac{GM}{r}, & r > R
\end{cases}
""")

            st.latex(r"""
g(r)=
\begin{cases}
\dfrac{GMr}{R^3}, & 0 \le r < R \\
\dfrac{GM}{r^2}, & r \ge R
\end{cases}
""")

            st.markdown("""
<div class="soft-note">
Interpretación física:
<br>• En el <b>interior</b>, el potencial describe un paraboloide invertido.
<br>• En el <b>centro</b>, el potencial alcanza su valor máximo.
<br>• En el <b>exterior</b>, la esfera se comporta como masa puntual.
<br>• En <b>r = R</b>, el potencial y el campo siguen siendo continuos.
</div>
""", unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        col_c, col_d = st.columns(2, gap="large")

        with col_c:
            st.markdown("""
<div class="step-card">
  <div class="step-title">Exterior: r &gt; R</div>
  <div class="step-text">
    La suma de todos los cascarones de la esfera reproduce exactamente
    el comportamiento de una masa puntual concentrada en el centro.
    Por eso, fuera de la esfera el potencial es newtoniano.
  </div>
</div>
""", unsafe_allow_html=True)
            st.latex(r"V_{\mathrm{ext}}(r)=\frac{GM}{r}")

        with col_d:
            st.markdown("""
<div class="step-card">
  <div class="step-title">Interior: 0 ≤ r ≤ R</div>
  <div class="step-text">
    El potencial interior combina la contribución de la masa interna,
    que actúa como masa puntual, y la contribución de los cascarones externos,
    que aportan un potencial constante. El resultado es una función parabólica.
  </div>
</div>
""", unsafe_allow_html=True)
            st.latex(r"V_{\mathrm{int}}(r)=\frac{GM(3R^2-r^2)}{2R^3}")

    with tab2:
        st.markdown('<div class="sec-label">04 &nbsp; CONTROLES DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Explora el potencial de la esfera homogénea</div>', unsafe_allow_html=True)

        st.markdown("""
<div class="soft-note">
La vista 3D de la esfera muestra la geometría del cuerpo homogéneo.
La superficie 3D del potencial muestra un <b>máximo central</b>,
una caída <b>parabólica</b> en el interior y un decaimiento <b>newtoniano</b> en el exterior.
</div>
""", unsafe_allow_html=True)

        col_ctrl, col_plot = st.columns([1.0, 1.45], gap="large")

        with col_ctrl:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)

            mode = st.radio(
                "Modo de parametrización",
                ["Ingresar M y R", "Ingresar ρ y R"],
                key="mod3_param_mode",
                horizontal=True
            )

            if mode == "Ingresar M y R":
                M = st.number_input(
                    "Masa total M (kg)",
                    min_value=1.0,
                    value=5.972e24,
                    step=1.0e23,
                    format="%.6e",
                    key="mod3_M"
                )
                R = st.number_input(
                    "Radio R (m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod3_R"
                )
                rho = solid_sphere_density_from_mass(M, R)
            else:
                rho = st.number_input(
                    "Densidad constante ρ (kg/m³)",
                    min_value=1.0,
                    value=5515.0,
                    step=10.0,
                    format="%.3f",
                    key="mod3_rho"
                )
                R = st.number_input(
                    "Radio R (m)",
                    min_value=1.0,
                    value=6.371e6,
                    step=1.0e5,
                    format="%.6e",
                    key="mod3_R_from_rho"
                )
                M = solid_sphere_mass_from_density(rho, R)

            G = st.number_input(
                "Constante G (m³ kg⁻¹ s⁻²)",
                min_value=1e-20,
                value=6.67430e-11,
                step=1e-12,
                format="%.6e",
                key="mod3_G"
            )

            max_eta = st.slider(
                "Alcance radial máximo (r_max / R)",
                min_value=1.20,
                max_value=5.00,
                value=3.00,
                step=0.05,
                key="mod3_max_eta"
            )

            eta_probe = st.slider(
                "Punto de evaluación (r / R)",
                min_value=0.00,
                max_value=float(max_eta),
                value=0.60,
                step=0.01,
                key="mod3_eta_probe"
            )

            r_probe = eta_probe * R
            V_probe = float(solid_sphere_potential_piecewise(np.array([r_probe]), M, R, G)[0])
            g_probe = float(solid_sphere_gravity_piecewise(np.array([r_probe]), M, R, G)[0])
            V_surface = G * M / R
            V_center = 3.0 * G * M / (2.0 * R)

            if eta_probe < 1:
                region = "Interior"
            elif np.isclose(eta_probe, 1.0):
                region = "Superficie"
            else:
                region = "Exterior"

            cards_html = f"""
<div class="metric-grid">
  <div class="metric-card">
    <div class="metric-label">Región actual</div>
    <div class="metric-value">{region}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">V(0)</div>
    <div class="metric-value">{V_center:.5f} m²/s²</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">V(R)</div>
    <div class="metric-value">{V_surface:.5f} m²/s²</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">r evaluado</div>
    <div class="metric-value">{r_probe/1e3:,.2f} km</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">V(r)</div>
    <div class="metric-value">{V_probe:.5f} m²/s²</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">g(r)</div>
    <div class="metric-value">{g_probe:.5f} m/s²</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">ρ derivada</div>
    <div class="metric-value">{rho:,.2f} kg/m³</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">M total</div>
    <div class="metric-value">{M:.3e} kg</div>
  </div>
</div>
"""
            st.markdown(cards_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_plot:
            radius = np.linspace(0.0, max_eta * R, 900)
            potential = solid_sphere_potential_piecewise(radius, M, R, G)
            gravity = solid_sphere_gravity_piecewise(radius, M, R, G)

            st.plotly_chart(
                build_mod3_sphere_figure(R, r_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod3_potential_surface_figure(max_eta, eta_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod3_potential_figure(radius, potential, R, r_probe, V_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod3_gravity_figure(radius, gravity, R, r_probe, g_probe),
                width="stretch",
                config={"displayModeBar": False}
            )

    with tab3:
        st.markdown('<div class="sec-label">05 &nbsp; VERIFICACIÓN DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Continuidad y máximo central del potencial</div>', unsafe_allow_html=True)

        V_R_inside = G * M * (3.0 * R**2 - R**2) / (2.0 * R**3)
        V_R_outside = G * M / R
        diff_R = abs(V_R_inside - V_R_outside)

        V_center = 3.0 * G * M / (2.0 * R)
        V_half = float(solid_sphere_potential_piecewise(np.array([0.5 * R]), M, R, G)[0])

        col_v1, col_v2 = st.columns([1.0, 1.1], gap="large")

        with col_v1:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Chequeo en la superficie</div>'
                '<div class="step-text">'
                'La función cambia de expresión al pasar por r = R, '
                'pero debe conservar el mismo valor numérico. '
                'Aquí se compara la rama interior con la exterior en la superficie.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.latex(r"V_{\mathrm{int}}(R)=\frac{GM(3R^2-R^2)}{2R^3}=\frac{GM}{R}")
            st.latex(r"V_{\mathrm{ext}}(R)=\frac{GM}{R}")

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Resultado numérico</b><br>'
                f'V<sub>int</sub>(R) = {V_R_inside:.8f} m²/s²<br>'
                f'V<sub>ext</sub>(R) = {V_R_outside:.8f} m²/s²<br>'
                f'|Δ| = {diff_R:.3e} m²/s²'
                f'</div>',
                unsafe_allow_html=True
            )

        with col_v2:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Chequeo en el centro</div>'
                '<div class="step-text">'
                'El documento establece que el potencial interior es parabólico '
                'y alcanza su valor máximo en r = 0. '
                'Por eso, V(0) debe ser mayor que V(r) para puntos interiores distintos del centro.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Comparación interior</b><br>'
                f'V(0) = {V_center:.8f} m²/s²<br>'
                f'V(0.5R) = {V_half:.8f} m²/s²<br>'
                f'V(0) − V(0.5R) = {V_center - V_half:.8f} m²/s²'
                f'</div>',
                unsafe_allow_html=True
            )

        sample_etas = [0.0, 0.25, 0.50, 0.75, 1.00, 1.50, 2.00, float(max_eta)]
        sample_etas = sorted(set(sample_etas))

        rows_html = ""
        for eta in sample_etas:
            r_i = eta * R
            V_i = float(solid_sphere_potential_piecewise(np.array([r_i]), M, R, G)[0])
            g_i = float(solid_sphere_gravity_piecewise(np.array([r_i]), M, R, G)[0])

            if eta < 1:
                region_i = "Interior"
            elif np.isclose(eta, 1.0):
                region_i = "Superficie"
            else:
                region_i = "Exterior"

            rows_html += (
                "<tr>"
                f"<td>{eta:.2f}</td>"
                f"<td>{r_i/1e3:,.2f}</td>"
                f"<td>{V_i:.6f}</td>"
                f"<td>{g_i:.6f}</td>"
                f"<td>{region_i}</td>"
                "</tr>"
            )

        table_html = (
            '<table class="mod-table">'
            '<thead>'
            '<tr>'
            '<th>r/R</th>'
            '<th>r (km)</th>'
            '<th>V(r) (m²/s²)</th>'
            '<th>g(r) (m/s²)</th>'
            '<th>Región</th>'
            '</tr>'
            '</thead>'
            '<tbody>'
            f'{rows_html}'
            '</tbody>'
            '</table>'
        )

        st.markdown(table_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="footer">'
        'MÓDULO 03 · POTENCIAL DE LA ESFERA HOMOGÉNEA'
        '</div>',
        unsafe_allow_html=True
    )


def render_mod4():
    m = next(x for x in MODULES if x["key"] == "mod4")
    color = m["color"]

    if st.button("← Volver al inicio", key="btn_back_mod4", width="stretch"):
        st.session_state.pagina = "home"
        st.rerun()

    st.markdown(f"""
<div style="border-left: 3px solid {color}; padding-left: 1.3rem; margin: 1.5rem 0 0.5rem;">
  <div class="page-num">{m['num']}</div>
  <div class="page-title">{m['icon']} &nbsp;{m['title'].replace(chr(10), ' ')}</div>
</div>
<p style="font-family:Space Mono,monospace; font-size:0.8rem; color:#6b7f86;
          line-height:1.7; max-width:900px; margin: 0.8rem 0 2rem; padding-left:1.3rem;">
  Modelo clásico de prospección gravimétrica: cilindro vertical de radio R, contraste de densidad Δρ,
  tope a profundidad z₁ y base a profundidad z₂. El módulo evalúa la atracción vertical Δg
  en el punto de observación ubicado en la superficie, justo sobre el eje de simetría.
</p>""", unsafe_allow_html=True)

    st.markdown(f'<div class="sec-label" style="color:{color};">SUBTEMAS</div>', unsafe_allow_html=True)
    cols_sub = st.columns(len(m["subtemas"]))
    for col, sub in zip(cols_sub, m["subtemas"]):
        col.markdown(f"""
<div style="background:var(--panel); border:1px solid var(--border); border-top:2px solid {color};
     border-radius:8px; padding:1rem 0.8rem; font-family:'Space Mono',monospace;
     font-size:0.72rem; color:var(--text); line-height:1.5; text-align:center; min-height:70px;
     display:flex; align-items:center; justify-content:center;">
  {sub}
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Fundamento matemático",
        "Explorador interactivo",
        "Validación numérica"
    ])

    with tab1:
        col_a, col_b = st.columns([1.2, 1.0], gap="large")

        with col_a:
            st.markdown('<div class="sec-label">01 &nbsp; CONFIGURACIÓN DEL MODELO</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Cilindro vertical en el subsuelo</div>', unsafe_allow_html=True)

            st.markdown("""
<div class="soft-note">
Se modela un <b>cilindro vertical</b> de radio <b>R</b>,
tope a profundidad <b>z₁</b> y base a profundidad <b>z₂</b>.
La densidad anómala del cuerpo respecto al medio encajante es <b>Δρ</b>.
El punto de observación <b>P</b> está en la superficie, sobre el eje del cilindro, con <b>z = 0</b>.
</div>
""", unsafe_allow_html=True)

            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-label">02 &nbsp; ECUACIONES BASE</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Expresión analítica del módulo 4</div>', unsafe_allow_html=True)

            st.latex(r"\Delta g = 2\pi G\Delta \rho \left[(z_2-z_1)+\sqrt{R^2+z_1^2}-\sqrt{R^2+z_2^2}\right]")
            st.latex(r"z_2 = z_1 + L")

        with col_b:
            st.markdown('<div class="sec-label">03 &nbsp; INTERPRETACIÓN FÍSICA</div>', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">Sensibilidad del modelo</div>', unsafe_allow_html=True)

            st.markdown("""
<div class="soft-note">
Interpretación física:
<br>• Si <b>Δρ</b> aumenta, la anomalía crece linealmente.
<br>• Si el <b>radio R</b> aumenta, la anomalía sobre el eje tiende a crecer.
<br>• Si el cilindro se ubica a mayor <b>profundidad</b>, la anomalía disminuye.
<br>• La expresión puede escribirse con <b>z₁ y z₂</b> o con <b>z₁ y L</b>.
</div>
""", unsafe_allow_html=True)

            st.markdown("""
<div class="step-card">
  <div class="step-title">Idea de la demostración</div>
  <div class="step-text">
    El documento construye la anomalía del cilindro integrando
    la atracción gravitatoria de discos delgados a lo largo de toda su longitud.
    El resultado final es una expresión cerrada para la componente vertical Δg.
  </div>
</div>
""", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="sec-label">04 &nbsp; CONTROLES DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Explora la anomalía gravimétrica del cilindro vertical</div>', unsafe_allow_html=True)

        st.markdown("""
<div class="soft-note">
La vista 3D muestra el cilindro enterrado y el punto de observación en la superficie.
La superficie de sensibilidad muestra cómo cambia Δg cuando varían simultáneamente
el radio del cilindro y la profundidad del tope, manteniendo fija su longitud.
</div>
""", unsafe_allow_html=True)

        col_ctrl, col_plot = st.columns([1.0, 1.45], gap="large")

        with col_ctrl:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)

            mode = st.radio(
                "Modo de parametrización vertical",
                ["Ingresar z₁ y z₂", "Ingresar z₁ y L"],
                key="mod4_param_mode",
                horizontal=True
            )

            radius = st.number_input(
                "Radio del cilindro R (m)",
                min_value=1.0,
                value=120.0,
                step=5.0,
                format="%.3f",
                key="mod4_radius"
            )

            delta_rho = st.number_input(
                "Contraste de densidad Δρ (kg/m³)",
                min_value=1.0,
                value=450.0,
                step=10.0,
                format="%.3f",
                key="mod4_delta_rho"
            )

            z1 = st.number_input(
                "Profundidad del tope z₁ (m)",
                min_value=1.0,
                value=80.0,
                step=5.0,
                format="%.3f",
                key="mod4_z1"
            )

            if mode == "Ingresar z₁ y z₂":
                z2 = st.number_input(
                    "Profundidad de la base z₂ (m)",
                    min_value=float(z1 + 1.0),
                    value=max(float(z1 + 220.0), 81.0),
                    step=5.0,
                    format="%.3f",
                    key="mod4_z2"
                )
                length = z2 - z1
            else:
                length = st.number_input(
                    "Longitud L (m)",
                    min_value=1.0,
                    value=220.0,
                    step=5.0,
                    format="%.3f",
                    key="mod4_length"
                )
                z2 = z1 + length

            G = st.number_input(
                "Constante G (m³ kg⁻¹ s⁻²)",
                min_value=1e-20,
                value=6.67430e-11,
                step=1e-12,
                format="%.6e",
                key="mod4_G"
            )

            dg_si = float(cylinder_vertical_anomaly(radius, z1, z2, delta_rho, G))
            dg_mgal = dg_si * 1e5

            cards_html = f"""
<div class="metric-grid">
  <div class="metric-card">
    <div class="metric-label">Punto evaluado</div>
    <div class="metric-value">P sobre el eje</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Longitud L</div>
    <div class="metric-value">{length:,.2f} m</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">z₁</div>
    <div class="metric-value">{z1:,.2f} m</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">z₂</div>
    <div class="metric-value">{z2:,.2f} m</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Δg</div>
    <div class="metric-value">{dg_si:.6e} m/s²</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Δg</div>
    <div class="metric-value">{dg_mgal:.5f} mGal</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Radio R</div>
    <div class="metric-value">{radius:,.2f} m</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Δρ</div>
    <div class="metric-value">{delta_rho:,.2f} kg/m³</div>
  </div>
</div>
"""
            st.markdown(cards_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_plot:
            st.plotly_chart(
                build_mod4_cylinder_figure(radius, z1, z2),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod4_sensitivity_surface_figure(radius, z1, length, delta_rho, G),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod4_radius_response_figure(radius, z1, z2, delta_rho, G),
                width="stretch",
                config={"displayModeBar": False}
            )

            st.plotly_chart(
                build_mod4_depth_response_figure(radius, z1, length, delta_rho, G),
                width="stretch",
                config={"displayModeBar": False}
            )

    with tab3:
        st.markdown('<div class="sec-label">05 &nbsp; VERIFICACIÓN DEL MODELO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Equivalencia de formas y linealidad en Δρ</div>', unsafe_allow_html=True)

        dg_form1 = float(cylinder_vertical_anomaly(radius, z1, z2, delta_rho, G))
        dg_form2 = float(cylinder_vertical_anomaly_from_length(radius, z1, length, delta_rho, G))
        diff_forms = abs(dg_form1 - dg_form2)

        dg_double_density = float(cylinder_vertical_anomaly(radius, z1, z2, 2.0 * delta_rho, G))
        ratio_density = dg_double_density / dg_form1 if dg_form1 != 0 else np.nan

        col_v1, col_v2 = st.columns([1.0, 1.1], gap="large")

        with col_v1:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Equivalencia de expresiones</div>'
                '<div class="step-text">'
                'El documento presenta la anomalía usando z₁ y z₂, '
                'y luego usando la longitud L con z₂ = z₁ + L. '
                'Ambas expresiones deben producir exactamente el mismo valor numérico.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.latex(r"\Delta g = 2\pi G\Delta \rho \left[(z_2-z_1)+\sqrt{R^2+z_1^2}-\sqrt{R^2+z_2^2}\right]")
            st.latex(r"\Delta g = 2\pi G\Delta \rho \left[L+\sqrt{R^2+z_1^2}-\sqrt{R^2+(z_1+L)^2}\right]")

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Resultado numérico</b><br>'
                f'Forma con z₂ = {dg_form1:.8e} m/s²<br>'
                f'Forma con L = {dg_form2:.8e} m/s²<br>'
                f'|Δ| = {diff_forms:.3e} m/s²'
                f'</div>',
                unsafe_allow_html=True
            )

        with col_v2:
            st.markdown(
                '<div class="step-card">'
                '<div class="step-title">Linealidad en el contraste de densidad</div>'
                '<div class="step-text">'
                'La expresión final depende linealmente de Δρ. '
                'Si duplicas el contraste de densidad, la anomalía debe duplicarse.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="soft-note">'
                f'<b>Chequeo de proporcionalidad</b><br>'
                f'Δg(Δρ) = {dg_form1*1e5:.6f} mGal<br>'
                f'Δg(2Δρ) = {dg_double_density*1e5:.6f} mGal<br>'
                f'Razón = {ratio_density:.6f}'
                f'</div>',
                unsafe_allow_html=True
            )

        sample_radii = [0.5 * radius, 0.75 * radius, radius, 1.25 * radius, 1.50 * radius, 2.00 * radius]
        sample_radii = sorted(set([max(1.0, float(v)) for v in sample_radii]))

        rows_html = ""
        for r_i in sample_radii:
            dg_i = float(cylinder_vertical_anomaly(r_i, z1, z2, delta_rho, G))
            rows_html += (
                "<tr>"
                f"<td>{r_i:.2f}</td>"
                f"<td>{z1:.2f}</td>"
                f"<td>{z2:.2f}</td>"
                f"<td>{dg_i:.6e}</td>"
                f"<td>{dg_i*1e5:.6f}</td>"
                "</tr>"
            )

        table_html = (
            '<table class="mod-table">'
            '<thead>'
            '<tr>'
            '<th>R (m)</th>'
            '<th>z₁ (m)</th>'
            '<th>z₂ (m)</th>'
            '<th>Δg (m/s²)</th>'
            '<th>Δg (mGal)</th>'
            '</tr>'
            '</thead>'
            '<tbody>'
            f'{rows_html}'
            '</tbody>'
            '</table>'
        )

        st.markdown(table_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="footer">'
        'MÓDULO 04 · ANOMALÍA GRAVIMÉTRICA DEL CILINDRO VERTICAL'
        '</div>',
        unsafe_allow_html=True
    )
# ═════════════════════════════════════════════
# PÁGINA HOME
# ═════════════════════════════════════════════

def render_home():
    st.markdown("""
    <div class="hero-wrapper">
    <div class="hero-globe">🌍</div>
    <div class="badge">// Modelos clásicos de Geodesia Física</div>
    <h1 class="hero-title">Campo Gravitacional<br><span>de la Tierra</span></h1>
    <p class="hero-sub">
        Demostraciones matemáticas + implementación computacional
        de los fundamentos de la geodesia física moderna.
        Potenciales, anomalías gravimétricas y estructuras esféricas.
    </p>
    <div class="hero-meta">
        <div class="hero-meta-item">DEMOSTRACIONES<b>4 Modelos</b></div>
        <div class="hero-meta-item">ENFOQUE<b>Analítico + computacional</b></div>
        <div class="hero-meta-item">VISUALIZACIÓN<b>Plotly 3D / 2D</b></div>
        <div class="hero-meta-item">INTERFAZ<b>Streamlit</b></div>
    </div>
    </div>
""", unsafe_allow_html=True)
    

    col_globe, col_info = st.columns([3, 2], gap="large")

    with col_globe:
        st.markdown('<div class="sec-label">01 &nbsp; VISUALIZACIÓN INTERACTIVA</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Campo Gravitacional Terrestre</div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="margin-bottom:1rem; font-family:Space Mono,monospace; font-size:0.78rem; color:#5a7a8a;">'
            'Vista preliminar del modelo esférico con variación de gravedad superficial.</p>',
            unsafe_allow_html=True
        )

        phi = np.linspace(0, np.pi, 80)
        theta = np.linspace(0, 2 * np.pi, 120)
        PHI, THETA = np.meshgrid(phi, theta)
        R = 6371
        x = R * np.sin(PHI) * np.cos(THETA)
        y = R * np.sin(PHI) * np.sin(THETA)
        z = R * np.cos(PHI)
        lat = np.pi / 2 - PHI
        g_surface = 9.780327 * (1 + 0.0053024 * np.sin(lat)**2 - 0.0000058 * np.sin(2 * lat)**2)

        fig_globe = go.Figure(data=[go.Surface(
            x=x,
            y=y,
            z=z,
            surfacecolor=g_surface,
            colorscale=[
                [0.0,   "#440154"],
                [0.125, "#482878"],
                [0.25,  "#3e4989"],
                [0.375, "#31688e"],
                [0.5,   "#26828e"],
                [0.625, "#1f9e89"],
                [0.75,  "#35b779"],
                [0.875, "#6ece58"],
                [1.0,   "#fde725"]
            ],
            colorbar=dict(
                title=dict(text="g (m/s²)", font=dict(color='#5a7a8a', size=11, family='JetBrains Mono')),
                tickfont=dict(color='#5a7a8a', size=10, family='JetBrains Mono'),
                bgcolor='rgba(0,0,0,0)',
                bordercolor='#1a3044',
                thickness=12,
                len=0.7
            ),
            showscale=True,
            lighting=dict(ambient=0.6, diffuse=0.7, specular=0.3, roughness=0.4),
            lightposition=dict(x=2, y=2, z=3),
        )])

        fig_globe.update_layout(
            paper_bgcolor='rgba(255,255,255,0)',
            plot_bgcolor='rgba(255,255,255,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=410,
            scene=dict(
                bgcolor='rgba(255,255,255,1)',
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                camera=dict(eye=dict(x=1.4, y=1.0, z=0.7))
            ),
            hoverlabel=dict(
                bgcolor='#ffffff',
                bordercolor='#d7e4df',
                font=dict(color='#24343a', family='JetBrains Mono', size=11)
            )
        )

        st.plotly_chart(fig_globe, width="stretch", config={"displayModeBar": False})

    with col_info:
        st.markdown('<div class="sec-label">02 &nbsp; RESUMEN MATEMÁTICO</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">Funciones que estructuran los 4 módulos</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="formula-box">
        <span class="comment"> Módulo 1 · gravedad de una esfera homogénea</span><br>
        g(r) = GMr/R³ &nbsp; si r &lt; R &nbsp;&nbsp;•&nbsp;&nbsp; g(r) = GM/r² &nbsp; si r ≥ R<br><br>

        <span class="comment">Módulo 2 · potencial del cascarón esférico</span><br>
        V(r) = GM/R &nbsp; si r ≤ R &nbsp;&nbsp;•&nbsp;&nbsp; V(r) = GM/r &nbsp; si r &gt; R<br><br>

        <span class="comment">Módulo 3 · potencial de la esfera homogénea</span><br>
        V(r) = GM(3R² − r²)/(2R³) &nbsp; si r &lt; R &nbsp;&nbsp;•&nbsp;&nbsp; V(r) = GM/r &nbsp; si r ≥ R<br><br>

        <span class="comment">Módulo 4 · anomalía del cilindro vertical</span><br>
        Δg = 2πGΔρ[(z₂ − z₁) + √(R² + z₁²) − √(R² + z₂²)]
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">03 &nbsp; CONTENIDO DEL TALLER</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title" style="margin-bottom:1.4rem;">Selecciona un Módulo</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    cols_map = [col1, col2, col1, col2]

    for m, col in zip(MODULES, cols_map):
        tags_html = "".join(f'<span class="mod-tag {t[1]}">{t[0]}</span>' for t in m["tags"])
        title_display = m["title"].replace("\n", "<br>")

        with col:
            st.markdown(f"""
    <div class="mod-btn-card {m['cls']}">
    <div class="mod-num">{m['num']}</div>
    <span class="mod-icon">{m['icon']}</span>
    <div class="mod-title">{title_display}</div>
    <div class="mod-desc">{m['desc']}</div>
    <div class="mod-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

            if st.button(
                f"Abrir · {m['title'].split(chr(10))[0]}",
                key=f"btn_{m['key']}",
                width="stretch"
            ):
                st.session_state.pagina = m["key"]
                st.rerun()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">04 &nbsp; PREVIEW · ANÁLISIS RADIAL</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title" style="margin-bottom:1.2rem;">Perfil g(r) — Interior y Exterior</div>', unsafe_allow_html=True)

    G_c = 6.674e-11
    M_c = 5.972e24
    Re = 6.371e6

    r_int = np.linspace(0, Re, 500)
    r_ext = np.linspace(Re, 3 * Re, 500)
    g_int = G_c * M_c / Re**3 * r_int
    g_ext = G_c * M_c / r_ext**2

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=r_int / 1e6,
        y=g_int,
        fill='tozeroy',
        fillcolor='rgba(47,168,143,0.12)',
        line=dict(color='#2fa88f', width=2.5),
        name='g interior  (r < R⊕)',
        hovertemplate='r = %{x:.2f} × 10⁶ m<br>g = %{y:.4f} m/s²<extra></extra>'
    ))
    fig2.add_trace(go.Scatter(
        x=r_ext / 1e6,
        y=g_ext,
        fill='tozeroy',
        fillcolor='rgba(212,168,30,0.10)',
        line=dict(color='#d4a81e', width=2.5),
        name='g exterior  (r > R⊕)',
        hovertemplate='r = %{x:.2f} × 10⁶ m<br>g = %{y:.4f} m/s²<extra></extra>'
    ))
    fig2.add_vline(
        x=Re / 1e6,
        line=dict(color='#f5c842', width=1.5, dash='dot'),
        annotation_text="Superficie  R⊕ = 6371 km",
        annotation_font=dict(color='#f5c842', size=10, family='JetBrains Mono'),
        annotation_position="top right"
    )
    fig2.update_layout(
        paper_bgcolor='rgba(255,255,255,0)',
        plot_bgcolor='rgba(255,255,255,1)',
        height=320,
        margin=dict(l=60, r=30, t=20, b=60),
        font=dict(family='JetBrains Mono', color='#6b7f86', size=10),
        legend=dict(
            bgcolor='rgba(255,255,255,0.95)',
            bordercolor='#d7e4df',
            borderwidth=1,
            font=dict(color='#24343a', size=11),
            x=0.6,
            y=0.95
        ),
        xaxis=dict(
            title=dict(text="Radio  r  (× 10⁶ m)", font=dict(color='#6b7f86', size=11)),
            gridcolor='#e2ece8',
            linecolor='#d7e4df',
            tickfont=dict(color='#6b7f86'),
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text="g (m/s²)", font=dict(color='#6b7f86', size=11)),
            gridcolor='#e2ece8',
            linecolor='#d7e4df',
            tickfont=dict(color='#6b7f86'),
            zeroline=False
        ),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor='#ffffff',
            bordercolor='#d7e4df',
            font=dict(color='#24343a', family='JetBrains Mono', size=11)
        ),
    )

    st.plotly_chart(fig2, width="stretch", config={"displayModeBar": False})

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">05 &nbsp; STACK TECNOLÓGICO</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="stack-row">
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#00c8ff;"></span>Python 3.x</div>
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#00ffb3;"></span>Streamlit</div>
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#ff6b35;"></span>Plotly</div>
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#f5c842;"></span>NumPy</div>
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#a78bfa;"></span>SciPy</div>
  <div class="stack-chip"><span class="stack-chip-dot" style="background:#f472b6;"></span>Matplotlib</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="footer">
  TALLER DE GEODESIA FÍSICA &nbsp;·&nbsp; PYTHON &nbsp;·&nbsp;
  CAMPO GRAVITACIONAL &amp; POTENCIALES &nbsp;·&nbsp; ANOMALÍAS GRAVIMÉTRICAS
</div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════
# PÁGINAS DE MÓDULOS
# ═════════════════════════════════════════════
def render_module(key: str):
    if key == "mod1":
        render_mod1()
        return

    if key == "mod2":
        render_mod2()
        return

    if key == "mod3":
        render_mod3()
        return

    if key == "mod4":
        render_mod4()
        return

    m = next(x for x in MODULES if x["key"] == key)
    color = m["color"]

    if st.button("← Volver al inicio", key="btn_back", width="stretch"):
        st.session_state.pagina = "home"
        st.rerun()

    st.markdown(f"""
    <div style="border-left: 3px solid {color}; padding-left: 1.3rem; margin: 1.5rem 0 0.5rem;">
    <div class="page-num">{m['num']}</div>
    <div class="page-title">{m['icon']} &nbsp;{m['title'].replace(chr(10), ' ')}</div>
    </div>
    <p style="font-family:Space Mono,monospace; font-size:0.8rem; color:#6b7f86;
            line-height:1.7; max-width:720px; margin: 0.8rem 0 2rem; padding-left:1.3rem;">
    {m['desc']}
    </p>""", unsafe_allow_html=True)

    st.markdown(f'<div class="sec-label" style="color:{color};">SUBTEMAS</div>', unsafe_allow_html=True)
    cols_sub = st.columns(len(m["subtemas"]))
    for col, sub in zip(cols_sub, m["subtemas"]):
        col.markdown(f"""
        <div style="background:var(--panel); border:1px solid var(--border); border-top:2px solid {color};
            border-radius:8px; padding:1rem 0.8rem; font-family:'Space Mono',monospace;
            font-size:0.72rem; color:var(--text); line-height:1.5; text-align:center; min-height:70px;
            display:flex; align-items:center; justify-content:center;">
        {sub}
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="coming-soon-box">
    <span class="cs-icon">{m['icon']}</span>
    <div class="cs-title">Contenido en desarrollo</div>
    <p class="cs-sub">
        Aquí irán la demostración matemática con LaTeX,
        los scripts Python interactivos con parámetros ajustables
        y las visualizaciones <b style="color:{color};">2D y 3D</b> con Plotly.
    </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
<div class="footer">TALLER DE GEODESIA FÍSICA &nbsp;·&nbsp; PYTHON</div>
""", unsafe_allow_html=True)
    

# ═════════════════════════════════════════════
# ROUTER PRINCIPAL
# ═════════════════════════════════════════════
pagina = st.session_state.pagina

if pagina == "home":
    render_home()
else:
    render_module(pagina)


    