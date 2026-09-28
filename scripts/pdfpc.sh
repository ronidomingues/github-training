#!/usr/bin/env bash
# Apresenta os slides com as notas do apresentador numa segunda tela.
# O projetor mostra o slide; o seu monitor mostra o slide, as notas e o relógio.
set -euo pipefail
command -v pdfpc >/dev/null || sudo apt install -y pdfpc
cd "$(dirname "$0")/../docs"
pdfpc --notes=right apresentacao_notes.pdf
