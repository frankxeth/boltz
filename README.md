# 🧬 Boltz API — Protein Structure Prediction

Predict 3D protein structures and binding affinities using the [Boltz API](https://api.boltz.bio).

## Features

- 🔬 Protein structure & binding prediction
- 💊 Small molecule (ligand) docking
- 🧫 Protein-protein interaction analysis
- 🎨 3D visualization via Mol* Viewer

## Setup

### 1. Install

```bash
pip install boltz-api
```

### 2. Set API Key

```bash
export BOLTZ_API_KEY="your-api-key"
```

Get your API key at [api.boltz.bio/console](https://api.boltz.bio/console).

## Usage

### Predict Structure & Binding (Simple)

```python
import os
from boltz_api import Boltz

client = Boltz(api_key=os.environ["BOLTZ_API_KEY"])

run_dir = client.experiments.run_structure_and_binding(
    entities=[
        {"type": "protein", "value": "MKTIIALSYIFCLVFA", "chain_ids": ["A"]},
        {
            "type": "ligand_smiles",
            "value": "CC(=O)OC1=CC=CC=C1C(=O)O",  # Aspirin
            "chain_ids": ["B"],
        },
    ],
    model="boltz-2.1",
    name="first-run",
)
print("Done! Results saved at:", run_dir)
```

### Read Results

```python
import time

# Poll until complete
while prediction.status not in ("succeeded", "failed"):
    time.sleep(5)
    prediction = client.predictions.structure_and_binding.retrieve(prediction.id)
    print(f"Status: {prediction.status}")

# Get results
if prediction.status == "succeeded":
    for sample in prediction.output.all_sample_results:
        print(f"Structure confidence: {sample.metrics.structure_confidence}")
        print(f"Binding confidence: {prediction.output.binding_metrics.binding_confidence}")
        print(f"Download URL: {sample.structure.url}")
```

## Visualize in 3D

1. Download the output `.cif` file from `boltz-experiments/<name>/outputs/files/`
2. Upload to [molstar.org/viewer](https://molstar.org/viewer/)
3. Rotate, zoom, and explore the structure!

## Entity Types Supported

| Type | Description | Example Value |
|------|-------------|---------------|
| `protein` | Amino acid sequence | `MKTIIALSYIFCLVFA` |
| `ligand_smiles` | Small molecule (SMILES) | `CC(=O)OC1=CC=CC=C1C(=O)O` |
| `ligand_ccd` | Small molecule (CCD code) | `ATP` |
| `rna` | RNA sequence | `AUGCAU` |
| `dna` | DNA sequence | `ATGCAT` |

## Prediction Status

| Status | Meaning |
|--------|---------|
| `pending` | Queued, not started |
| `running` | Currently processing |
| `succeeded` | ✅ Done, results available |
| `failed` | ❌ Error, check `error` field |

## Links

- 📖 [Documentation](https://api.boltz.bio/docs)
- 🖥️ [Console](https://api.boltz.bio/console)
- 🎨 [Mol* Viewer](https://molstar.org/viewer/)
