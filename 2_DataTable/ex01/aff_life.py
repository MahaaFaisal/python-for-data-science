from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(series: pd.Series, country: str) -> None:
    try:
        series.index = series.index.astype(int)
        series.plot()

        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(range(series.index.min(), series.index.max() + 1, 40))

        plt.show()
    except KeyboardInterrupt:
        plt.close()


def main():
    try:
        df = load("life_expectancy_years.csv")
        if df is not None:
            df = df.set_index('country')
            country = "United Arab Emirates"
            aff_life(df.loc[country], country)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
