# python_gil_comparision

# Python GIL Performance Analysis

This project analyzes the performance impact of disabling the **Global Interpreter Lock (GIL)** in **Python 3.13** for multi-threaded and multi-processing tasks, as well as comparing it with **Python 3.12**. The script will run performance tests with Python 3.13 (with and without the GIL) and Python 3.12, and generate a plot along with a table showing the performance results.

## Requirements

- **Python 3.13** (both with and without GIL enabled).
- **Python 3.12**.
- **Matplotlib**: For generating performance comparison plots.
- **Pandas**: For creating performance tables in image format.

To install the required libraries, run:

```bash
pip install matplotlib pandas
```

**Running the Script**

To run the performance analysis, execute the run_command.py script. This script will:

- Run the performance tests using Python 3.13 with GIL disabled.
- Run the tests using Python 3.13 with GIL enabled.
- Run the tests using Python 3.12.
- Generate a performance comparison plot.
- Create an image showing a table of the performance results.


