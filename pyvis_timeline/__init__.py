# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from .__about__ import (
    __version__,
    __license__,
)

from .timeline import timeline
from .examples import dataset

# this is for "from <package_name> import *"
__all__ = ["timeline", "dataset"]
