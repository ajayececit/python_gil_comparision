import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot(python3_13_gil_0, python3_13_gil_1, python3_12_gil_1):
    # Labels for the GIL settings
    labels = ['GIL=0 (3.13)', 'GIL=1 (3.13)', 'GIL=1 (3.12)']

    # Extracting the data for plotting
    single_threaded = [python3_13_gil_0['single_threaded'], python3_13_gil_1['single_threaded'], python3_12_gil_1['single_threaded']]
    multi_threaded = [python3_13_gil_0['multi_threaded'], python3_13_gil_1['multi_threaded'], python3_12_gil_1['multi_threaded']]
    multi_processing = [python3_13_gil_0['multi_processing'], python3_13_gil_1['multi_processing'], python3_12_gil_1['multi_processing']]

    # Bar width
    bar_width = 0.2

    # Positions of the bars on the x-axis
    r1 = np.arange(len(single_threaded))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    # Create the bar graph
    plt.bar(r1, single_threaded, color='b', width=bar_width, edgecolor='grey', label='Single-threaded')
    plt.bar(r2, multi_threaded, color='orange', width=bar_width, edgecolor='grey', label='Multi-threaded')
    plt.bar(r3, multi_processing, color='lightblue', width=bar_width, edgecolor='grey', label='Multi-processing')

    # Adding labels
    plt.xlabel('GIL (Python Version)', fontweight='bold')
    plt.ylabel('Time Taken (seconds)', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(single_threaded))], labels)

    # Adding the legend
    plt.legend()

    # Save the plot before showing it
    plt.savefig('gil_performance_plot.png')

    # Now display the plot
    plt.show()

    # Create a table similar to the one in the image using pandas DataFrame
    data = {
        'GIL (Py Version)': ['GIL=0 (3.13)', 'GIL=1 (3.13)', 'GIL=1 (3.12)'],
        'Single-threaded': single_threaded,
        'Multi-threaded': multi_threaded,
        'Multi-processing': multi_processing
    }

    # Create the table using pandas DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame as a table
    print(df)
    save_dataframe_as_image(df, 'gil_performance_table.png')

    # Save the DataFrame as an image using Matplotlib
def save_dataframe_as_image(dataframe, filename):
    fig, ax = plt.subplots(figsize=(8, 2))  # Set the figure size
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=dataframe.values, colLabels=dataframe.columns, cellLoc='center', loc='center')

    # Save the table as an image file
    plt.savefig(filename)

# Save the DataFrame as an image


