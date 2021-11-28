# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause

from pyvis_timeline import timeline, dataset
df = dataset().load_as_df("COVID19_Variants_Date_of_Designation")
print(df)
vis1 = timeline(title='COVID-19 Variants - Date of Designation')
vis1.add_df(df = df)
vis1.write_html('test.html')
print(vis1.html)

