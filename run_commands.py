import re
import subprocess
from plot import plot
def run_python_script(python, gil):
    """
    Run the Python 3.13 script and capture the time taken for each task in seconds.
    """
    try:
        command = [python, "-X", gil, "/Users/ajay_thangavelu/PycharmProjects/pythonProject/GIL_TEST/gil_test.py"]

        # Run the command and capture stdout
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Extract the time in seconds for each task
        times = {
            "single_threaded": extract_time_in_seconds(result.stdout, "run_single_threaded"),
            "multi_threaded": extract_time_in_seconds(result.stdout, "run_multi_threaded"),
            "multi_processing": extract_time_in_seconds(result.stdout, "run_multi_processing")
        }

        return times

    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")
        return e.stderr


def extract_time_in_seconds(output, task_name):
    """
    Extracts the time in seconds for a specific task using regex.
    Args:
        output (str): The stdout string that contains the time in seconds.
        task_name (str): The name of the task to extract the time for.
    Returns:
        float: The extracted time in seconds as a float.
    """
    # Use a regular expression to find the time for the specified task
    match = re.search(rf'{task_name} took ([\d.]+) seconds', output)

    # If a match is found, return the time as a float
    if match:
        return float(match.group(1))
    else:
        return None  # Return None if no match is found


# Example usage: Running the Python script and extracting times for all tasks
python3_13_gil_0 = run_python_script("Python3.13", "gil=0")
if python3_13_gil_0:
    print(f"Single-threaded time: {python3_13_gil_0['single_threaded']}")
    print(f"Multi-threaded time: {python3_13_gil_0['multi_threaded']}")
    print(f"Multi-processing time: {python3_13_gil_0['multi_processing']}")
else:
    print("No times found in output")


python3_13_gil_1 = run_python_script("Python3.13", "gil=1")
if python3_13_gil_1:
    print(f"Single-threaded time: {python3_13_gil_1['single_threaded']}")
    print(f"Multi-threaded time: {python3_13_gil_1['multi_threaded']}")
    print(f"Multi-processing time: {python3_13_gil_1['multi_processing']}")
else:
    print("No times found in output")


python3_12_gil_1 = run_python_script("Python3.12", "gil=0")
if python3_12_gil_1:
    print(f"Single-threaded time: {python3_12_gil_1['single_threaded']}")
    print(f"Multi-threaded time: {python3_12_gil_1['multi_threaded']}")
    print(f"Multi-processing time: {python3_12_gil_1['multi_processing']}")
else:
    print("No times found in output")

plot(python3_13_gil_0, python3_13_gil_1, python3_12_gil_1)
