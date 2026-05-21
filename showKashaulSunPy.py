#!/usr/bin/env python

import sunpy.map
import sunpy.data.sample

sunpy.data.sample.AIA_171_IMAGE
my_map = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

my_map.quicklook()

quit()

