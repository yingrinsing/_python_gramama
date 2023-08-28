#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-11

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import hashlib
#===============================================================================
# 
#===============================================================================
#<module 'hashlib' from 'D:\software\Anaconda2\lib\hashlib.pyc'>,<type 'module'>
#attribute---->
    #algorithms[<type 'tuple'>] [('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')]
    #algorithms_available[<type 'set'>] [set(['SHA1', 'SHA224', 'SHA', 'SHA384', 'ecdsa-with-SHA1', 'SHA256', 'SHA512', 'md4', 'md5', 'sha1', 'dsaWithSHA', 'DSA-SHA', 'sha224', 'dsaEncryption', 'DSA', 'ripemd160', 'sha', 'MD5', 'MD4', 'sha384', 'sha256', 'sha512', 'RIPEMD160', 'whirlpool'])]
    #algorithms_guaranteed[<type 'set'>] [set(['sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'])]
#builtin-method---->
    #md5 [<type 'builtin_function_or_method'>] [Returns a md5 hash object; optionally initialized with a string]
    #pbkdf2_hmac [<type 'builtin_function_or_method'>] [pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key    Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as  pseudorandom function.]
    #sha1 [<type 'builtin_function_or_method'>] [Returns a sha1 hash object; optionally initialized with a string]
    #sha224 [<type 'builtin_function_or_method'>] [Returns a sha224 hash object; optionally initialized with a string]
    #sha256 [<type 'builtin_function_or_method'>] [Returns a sha256 hash object; optionally initialized with a string]
    #sha384 [<type 'builtin_function_or_method'>] [Returns a sha384 hash object; optionally initialized with a string]
    #sha512 [<type 'builtin_function_or_method'>] [Returns a sha512 hash object; optionally initialized with a string]
#funcs/method---->
    #new(name, string='') [new(name, string='') - Return a new hashing object using the named algorithm;]

def _lktest():
    obj = hashlib
    laok.dump_description_help(obj)
    
if __name__ == '__main__':
    laok.lktest_run()
