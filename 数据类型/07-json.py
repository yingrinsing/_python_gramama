#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018-4-4

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import json
#===============================================================================
# 
#===============================================================================
#<module 'json' from 'D:\InstallSoftware\Anaconda2\lib\json\__init__.pyc'>,<type 'module'>
#attribute---->
    #JSONDecoder[<type 'type'>] [<class 'json.decoder.JSONDecoder'>]
    #JSONEncoder[<type 'type'>] [<class 'json.encoder.JSONEncoder'>]
    #decoder[<type 'module'>] [<module 'json.decoder' from 'D:\InstallSoftware\Anaconda2\lib\json\decoder.pyc'>]
    #encoder[<type 'module'>] [<module 'json.encoder' from 'D:\InstallSoftware\Anaconda2\lib\json\encoder.pyc'>]
    #scanner[<type 'module'>] [<module 'json.scanner' from 'D:\InstallSoftware\Anaconda2\lib\json\scanner.pyc'>]
#funcs/method---->
    #dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw) [Serialize ``obj`` as a JSON formatted stream to ``fp`` (a]
    #dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw) [Serialize ``obj`` to a JSON formatted ``str``.]
    #load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) [Deserialize ``fp`` (a ``.read()``-supporting file-like object containing]
    #loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) [Deserialize ``s`` (a ``str`` or ``unicode`` instance containing a JSON]

def _lktest():
    obj = json
    laok.dump_description_help(obj)
    


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True