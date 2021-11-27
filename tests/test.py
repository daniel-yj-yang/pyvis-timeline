# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause

import pandas as pd
from pyvis_timeline import timeline

data = {'content': ['item1', 'item2', 'item3', 'item4'], 'start': ['2021-03-20', '2021-04-30', '2021-05-15', '2021-06-27'], 'end': [None, None, None, '2021-07-31']}
df = pd.DataFrame.from_dict(data)
print(df)
vis1 = timeline(title='Basic Timeline')
vis1.add_df(df = df)
vis1.write_html('test.html')
print(vis1.html)

