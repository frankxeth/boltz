import os
from boltz_api import Boltz

client = Boltz(api_key=os.environ["BOLTZ_API_KEY"])

run_dir = client.experiments.run_structure_and_binding(
    entities=[
        {"type": "protein", "value": "MKTIIALSYIFCLVFA", "chain_ids": ["A"]},
        {
            "type": "ligand_smiles",
            "value": "CC(=O)OC1=CC=CC=C1C(=O)O",
            "chain_ids": ["B"],
        },
    ],
    model="boltz-2.1",
    name="coba-pertama",
)

print("Selesai! Hasil ada di:", run_dir)
