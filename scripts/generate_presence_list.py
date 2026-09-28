"""Gera docs/pages/presence_list.tex a partir dos arquivos em presences/.

Cada participante registra presença abrindo um Pull Request que cria o arquivo
presences/<Nome>.txt (Exercício 7 do guia). A data registrada é a do commit,
na main, que adicionou o arquivo: com o PR integrado por merge, é a data em que
o PR foi aceito. Essa data vem do histórico do Git, e não do sistema de
arquivos: num checkout do CI todos os arquivos têm a mesma data de criação.

Uso (na raiz do repositório):
    python3 scripts/generate_presence_list.py
"""

import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "presences"
SAIDA = RAIZ / "docs" / "pages" / "presence_list.tex"
FUSO = ZoneInfo("America/Sao_Paulo")

# Caracteres com significado especial no LaTeX. Sem o escape, um nome como
# "Ana & João" quebraria a compilação do guia.
ESCAPES = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
    "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def escapar(texto: str) -> str:
    return "".join(ESCAPES.get(c, c) for c in texto)


def data_de_entrada(arquivo: Path) -> datetime | None:
    """Data do commit, na linha principal, que adicionou o arquivo."""
    caminho = arquivo.relative_to(RAIZ).as_posix()
    resultado = subprocess.run(
        ["git", "log", "--first-parent", "--diff-filter=A", "--format=%cI",
         "-1", "--", caminho],
        cwd=RAIZ, capture_output=True, text=True, check=False,
    )
    iso = resultado.stdout.strip()
    return datetime.fromisoformat(iso).astimezone(FUSO) if iso else None


def main() -> None:
    presencas = []
    for arquivo in sorted(PASTA.glob("*.txt")):
        quando = data_de_entrada(arquivo)
        presencas.append((quando, arquivo.stem))

    # Mais antigos primeiro; arquivos ainda sem commit vão para o fim.
    presencas.sort(key=lambda p: (p[0] is None, p[0] or datetime.min.replace(tzinfo=FUSO), p[1]))

    linhas = [
        r"\begin{longtable}{@{}p{0.6\textwidth} p{0.35\textwidth}@{}}",
        r"\toprule",
        r"\textbf{Nome} & \textbf{Presença registrada em} \\",
        r"\midrule",
        r"\endhead",
    ]
    if not presencas:
        linhas.append(r"\multicolumn{2}{@{}l}{\textit{Nenhuma presença registrada ainda.}} \\")
    for quando, nome in presencas:
        data = quando.strftime("%d/%m/%Y às %H:%M") if quando else "ainda sem commit"
        linhas.append(f"{escapar(nome)} & {data} \\\\")
    linhas += [r"\bottomrule", r"\end{longtable}"]

    SAIDA.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"{len(presencas)} presença(s) em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
