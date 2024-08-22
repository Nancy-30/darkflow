import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def scatter_plot(df, x, y, hue, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue)
    plt.title(title)
    plt.show()

def line_plot(df, x, y, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()

def bar_plot(df, x, y, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()

def box_plot(df, x, y, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()

def violin_plot(df, x, y, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()

def heatmap(df, title):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True)
    plt.title(title)
    plt.show()

