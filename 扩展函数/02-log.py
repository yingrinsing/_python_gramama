#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-25

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import logging
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = None
    laok.dump_description_help(obj)


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True
    #logging.basicConfig(level=logging.INFO)
    #logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
     
#     logger.info('Start reading database')
#     # read database here
#      
    records = {'john': 55, 'tom': 66}
#     logger.debug('Records: %s', records)
#     logger.info('Updating records ...')
#     # update records here
#     logger.info('Finish updating records')
    
    # create a file handler
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
     
    logger.info('Hello baby')
    logger.debug('Records: %s', records)