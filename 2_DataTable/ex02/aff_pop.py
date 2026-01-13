from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


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


def process_df(df: pd.DataFrame, country1: str, country2: str) -> pd.DataFrame:
    df = df.loc[[country1, country2]].T
    df.index = df.index.astype(int)
    df[[country1, country2]] = df[[country1, country2]].map(numerize)

    return df


def aff_pop(df: pd.DataFrame, country1: str, country2: str) -> None:
    try:
        ax = df.plot(title="Population Projections",
                     xlabel="Year", ylabel="Population",
                     color=["blue", "green"])
        ax.legend(loc="lower right")

        ymin = 20000000

        ymax = max(int(df[country1].max()), int(df[country2].max()))

        plt.xticks(range(df.index.min(), 2041, 40))
        plt.yticks(range(ymin, ymax, 20000000), ["20M", "40M", "60M"])
        ax.set_xlim(df.index.min(), 2050)
        plt.show()

    except KeyboardInterrupt:
        plt.close()


def main():
    try:
        df = load("population_total.csv").set_index('country')
        if df is not None:
            country1 = "United Arab Emirates"
            country2 = "France"
            plot_df = process_df(df, country1, country2)
            aff_pop(plot_df, country1, country2)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
