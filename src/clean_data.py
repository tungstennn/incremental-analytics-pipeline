import os
import pandas as pd


def clean_column(input_path: str, output_path: str) -> None:
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.read_csv(input_path)

    if "name" in df.columns:
        df["name"] = df["name"].astype(str).str.strip()

    df.to_csv(output_path, index=False)
