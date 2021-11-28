# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


import pandas as pd
import importlib.resources as pkg_resources
from io import StringIO
from . import data


class dataset(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_as_df(self, name: str):
        if name == "COVID19_Variants_Date_of_Designation":
            self.df = pd.read_csv(StringIO(pkg_resources.read_text(data, 'COVID19_Variants_Date_of_Designation.csv')), keep_default_na=False)
        return self.df
        
