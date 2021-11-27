# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from typing import Union
from pathlib import Path
import pandas as pd
import webbrowser


class timeline(object):
    def __init__(self, title="Timeline", *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.title = title
      self.df = pd.DataFrame(columns=['content', 'start', 'end'])

    def add_df(self, df: pd.DataFrame) -> None:
      self.df = df.copy()

    def _generate_html(self) -> None:
      """
      see also: https://visjs.org/
      """
      self.html = f"""<!DOCTYPE HTML>
<html>
<head>
  <title>{self.title}</title>
  <style type="text/css">
    body, html {{
      font-family: sans-serif;
    }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis-timeline-graph2d.min.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="visualization"></div>
<script type="text/javascript">
  var container = document.getElementById('visualization');
  var items = new vis.DataSet(["""

      for idx, row in self.df.iterrows():
        start_part = f", start: '{row['start']}'" if row['start'] else ""
        end_part = f", end: '{row['end']}'" if row['end'] else ""
        self.html += f"""
    {{id: {idx+1}, content: '{row['content']}'{start_part}{end_part}}},"""

      self.html += f"""
  ]);
  var options = {{}};
  var timeline = new vis.Timeline(container, items, options);
</script>
</body>
</html>"""

    def write_html(self, filename: Union[Path, str]) -> None:
      self._generate_html()
      if not isinstance(filename, Path):
        output_path = Path(filename)
      else:
        output_path = filename
      output_path.write_text(self.html)

    def show(self, filename: Union[Path, str]) -> None:
      if not isinstance(filename, Path):
        output_path = Path(filename)
      else:
        output_path = filename
      self.write_html(filename=output_path)
      webbrowser.open(output_path.resolve().as_uri(), new = 2)



