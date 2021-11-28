# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from typing import Union
from pathlib import Path
import pandas as pd
import webbrowser
import sys


class timeline(object):
    def __init__(self, title="Timeline", *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.title = title
      self.df = pd.DataFrame(columns=['content', 'start', 'end'])

    def add_df(self, df: pd.DataFrame) -> None:
      self.df = df.copy()
      return self

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
  var container = document.getElementById('visualization');"""

      use_group = False
      if (self.df['group'] != '').all():
        use_group = True

      if use_group:
        self.html += f"""
  var groups = new vis.DataSet(["""
        group_array = self.df['group'].unique().tolist()
        group_hashmap = {}
        for i in range(len(group_array)):
          group_hashmap[group_array[i]] = i
          self.html += f"""
    {{ id: {i}, content: "{group_array[i]}" }},"""
        self.html += f"""
  ]);"""

      self.html += f"""
  var items = new vis.DataSet(["""
      for idx, row in self.df.iterrows():
        if row['content'] == '' or row['start'] == '':
          print("Error. The 'content' or 'start' columns cannot be empty.")
          sys.exit(1)
        item_id = f"id: {idx}"
        if use_group:
          item_group = f", group: {group_hashmap[row['group']]}"
        else:
          item_group = ""
        item_content = f", content: '{row['content']}'"
        item_start = f", start: '{row['start']}'"
        item_end = "" if row['end'] == '' else f", end: '{row['end']}'"
        self.html += f"""
    {{{item_id}{item_group}{item_content}{item_start}{item_end}}},"""

      self.html += f"""
  ]);
  var options = {{}};"""

      self.html += f"""
  var timeline = new vis.Timeline(container, items, options);"""
      if use_group:
        self.html += f"""
  timeline.setGroups(groups);"""
      self.html += f"""
</script>
</body>
</html>"""

    def write_html(self, filename: Union[Path, str]) -> None:
      self._generate_html()
      output_path = filename
      if not isinstance(output_path, Path):
        output_path = Path(output_path)
      output_path.write_text(self.html)

    def show(self, filename: Union[Path, str]) -> None:
      output_path = filename
      if not isinstance(output_path, Path):
        output_path = Path(output_path)
      self.write_html(filename=output_path)
      webbrowser.open(output_path.resolve().as_uri(), new = 2)



