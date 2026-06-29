import pandas as pd
from pathlib import Path


def load_dataset(file_path: str):
    """
    Load a dataset from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame | None
    """

    path = Path(file_path)

    if not path.is_file():
        print(f"Error: '{file_path}' is not a valid file.")
        return None

    try:
        df = pd.read_csv(path)
        return df

    except pd.errors.EmptyDataError:
        print("Error: The dataset is empty.")
        return None

    except pd.errors.ParserError:
        print("Error: Invalid CSV format.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None