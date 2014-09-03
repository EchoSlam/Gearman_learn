# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 16:55:44 2014

@author: jiran
"""

import os  
import gearman  
import math  
  
class CustomGearmanWorker(gearman.GearmanWorker):    
    def on_job_execute(self, current_job):    
        print "Job started"   
        return super(CustomGearmanWorker, self).on_job_execute(current_job)    
   
def task_callback(gearman_worker, job):    
    print job.data   
    return job.data  
   
new_worker = CustomGearmanWorker(['127.0.0.1:4730'])    
new_worker.register_task("echo", task_callback)    
new_worker.work()
