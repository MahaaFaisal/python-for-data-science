from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def projection_life(df: pd.DataFrame) -> None:
    try:
        ax = df.plot(
                     kind="scatter",
                     title="1900",
                     x="Gross Domestic Product",
                     y="Life Expectancy"
                    )
        ax.set_xscale("log")
        ax.get_xaxis().set_major_formatter(
            plt.FuncFormatter(
                lambda x, _: f"{int(x/1000)}k" if x >= 1000 else int(x))
        )
        plt.show()

    except KeyboardInterrupt:
        plt.close()


def load_dfs(df1: str, df2: str) -> pd.DataFrame:
    life_df = load(df1)
    if life_df:
        life_df = life_df.set_index("country")

    income_df = load(df2)
    if income_df:
        income_df = income_df.set_index("country")

    return life_df, income_df


def concat_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1 = df1["1900"].rename("Life Expectancy")
    df2 = df2["1900"].rename("Gross Domestic Product")
    return pd.concat([df2, df1], axis=1)


def main():
    try:
        life_df, income_df = load_dfs(
            "life_expectancy_years.csv",
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        if life_df is not None and income_df is not None:
            df = concat_dfs(life_df, income_df)
            projection_life(df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
