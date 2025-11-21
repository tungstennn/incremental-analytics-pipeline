import pandas as pd

def clean_column(input_path: str, output_path: str) -> None:
    """
    Reads a CSV, cleans a column, saves output.
    Stage 1: intentionally simple.
    """
    df = pd.read_csv(input_path)

    # clean column: strip whitespace
    if "name" in df.columns:
        df["name"] = df["name"].astype(str).str.strip()

    df.to_csv(output_path, index=False)
    return None


if __name__ == "__main__":
    clean_column("data/input.csv", "data/output/cleaned.csv")
