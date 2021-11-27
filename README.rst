.. -*- mode: rst -*-

|BuildTest|_ |PyPi|_ |License|_ |Downloads|_ |PythonVersion|_

.. |BuildTest| image:: https://travis-ci.com/daniel-yj-yang/pyvis-timeline.svg?branch=main
.. _BuildTest: https://app.travis-ci.com/github/daniel-yj-yang/pyvis-timeline

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. _PythonVersion: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue

.. |PyPi| image:: https://img.shields.io/pypi/v/pyvis-timeline
.. _PyPi: https://pypi.python.org/pypi/pyvis-timeline

.. |Downloads| image:: https://pepy.tech/badge/pyvis-timeline
.. _Downloads: https://pepy.tech/project/pyvis-timeline

.. |License| image:: https://img.shields.io/pypi/l/pyvis-timeline
.. _License: https://pypi.python.org/pypi/pyvis-timeline


===================================
Interactive Timeline Visualizations
===================================

This tool leverages the amazing vis-timeline library (https://github.com/visjs/vis-timeline) to provide visualization.


Installation
------------

.. code-block::

   pip install pyvis-timeline


Sample Usage
------------

.. code-block::

import pandas as pd
from pyvis_timeline import timeline
data = {'content': ['item1', 'item2', 'item3', 'item4'], 'start': ['2021-03-20', '2021-04-30', '2021-05-15', '2021-06-27'], 'end': [None, None, None, '2021-07-31']}
df = pd.DataFrame.from_dict(data)
vis1 = timeline(title='Basic Timeline')
vis1.add_df(df = df)
vis1.show('timeline.html') # this will generate a html and open a webbrowser tab to view it


Sample Screenshot
-----------------
Basic Timeline

|image1|


.. |image1| image:: https://github.com/daniel-yj-yang/pyvis-timeline/raw/main/treekit/examples/basic_timeline.png

