from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def aff_life(df: pd.Series) -> None:
    try:
        df.index = df.index.astype(int)
        df.plot()
        plt.title("United Arab Emirates Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(range(df.index.min(), df.index.max() + 1, 40))

        plt.show()
    except KeyboardInterrupt:
        plt.close()


def main():
    try:
        df = load("life_expectancy_years.csv").set_index('country')
        aff_life(df.loc["United Arab Emirates"])

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
