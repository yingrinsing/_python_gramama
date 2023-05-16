#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-9

@author: laok@ArgusTech
@email:  1306743659@qq.com
@copyright: Apache License, Version 2.0
"""
import sys, os
from types import ModuleType
#===============================================================================
# 
#===============================================================================

class DownModule(ModuleType):
    __all__ = ()  
    __package__ = __name__
    def __getattr__(self, name):
        try:
            return __import__(name)
        except ImportError:
            try:
                os.system('pip install %s' % name )
                return __import__(name)
            except Exception:
                raise ImportError(name)
            
    __path__ = []
    __file__ = __file__
_mod = DownModule(__name__, DownModule.__doc__)
sys.modules[_mod.__name__] = _mod
