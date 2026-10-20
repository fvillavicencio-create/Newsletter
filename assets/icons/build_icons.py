"""Genera la iconografía Regcheq (SVG + PNG) en estilo dibujado a mano.

Uso: python3 assets/icons/build_icons.py   (PNG requiere Playwright + Chromium)
"""
import base64
import math
import re
import os
import pathlib

OUT = pathlib.Path(__file__).parent
INK = "#0a2342"      # azul marino Regcheq (trazo)
BLUE = "#368fff"     # azul logo Regcheq
SKY = "#bcd9ff"      # azul claro (manchas)
SUN = "#f4c542"      # amarillo Regcheq
MINT = "#7fd8aa"     # verde menta (de #2e9e6b)
WHITE = "#ffffff"

S = f'stroke="{INK}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"'


def blob(cx, cy, r, color, seed=0):
    """Mancha orgánica de color detrás del icono."""
    r *= 1.15
    n = 7
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n + seed
        k = 1 + 0.13 * math.sin(3 * i + seed * 5) + 0.07 * math.cos(5 * i + seed)
        pts.append((cx + r * k * math.cos(a), cy + r * k * math.sin(a)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} "
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f} "
    return f'<path d="{d}Z" fill="{color}"/>'


def rays(x, y, angle, n=3, spread=34, r0=10, r1=18):
    """Rayitas de 'brillo' alrededor de los iconos."""
    out = []
    for i in range(n):
        a = math.radians(angle + (i - (n - 1) / 2) * spread)
        out.append(f'M{x + r0 * math.cos(a):.1f} {y + r0 * math.sin(a):.1f} '
                   f'L{x + r1 * math.cos(a):.1f} {y + r1 * math.sin(a):.1f}')
    return f'<path d="{" ".join(out)}" fill="none" {S}/>'


def sparkle(x, y, s=6, color=INK):
    return (f'<path d="M{x} {y - s} Q{x} {y} {x + s} {y} Q{x} {y} {x} {y + s} '
            f'Q{x} {y} {x - s} {y} Q{x} {y} {x} {y - s} Z" fill="{color}" '
            f'stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>')


def face(x, y, s=1.0):
    """Carita sonriente (ojos cerrados felices + sonrisa)."""
    e = 6 * s
    return (f'<path d="M{x - e - 3*s} {y} q3 {-3*s} {6*s} 0 M{x + e - 3*s} {y} q3 {-3*s} {6*s} 0 '
            f'M{x - 6*s} {y + 7*s} q{6*s} {6*s} {12*s} 0" fill="none" {S} stroke-width="3.5"/>')


def check(d, color=INK, w=6):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def person(cx, cy, r, color):
    """Persona simple (cabeza + hombros) dentro de un círculo de radio r."""
    return (f'<path d="M{cx - r*0.62} {cy + r*0.72} C{cx - r*0.62} {cy + r*0.1} {cx + r*0.62} {cy + r*0.1} {cx + r*0.62} {cy + r*0.72}" fill="{color}" {S} stroke-width="3.5"/>'
            f'<circle cx="{cx}" cy="{cy - r*0.22}" r="{r*0.3}" fill="{WHITE}" {S} stroke-width="3.5"/>')


DOC = f'<path d="M22 14 H66 L82 30 V106 H22 Z" fill="{WHITE}" {S}/><path d="M66 14 V30 H82" fill="none" {S}/>'

ICONS = {
    "cumplimiento": ("Cumplimiento", blob(82, 82, 24, SKY, 1) + rays(28, 22, 225) +
        f'<path d="M60 14 C48 22 36 24 24 24 V58 C24 82 42 98 60 106 C78 98 96 82 96 58 V24 C84 24 72 22 60 14 Z" fill="{WHITE}" {S}/>' +
        check("M42 60 L55 73 L80 44", BLUE, 8)),
    "revision-documental": ("Revisión documental", blob(86, 84, 20, MINT, 2) + rays(102, 40, -30) + DOC +
        f'<path d="M32 36 H54 M32 46 H58 M32 56 H48 M32 92 q4 -10 8 -2 t8 -2 t8 0" fill="none" {S}/>' +
        f'<circle cx="74" cy="66" r="16" fill="{SUN}" {S}/>' +
        f'<path d="M86 78 L102 94" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'),
    "identificacion": ("Identificación (KYC)", blob(90, 92, 18, SUN, 3) + rays(92, 20, -70) +
        f'<rect x="10" y="30" width="100" height="66" rx="12" fill="{WHITE}" {S}/>' +
        f'<path d="M22 84 C22 70 50 70 50 84 Z" fill="{BLUE}" {S}/><circle cx="36" cy="56" r="9" fill="{WHITE}" {S}/>' +
        f'<path d="M60 50 H96 M60 60 H96 M60 70 H84" fill="none" {S}/>' +
        f'<path d="M60 84 H68" stroke="{BLUE}" stroke-width="6" stroke-linecap="round"/>' +
        f'<path d="M78 84 h.1 M87 84 h.1 M96 84 h.1" {S} stroke-width="6"/>'),
    "checklist": ("Checklist", blob(84, 86, 22, MINT, 4) + rays(96, 16, -50) + DOC +
        "".join(f'<rect x="30" y="{y}" width="15" height="15" rx="3" fill="{SUN}" {S} stroke-width="3.5"/>'
                + check(f"M33 {y+8} L37 {y+12} L46 {y+1}", INK, 4) + f'<path d="M54 {y+8} H72" fill="none" {S}/>'
                for y in (34, 56, 78))),
    "alertas": ("Alertas y avisos", blob(84, 82, 22, SKY, 5) + rays(22, 46, 200) + rays(98, 46, -20) +
        f'<circle cx="60" cy="18" r="5" fill="{WHITE}" {S}/>' +
        f'<circle cx="60" cy="92" r="8" fill="{BLUE}" {S}/>' +
        f'<path d="M60 23 C40 23 36 40 36 56 C36 70 30 78 22 86 H98 C90 78 84 70 84 56 C84 40 80 23 60 23 Z" fill="{WHITE}" {S}/>' +
        face(60, 54)),
    "monitoreo": ("Monitoreo", rays(96, 34, -30, 2) +
        f'<path d="M12 30 V16 H26 M94 16 H108 V30 M108 90 V104 H94 M26 104 H12 V90" fill="none" stroke="{MINT}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' +
        f'<path d="M42 30 L38 22 M60 26 V17 M78 30 L82 22" fill="none" {S}/>' +
        f'<path d="M16 62 Q60 18 104 62 Q60 104 16 62 Z" fill="{WHITE}" {S}/>' +
        f'<circle cx="60" cy="62" r="18" fill="{BLUE}" {S}/>' + person(60, 62, 14, INK)),
    "metricas": ("Métricas y reportes", rays(100, 20, -60, 2) +
        f'<path d="M14 102 H106" fill="none" {S}/>' +
        f'<rect x="20" y="78" width="14" height="24" fill="{MINT}" {S}/>' +
        f'<rect x="42" y="64" width="14" height="38" fill="{SKY}" {S}/>' +
        f'<rect x="64" y="50" width="14" height="52" fill="{WHITE}" {S}/>' +
        f'<rect x="86" y="32" width="14" height="70" fill="{SUN}" {S}/>' +
        f'<path d="M16 64 L38 44 L50 50 L82 18 M70 18 H82 V30" fill="none" {S}/>'),
    "beneficiario-controlador": ("Beneficiario controlador",
        sparkle(22, 30) + sparkle(100, 30, 5) + sparkle(60, 108, 5) +
        f'<path d="M60 64 L60 30 M60 64 L28 88 M60 64 L92 88" fill="none" {S}/>' +
        f'<circle cx="60" cy="64" r="10" fill="{SUN}" {S}/>' +
        "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="{WHITE}" {S}/>' + person(x, y, 14, c)
                for x, y, c in ((60, 26, SKY), (26, 88, BLUE), (94, 88, MINT)))),
    "proteccion-datos": ("Protección de datos", rays(30, 30, 210) + rays(92, 24, -30, 2) +
        f'<path d="M50 30 V22 a10 10 0 0 1 20 0 V30" fill="none" {S}/>' +
        f'<rect x="42" y="30" width="36" height="28" rx="6" fill="{MINT}" {S}/>' +
        f'<circle cx="60" cy="41" r="3.5" fill="{INK}"/><path d="M60 43 V50" {S} stroke-width="4"/>' +
        f'<path d="M6 90 L20 80 L34 102 L20 112 Z" fill="{BLUE}" {S}/>' +
        f'<path d="M26 84 C36 76 50 74 62 78 H78 C86 78 86 89 78 89 H60 M78 87 L96 75 C104 70 111 78 105 84 L88 99 C80 105 72 107 60 107 H38 Z" fill="{WHITE}" {S}/>'),
    "en-la-practica": ("En la práctica", rays(102, 24, -40) +
        f'<rect x="28" y="22" width="70" height="88" rx="8" fill="{WHITE}" {S}/>' +
        f'<rect x="22" y="18" width="70" height="88" rx="8" fill="{WHITE}" {S}/>' +
        f'<rect x="40" y="10" width="34" height="14" rx="5" fill="{BLUE}" {S}/>' +
        "".join(f'<rect x="32" y="{y}" width="14" height="14" rx="3" fill="{SKY}" {S} stroke-width="3.5"/>'
                + check(f"M35 {y+7} L39 {y+11} L47 {y}", INK, 4) + f'<path d="M56 {y+8} H80" fill="none" {S}/>'
                for y in (38, 60, 82))),
    "hablemos": ("Hablemos", sparkle(108, 14, 5) +
        f'<path d="M30 52 L24 62 L40 52" fill="{SKY}" {S}/>' +
        f'<rect x="10" y="14" width="54" height="38" rx="18" fill="{SKY}" {S}/>' +
        f'<path d="M86 64 L94 74 L76 64" fill="{SUN}" {S}/>' +
        f'<rect x="54" y="28" width="54" height="36" rx="18" fill="{SUN}" {S}/>' +
        f'<path d="M71 46 h.1 M81 46 h.1 M91 46 h.1" {S} stroke-width="6"/>' +
        f'<path d="M14 116 C14 98 50 98 50 116" fill="{MINT}" {S}/>' +
        f'<path d="M70 116 C70 98 106 98 106 116" fill="{BLUE}" {S}/>' +
        f'<circle cx="32" cy="88" r="11" fill="{WHITE}" {S}/><circle cx="88" cy="88" r="11" fill="{WHITE}" {S}/>' +
        f'<path d="M27 91 q5 5 10 0 M83 91 q5 5 10 0" fill="none" {S} stroke-width="3"/>'),
    "plataforma": ("Plataforma Regcheq", blob(92, 80, 22, SKY, 6) + rays(104, 22, -40) +
        f'<rect x="20" y="22" width="80" height="56" rx="7" fill="{WHITE}" {S}/>' +
        f'<rect x="28" y="30" width="64" height="40" rx="3" fill="none" {S} stroke-width="3"/>' +
        f'<circle cx="60" cy="50" r="13" fill="{MINT}" {S}/>' + check("M53 50 L58 55 L67 45", INK, 4.5) +
        f'<path d="M8 84 H112 L104 98 H16 Z" fill="{WHITE}" {S}/>' +
        f'<path d="M30 91 H90" fill="none" {S} stroke-width="3" stroke-dasharray="6 5"/>'),
    "fechas-clave": ("Fechas clave", blob(88, 88, 20, SUN, 7) + rays(104, 18, -40, 2) +
        f'<rect x="16" y="24" width="86" height="80" rx="10" fill="{WHITE}" {S}/>' +
        f'<path d="M16 46 V34 a10 10 0 0 1 10 -10 H92 a10 10 0 0 1 10 10 V46 Z" fill="{BLUE}" {S}/>' +
        f'<path d="M38 16 V30 M80 16 V30" fill="none" {S}/>' +
        "".join(f'<path d="M{x} {y} h.1" {S} stroke-width="6"/>' for x in (32, 50, 68, 86) for y in (62, 80)
                if (x, y) != (68, 80)) +
        f'<circle cx="68" cy="80" r="10" fill="{SUN}" {S} stroke-width="3.5"/>' +
        f'<path d="M30 96 H48" stroke="{SKY}" stroke-width="5" stroke-linecap="round"/>'),
    "novedades": ("Novedades", blob(36, 86, 20, SKY, 8) +
        f'<path d="M94 46 q8 14 0 28 M102 36 q16 24 0 48" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>' +
        f'<path d="M38 72 L46 98 H58 L52 74" fill="{WHITE}" {S}/>' +
        f'<path d="M30 46 L80 22 V98 L30 74 Z" fill="{SUN}" {S}/>' +
        f'<rect x="14" y="44" width="18" height="32" rx="5" fill="{WHITE}" {S}/>' +
        sparkle(98, 18, 6, WHITE)),
    "webinar": ("Webinars y eventos", blob(90, 92, 18, MINT, 9) + rays(108, 16, -45, 2) +
        f'<rect x="12" y="18" width="96" height="66" rx="10" fill="{WHITE}" {S}/>' +
        f'<path d="M52 38 L76 51 L52 64 Z" fill="{BLUE}" {S}/>' +
        f'<rect x="20" y="26" width="24" height="10" rx="5" fill="{SUN}" {S} stroke-width="3"/>' +
        f'<path d="M60 84 V98 M42 102 H78" fill="none" {S}/>'),
    "blog": ("Blog", blob(30, 84, 20, SUN, 10) +
        f'<rect x="20" y="16" width="64" height="88" rx="8" fill="{WHITE}" {S}/>' +
        f'<path d="M32 34 H70 M32 46 H66 M32 58 H70 M32 70 H52" fill="none" {S}/>' +
        f'<g transform="rotate(40 88 72)"><rect x="81" y="36" width="14" height="44" rx="2" fill="{SUN}" {S}/>'
        f'<rect x="81" y="28" width="14" height="10" rx="3" fill="{BLUE}" {S}/>'
        f'<path d="M81 80 L88 94 L95 80 Z" fill="{WHITE}" {S}/></g>' + sparkle(100, 24, 6)),
    "tip": ("Tip / idea", rays(60, 14, -90, 3, 40, 10, 16) + rays(28, 40, 200, 1, 0, 6, 14) + rays(92, 40, -20, 1, 0, 6, 14) +
        f'<path d="M60 22 C42 22 32 35 32 50 C32 63 43 68 45 82 H75 C77 68 88 63 88 50 C88 35 78 22 60 22 Z" fill="{SUN}" {S}/>' +
        f'<rect x="46" y="84" width="28" height="9" rx="3" fill="{WHITE}" {S}/>' +
        f'<rect x="48" y="95" width="24" height="9" rx="3" fill="{SKY}" {S}/>' + face(60, 48)),
    "descargable": ("Recurso descargable", rays(98, 26, -40) +
        f'<path d="M34 78 C18 78 14 56 30 52 C30 34 54 28 62 42 C68 30 92 32 92 52 C108 52 108 78 90 78 Z" fill="{SKY}" {S}/>' +
        f'<path d="M60 52 V102 M48 90 L60 102 L72 90" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>' +
        f'<circle cx="60" cy="52" r="0" />'),
    "regulacion": ("Regulación / Ley", blob(60, 100, 18, SKY, 11) +
        f'<path d="M60 22 V98 M40 102 H80 M22 36 H98" fill="none" {S}/>' +
        f'<path d="M22 36 L12 68 M22 36 L32 68 M98 36 L88 68 M98 36 L108 68" fill="none" {S} stroke-width="3"/>' +
        f'<path d="M10 68 H34 C34 80 10 80 10 68 Z" fill="{BLUE}" {S}/>' +
        f'<path d="M86 68 H110 C110 80 86 80 86 68 Z" fill="{MINT}" {S}/>' +
        f'<circle cx="60" cy="20" r="7" fill="{SUN}" {S}/>'),
    "institucion": ("Institución financiera", blob(88, 88, 20, MINT, 12) + rays(104, 22, -40, 2) +
        f'<path d="M12 44 L60 16 L108 44 Z" fill="{BLUE}" {S}/>' +
        f'<circle cx="60" cy="33" r="5" fill="{WHITE}" {S} stroke-width="3"/>' +
        "".join(f'<rect x="{x}" y="50" width="12" height="38" rx="2" fill="{WHITE}" {S}/>' for x in (22, 44, 64, 86)) +
        f'<rect x="14" y="90" width="92" height="12" rx="3" fill="{SUN}" {S}/>'),
    "listas-restrictivas": ("Búsqueda en listas", blob(32, 32, 20, MINT, 13) + rays(98, 24, -40) +
        f'<path d="M74 74 L102 102" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>' +
        f'<circle cx="52" cy="52" r="30" fill="{WHITE}" {S}/>' +
        f'<path d="M36 72 C36 56 68 56 68 72" fill="{BLUE}" {S} stroke-width="3.5"/>' +
        f'<circle cx="52" cy="44" r="9" fill="{SUN}" {S} stroke-width="3.5"/>'),
    "newsletter": ("Newsletter", blob(30, 90, 18, SKY, 14) +
        f'<rect x="12" y="30" width="92" height="64" rx="9" fill="{WHITE}" {S}/>' +
        f'<path d="M14 36 L58 66 L102 36" fill="none" {S}/>' +
        f'<circle cx="100" cy="30" r="12" fill="{SUN}" {S}/>' +
        f'<path d="M100 36 c-6 -4 -7 -8 -4 -10 c2 -1 4 0 4 2 c0 -2 2 -3 4 -2 c3 2 2 6 -4 10 Z" fill="{INK}"/>'),
    "logro": ("Logro / certificación", sparkle(22, 26) + sparkle(98, 30, 5) +
        f'<path d="M44 64 L34 104 L46 98 L54 108 L62 70 Z" fill="{BLUE}" {S}/>' +
        f'<path d="M76 64 L86 104 L74 98 L66 108 L58 70 Z" fill="{SKY}" {S}/>' +
        f'<circle cx="60" cy="46" r="28" fill="{SUN}" {S}/>' +
        f'<path d="M60 32 L64 42 L75 42 L66 49 L70 60 L60 53 L50 60 L54 49 L45 42 L56 42 Z" fill="{WHITE}" {S} stroke-width="3"/>'),
    "lanzamiento": ("Lanzamiento", sparkle(22, 30) + sparkle(98, 22, 5) + sparkle(100, 70, 4) +
        f'<path d="M50 84 Q60 112 70 84 Z" fill="{SUN}" {S}/>' +
        f'<path d="M46 62 L30 84 L48 82 Z M74 62 L90 84 L72 82 Z" fill="{SUN}" {S}/>' +
        f'<path d="M60 12 C78 26 82 52 74 84 H46 C38 52 42 26 60 12 Z" fill="{WHITE}" {S}/>' +
        f'<circle cx="60" cy="44" r="10" fill="{BLUE}" {S}/>'),
}

FILTER = ('<defs><filter id="hand" x="-5%" y="-5%" width="110%" height="110%">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4"/>'
          '<feDisplacementMap in="SourceGraphic" scale="2.6"/></filter></defs>')


def dedupe_stroke_width(body):
    """Si un elemento repite stroke-width, conserva el último (el específico)."""
    def fix(m):
        tag = m.group(0)
        widths = re.findall(r' stroke-width="[^"]*"', tag)
        for w in widths[:-1]:
            tag = tag.replace(w, "", 1)
        return tag
    return re.sub(r"<[^>]+>", fix, body)


def svg(body):
    body = dedupe_stroke_width(body)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">'
            f'{FILTER}<g filter="url(#hand)">{body}</g></svg>\n')


def main():
    (OUT / "svg").mkdir(exist_ok=True)
    for slug, (_, body) in ICONS.items():
        (OUT / "svg" / f"{slug}.svg").write_text(svg(body))

    cards = "".join(
        f'<figure><img src="svg/{slug}.svg" alt="{name}"><figcaption>{name}<span>{slug}</span></figcaption></figure>'
        for slug, (name, _) in ICONS.items())
    (OUT / "index.html").write_text(PAGE.replace("{{cards}}", cards))

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright no disponible: se omiten los PNG")
        return
    (OUT / "png").mkdir(exist_ok=True)
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH")
        browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        page = browser.new_page(viewport={"width": 256, "height": 256})
        for slug in ICONS:
            page.set_content(f'<html><body style="margin:0;background:transparent">'
                             f'<img src="data:image/svg+xml;base64,{base64.b64encode((OUT / "svg" / f"{slug}.svg").read_bytes()).decode()}" '
                             f'width="256" height="256" style="display:block"></body></html>')
            page.screenshot(path=str(OUT / "png" / f"{slug}.png"), omit_background=True)
        page.set_viewport_size({"width": 1200, "height": 800})
        page.goto((OUT / "index.html").resolve().as_uri())
        page.screenshot(path=str(OUT / "preview.png"), full_page=True)
        browser.close()


PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iconografía Regcheq</title>
<style>
  :root { --ink:#0a2342; --blue:#368fff; --sky:#bcd9ff; --sun:#f4c542; --mint:#7fd8aa; --bg:#f7f9fc; }
  body { margin:0; background:var(--bg); color:var(--ink); font-family: Arial, Helvetica, sans-serif; }
  header { padding:40px 24px 8px; max-width:1100px; margin:0 auto; }
  h1 { margin:0; font-size:30px; }
  p { margin:8px 0 0; color:#5a6b7d; }
  .palette { display:flex; gap:10px; flex-wrap:wrap; margin-top:18px; }
  .palette span { display:flex; align-items:center; gap:6px; font-size:12px; }
  .palette i { width:22px; height:22px; border-radius:50%; border:2px solid var(--ink); }
  main { max-width:1100px; margin:0 auto; padding:24px; display:grid; gap:18px;
         grid-template-columns:repeat(auto-fill, minmax(150px, 1fr)); }
  figure { margin:0; background:#fff; border-radius:18px; padding:18px 10px 14px; text-align:center;
           box-shadow:0 2px 10px rgba(10,35,66,.06); }
  img { width:96px; height:96px; }
  figcaption { font-size:13px; font-weight:700; margin-top:6px; }
  figcaption span { display:block; font-weight:400; font-size:11px; color:#7a8ba0; margin-top:2px; }
</style></head><body>
<header><h1>Iconografía Regcheq</h1>
<p>Estilo dibujado a mano, cercano y amigable. Trazo azul marino + manchas de color de marca.</p>
<div class="palette">
  <span><i style="background:#0a2342"></i>#0A2342</span><span><i style="background:#368fff"></i>#368FFF</span>
  <span><i style="background:#bcd9ff"></i>#BCD9FF</span><span><i style="background:#f4c542"></i>#F4C542</span>
  <span><i style="background:#7fd8aa"></i>#7FD8AA</span>
</div></header>
<main>{{cards}}</main>
</body></html>
"""

if __name__ == "__main__":
    main()
