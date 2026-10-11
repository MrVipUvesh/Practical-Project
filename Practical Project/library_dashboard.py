import os
import time
import random
import shutil
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

class LibraryDashboard:
    def load_data(self, file_path): #Load & Validate data
        try:
            file_path = file_path.strip().strip('"')
            if not file_path:
                print("[Error: File path can't be empty]")
                return False
            if not file_path.lower().endswith(".csv"):
                print("[Error: Please select a CSV file]")
                return False
            df = pd.read_csv(file_path)
            if df.empty or len(df.columns) == 0:
                print("[Error: Dataset is empty]")
                return False
            current_path = os.path.dirname(os.path.abspath(__file__))
            destination_path = os.path.join(current_path, os.path.basename(file_path))
            if os.path.abspath(file_path) != os.path.abspath(destination_path):
                shutil.copy2(file_path, destination_path)
            self.data = df
            self.file_path = destination_path
            print("Dataset imported successfully!")
            return True
        except PermissionError:
            print("[Error: You don't have permission to access this file]")
        except FileNotFoundError:
            print("[Error: File not found]")
        return False
    def calculate_statistics(self): #Calculate: most borrowed book, borrowing time, busiest day
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            df = self.data.copy()

            if df.isnull().values.any():
                null_count = int(df.isnull().sum().sum())
                print(f"{null_count} null values found!")
                print("Filling numeric null values with column averages...")
                print()
                numeric_columns = df.select_dtypes(include=np.number).columns
                for column in numeric_columns:
                    if df[column].isnull().any():
                        average = df[column].mean()
                        df[column] = df[column].fillna(average)
                self.data = df
                print("Numeric null values handled successfully!")
                remaining = int(df.isnull().sum().sum())
                if remaining:
                    print(f"[Notice: {remaining} null values remain in non-numeric or empty columns]")
            else:
                print("No null values found in the dataset.")
            print(f"\nTotal records: {len(self.data)}")
            print(f"Total columns: {len(self.data.columns)}")
            print("\nAvailable columns:")
            for column in self.data.columns:
                print(f"- {column}")
        except Exception as error:
            print(f"[Error: Unable to analyze dataset: {error}]")
    def filter_transactions(self, condition): #Filter data by user defined condition
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            if not condition.strip():
                print("[Error: Filter condition can't be empty]")
                return
            columns = {
                str(column).strip().lower(): column
                for column in self.data.columns
            }
            if "=" in condition:
                column_name, value = condition.split("=", 1)
                column_name = column_name.strip().strip("'\"").lower()
                value = value.strip().strip("'\"")
                if column_name not in columns:
                    print("[Error: Column not found]")
                    return
                column = columns[column_name]
                result = self.data[
                    self.data[column].astype(str).str.contains(
                        value, case=False, na=False, regex=False
                    )
                ]
            else:
                matches = pd.Series(False, index=self.data.index)
                for column in self.data.columns:
                    matches |= self.data[column].astype(str).str.contains(
                        condition.strip(), case=False, na=False, regex=False
                    )
                result = self.data[matches]
            if result.empty:
                print("No matching transactions found.")
                return
            print(f"\nMatching records: {len(result)}")
            print(result.to_string(index=False))
            save_choice = input("Save filtered data to a CSV file? (y/n): ").strip().lower()
            if save_choice == "y":
                output_name = input("Enter output file name: ").strip().strip('"')
                if not output_name:
                    print("[Error: File name can't be empty]")
                    return
                if not output_name.lower().endswith(".csv"):
                    output_name += ".csv"
                if os.path.basename(output_name) != output_name:
                    print("[Error: Enter a file name, not a path]")
                    return
                output_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    output_name
                )
                result.to_csv(output_path, index=False)
                print("Filtered data saved successfully!")
            elif save_choice != "n":
                print("[Error: Invalid input. Enter y or n]")
        except PermissionError:
            print("[Error: Permission denied while saving or reading data]")
        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"[Error: Unable to filter data: {error}]")
        except Exception as error:
            print(f"[Error: Unexpected filtering error: {error}]")
    def generate_report(self): #Generate summary of the analysis
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            df = self.data
            numeric_data = df.select_dtypes(include=np.number)
            report = [
                "Library Dataset Report",
                "-" * 30,
                f"Generated on: {dt.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')}",
                f"Total transactions: {len(df)}",
                f"Total columns: {len(df.columns)}",
                f"Missing values: {int(df.isnull().sum().sum())}",
                "",
                "Column details:",
                df.dtypes.to_string(),
                "",
                "Numerical summary:",
                numeric_data.describe().to_string()
                if not numeric_data.empty
                else "No numerical columns available."
            ]
            print("\n" + "\n".join(report))
            save_choice = input("\nSave report to a text file? (y/n): ").strip().lower()
            if save_choice == "y":
                report_name = input("Enter report file name: ").strip().strip('"')
                if not report_name:
                    print("[Error: File name can't be empty]")
                    return
                if not report_name.lower().endswith(".txt"):
                    report_name += ".txt"
                if os.path.basename(report_name) != report_name:
                    print("[Error: Enter a file name, not a path]")
                    return
                report_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    report_name
                )
                with open(report_path, "w", encoding="utf-8") as file:
                    file.write("\n".join(report))
                print("Report saved successfully!")
            elif save_choice != "n":
                print("[Error: Invalid input. Enter y or n]")
        except PermissionError:
            print("[Error: Permission denied while saving the report]")
        except (OSError, ValueError, TypeError) as error:
            print(f"[Error: Unable to generate report: {error}]")
        except Exception as error:
            print(f"[Error: Unexpected report error: {error}]")
    def find_column(self, keywords):
        for column in self.data.columns:
            name = str(column).strip().lower().replace("_", " ").replace("-", " ")
            if any(keyword in name for keyword in keywords):
                return column
        return None
    def show_table(self, data):
        if data.empty:
            print("No records available.")
            return
        print(data.to_string(index=False))
    def show_analysis(self, choice):
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            if choice == "1":
                column = self.find_column(["genre", "category", "subject"])
                if column is None:
                    print("[Error: Genre/category column not found]")
                    return
                counts = self.data[column].value_counts()
                if counts.empty:
                    print("No genre data available.")
                    return
                print("\nMost borrowed genre:")
                print(f"{counts.index[0]} - {counts.iloc[0]} borrows")
            elif choice == "2":
                column = self.find_column(["book title", "book name", "title", "book"])
                if column is None:
                    print("[Error: Book title/name column not found]")
                    return
                result = self.data[column].value_counts().rename_axis("Book").reset_index(name="Total borrows")
                self.show_table(result)
            elif choice == "3":
                column = self.find_column([
                    "duration", "days borrowed", "borrowing time", "borrow days"
                ])
                if column is None:
                    numeric_columns = list(self.data.select_dtypes(include=np.number).columns)
                    if not numeric_columns:
                        print("[Error: Borrowing duration column not found]")
                        return
                    print("\nNumeric columns:")
                    for index, name in enumerate(numeric_columns):
                        print(f"{index + 1}. {name}")
                    choice = input("Select borrowing duration column: ").strip()
                    if not choice.isdigit() or not 1 <= int(choice) <= len(numeric_columns):
                        print("[Error: Invalid column selection]")
                        return
                    column = numeric_columns[int(choice) - 1]
                duration = pd.to_numeric(self.data[column], errors="coerce").dropna()
                if duration.empty:
                    print("[Error: No valid duration values found]")
                    return
                print(f"Average borrowing duration: {duration.mean():.2f}")
                print(f"Minimum borrowing duration: {duration.min():.2f}")
                print(f"Maximum borrowing duration: {duration.max():.2f}")
        except Exception as error:
            print(f"[Error: Unable to complete analysis: {error}]")
    def show_filter(self, choice):
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            if choice == "1":
                column = self.find_column(["book title", "book name", "title", "book"])
                if column is None:
                    print("[Error: Book title/name column not found]")
                    return
                result = self.data[column].value_counts().rename_axis("Book").reset_index(name="Total borrows")
                self.show_table(result)
            elif choice == "2":
                column = self.find_column(["date", "borrowed at", "borrow date", "transaction date", "checkout"])
                if column is None:
                    print("[Error: Date column not found]")
                    return
                dates = pd.to_datetime(self.data[column], errors="coerce")
                dates = dates.dropna()
                if dates.empty:
                    print("[Error: No valid dates found]")
                    return
                result = dates.dt.to_period("M").value_counts().sort_index()
                self.show_table(result.rename_axis("Month").reset_index(name="Total borrows"))
            elif choice == "3":
                column = self.find_column(["genre", "category", "subject"])
                if column is None:
                    print("[Error: Genre/category column not found]")
                    return
                result = self.data[column].value_counts().rename_axis("Genre").reset_index(name="Book count")
                self.show_table(result)
            elif choice == "4":
                column = self.find_column(["date", "borrowed at", "borrow date", "transaction date", "checkout"])
                if column is None:
                    print("[Error: Date column not found]")
                    return
                dates = pd.to_datetime(self.data[column], errors="coerce").dropna()
                if dates.empty:
                    print("[Error: No valid dates found]")
                    return
                result = dates.dt.day_name().value_counts()
                self.show_table(result.rename_axis("Day").reset_index(name="Total borrows"))
        except Exception as error:
            print(f"[Error: Unable to filter data: {error}]")
    def show_visualization(self, choice):
        try:
            if not hasattr(self, "data"):
                print("[Error: Please import a dataset first]")
                return
            df = self.data
            if choice == "1":
                column = self.find_column(["book title", "book name", "title", "book"])
                if column is None:
                    print("[Error: Book title/name column not found]")
                    return
                counts = df[column].dropna().value_counts().head(5)
                if counts.empty:
                    print("No book borrowing data available.")
                    return
                x = counts.index.astype(str)
                y = counts.values
                plt.bar(x, y)
                plt.title("Top 5 Most Borrowed Books")
                plt.xlabel("Book")
                plt.ylabel("Total Borrows")
                plt.xticks(rotation=35, ha="right")
                plt.tight_layout()
                plt.show()
            elif choice == "2":
                column = self.find_column([
                    "borrowed at", "borrow date", "transaction date",
                    "checkout date", "date", "timestamp"
                ])
                if column is None:
                    print("[Error: Borrowing date column not found]")
                    return
                dates = pd.to_datetime(df[column], errors="coerce").dropna()
                if dates.empty:
                    print("[Error: No valid borrowing dates found]")
                    return
                counts = dates.dt.to_period("M").value_counts().sort_index()
                if counts.empty:
                    print("No monthly borrowing data available.")
                    return
                x = counts.index.astype(str)
                y = counts.values
                plt.plot(x, y, marker="o")
                plt.title("Borrowing Trends Over Month")
                plt.xlabel("Month")
                plt.ylabel("Total Borrows")
                plt.xticks(rotation=35, ha="right")
                plt.tight_layout()
                plt.show()
            elif choice == "3":
                column = self.find_column(["genre", "category", "subject"])
                if column is None:
                    print("[Error: Genre/category column not found]")
                    return
                counts = df[column].dropna().value_counts()
                if counts.empty:
                    print("No genre data available.")
                    return
                plt.pie(counts.values, labels=counts.index.astype(str), autopct="%1.1f%%")
                plt.title("Distribution of Books Borrowed by Genre")
                plt.tight_layout()
                plt.show()
            elif choice == "4":
                date_column = self.find_column([
                    "borrowed at", "transaction date", "borrow date",
                    "checkout date", "timestamp", "date"
                ])
                time_column = self.find_column(["borrow time", "checkout time", "time"])
                if date_column is None:
                    print("[Error: Borrowing date column not found]")
                    return
                dates = pd.to_datetime(df[date_column], errors="coerce")
                if time_column is not None and time_column != date_column:
                    combined_values = df[date_column].astype(str) + " " + df[time_column].astype(str)
                    combined_dates = pd.to_datetime(combined_values, errors="coerce")
                    if combined_dates.notna().any():
                        dates = combined_dates
                valid_dates = dates.dropna()
                if valid_dates.empty:
                    print("[Error: No valid borrowing date/time values found]")
                    return
                activity = pd.DataFrame({
                    "Day": valid_dates.dt.day_name(),
                    "Hour": valid_dates.dt.hour
                })
                day_order = [
                    "Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"
                ]
                heatmap_data = activity.groupby(["Day", "Hour"]).size().unstack(fill_value=0)
                heatmap_data = heatmap_data.reindex(day_order, fill_value=0)
                if heatmap_data.empty:
                    print("No borrowing activity data available.")
                    return
                sns.heatmap(heatmap_data, cmap="YlOrBr", linewidths=0.3)
                plt.title("Borrowing Activity by Day and Time")
                plt.xlabel("Hour of Day")
                plt.ylabel("Day of Week")
                plt.tight_layout()
                plt.show()
        except PermissionError:
            print("[Error: Permission denied]")
        except (ValueError, TypeError, KeyError) as error:
            print(f"[Error: Unable to create visualization: {error}]")
        except Exception as error:
            print(f"[Error: Unexpected visualization error: {error}]")
        finally:
            plt.close()
ld = LibraryDashboard()
imported = 0
print("\n\033[1mWELCOME TO DASHBOARD\033[0m")
while True:
    print("\nSelect an Operation:")
    print("1. Import Library Dataset")
    print("2. Analyze Library Data")
    print("3. Filter Library Data")
    print("4. Visualize Library Data")
    print("5. Exit Dashboard")
    choice = input("Enter your choice: ").strip()
    match choice:
        case "1":
            while True:
                print("\nSelect an operation:")
                print("1. Import dataset")
                print("2. Remove dataset")
                print("3. Back to dashboard")
                ild_choice = input("Enter your choice: ").strip()
                match ild_choice:
                    case "1":
                        file_path = input("Enter file path/name: ").strip()
                        if not file_path:
                            print("[Error: File path can't be empty]")
                            continue
                        if ld.load_data(file_path):
                            imported = 1
                    case "2":
                        file_name = input("Enter file name with extension: ").strip().strip('"')
                        if not file_name:
                            print("[Error: File name can't be empty]")
                            continue
                        try:
                            current_path = os.path.dirname(os.path.abspath(__file__))
                            file_path = os.path.join(current_path, file_name)
                            os.remove(file_path)
                            if hasattr(ld, "file_path") and os.path.abspath(ld.file_path) == os.path.abspath(file_path):
                                del ld.data
                                del ld.file_path
                                imported = 0
                            print("File removed successfully")
                        except PermissionError:
                            print("[Error: Permission denied]")
                        except FileNotFoundError:
                            print("[Error: File not found]")
                        except IsADirectoryError:
                            print("[Error: The selected path is a directory]")
                        except OSError as error:
                            print(f"[Error: Unable to remove file: {error}]")
                    case "3":
                        print("Returning to dashboard...")
                        time.sleep(random.randint(1, 3))
                        break

                    case _:
                        print("[Error: Invalid option selected]")
                        continue
        case "2":
            if imported == 1:
                ld.calculate_statistics()
                while True:
                    print("\nSelect an operation:")
                    print("1. Most borrowed genre")
                    print("2. Total borrows per book")
                    print("3. Average borrowing duration")
                    print("4. Generate analysis report")
                    print("5. Back to dashboard")
                    ald_choice = input("Enter your choice: ").strip()
                    match ald_choice:
                        case "1":
                            ld.show_analysis(ald_choice)
                        case "2":
                            ld.show_analysis(ald_choice)
                        case "3":
                            ld.show_analysis(ald_choice)
                        case "4":
                            ld.generate_report()
                        case "5":
                            print("Returning to dashboard...")
                            time.sleep(random.randint(1, 3))
                            break
                        case _:
                            print("[Error: Invalid option selected]")
                            continue
            else:
                print("[Error: Please import a dataset first]")
        case "3":
            if imported != 1:
                print("[Error: Please import a dataset first]")
                continue
            while True:
                print("\nSelect an operation:")
                print("1. Most borrowed books")
                print("2. Borrowing trends")
                print("3. Books distribution")
                print("4. Borrowing activity")
                print("5. Filter transactions")
                print("6. Back to dashboard")
                vld_choice = input("Enter your choice: ").strip()
                match vld_choice:
                    case "1":
                        ld.show_filter(vld_choice)
                    case "2":
                        ld.show_filter(vld_choice)
                    case "3":
                        ld.show_filter(vld_choice)
                    case "4":
                        ld.show_filter(vld_choice)
                    case "5":
                        condition = input("Enter keyword or condition (e.g. Genre=Fiction): ").strip()
                        ld.filter_transactions(condition)
                    case "6":
                        print("Returning to dashboard...")
                        time.sleep(random.randint(1, 3))
                        break
                    case _:
                        print("[Error: Invalid option selected]")
                        continue
        case "4":
            if imported != 1:
                print("[Error: Please import a dataset first]")
                continue
            while True:
                print("\nSelect a visualization:")
                print("1. Top 5 most borrowed books")
                print("2. Borrowing trends over month")
                print("3. Distribution of books borrowed by genre")
                print("4. Borrowing activity by day and time")
                print("5. Back to dashboard")
                filter_choice = input("Enter your choice: ").strip()
                match filter_choice:
                    case "1":
                        ld.show_visualization(filter_choice)
                    case "2":
                        ld.show_visualization(filter_choice)
                    case "3":
                        ld.show_visualization(filter_choice)
                    case "4":
                        ld.show_visualization(filter_choice)
                    case "5":
                        print("Returning to dashboard...")
                        time.sleep(random.randint(1, 3))
                        break
                    case _:
                        print("[Error: Invalid option selected]")
                        continue
        case "5":
            print("Closing Library Dashboard...")
            time.sleep(random.randint(1, 3))
            print("Exittin Programme...")
            time.sleep(random.randint(1, 3))
            print("Thank you for using Library Dashboard by \033[1mUvesh Ansari\033[0m")
            break
        case _:
            print("[Error: Invalid option selected]")
            continue