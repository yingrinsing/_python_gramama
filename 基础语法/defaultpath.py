#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-25

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import sys
import os
import laok
#===============================================================================
# 
#===============================================================================
#<module 'ntpath' from 'D:\InstallSoftware\Anaconda2\lib\ntpath.pyc'>,<type 'module'>
#attribute---->
    #altsep[<type 'str'>] [/]
    #curdir[<type 'str'>] [.]
    #defpath[<type 'str'>] [.;C:\bin]
    #devnull[<type 'str'>] [nul]
    #extsep[<type 'str'>] [.]
    #genericpath[<type 'module'>] [<module 'genericpath' from 'D:\InstallSoftware\Anaconda2\lib\genericpath.pyc'>]
    #os[<type 'module'>] [<module 'os' from 'D:\InstallSoftware\Anaconda2\lib\os.pyc'>]
    #pardir[<type 'str'>] [..]
    #pathsep[<type 'str'>] [;]
    #sep[<type 'str'>] [\]
    #stat[<type 'module'>] [<module 'stat' from 'D:\InstallSoftware\Anaconda2\lib\stat.pyc'>]
    #supports_unicode_filenames[<type 'bool'>] [True]
    #sys[<type 'module'>] [<module 'sys' (built-in)>]
    #warnings[<type 'module'>] [<module 'warnings' from 'D:\InstallSoftware\Anaconda2\lib\warnings.pyc'>]
#builtin-method---->
    #isdir [<type 'builtin_function_or_method'>] [Return true if the pathname refers to an existing directory.]
#funcs/method---->
    #abspath(path) [Return the absolute version of a path.]
    #basename(p) [Returns the final component of a pathname]
    #commonprefix(m) [Given a list of pathnames, returns the longest common leading component]
    #dirname(p) [Returns the directory component of a pathname]
    #exists(path) [Test whether a path exists.  Returns False for broken symbolic links]
    #expanduser(path) [Expand ~ and ~user constructs.]
    #expandvars(path) [Expand shell variables of the forms $var, ${var} and %var%.]
    #getatime(filename) [Return the last access time of a file, reported by os.stat().]
    #getctime(filename) [Return the metadata change time of a file, reported by os.stat().]
    #getmtime(filename) [Return the last modification time of a file, reported by os.stat().]
    #getsize(filename) [Return the size of a file, reported by os.stat().]
    #isabs(s) [Test whether a path is absolute]
    #isfile(path) [Test whether a path is a regular file]
    #islink(path) [Test for symbolic link.]
    #ismount(path) [Test whether a path is a mount point (defined as root of drive)]
    #join(path, *paths) [Join two or more pathname components, inserting "\" as needed.]
    #lexists(path) [Test whether a path exists.  Returns False for broken symbolic links]
    #normcase(s) [Normalize case of pathname.]
    #normpath(path) [Normalize path, eliminating double slashes, etc.]
    #realpath(path) [Return the absolute version of a path.]
    #relpath(path, start='.') [Return a relative version of a path]
    #split(p) [Split a pathname.]
    #splitdrive(p) [Split a pathname into drive/UNC sharepoint and relative path specifiers.]
    #splitext(p) [Split the extension from a pathname.]
    #splitunc(p) [Split a pathname into UNC mount point and relative path specifiers.]
    #walk(top, func, arg) [Directory tree walk with callback function.]    


def _lktest():
    obj = os.path
    laok.dump_description_help(obj)


if __name__ == '__main__':
    # print sys.path
    laok.lktest_run()
