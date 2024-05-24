import pandas as pd
import numpy as np
from pathlib import Path


# write a class that reads the data and does some basic analysis
class CerealAnalysis:
    def __init__(self, data_path: Path):
        self.df = pd.read_csv(data_path)
        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]
        self.columns = self.df.columns
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.categorical_cols = self.df.select_dtypes(include=object).columns
        self.missing_values = self.df.isnull().sum()
        self.unique_values = self.df.nunique()
        self.dtypes = self.df.dtypes

    def __str__(self):
        return f"Dataframe with {self.n_rows} rows and {self.n_cols} columns"

    def __repr__(self):
        return f"CerealAnalysis(data_path={self.data_path})"

    def get_numeric_summary(self):
        return self.df.describe()

    def get_missing_values(self):
        return self.missing_values

    def get_unique_values(self):
        return self.unique_values

    def get_dtypes(self):
        return self.dtypes

    def get_columns(self):
        return self.columns

    def get_numeric_cols(self):
        return self.numeric_cols

    def get_categorical_cols(self):
        return self.categorical_cols

    def get_data(self):
        return self.df

    def get_column(self, col):
        return self.df[col]

    def get_value_counts(self, col):
        return self.df[col].value_counts()

    def get_correlation(self):
        return self.df.corr()

    def get_column_correlation(self, col1, col2):
        return self.df[col1].corr(self.df[col2])

    def get_column_correlation_with_all(self, col):
        return self.df.corrwith(self.df[col])

    def get_info(self):
        return self.df.info()
