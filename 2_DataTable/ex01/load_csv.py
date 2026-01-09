import pandas as pd


def load(path: str) -> pd.DataFrame:
    """ a fuunction that takes a csv file and\
loads it to dataframe
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
