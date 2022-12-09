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

        #print(correlation)
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

        #print(correlation)
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
        df["Log Inital lines"],
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

    normality_test(
        df["Function Complexity Ratio"],
        "Function Complexity Ratio",
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
        df["Lines Six Months"],
        df["Commits Six Months"],
        "Lines in six months and Commits in six months",
        alpha
    )

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Lines Six Months"],
        "Log Commits in six months and Log lines in six months",
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

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Inital lines"],
        "Log Commits in six months and Log Inital lines",
        alpha
    )

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Inital Comments"],
        "Log Commits in six months and Log Inital Comments",
        alpha
    )

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Initial Average CCN"],
        "Log Commits in six months and Log Initial Average CCN",
        alpha
    )

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Functions"],
        "Log Commits in six months and Log Functions",
        alpha
    )

    #spearman_test(
    #    df["Log Commits Six Months"],
    #    df["Log Complex Functions"],
    #    "Log Commits in six months and Log Complex Functions",
    #    alpha
    #)

    spearman_test(
        df["Log Commits Six Months"],
        df["Log Comment Ratio"],
        "Log Commits in six months and Log Complex Functions",
        alpha
    )

    spearman_test(
        df["Log Lines Six Months"],
        df["Log Inital lines"],
        "Log Lines Six Months and Log Inital lines",
        alpha
    )

    spearman_test(
        df["Log Lines Six Months"],
        df["Log Inital Comments"],
        "Log Lines Six Months and Log Inital Comments",
        alpha
    )

    spearman_test(
        df["Log Lines Six Months"],
        df["Log Initial Average CCN"],
        "Log Lines Six Months and Log Initial Average CCN",
        alpha
    )

    spearman_test(
        df["Log Lines Six Months"],
        df["Log Functions"],
        "Log Lines Six Months and Log Functions",
        alpha
    )

    #spearman_test(
    #    df["Log Lines Six Months"],
    #    df["Log Complex Functions"],
    #    "Log Lines Six Months and Log Complex Functions",
    #    alpha
    #)

    spearman_test(
        df["Log Lines Six Months"],
        df["Log Comment Ratio"],
        "Log Lines Six Months and Log Complex Functions",
        alpha
    )

    spearman_test(
        df["Commits Six Months"],
        df["Function Complexity Ratio"],
        "Commits in six months to Function Complixity Ratio",
        alpha
    )

    spearman_test(
        df["Lines Six Months"],
        df["Function Complexity Ratio"],
        "Lines in six months to complexity ratio",
        alpha
    )




    print("Running Pearson Tests for normal data.")

    pearson_test(
        df["Log Lines Six Months"],
        df["Log Inital Comments"],
        "Log Lines six months and Log Inital Comments",
        alpha
    )

    pearson_test(
        df["Log Lines Six Months"],
        df["Log Initial Average CCN"],
        "Log Lines six months and Log IInitial Average CCN",
        alpha
    )

    pearson_test(
        df["Log Lines Six Months"],
        df["Log Functions"],
        "Log Lines six months and Log Functions",
        alpha
    )


def main():
    alpha = 0.05

    df = pd.read_csv("ExportedDataNov30.csv", sep=",", header=0)
    df["Log Commits Six Months"] = np.log(df["Commits Six Months"])
    df["Log Lines Six Months"] = np.log(df["Lines Six Months"])
    df["Log Inital lines"] = np.log(df["Initial lines"])
    df["Log Inital Comments"] = np.log(df["Inital Comments"])
    df["Log Initial Average CCN"] = np.log(df["Initial Average CCN"])
    df["Log Functions"] = np.log(df["Functions"])
    #df["Log Complex Functions"] = np.log(df["Complex Functions"])
    df["Log Comment Ratio"] = np.log(df["Comment Ratio"])
    df["Function Complexity Ratio"] = df["Complex Functions"] / df["Functions"]
    #df["Log Function Complexity Ratio"] = np.log(df["Function Complexity Ratio"])

    run_normality_tests(df, alpha)

    run_corrolation_tests(df, alpha)

    print("Testing affect of Documentation level")
    df_doc_1 = df[df["Documentation Level"] == 1]
    df_doc_2 = df[df["Documentation Level"] == 2]
    df_doc_3 = df[df["Documentation Level"] == 3]

    print("Number of Documentation Level 1 entries: " + str(df_doc_1["Documentation Level"].count()))
    print("Number of Documentation Level 2 entries: " + str(df_doc_2["Documentation Level"].count()))
    print("Number of Documentation Level 3 entries: " + str(df_doc_3["Documentation Level"].count()))


    comm_doc_2 = df_doc_2["Commits Six Months"]
    comm_doc_3 = df_doc_3["Commits Six Months"]

    lines_doc_2 = df_doc_2["Lines Six Months"]
    lines_doc_3 = df_doc_3["Lines Six Months"]

    print("\n")

    print("mannwhitneyu for commits by Documentation level")
    s, p = stats.mannwhitneyu(comm_doc_2, comm_doc_3, alternative='greater')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))


    median_2 = comm_doc_2.median()
    median_3 = comm_doc_3.median()

    print("Median commits doc level 2 " + str(median_2))
    print("Median commits doc level 3 " + str(median_3))

    print("\n")

    print("mannwhitneyu for lines by Documentation level")
    s, p = stats.mannwhitneyu(lines_doc_2, lines_doc_3, alternative='greater')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))

    median_2 = lines_doc_2.mean()
    median_3 = lines_doc_3.mean()

    print("Median lines doc level 2 " + str(median_2))
    print("Median lines doc level 3 " + str(median_3))


    print("Testing affect of Modularity level")
    df_doc_1 = df[df["Modularity Level"] == 1]
    df_doc_2 = df[df["Modularity Level"] == 2]
    df_doc_3 = df[df["Modularity Level"] == 3]

    print("Number of Modularity Level 1 entries: " + str(df_doc_1["Modularity Level"].count()))
    print("Number of Modularity Level 2 entries: " + str(df_doc_2["Modularity Level"].count()))
    print("Number of Modularity Level 3 entries: " + str(df_doc_3["Modularity Level"].count()))


    comm_doc_2 = df_doc_2["Commits Six Months"]
    comm_doc_3 = df_doc_3["Commits Six Months"]

    lines_doc_2 = df_doc_2["Lines Six Months"]
    lines_doc_3 = df_doc_3["Lines Six Months"]

    print("\n")

    print("mannwhitneyu for commits by Modularity level")
    s, p = stats.mannwhitneyu(comm_doc_2, comm_doc_3, alternative='less')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))


    median_2 = comm_doc_2.median()
    median_3 = comm_doc_3.median()

    print("Median commits Modularity level 2 " + str(median_2))
    print("Median commits Modularity level 3 " + str(median_3))

    print("\n")

    print("mannwhitneyu for lines by Modularity level")
    s, p = stats.mannwhitneyu(lines_doc_2, lines_doc_3, alternative='less')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))

    median_2 = lines_doc_2.mean()
    median_3 = lines_doc_3.mean()

    print("Median lines Modularity level 2 " + str(median_2))
    print("Median lines Modularity level 3 " + str(median_3))


    print("Testing affect of Install Guide")
    df_doc_1 = df[df["Install"] == 0]
    df_doc_2 = df[df["Install"] == 1]


    print("Number of Install 0 entries: " + str(df_doc_1["Install"].count()))
    print("Number of Install 1 entries: " + str(df_doc_2["Install"].count()))


    comm_doc_1 = df_doc_1["Commits Six Months"]
    comm_doc_2 = df_doc_2["Commits Six Months"]

    lines_doc_1 = df_doc_1["Lines Six Months"]
    lines_doc_2 = df_doc_2["Lines Six Months"]

    print("\n")

    print("mannwhitneyu for commits by Install")
    s, p = stats.mannwhitneyu(comm_doc_1, comm_doc_2, alternative='greater')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))


    median_1 = comm_doc_1.median()
    median_2 = comm_doc_2.median()

    print("Median commits Install 0 " + str(median_1))
    print("Median commits Install 1 " + str(median_2))

    print("\n")

    print("mannwhitneyu for lines by Install")
    s, p = stats.mannwhitneyu(lines_doc_1, lines_doc_2, alternative='less')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))

    median_1 = lines_doc_1.mean()
    median_2 = lines_doc_2.mean()

    print("Median lines Install 0 " + str(median_1))
    print("Median lines Install 1 " + str(median_2))

    print("Testing affect of Tutorial Guide")
    df_doc_1 = df[df["Tutorial"] == 0]
    df_doc_2 = df[df["Tutorial"] == 1]


    print("Number of Tutorial 0 entries: " + str(df_doc_1["Tutorial"].count()))
    print("Number of Tutorial 1 entries: " + str(df_doc_2["Tutorial"].count()))


    comm_doc_1 = df_doc_1["Commits Six Months"]
    comm_doc_2 = df_doc_2["Commits Six Months"]

    lines_doc_1 = df_doc_1["Lines Six Months"]
    lines_doc_2 = df_doc_2["Lines Six Months"]

    print("\n")

    print("mannwhitneyu for commits by Tutorial")
    s, p = stats.mannwhitneyu(comm_doc_1, comm_doc_2, alternative='greater')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))


    median_1 = comm_doc_1.median()
    median_2 = comm_doc_2.median()

    print("Median commits Tutorial 0 " + str(median_1))
    print("Median commits Tutorial 1 " + str(median_2))

    print("\n")

    print("mannwhitneyu for lines by Tutorial")
    s, p = stats.mannwhitneyu(lines_doc_1, lines_doc_2, alternative='less')
    print("Statistic: "+ str(s))
    print("p-value: " + str(p))

    median_1 = lines_doc_1.mean()
    median_2 = lines_doc_2.mean()

    print("Median lines Tutorial 0 " + str(median_1))
    print("Median lines Tutorial 1 " + str(median_2))

if __name__ == "__main__":
    main()
