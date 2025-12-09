# Automatização de Tarefas com Python

Este repositório reúne scripts de automação em Python voltados para resolver tarefas comuns do dia a dia, com foco em organização, produtividade e reaproveitamento de código. O objetivo é praticar conceitos de automação, manipulação de arquivos e uso de bibliotecas da linguagem em situações reais, criando soluções que possam ser facilmente adaptadas e evoluídas.

## Tecnologias utilizadas

- Python 3
- `os` – manipulação de pastas e arquivos
- `shutil` – movimentação e cópia de arquivos
- `tkinter` – interface gráfica simples para seleção de diretórios
- `PyPDF2` – leitura, manipulação e merge de arquivos PDF

## Estrutura do projeto

- `organizador_arquivos.py`  
  Script responsável por organizar automaticamente os arquivos de um diretório em subpastas, de acordo com a extensão.

- `merge_pdfs.py`  
  Script que une todos os arquivos PDF de uma pasta em um único documento consolidado.

Novos scripts de automação poderão ser adicionados futuramente, mantendo o repositório como um laboratório pessoal de práticas em Python.

## Funcionalidades

### 1. Organização automática de arquivos

**Script:** `organizador_arquivos.py`

- Permite ao usuário selecionar uma pasta através de uma janela gráfica utilizando `tkinter`.
- Varre todos os arquivos do diretório selecionado.
- Cria subpastas automaticamente (por exemplo: `imagens`, `planilhas`, `pdfs`, `csv`, etc.) com base na extensão dos arquivos.
- Move cada arquivo para a subpasta correspondente, deixando o diretório inicial mais limpo e organizado.

**Conceitos praticados:**

- Manipulação de sistema de arquivos (`os`, `shutil`)
- Criação e verificação de diretórios
- Iteração sobre arquivos e extensões
- Uso básico de interface gráfica (`tkinter`)

### 2. União de múltiplos PDFs

**Script:** `merge_pdfs.py`

- Lê todos os arquivos `.pdf` presentes em um diretório.
- Ordena os arquivos pelo nome para manter uma sequência lógica.
- Utiliza `PyPDF2` para combinar todos os PDFs em um único documento final.
- Gera um arquivo consolidado (por exemplo, `resultado_final.pdf`) com todas as páginas na ordem definida.

**Conceitos praticados:**

- Uso de bibliotecas externas (`PyPDF2`)
- Leitura e iteração sobre arquivos em um diretório
- Manipulação de PDFs (leitura, merge e gravação)

## Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. (Opcional) Crie e ative um ambiente virtual.
3. Instale as dependências necessárias:
pip install PyPDF2

4. Para executar o organizador de arquivos:
   python organizador_arquivos.py


Uma janela será aberta para você selecionar a pasta que deseja organizar.

5. Para executar o script de merge de PDFs:
   python merge_pdfs.py


Ajuste no código o caminho da pasta com os PDFs, se necessário.

## Objetivo do projeto

Este projeto foi criado com foco em estudo e aprimoramento das habilidades em Python, principalmente nas áreas de:

- Automação de tarefas rotineiras
- Manipulação de arquivos e diretórios
- Uso de bibliotecas externas
- Criação de pequenos utilitários reaproveitáveis

Além de servir como registro da evolução no aprendizado, o repositório funciona como base para futuros projetos de automação mais robustos e profissionais, que podem incluir agendamentos, logs, tratamento de erros mais elaborado, interfaces gráficas mais completas ou integração com outros sistemas.









