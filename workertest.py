# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:35:06 2014

@author: jiran
"""

import gearman
def task_listen_reverse(gearman_worker,gearman_job):
    return gearman_job.data[::-1]
    
gm_worker = gearman.GearmanWorker(['192.168.1.123:4730'])
gm_worker.set_client_id('ss')
gm_worker.register_task("reverse",task_listen_reverse)

gm_worker.work()