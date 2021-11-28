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

>>> from pyvis_timeline import timeline, dataset
>>> df = dataset().load_as_df("COVID19_Variants_Date_of_Designation")
>>> timeline(title='COVID-19 Variants - Date of Designation').add_df(df).show('output.html')


Sample Screenshot
-----------------
COVID-19 Variants Designation Timeline

|image1|


.. |image1| image:: https://github.com/daniel-yj-yang/pyvis-timeline/raw/main/pyvis_timeline/examples/covid19_variants_designation_timeline.png

