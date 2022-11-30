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

def main():
    alpha = 1e-3

    df = pd.read_csv("ExportedDataNov30.csv", sep=",", header=0)

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


if __name__ == "__main__":
    main()
