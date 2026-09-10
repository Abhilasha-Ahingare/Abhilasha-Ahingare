"""Violet Signal / Design 29. Editable, dependency-free SVG primitives."""
from html import escape

BG = '#0d1117'
PANEL = '#14151d'
BORDER = '#2a2938'
TEXT = '#f5f3ff'
MUTED = '#b0adbf'
ACCENT = '#b28aff'
LEVELS = ['#211f2c', '#36274f', '#5d3e89', '#855fc1', ACCENT]
FONT = 'Arial, Helvetica, sans-serif'

def text(x, y, value, size=20, color=TEXT, weight=400, anchor='start', **kwargs):
    extra = ' '.join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k, v in kwargs.items())
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" {extra}>{escape(str(value))}</text>'

def rect(x, y, w, h, fill=PANEL, stroke=BORDER, radius=14, **kwargs):
    extra = ' '.join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k, v in kwargs.items())
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>'

def line(x1, y1, x2, y2, color=BORDER, width=1):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'

def svg(w, h, body, title, desc='', background=True):
    panel = rect(1, 1, w-2, h-2) if background else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{panel}{body}</svg>\n'

def heading(label, sub, width=1000):
    return text(30, 42, label, 25, TEXT, 700) + text(30, 70, sub, 14, MUTED) + line(30, 88, width-30, 88)

def fmt(number):
    return f'{number:,}'
