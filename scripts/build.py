"""Regenerate index.html by embedding data/questions.json, data/meta.json,
and the base64-encoded figures from data/figs/ into scripts/template.html.

Usage: python3 scripts/build.py
"""
import base64
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

questions = json.load(open(os.path.join(ROOT, "data/questions.json")))
meta = json.load(open(os.path.join(ROOT, "data/meta.json")))

figs = {}
for name, key in [("fig_T1.png", "T-1"), ("fig_T2.png", "T-2"), ("fig_T3.png", "T-3")]:
    with open(os.path.join(ROOT, "data/figs", name), "rb") as f:
        figs[key] = base64.b64encode(f.read()).decode()

pool_data = {
    "questions": questions,
    "subelements": meta["subelements"],
    "groups": meta["groups"],
    "figs": figs,
}

template_path = os.path.join(ROOT, "scripts/template.html")
tpl = open(template_path, encoding="utf-8").read()
out = tpl.replace("__DATA__", json.dumps(pool_data))

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)

print(f"wrote index.html ({len(out) / 1024:.1f} KB)")
