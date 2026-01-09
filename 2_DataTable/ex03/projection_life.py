from load_csv import load
import matplotlib.pyplot as plt 
import pandas as pd


def projection_life(df: pd.DataFrame) -> None:
    try:
        ax = df.plot(
                     kind="scatter",
                     x="Gross Domestic Product",
                     y="Life Expectancy"
                    )
        ax.set_xscale("log")
        plt.xticks([300, 1000, 10000], [300, "1k", "10k"])
        ax.get_xaxis().set_major_formatter(
            plt.FuncFormatter(lambda x, _: f"{int(x/1000)}k" if x >= 1000 else int(x))
        )

        plt.title("1900")
        plt.show()

    except KeyboardInterrupt:
        plt.close()


def main():
    try:
        life_df = load("life_expectancy_years.csv").set_index("country")
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            ).set_index("country")
        life_df = life_df["1900"].rename("Life Expectancy")
        income_df = income_df["1900"].rename("Gross Domestic Product")
        df = pd.concat([income_df, life_df], axis=1)
        projection_life(df)

    except Exception as e:

        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
