import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Use a non-interactive backend
mpl.use('Agg')

def scatter_plot(df, x, y, hue, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def line_plot(df, x, y, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def bar_plot(df, x, y, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x=x, y=y)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def box_plot(df, x, y, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def violin_plot(df, x, y, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x=x, y=y)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def heatmap(df, title, save_path=None):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

def generate_and_save_graphs(df, save_folder):
    try:
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        
        # Dynamically select columns for plotting
        numeric_cols = df.select_dtypes(include=["number"]).columns
        if len(numeric_cols) >= 2:
            print(f"Generating plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
            scatter_plot(df, x=numeric_cols[0], y=numeric_cols[1], hue=None, title='Scatter Plot', save_path=os.path.join(save_folder, 'scatter_plot.png'))
            print(f"Generated scatter plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
            line_plot(df, x=numeric_cols[0], y=numeric_cols[1], title='Line Plot', save_path=os.path.join(save_folder, 'line_plot.png'))
            print(f"Generated line plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
            bar_plot(df, x=numeric_cols[0], y=numeric_cols[1], title='Bar Plot', save_path=os.path.join(save_folder, 'bar_plot.png'))
            print(f"Generated bar plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
            box_plot(df, x=numeric_cols[0], y=numeric_cols[1], title='Box Plot', save_path=os.path.join(save_folder, 'box_plot.png'))
            print(f"Generated box plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
            violin_plot(df, x=numeric_cols[0], y=numeric_cols[1], title='Violin Plot', save_path=os.path.join(save_folder, 'violin_plot.png'))
            print(f"Generated violin plots for columns: {numeric_cols[0]} and {numeric_cols[1]}")
        heatmap(df, title='Heatmap', save_path=os.path.join(save_folder, 'heatmap.png'))
        print(f"Generated heatmap")
    except Exception as e:
        print(f"Error generating plots: {str(e)}")