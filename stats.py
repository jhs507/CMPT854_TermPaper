import math
import pandas as pd
import numpy as np
from scipy import stats

def normality_test(data, label, alpha):
    statistic, p_value = stats.normaltest(data)

    print("\nTesting if \"" + label + "\" is normaly distributed")
    print("Null hypothesis is that it is from a normal distribution.\n")

    if p_value < alpha:
        print("Null hypothesis can be rejected.")
        print("p-value: "+ str(p_value))
        print("Data is not from a normal distribution.\n")
    else:
        print("Fail to reject null hypothesis.")
        print("p-value: "+ str(p_value))
        print("Data is from a normal distribution.\n")

def pearson_test(data_a, data_b, label, alpha):
    correlation, p_value = stats.pearsonr(data_a, data_b)

    print("\nTesting if \"" + label + "\" are corrolated.")
    print("Null hypothesis is that correlation is zero")

    if p_value < alpha:
        print("Null hypothesis can be rejected.")
        print("p-value: "+ str(p_value))

        print(correlation)
        cor_abs = abs(correlation)
        if cor_abs > 0.0 and cor_abs < 0.30:
            print("Little if any correlation "+ str(correlation)+"\n")
        elif cor_abs > 0.30 and cor_abs < 0.50:
            print("Low correlation "+str(correlation)+"\n")
        elif cor_abs > 0.50 and cor_abs < 0.70:
            print("Moderate correlation "+str(correlation)+"\n")
        elif cor_abs > 0.70 and cor_abs < 0.90:
            print("High correlation "+str(correlation)+"\n")
        elif cor_abs > 0.90 and cor_abs < 1.00:
            print("Very high correlation "+str(correlation)+"\n")
    else:
        print("Cannot reject null hypothesis.\n")

def spearman_test(data_a, data_b, label, alpha):
    correlation, p_value = stats.spearmanr(data_a, data_b)

    print("\nTesting if \"" + label + "\" are corrolated.")
    print("Null hypothesis is that correlation is zero")

    if p_value < alpha:
        print("Null hypothesis can be rejected.")
        print("p-value: "+ str(p_value))

        print(correlation)
        cor_abs = abs(correlation)
        if cor_abs > 0.0 and cor_abs < 0.30:
            print("Little if any correlation "+ str(correlation)+"\n")
        elif cor_abs > 0.30 and cor_abs < 0.50:
            print("Low correlation "+str(correlation)+"\n")
        elif cor_abs > 0.50 and cor_abs < 0.70:
            print("Moderate correlation "+str(correlation)+"\n")
        elif cor_abs > 0.70 and cor_abs < 0.90:
            print("High correlation "+str(correlation)+"\n")
        elif cor_abs > 0.90 and cor_abs < 1.00:
            print("Very high correlation "+str(correlation)+"\n")
    else:
        print("Cannot reject null hypothesis.\n")



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

    normality_test(
        df["Log Commits Six Months"],
        "Log of Commits made in fist six months",
        alpha
    )

    normality_test(
        df["Log Lines Six Months"],
        "Log of Lines contributed in six months",
        alpha
    )

    normality_test(
        df["Log Initial lines"],
        "Log of Inital Lines",
        alpha
    )

    normality_test(
        df["Log Inital Comments"],
        "Log of Inital Comments",
        alpha
    )

    normality_test(
        df["Log Initial Average CCN"],
        "Log of Initial Average CCN",
        alpha
    )

    normality_test(
        df["Log Functions"],
        "Log of Functions",
        alpha
    )

    normality_test(
        df["Log Comment Ratio"],
        "Log of Comment Ratio",
        alpha
    )

def run_corrolation_tests(df, alpha):

    spearman_test(
        df["Commits Six Months"],
        df["Lines Six Months"],
        "Commits in six months and Lines in six months",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Initial lines"],
        "Commits in Six Months to Inital Lines",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Inital Comments"],
        "Commits in Six Months and Inital comments",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Comment Ratio"],
        "Commits in Six Months and Comment Ratio",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Initial Average CCN"],
        "Commits in Six Months and Initial Average CCN",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Functions"],
        "Commits in Six Months and Functions",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Complex Functions"],
        "Commits in Six Months and Complex Functions",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Initial lines"],
        "Lines Six Months to Inital Lines",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Inital Comments"],
        "Lines Six Months and Inital comments",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Comment Ratio"],
        "Lines Six Months and Comment Ratio",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Initial Average CCN"],
        "Lines Six Months and Initial Average CCN",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Functions"],
        "Lines Six Months and Functions",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Complex Functions"],
        "Lines Six Months and Complex Functions",
        alpha
    )


def main():
    alpha = 0.05

    df = pd.read_csv("ExportedDataNov30.csv", sep=",", header=0)
    df["Log Commits Six Months"] = np.log(df["Commits Six Months"])
    df["Log Lines Six Months"] = np.log(df["Lines Six Months"])
    df["Log Initial lines"] = np.log(df["Initial lines"])
    df["Log Inital Comments"] = np.log(df["Inital Comments"])
    df["Log Initial Average CCN"] = np.log(df["Initial Average CCN"])
    df["Log Functions"] = np.log(df["Functions"])
    #df["Log Complex Functions"] = np.log(df["Complex Functions"])
    df["Log Comment Ratio"] = np.log(df["Comment Ratio"])

    run_normality_tests(df, alpha)

    #run_corrolation_tests(df, alpha)

    #df_doc_1 = df[df["Documentation Level"] == 1]
    #df_doc_2 = df[df["Documentation Level"] == 2]
    #df_doc_3 = df[df["Documentation Level"] == 3]

    #comm_doc_1 = df_doc_1["Commits Six Months"]
    #comm_doc_2 = df_doc_2["Commits Six Months"]
    #comm_doc_3 = df_doc_3["Commits Six Months"]

    #s, p = stats.mannwhitneyu(comm_doc_3, comm_doc_2)

    #print(s)
    #print(p)







if __name__ == "__main__":
    main()
