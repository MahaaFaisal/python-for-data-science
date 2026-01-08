from load_csv import load
import numpy
import matplotlib.pyplot as plt
import pandas as pd


def projection_life(life_df: pd.Series, income_df: pd.Series) -> None:
    try:
        plt.scatter(income_df, life_df)
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
        projection_life(life_df, income_df)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()