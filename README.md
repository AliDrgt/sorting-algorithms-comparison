# Sorting Algorithms Comparison

## Overview

This project compares various sorting algorithms: Selection Sort, Bubble Sort, Merge Sort, and Quick Sort. It includes implementations of these algorithms in Python and analyzes their performance based on execution time.

## Features

- **Sorting Algorithms:** Implementations of Bubble Sort, Selection Sort, Merge Sort, and Quick Sort in Python.
- **Performance Analysis:** Comparison of execution time for various input sizes.
- **Random Input Generation:** Script to generate random input data for testing.

## Project Structure

- **bubblesort.py:** Implementation of Bubble Sort.
- **selectionsort.py:** Implementation of Selection Sort.
- **mergesort.py:** Implementation of Merge Sort.
- **quicksort.py:** Implementation of Quick Sort.
- **timeaverage.py:** Script to analyze and compare the performance of all algorithms.
- **randomGen.py:** Script to generate random input data for testing.
- **data/**: Directory containing input files for testing.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/sorting-algorithms-comparison.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd sorting-algorithms-comparison
    ```
3. **Install required packages (if any):**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Sorting Algorithms

1. **Bubble Sort:**
    ```sh
    python bubblesort.py
    ```

2. **Selection Sort:**
    ```sh
    python selectionsort.py
    ```

3. **Merge Sort:**
    ```sh
    python mergesort.py
    ```

4. **Quick Sort:**
    ```sh
    python quicksort.py
    ```

### Performance Analysis

1. **Run performance analysis:**
    ```sh
    python timeaverage.py
    ```

2. **View results:**
    - Check the output in the console for detailed performance data.

## Example Output

### Execution Time Comparison

| Input Size | Bubble Sort Time | Selection Sort Time | Merge Sort Time | Quick Sort Time |
|------------|------------------|---------------------|-----------------|-----------------|
| 100        | 0.002 sec        | 0.0002 sec          | 0.0001 sec      | 0.0001 sec      |
| 1000       | 0.13 sec         | 0.02 sec            | 0.01 sec        | 0.01 sec        |
| 10000      | 5.59 sec         | 2.56 sec            | 0.1 sec         | 0.09 sec        |
| 50000      | 147 sec          | 69.98 sec           | 0.5 sec         | 0.4 sec         |

## Acknowledgments

This project was created by Ali Fatih Durgut as part of a comparative study on sorting algorithms.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
