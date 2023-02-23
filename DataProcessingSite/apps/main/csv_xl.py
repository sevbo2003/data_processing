import sys
import csv

csv.field_size_limit(sys.maxsize)

import os
import pandas as pd
import numpy as np


class FileReader:
    CSV_EXTENSION = '.csv'
    NULL_CELL = np.nan
    
    def __init__(self, path:str=None, *args, **kwargs):
        """Read either csv or excel generated files"""
        if path:
            self.filename = path
            self.read_file()
            
        self.output_filename = kwargs.get('output_filename', self.filename)
        # if kwargs.get('output_filename'):
        #     self.write_file()

    def read_file(self,):
        """Determine which pandas fx to use to read the files"""
        name, ext = os.path.splitext(self.filename)
        if ext == self.CSV_EXTENSION:
            self.dataframe = pd.read_csv(self.filename, 
                                        encoding="UTF-8", 
                                        sep=',', engine="python")

        else:
            self.dataframe = pd.read_excel(self.filename,
                                        header=0, engine='openpyxl')
        self.headers = list(self.dataframe.columns)
        
    def new_column(self, column):
        """create a new column"""
        self.dataframe[column] = np.nan
        return

    def find_or_create_column(self, column:str):
        """search for a column; if not found, create one"""
        if column not in self.headers:
            self.new_column(column)
        return

    def new_row(self, values:dict):
        """create a new row and reset the index of the dataframe"""
        r = dict(zip(self.headers, [np.nan for i in range(len(self.headers))]))
        for key, value in values:
            r[key] = value
        
        self.dataframe.loc[len(self.dataframe.index)] = list(r.values)
        # sort file
        self.dataframe.sort_index().reset_index(drop=True)
        return self.dataframe

    def write_file(self,):
        """write output to a file"""
        name, ext = os.path.splitext(self.output_filename)
        if ext == self.CSV_EXTENSION:
            self.dataframe.to_csv(self.output_filename,
                                        sep=',')
        else:
            self.dataframe.to_excel(self.output_filename,
                                        header=0, engine="python")
        return format(self.output_filename)
    
    def query_by_column(self, column, query):
        """search for row where specific column == value"""
        return self.dataframe.loc[self.dataframe[column] == query]
    
    def update_value(self, column, row, value):
        """update value of a specific cell"""
        self.dataframe.at[row, column] = value
        return