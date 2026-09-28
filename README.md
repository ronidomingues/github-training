# Capacitação de Git e GitHub

![Git](https://img.shields.io/badge/Git-Controle_de_Versão-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Pages_e_Actions-181717?logo=github)
![LaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-008080?logo=latex)
![Licença](https://img.shields.io/badge/conteúdo-CC_BY--SA_4.0-lightgrey)

Fontes da capacitação de **Git e GitHub** da liga acadêmica
[for_code](https://www.instagram.com/forcodeufrj/): guia prático, slides e
materiais dos exercícios, para uma aula de **2 horas** sem pré-requisitos.

Edição 2025, revisada em 2026.

### 📖 **[Acessar o material publicado](https://andradasdev.github.io/github/)**

| | |
|---|---|
| 📘 Guia completo, com exercícios | [`docs/guia.pdf`](docs/guia.pdf) |
| 🖥️ Slides da apresentação | [`docs/apresentacao.pdf`](docs/apresentacao.pdf) |
| 🎤 Slides com as notas do apresentador | [`docs/apresentacao_notes.pdf`](docs/apresentacao_notes.pdf) |
| 🧩 Materiais dos exercícios | [`materials/`](materials/) |

---

## 🎯 O que a capacitação cobre

Ao final, o participante é capaz de:

1. Criar e proteger a conta no GitHub (2FA) e pedir os benefícios de estudante
2. Instalar e configurar o Git e o GitHub CLI no Windows, no Linux ou no macOS
3. Fazer commits, trabalhar com branches e resolver um conflito
4. Contribuir por fork e Pull Request, com mensagens de commit padronizadas
5. Publicar um site com o GitHub Pages e automatizar uma tarefa com o GitHub Actions
6. Versionar arquivos grandes com o Git LFS e assinar commits (GPG ou SSH)

### Os 120 minutos

| # | Bloco | Início | Duração |
|---|---|---|---|
| 0 | Abertura, objetivos e combinados | 00:00 | 5 min |
| 1 | A conta no GitHub, 2FA e benefícios de estudante | 00:05 | 15 min |
| 2 | Instalação, configuração e login | 00:20 | 20 min |
| 3 | Git no dia a dia: commits, branches, merge e conflito | 00:40 | 20 min |
| — | *Pausa* | 01:00 | 5 min |
| 4 | Colaboração: fork, Pull Request e padrões de commit | 01:05 | 20 min |
| 5 | GitHub Pages e GitHub Actions | 01:25 | 15 min |
| 6 | Git LFS e assinatura de commits | 01:40 | 15 min |
| 7 | Encerramento e próximos passos | 01:55 | 5 min |
| | **Total** | | **120 min** |

---

## 📝 Lista de presença por Pull Request

A presença é registrada do jeito que se contribui em projetos reais: cada
participante faz um fork, cria o arquivo `presences/<Seu Nome>.txt` numa branch
e abre um Pull Request. Quando o PR é aceito, o workflow recompila o guia e o
nome entra no anexo, com a data em que o PR foi integrado. O passo a passo é o
Exercício 7 do guia.

## 🔄 Publicação automática

Este é o repositório de **código**. A cada push na `main`, o workflow
[`.github/workflows/build.yml`](.github/workflows/build.yml):

1. gera a lista de presença a partir de `presences/`;
2. compila o guia e os slides com XeLaTeX;
3. verifica se os PDFs saíram íntegros;
4. commita os PDFs de volta aqui;
5. envia o guia, os slides e os materiais para
   [`andradasdev/github`](https://github.com/andradasdev/github), que publica
   o site no GitHub Pages.

A versão com notas do apresentador fica só aqui. O envio usa o secret
`TRAINING_ANDRADASDEV`; o passo a passo para criá-lo está em
[`andradasdev/github/documentacao`](https://github.com/andradasdev/github/blob/main/documentacao/autenticacao-github-actions.md).

## 🛠️ Compilar localmente

É preciso uma distribuição TeX Live com XeLaTeX e abnTeX2 (a fonte Lexend já
vem no repositório):

```bash
python3 scripts/generate_presence_list.py   # opcional: gera o anexo de presença
cd docs
latexmk -xelatex guia.tex
latexmk -xelatex apresentacao.tex
latexmk -xelatex apresentacao_notes.tex
```

Para apresentar com as notas numa segunda tela, use o `pdfpc`:
`pdfpc --notes=right docs/apresentacao_notes.pdf` (script em [`scripts/pdfpc.sh`](scripts/pdfpc.sh)).

## 📂 Estrutura

```
github-training/
├── docs/
│   ├── guia.tex / guia.pdf                 guia (abnTeX2)
│   ├── apresentacao.tex / .pdf             slides de projeção
│   ├── apresentacao_notes.tex / .pdf       slides com notas do apresentador
│   ├── pages/                              capítulos, apêndices e slides
│   └── assets/                             fontes Lexend, logos e imagens
├── materials/
│   ├── jogo-da-memoria.zip                 site do exercício de GitHub Pages
│   ├── main.py                             script do exercício de GitHub Actions
│   └── modelo-actions.zip                  exemplo de workflow em Fortran
├── presences/                              um arquivo por participante (via PR)
├── scripts/
│   ├── generate_presence_list.py           gera o anexo de presença
│   └── pdfpc.sh                            apresenta com notas
├── .github/workflows/build.yml
├── LICENSE                                 MIT, para o código
└── LICENSE-CONTENT                         CC BY-SA 4.0, para o conteúdo
```

## 🤝 Como contribuir

Correções são bem-vindas. Faça um fork, crie uma branch, siga o padrão de
commits do capítulo 7 do guia (Conventional Commits) e abra um Pull Request.

## ⚖️ Licença

- **Conteúdo didático** (guia, slides, textos, exercícios): [CC BY-SA 4.0](LICENSE-CONTENT)
- **Código** (scripts, workflows, materiais, fontes LaTeX): [MIT](LICENSE)

## 👨‍🏫 Autor

**Ronivaldo Domingues de Andrade**
LinkedIn: [ronidomingues](https://www.linkedin.com/in/ronidomingues/) ·
GitHub: [@ronidomingues](https://github.com/ronidomingues)
📍 Rio de Janeiro, RJ

### ⭐ Se este material foi útil, considere dar uma estrela no repositório!
