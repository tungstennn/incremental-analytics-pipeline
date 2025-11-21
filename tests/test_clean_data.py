import pandas as pd
from clean_data import clean_column
import os

def test_clean_column(tmp_path):
    # create temp input file
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    df = pd.DataFrame({"name": [" Alice ", "Bob   "]})
    df.to_csv(input_file, index=False)

    clean_column(input_file, output_file)

    result = pd.read_csv(output_file)

    assert result["name"].tolist() == ["Alice", "Bob"]
