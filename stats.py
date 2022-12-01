import pandas as pd

from scipy import stats

def normality_test(data, label, alpha):
    statistic, pvalue = stats.normaltest(data)

    print("\nTesting if \"" + label + "\" is normaly distributed")
    print("Null hypothesis is that it is from a normal distribution.\n")

    if pvalue < alpha:
        print("Null hypothesis can be rejected.")
        print("p-value: "+ str(pvalue))
        print("Data is not from a normal distribution.\n")
    else:
        print("Fail to reject null hypothesis.")
        print("p-value: "+ str(pvalue))
        print("Data is from a normal distribution.\n")


def run_normality_tests(df, alpha):
    normality_test(
        df["Commits Six Months"],
        "Commits made in fist six months",
        alpha
    )

    normality_test(
        df["Lines Six Months"],
        "Lines contributed in first six months",
        alpha
    )

    normality_test(
        df["Initial lines"],
        "Inital LOC",
        alpha
    )

    normality_test(
        df["Inital Comments"],
        "Inital Comment Lines",
        alpha
    )

    normality_test(
        df["Initial Average CCN"],
        "Average CCN",
        alpha
    )

    normality_test(
        df["Functions"],
        "Number of functions",
        alpha
    )

    normality_test(
        df["Complex Functions"],
        "Complex functions",
        alpha
    )

    normality_test(
        df["Comment Ratio"],
        "Comment Ratio",
        alpha
    )

    normality_test(
        df["Modularity Level"],
        "Modularity level",
        alpha
    )

    normality_test(
        df["Documentation Level"],
        "Documentation level",
        alpha
    )

    normality_test(
        df["Install"],
        "Install",
        alpha
    )

    normality_test(
        df["Tutorial"],
        "Tutorial",
        alpha
    )


def main():
    alpha = 0.05

    df = pd.read_csv("ExportedDataNov30.csv", sep=",", header=0)

    run_normality_tests(df, alpha)




if __name__ == "__main__":
    main()
