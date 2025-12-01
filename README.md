# Integrated Bioinformatics Workflow for Evolutionary Analysis

This repository hosts the artifacts for Divya Dhole's M.S. in Data Science capstone at the University of Arizona. The project integrates whole-genome sequencing, paleo/climate reconstructions, ecological niche modeling, and ABBA-BABA introgression statistics to understand how climatic shifts shaped langur evolution across Asia.

## Highlights

- **Eight Jupyter notebooks** covering the full analysis pipeline—from variant discovery and PSMC demographic reconstruction to advanced species distribution modeling.
- **ABBA-BABA/DSuite outputs** organized under `ABBA-BABA/` for quick inspection of introgression tests.
- **Poster-ready assets** (HTML, PNG, PDF) under `poster/`, matching the "Integrated Bioinformatics Workflow for Evolutionary Analysis" layout.
- **Clean repository structure** so you can reproduce the workflow or reuse specific components.

## Repository Structure

| Path | Description |
|------|-------------|
| `notebooks/` | Ordered notebooks (`01_` … `08_`) covering genomic, climate, SDM, and unified workflows. |
| `ABBA-BABA/` | Logs and test outputs produced by the ABBA-BABA/DSuite pipeline (BBAA, D-statistics, chunked trees, etc.). |
| `poster/` | Poster HTML (`Clean_Theme.html`), rendering script (`save_poster.py`), PNG screenshot, and PDF export. |
| `Dsuite/`, `workflow/`, `data/`, `outputs/` | Supporting scripts, Snakemake workflows, raw/intermediate data, and generated figures (large—kept locally). |
| `requirements.txt` | Python dependencies for notebooks/scripts. |

> **Note:** The `data/`, `outputs/`, and related folders may contain large files that are not tracked by GitHub. Keep them locally or sync via your preferred storage solution.

## Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Divyadhole/Capstone-project.git
   cd Capstone-project
   ```
2. **Create an environment & install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Download data (if needed)** – populate the `data/` and `outputs/` directories with the raw genomes, climate rasters, and intermediate artifacts referenced by the notebooks.

## Notebook Overview

All notebooks live under `notebooks/` and are numbered to reflect the typical execution order:

1. `01_PSMC_Demographic_Reconstruction.ipynb` – GATK-ready genomes → PSMC/MSMC2 demographic curves.
2. `02_Paleoclimate_Data_Processing.ipynb` – PaleoClim + CMIP6 rasters pre-processing.
3. `03_MaxEnt_Distribution_Modeling.ipynb` – Species distribution models for present/future climates.
4. `04_Demographic_Climate_Integration.ipynb` – Links between demographic histories and climate anomalies.
5. `05_VCF_Processing_ABBA_BABA.ipynb` – Variant filtering and site preparation for Dsuite.
6. `06_Sliding_Window_Introgression.ipynb` – Sliding-window analysis of introgression signals.
7. `07_Unified_Pipeline.ipynb` – Snakemake/Docker orchestration notes for end-to-end runs.
8. `08_Advanced_SDM_Analysis.ipynb` – Ensemble SDMs, sensitivity analyses, and visualizations.

Open notebooks in VS Code, JupyterLab, or any compatible environment:

```bash
jupyter lab notebooks/03_MaxEnt_Distribution_Modeling.ipynb
```

## ABBA-BABA Outputs

The `ABBA-BABA/` folder contains:

- `abba_baba_analysis.log` – pipeline run log.
- `abba_baba_results_*` files – BBAA counts, D-statistics, chunked tree summaries, and combined statistics.
- `test_results_*` – Sanity-check runs for BBAA/Dmin/combine steps on smaller datasets.

Use these files to quickly inspect introgression signals without rerunning Dsuite.

## Poster Generation

1. Ensure Google Chrome and ChromeDriver are available.
2. Install Selenium requirements (already in `requirements.txt`).
3. Run the rendering script from the repo root:
   ```bash
   python3 poster/save_poster.py
   ```
4. The script loads `poster/Clean_Theme.html`, generates `poster/poster.png`, and uses Chrome DevTools to create a PDF. For a print-ready PDF, an additional `sips` command can convert the PNG:
   ```bash
   sips -s format pdf poster/poster.png --out poster/Integrated\ Bioinformatics\ Workflow\ for\ Evolutionary\ Analysis\ poster.pdf
   ```

## Workflow Summary

1. **Genomic Processing** – BWA/GATK best practices, variant filtering, population structure inference.
2. **Demographic Modeling** – PSMC/MSMC2 reconstructions of effective population size through time.
3. **Climate + SDMs** – PaleoClim/CMIP6 rasters → MaxEnt models for baseline and 2050 scenarios.
4. **Hybridization Analysis** – Dsuite ABBA-BABA tests, sliding windows, and hotspot mapping.
5. **Integration & Visualization** – Redundancy analyses tying climate seasonality to genomic variance and a publication-ready poster.

## Contributing & Issues

Feel free to open issues or pull requests for bug fixes or extensions (e.g., additional species, new climate scenarios). For large data files, please coordinate via shared storage rather than GitHub.

## Contact

Divya Dhole  
M.S. in Data Science, University of Arizona