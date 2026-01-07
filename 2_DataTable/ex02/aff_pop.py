from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def numerize(string: str) -> int:
    numeric_dict = {
        "k": 1000,
        "K": 1000,
        "m": 1000000,
        "M": 1000000
    }
    init_num = float(string[:-1])
    if string[-1] in numeric_dict:
        numeric = init_num * numeric_dict[string[-1]]
    else:
        numeric = string
    return numeric


def aff_pop(df: pd.DataFrame) -> None:
    try:
        df.index = df.index.astype(int)
        df[["Belgium", "France"]] = df[["Belgium", "France"]].map(numerize)
        axes = df.plot(title="Population Projections",
                       xlabel="Year", ylabel="Population")
        axes.ticklabel_format(style="plain", axis='y')

        ymin = 20000000
        ymax = max(int(df["Belgium"].max()), int(df["France"].max()))

        plt.xticks(range(df.index.min(), df.index.max() - 41, 40))
        plt.yticks(range(ymin, ymax, 20000000), ["20M", "40M", "60M"])

        plt.show()

    except KeyboardInterrupt:
        plt.close()


def main():
    try:
        df = load("population_total.csv").set_index('country')
        plot_df = df.loc[["Belgium", "France"]].T

        aff_pop(plot_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
