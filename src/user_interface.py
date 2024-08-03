import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
import pandas as pd
from data_import_export import import_csv, import_excel, import_text, import_json, import_xml, import_sql, export_csv, export_excel, export_pdf, export_html, export_sql
from data_management import impute_missing_values, remove_duplicates, validate_data, scale_data, normalize_data, filter_data, subset_data, merge_data, reshape_data, pivot_data, add_calculated_field

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analysis Application")
        self.dataframe = None

        # Create buttons
        self.import_csv_button = tk.Button(root, text="Import CSV", command=self.import_csv)
        self.import_csv_button.pack(pady=10)
        self.export_csv_button = tk.Button(root, text="Export CSV", command=self.export_csv)
        self.export_csv_button.pack(pady=10)

        self.impute_button = tk.Button(root, text="Impute Missing Values", command=self.impute_missing_values)
        self.impute_button.pack(pady=10)
        self.remove_duplicates_button = tk.Button(root, text="Remove Duplicates", command=self.remove_duplicates)
        self.remove_duplicates_button.pack(pady=10)
        self.filter_button = tk.Button(root, text="Filter Data", command=self.filter_data)
        self.filter_button.pack(pady=10)

    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.dataframe = import_csv(file_path)
            messagebox.showinfo("Import CSV", "Data imported successfully.")

    def export_csv(self):
        if self.dataframe is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                export_csv(self.dataframe, file_path)
                messagebox.showinfo("Export CSV", "Data exported successfully.")
        else:
            messagebox.showwarning("Export CSV", "No data to export.")

    def impute_missing_values(self):
        if self.dataframe is not None:
            strategy = simpledialog.askstring("Impute Missing Values", "Enter strategy (mean/median/mode):")
            if strategy:
                self.dataframe = impute_missing_values(self.dataframe, strategy)
                messagebox.showinfo("Impute Missing Values", "Missing values imputed successfully.")
        else:
            messagebox.showwarning("Impute Missing Values", "No data to process.")

    def remove_duplicates(self):
        if self.dataframe is not None:
            self.dataframe = remove_duplicates(self.dataframe)
            messagebox.showinfo("Remove Duplicates", "Duplicates removed successfully.")
        else:
            messagebox.showwarning("Remove Duplicates", "No data to process.")

    def filter_data(self):
        if self.dataframe is not None:
            condition = simpledialog.askstring("Filter Data", "Enter filter condition (e.g., 'column > 10'):")
            if condition:
                self.dataframe = filter_data(self.dataframe, condition)
                messagebox.showinfo("Filter Data", "Data filtered successfully.")
        else:
            messagebox.showwarning("Filter Data", "No data to filter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
