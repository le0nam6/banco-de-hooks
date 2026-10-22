#!/usr/bin/env python3
"""Banco de hooks: gera o Markdown a partir do JSON e permite consultar pelo terminal.

Uso:
  python3 scripts/hooks.py build                      # regera 03-hooks-verbais.md
  python3 scripts/hooks.py listar                     # categorias e quantidades
  python3 scripts/hooks.py sortear --cat VE --n 5     # sorteia hooks de uma categoria
  python3 scripts/hooks.py buscar "bilionário"        # busca por texto
  python3 scripts/hooks.py provados --n 20            # só hooks reais minerados
"""
import argparse
import json
import random
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data" / "hooks.json"
SAIDA = RAIZ / "03-hooks-verbais.md"


def carregar():
    dados = json.loads(DADOS.read_text(encoding="utf-8"))
    for cat in dados["categorias"]:
        for i, h in enumerate(cat["hooks"], 1):
            h["id"] = f"{cat['id']}-{i:02d}"
            h["categoria"] = cat["nome"]
    return dados


def todos(dados):
    return [h for cat in dados["categorias"] for h in cat["hooks"]]


def formatar(h):
    linhas = [f"[{h['id']}] {h['e']}", f"    template: {h['t']}"]
    if h.get("p"):
        linhas.append(f"    prova: {h['p']}")
    return "\n".join(linhas)


def build(dados):
    hooks = todos(dados)
    provados = sum(1 for h in hooks if h.get("p"))
    md = [
        "# 03 · Banco de hooks verbais",
        "",
        "> Arquivo gerado por `scripts/hooks.py build` a partir de `data/hooks.json`. Edite o JSON, não este arquivo.",
        "",
        f"**{len(hooks)} hooks** em **{len(dados['categorias'])} categorias**. "
        f"**{provados}** têm prova (hook real minerado no Instagram, com views e envios na data da coleta). "
        "Os demais são modelos escritos a partir dos mesmos padrões.",
        "",
        "Como ler: **Exemplo** é a frase pronta. **Template** é a estrutura pra você trocar o que está entre [colchetes]. "
        "**Prova** mostra de onde veio e quanto performou.",
        "",
        "## Índice",
        "",
    ]
    for cat in dados["categorias"]:
        ancora = f"{cat['id'].lower()}"
        md.append(f"- [{cat['id']} · {cat['nome']}](#{ancora}) ({len(cat['hooks'])})")
    md.append("")
    for cat in dados["categorias"]:
        md += [
            f'<a id="{cat["id"].lower()}"></a>',
            f"## {cat['id']} · {cat['nome']}",
            "",
            f"**Gatilho:** {cat['gatilho']}",
            "",
            f"**Quando usar:** {cat['quando_usar']}",
            "",
            f"**Referências:** {', '.join(cat['referencias'])}",
            "",
            "| ID | Exemplo | Template | Prova |",
            "|---|---|---|---|",
        ]
        for h in cat["hooks"]:
            celula = lambda s: s.replace("|", "\\|")
            md.append(f"| {h['id']} | {celula(h['e'])} | {celula(h['t'])} | {celula(h.get('p', '—'))} |")
        md.append("")
    SAIDA.write_text("\n".join(md), encoding="utf-8")
    print(f"Gerado {SAIDA.relative_to(RAIZ)}: {len(hooks)} hooks, {provados} com prova.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("listar")
    s = sub.add_parser("sortear")
    s.add_argument("--cat", help="ID da categoria (ex.: VE, NQ, IA)")
    s.add_argument("--n", type=int, default=5)
    b = sub.add_parser("buscar")
    b.add_argument("texto")
    pv = sub.add_parser("provados")
    pv.add_argument("--n", type=int, default=20)
    args = ap.parse_args()

    dados = carregar()
    if args.cmd == "build":
        build(dados)
    elif args.cmd == "listar":
        for cat in dados["categorias"]:
            print(f"{cat['id']:3} {len(cat['hooks']):3}  {cat['nome']}")
    elif args.cmd == "sortear":
        pool = todos(dados)
        if args.cat:
            pool = [h for h in pool if h["id"].startswith(args.cat.upper() + "-")]
        for h in random.sample(pool, min(args.n, len(pool))):
            print(formatar(h), end="\n\n")
    elif args.cmd == "buscar":
        termo = args.texto.lower()
        for h in todos(dados):
            if termo in (h["e"] + h["t"] + h.get("p", "")).lower():
                print(formatar(h), end="\n\n")
    elif args.cmd == "provados":
        pool = [h for h in todos(dados) if h.get("p", "").startswith("@")]
        for h in pool[: args.n]:
            print(formatar(h), end="\n\n")


if __name__ == "__main__":
    main()
