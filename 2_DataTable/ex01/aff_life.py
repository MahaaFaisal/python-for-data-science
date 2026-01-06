from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def aff_life(df: pd.Series) -> None:
    # print(type(df))
    obj = df.plot(title="United Arab Emirates Life expectancy Projections", 
                  xlabel="Year", ylabel="Life Expectancy")
    print(obj)
    # obj.xaxis.set_major_locator(MultipleLocator(40))
    # obj.set_xticklabels()
    plt.show()


def main():
    try:
        df = load("life_expectancy_years.csv").set_index('country')
        aff_life(df.loc["United Arab Emirates"])

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
