from abc import ABC, abstractmethod
from typing import Union
import pandas as pd

class read_doc(ABC):
    def __init__(self, filepath:'str', filename:'str') -> None:
        self.filepath = filepath
        self.filename = filename
    
    @abstractmethod
    def get_column_headers(self) -> None:
        pass

class read_xl(read_doc):
    def __init__(self, filepath: 'str', filename: 'str') -> None:
        super().__init__(filepath, filename)
        self.raw = pd.read_excel(self.filepath+self.filename, usecols=[1,2,3,4],skiprows=1)
        self.raw_dict = self.raw.replace({'\xa0':' ' , '\'': '', r'\W': '', 'and': '', 'Models': 'Model'},regex=True)
        self.raw_dict['Areas'] = self.raw_dict['Areas'].str.lower()
        self.raw_dict = self.raw_dict.to_dict()

    def get_column_headers(self) -> None:
        """Returns XL column headers as list"""
        raw_dict = self.raw_dict
        headers = [raw_dict[i][0] for i in raw_dict]
        return headers
    
    def get_rsts(self):
        column_list = [[self.raw_dict['Description'][i], self.raw_dict['Areas'][i], self.raw_dict['Type'][i]] for i in self.raw_dict['Type']]
        return column_list 

# raw = read_xl('X:\\Dropbox\\GitHub\\Skeleton_DB\\datafiles\\', 'catalogofrsts.xlsx')
# rst_listings = raw.get_rsts()
# print('hi')