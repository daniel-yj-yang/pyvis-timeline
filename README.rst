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

This tool leverages the amazing vis-timeline library to provide interactive visualizations.


Installation
------------

.. code-block::

   pip install pyvis-timeline


Sample Usage
------------

>>> import pandas as pd
>>> from pyvis_timeline import timeline
>>> df = pd.DataFrame.from_dict({'content': ['Alpha (B.1.1.7)', 'Beta (B.1.351)', 'Gamma (P.1)', 'Delta (B.1.617.2)', 'Omicron (B.1.1.529)'], 'start': ['2020-12-18', '2020-12-18', '2021-01-11', '2021-05-11', '2021-11-26'], 'end': [None, None, None, None, None]}) # https://www.who.int/en/activities/tracking-SARS-CoV-2-variants/
>>> timeline(title='SARS-CoV-2 VOC (Variants of Concern) Designation Timeline').add_df(df).show('covid19_VOC_timeline.html')


Sample Screenshot
-----------------
.. raw:: html
   :file: https://github.com/daniel-yj-yang/pyvis-timeline/raw/main/pyvis_timeline/examples/covid19_VOC_timeline.html

