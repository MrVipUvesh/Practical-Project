# Library Dashboard

## Overview

Library Dashboard is a Python-based data management and visualization application designed to analyze library transaction datasets through an interactive, menu-driven interface. It allows users to import CSV files, validate and inspect datasets, analyze borrowing patterns, filter transactions, generate reports, and visualize library activity using different types of charts.

The project combines data processing, file management, statistical analysis, and visualization to make library transaction data easier to understand. It is designed as a practical Python project that demonstrates how multiple Python libraries can work together to process structured data and present meaningful insights.

## Key Features

### 1. Dataset Management
- Import CSV datasets using a file path or file name.
- Remove imported dataset files from the project directory.
- Validate file paths and check file extensions.
- Detect empty datasets and handle missing files.
- Handle file permission errors.
- Automatically copy imported datasets into the project directory.
- Track the currently loaded dataset for subsequent operations.
- Clear the active dataset when its associated file is removed.

### 2. Data Validation and Inspection
- Check whether a dataset has been imported before performing operations.
- Detect missing values across all columns.
- Count and display the total number of missing values.
- Replace missing numeric values with their respective column averages.
- Notify users when missing values remain in non-numeric or entirely empty columns.
- Display the total number of records and columns.
- List all available column names.
- Handle errors that occur during dataset inspection and processing.

### 3. Library Data Analysis
The analysis section provides the following operations:

- **Most Borrowed Genre:** Identifies the genre or category with the highest number of recorded borrowing transactions.
- **Total Borrows per Book:** Counts borrowing records for individual books and displays the results in a table.
- **Average Borrowing Duration:** Calculates the average, minimum, and maximum borrowing duration using a suitable numeric column.
- **Analysis Report:** Generates a report containing dataset statistics, column data types, missing values, and numerical summaries.

### 4. Transaction Filtering
- Search for transactions using a keyword.
- Filter records using a column-based condition, such as `Genre=Fiction`.
- Match keywords across multiple columns when no specific column is provided.
- Perform case-insensitive searches.
- Display the number of matching records.
- Present matching records in a readable tabular format.
- Export filtered records to a CSV file.
- Validate output file names and extensions.
- Handle invalid conditions, missing columns, file errors, and unexpected exceptions.

### 5. Data Filtering and Summarization
The filtering menu provides four predefined data summaries:

- **Most Borrowed Books:** Displays books ranked by the number of recorded transactions.
- **Borrowing Trends:** Groups valid borrowing dates by month and counts the transactions for each month.
- **Books Distribution:** Counts the recorded transactions associated with each genre or category.
- **Borrowing Activity:** Groups transactions by weekday and calculates the number of records for each day.

### 6. Data Visualization
The dashboard supports four visualizations using Matplotlib and Seaborn.

#### Top 5 Most Borrowed Books
- Identifies the five most frequently recorded books.
- Uses a bar chart to compare borrowing counts.
- Displays book titles on the horizontal axis.
- Displays total borrowing records on the vertical axis.
- Rotates horizontal-axis labels to improve readability.

#### Borrowing Trends Over Month
- Converts borrowing dates into datetime values.
- Groups transactions by calendar month.
- Sorts monthly results chronologically.
- Uses a line chart with markers to display changes in borrowing activity over time.

#### Distribution of Books Borrowed by Genre
- Identifies the genre or category column.
- Counts the recorded borrowing transactions for each category.
- Uses a pie chart to represent the relative distribution of borrowing records.
- Displays percentage labels for each category.

#### Borrowing Activity by Day and Time
- Detects a suitable date or timestamp column.
- Optionally combines separate date and time columns.
- Extracts the weekday and hour from valid datetime values.
- Groups transactions by weekday and hour.
- Organizes weekdays from Monday through Sunday.
- Uses a heatmap to display borrowing activity across different times of the day.

### 7. Report Generation
- Generates a report using the currently loaded dataset.
- Records the date and time when the report is generated.
- Displays the total number of transactions and columns.
- Includes the total number of missing values.
- Lists the data type of each column.
- Includes descriptive statistics for numeric columns.
- Displays a suitable message when no numeric columns are available.
- Saves the report as a `.txt` file when requested.

### 8. Error Handling
The application includes error handling for common operational problems, including:

- Empty file paths and file names.
- Unsupported file extensions.
- Missing files.
- Permission-related errors.
- Empty datasets.
- Missing datasets during analysis.
- Missing or unrecognized columns.
- Invalid filtering conditions.
- Invalid menu selections.
- Invalid numeric column selections.
- Missing or invalid date and time values.
- Errors during report generation and file saving.
- Unexpected data processing and visualization errors.

## Technologies and Libraries

### Python Standard Library

- **os:** Handles file paths, directory operations, file existence through operating system operations, and path validation.
- **time:** Introduces delays when returning to menus and closing the application.
- **random:** Generates random delay durations.
- **shutil:** Copies imported datasets while preserving file metadata where supported.
- **datetime:** Provides date and time information for generated reports and date-related processing.

### Third-Party Libraries

- **Pandas:** Reads CSV files, processes tabular data, handles missing values, filters records, groups transactions, and calculates descriptive statistics.
- **NumPy:** Supports numerical data selection and numeric operations.
- **Matplotlib:** Creates bar charts, line charts, and pie charts.
- **Seaborn:** Creates heatmaps for borrowing activity analysis.

## Installation Requirements

Ensure Python is installed on your system.

Install all required third-party libraries using the following command:

    pip install pandas numpy matplotlib seaborn

The remaining modules used by the project are included in Python's standard library.

## How to Run the Project

1. Save the source code in a Python file named `library_dashboard.py`.
2. Open a terminal or command prompt in the directory containing the Python file.
3. Install the required libraries.
4. Execute the program using:

       python library_dashboard.py

5. Select an operation from the main dashboard menu.
6. Import a CSV dataset before accessing the analysis, filtering, or visualization features.
7. Follow the instructions displayed in the terminal.
8. Save filtered data or analysis reports when prompted.
9. Select the exit option to close the application.

## Dashboard Navigation

### Main Menu

The main menu contains five options:

1. Import Library Dataset
2. Analyze Library Data
3. Filter Library Data
4. Visualize Library Data
5. Exit Dashboard

### Import Library Dataset

This section contains three options:

1. Import dataset
2. Remove dataset
3. Back to dashboard

When a dataset is imported successfully, the program stores the DataFrame in the dashboard object and records the destination file path. The imported flag is updated so that other dashboard features become accessible.

When the currently loaded dataset file is removed through the removal menu, the program deletes its active data attributes and resets the imported flag.

### Analyze Library Data

This section contains five options:

1. Most borrowed genre
2. Total borrows per book
3. Average borrowing duration
4. Generate analysis report
5. Back to dashboard

Before displaying the analysis menu, the program checks and processes missing values through the dataset inspection method.

### Filter Library Data

This section contains six options:

1. Most borrowed books
2. Borrowing trends
3. Books distribution
4. Borrowing activity
5. Filter transactions
6. Back to dashboard

The first four options generate predefined summaries. The fifth option allows users to enter a custom keyword or column-based condition.

### Visualize Library Data

This section contains five options:

1. Top 5 most borrowed books
2. Borrowing trends over month
3. Distribution of books borrowed by genre
4. Borrowing activity by day and time
5. Back to dashboard

Each visualization is generated in a separate Matplotlib window. The program closes Matplotlib figures after the visualization operation finishes.

## Class and Method Documentation

The project uses a class named `LibraryDashboard` to organize dataset management, analysis, filtering, reporting, and visualization into separate methods.

### 1. `load_data(self, file_path)`

**Purpose:** Imports and validates a CSV dataset.

**How it works:**
- Removes surrounding whitespace and quotation marks from the supplied path.
- Checks whether the path is empty.
- Verifies that the file name ends with `.csv`, ignoring letter case.
- Reads the CSV file using `pd.read_csv()`.
- Rejects datasets that contain no records or no columns.
- Determines the directory containing the Python script.
- Copies the imported file into that directory when the source and destination differ.
- Stores the loaded DataFrame in `self.data`.
- Stores the destination path in `self.file_path`.
- Returns `True` after successful import or `False` when the handled import process fails.

**Important:** This method copies the original dataset into the project directory. It does not automatically modify the original file.

### 2. `calculate_statistics(self)`

**Purpose:** Inspects the imported dataset and handles missing numeric values.

**How it works:**
- Checks whether the `data` attribute exists.
- Creates a copy of the current DataFrame.
- Checks whether any missing values exist.
- Counts missing values across the dataset.
- Selects numeric columns using `select_dtypes(include=np.number)`.
- Calculates each affected numeric column's mean.
- Replaces missing values in those columns with the calculated mean.
- Updates `self.data` with the processed DataFrame.
- Reports any remaining missing values.
- Displays the total record count, column count, and column names.

**Important:** Missing values in non-numeric columns are not filled by this method. Numeric columns containing only missing values may also retain missing values because their mean cannot be calculated.

### 3. `filter_transactions(self, condition)`

**Purpose:** Searches and filters the dataset using a custom condition.

**How it works:**
- Checks whether a dataset has been imported.
- Rejects empty conditions.
- Creates a normalized mapping of column names for case-insensitive column matching.
- Checks whether the supplied condition contains an equals sign.
- If an equals sign exists, separates the column name from the search value.
- Searches the specified column using case-insensitive substring matching.
- If no equals sign exists, searches across all columns.
- Displays the matching records and their total count.
- Asks whether the filtered records should be saved.
- Validates the output file name and adds the `.csv` extension when necessary.
- Saves the filtered DataFrame using `to_csv()`.

**Example conditions:**

    Genre=Fiction
    Book Title=Python Programming
    Fiction

The first two examples search a specified column. The final example searches across all columns.

**Important:** The search uses substring matching rather than exact equality. For example, searching for `Fiction` can also match a value such as `Science Fiction`.

### 4. `generate_report(self)`

**Purpose:** Generates a textual summary of the imported dataset.

**How it works:**
- Checks whether a dataset is available.
- Selects numeric columns.
- Creates a report containing the generation timestamp, transaction count, column count, missing-value count, and column data types.
- Generates descriptive statistics for numeric columns using `describe()`.
- Displays the report in the terminal.
- Asks whether the user wants to save it.
- Validates the report file name.
- Saves the report as a text file using UTF-8 encoding.

**Numerical summary:** When numeric columns are available, the report includes statistics such as count, mean, standard deviation, minimum, quartiles, and maximum.

### 5. `find_column(self, keywords)`

**Purpose:** Finds a dataset column using a list of keywords.

**How it works:**
- Iterates through the available column names.
- Converts each name to lowercase.
- Replaces underscores and hyphens with spaces.
- Checks whether any supplied keyword appears in the normalized column name.
- Returns the first matching original column name.
- Returns `None` if no matching column is found.

**Example:**

    self.find_column(["genre", "category", "subject"])

This can identify columns such as `Genre`, `Book_Category`, or `Subject`, depending on their names.

**Important:** The method returns the first match, not necessarily the most specific match.

### 6. `show_table(self, data)`

**Purpose:** Displays a DataFrame in a readable tabular format.

**How it works:**
- Checks whether the supplied DataFrame is empty.
- Displays a message when no records are available.
- Otherwise, prints the DataFrame using `to_string(index=False)`.

The `index=False` argument hides the DataFrame index in the displayed output.

### 7. `show_analysis(self, choice)`

**Purpose:** Executes the selected data analysis operation.

**Available operations:**

- **Choice 1:** Finds the genre or category column, counts its values, and displays the most frequently recorded category.
- **Choice 2:** Finds the book title column, counts each book's transactions, and displays the results in a table.
- **Choice 3:** Finds a borrowing duration column or asks the user to select a numeric column. It converts values to numeric form, removes invalid entries, and calculates the average, minimum, and maximum.

The method checks for missing datasets and relevant columns before performing each operation.

### 8. `show_filter(self, choice)`

**Purpose:** Generates predefined summaries of library borrowing data.

**Available operations:**

- **Choice 1:** Counts transactions for each book.
- **Choice 2:** Converts borrowing dates to datetime values, groups them by month, and counts transactions per month.
- **Choice 3:** Counts transactions for each genre or category.
- **Choice 4:** Converts borrowing dates to datetime values and counts transactions for each weekday.

The resulting summaries are displayed through the `show_table()` method.

**Important:** The monthly summary is sorted chronologically. The weekday summary is sorted by transaction count rather than by weekday order.

### 9. `show_visualization(self, choice)`

**Purpose:** Generates the selected chart using Matplotlib or Seaborn.

**Available operations:**

- **Choice 1:** Creates a bar chart of the five most frequently recorded book titles.
- **Choice 2:** Creates a line chart showing monthly transaction counts.
- **Choice 3:** Creates a pie chart showing the distribution of transactions by genre.
- **Choice 4:** Creates a heatmap of borrowing activity by weekday and hour.

The method validates the availability of relevant columns and checks for usable data before plotting.

A `try-except-finally` structure handles errors and closes Matplotlib figures when the method finishes.

## Important Python Concepts Demonstrated

### Object-Oriented Programming
The `LibraryDashboard` class groups related operations into reusable methods. The `self` parameter allows methods to access shared instance attributes, including `self.data` and `self.file_path`.

### File Handling
The project reads CSV files, copies datasets, removes files, and writes CSV and text outputs.

### Exception Handling
`try`, `except`, and `finally` blocks help manage file access problems, invalid data, and visualization errors.

### Conditional Statements
`if`, `elif`, `else`, and `match-case` statements control menu navigation and operation selection.

### Loops
`while` loops maintain the main dashboard and its nested menus. `for` loops process columns, keywords, and weekday names.

### String Processing
Methods such as `strip()`, `lower()`, `replace()`, `split()`, and `endswith()` help normalize user input and validate names.

### DataFrame Operations
The project uses Pandas operations such as:
- `read_csv()`
- `copy()`
- `isnull()`
- `sum()`
- `select_dtypes()`
- `fillna()`
- `value_counts()`
- `dropna()`
- `to_numeric()`
- `to_datetime()`
- `groupby()`
- `reset_index()`
- `to_csv()`
- `describe()`

### Data Visualization
Matplotlib functions such as `bar()`, `plot()`, `pie()`, `title()`, `xlabel()`, `ylabel()`, `xticks()`, `tight_layout()`, and `show()` generate charts. Seaborn's `heatmap()` function visualizes grouped borrowing activity.

## Project Structure

A typical project directory may look like this:

    LibraryDashboard/
    ├── library_dashboard.py
    ├── library_transactions.csv
    ├── filtered_data.csv
    └── analysis_report.txt

- `library_dashboard.py`: Contains the dashboard implementation.
- `library_transactions.csv`: An example imported dataset.
- `filtered_data.csv`: An example filtered dataset generated by the application.
- `analysis_report.txt`: An example report generated by the application.

The output files are optional and are created only when the relevant operations are performed. The actual imported dataset may have a different name.

## Dataset Compatibility

For the best results, the CSV dataset should contain recognizable column names.

Examples of supported column names include:

| Information | Example column names |
|---|---|
| Book title | `Book Title`, `Book Name`, `Title`, `Book` |
| Genre | `Genre`, `Category`, `Subject` |
| Borrowing date | `Borrow Date`, `Borrowed At`, `Transaction Date`, `Checkout Date`, `Date` |
| Borrowing time | `Borrow Time`, `Checkout Time`, `Time` |
| Borrowing duration | `Duration`, `Days Borrowed`, `Borrowing Time`, `Borrow Days` |

Column detection uses keywords, so actual compatibility depends on the column names and the order in which matches are found.

For date-based analysis, the values must be interpretable by Pandas. If separate date and time columns are used for the heatmap, they should contain compatible date and time values.

## Limitations and Considerations

- The application currently works with CSV datasets rather than database systems.
- Imported files are copied into the script's directory, which may overwrite a file with the same destination name.
- The currently loaded DataFrame is stored in memory and is not automatically saved after changes.
- Missing-value handling fills numeric columns only.
- Borrowing frequency represents the number of recorded rows; it does not independently verify unique borrowing events.
- The average borrowing duration requires a suitable numeric column.
- Automatic column detection depends on recognizable column names and may select an unintended column when multiple names match.
- The monthly trend chart displays months present in the dataset and does not automatically insert missing months.
- The heatmap uses a 24-hour scale, with hours represented from 0 to 23 when present in the data.
- If a dataset stores dates and times in an unsupported format, some date-based operations may fail to identify valid values.
- File removal permanently deletes the selected file from the project directory, subject to operating system permissions.
- The dashboard is a terminal-based application; charts open in separate graphical windows.

## Future Improvements

Potential enhancements include:

- Adding configurable missing-value strategies for numeric and non-numeric columns.
- Improving automatic column detection and allowing users to select columns manually.
- Adding date-range filters and advanced transaction search.
- Including borrower-level statistics and unique transaction counts.
- Adding borrowing trends by year, quarter, and week.
- Displaying all 24 hours and all seven weekdays consistently in heatmaps.
- Supporting additional export formats such as Excel and PDF.
- Adding automated dataset validation and duplicate-record detection.
- Introducing a graphical user interface for easier navigation.
- Integrating a database for persistent storage and larger datasets.

## Learning Outcomes

This project provides practical experience in:

- Python programming and object-oriented design.
- CSV file management and filesystem operations.
- Data validation and missing-value handling.
- DataFrame manipulation using Pandas.
- Numerical processing using NumPy.
- Statistical summaries and transaction analysis.
- Data filtering and searching.
- Report generation and file exporting.
- Data visualization using Matplotlib and Seaborn.
- Exception handling and menu-driven application development.

## Author

**Uvesh Ansari**

## Conclusion

Library Dashboard demonstrates how Python can be used to build a structured data analysis application for library transactions. By combining file management, data processing, statistical summaries, custom filtering, report generation, and visualization, the project provides a practical foundation for understanding data analysis workflows and developing more advanced data-driven applications.
