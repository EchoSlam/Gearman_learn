# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 16:17:58 2014

@author: jiran
"""

from gearman import GearmanClient
client = GearmanClient(['127.0.0.1:4730'])
request = client.submit_job('reverse_string','reverse this string')
client.wait(86400)