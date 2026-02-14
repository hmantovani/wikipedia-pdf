# <img src="assets/us.png" width="24"> <img src="assets/uk.png" width="24"> Wikipedia to PDF

<img src="https://img.shields.io/badge/Wikipedia-000000?style=flat-square&logo=wikipedia&logoColor=white"/> <img src="https://img.shields.io/badge/CustomTkinter-blue?style=flat-square"/>

### Description and Purpose
A professional tool designed to automate the conversion of Wikipedia articles into high-quality PDFs. Optimized for creating clean, offline documentation and structured knowledge bases. This tool was built to connect web content and structured data. While browsing Wikipedia is easy, capturing its knowledge in a stable, offline format still has three main uses:

* **Building AI knowledge bases:** Ideal for organizing datasets to train or augment LLMs (RAG).
* **Academic research:** Keeping a local, immutable copy of references.
* **Offline learning:** Accessing information without an internet connection.

### Features
* Convert multiple URLs simultaneously using a queue system.
* Uses a headless browser (Playwright) to ensure the PDFs preserve the correct formatting and infoboxes.
* Import links directly from `.txt` or `.csv` files.
* Automatically cleans and formats filenames based on the article title.

### How to Run (Windows)
* Make sure you have **Python 3.x** installed and added to your PATH.
* Download or clone this repository.
* Double-click the **`run.bat`** file.
* The script will set up a virtual environment, install dependencies, and launch the app.
* Note: On the first run, it will automatically download the Chromium engine (~150MB) to ensure PDF quality.

### Structure

```text
/wikipedia-pdf
├── main.py
├── requirements.txt
├── run.bat
├── assets/
└── downloads/
```

<p style="font-size: 0.9em; font-style: italic;">
This project uses icons (flags) created by 
<a href="https://www.flaticon.com/authors/freepik">Freepik</a> 
from the website 
<a href="https://www.flaticon.com/">Flaticon</a>.
</p>

---

# <img src="assets/br.png" width="24"> <img src="assets/pt.png" width="24"> Wikipedia para PDF

<img src="https://img.shields.io/badge/Wikipedia-000000?style=flat-square&logo=wikipedia&logoColor=white"/> <img src="https://img.shields.io/badge/CustomTkinter-blue?style=flat-square"/>

### Descrição e Propósito
Uma ferramenta projetada para automatizar a conversão de artigos da Wikipédia em PDFs de alta qualidade. Otimizada para a criação de documentação limpa offline e bases estruturadas de conhecimento. Esta ferramenta foi criada para fazer uma conexão entre conteúdo da web e dados estruturados. Embora navegar na Wikipédia seja fácil, capturar seu conhecimento em um formato estável e offline ainda tem três grandes usos:

* **Construção de bases de conhecimento de IA:** Ideal para organizar conjuntos de dados para treinar ou aprimorar modelos de aprendizagem de linguagem (RAG).
* **Pesquisa acadêmica:** Manter uma cópia local e imutável de referências.
* **Aprendizado offline:** Acessar informações sem conexão com a internet.

### Funcionalidades
* Converte vários URLs simultaneamente usando um sistema sequencial.
* Utiliza um navegador sem interface gráfica (Playwright) para garantir que os PDFs preservem a formatação correta e as caixas de informações.
* Importa links diretamente de arquivos `.txt` ou `.csv`.
* Limpa e formata automaticamente os nomes dos arquivos com base no título do artigo.

### Como executar (Windows)
* Certifique-se de ter o **Python 3.x** instalado e adicionado ao seu PATH.
* Baixe ou clone este repositório.
* Clique duas vezes no arquivo **`run.bat`**.
* O script configurará um ambiente virtual, instalará as dependências e iniciará o aplicativo.
* Observação: na primeira execução, a engine do Chromium (~150 MB) será baixada automaticamente para garantir a qualidade do PDF.

### Estrutura

```text
/wikipedia-pdf
├── main.py
├── requirements.txt
├── run.bat
├── assets/
└── downloads/
```

<p style="font-size: 0.9em; font-style: italic;">
Este projeto utiliza ícones (bandeiras) criados por 
<a href="https://www.flaticon.com/authors/freepik">Freepik</a> 
do site 
<a href="https://www.flaticon.com/">Flaticon</a>.
</p>