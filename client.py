# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 16:17:58 2014

@author: jiran
"""

from gearman import GearmanClient
client = GearmanClient(['192.168.1.123:4730'])
request = client.submit_job('reverse','this string')
newresult = request.result
print newresult