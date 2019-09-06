#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-26

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import re
#===============================================================================
# 
#===============================================================================
#abc,<type 'str'>
#builtin-method---->
    #capitalize [<type 'builtin_function_or_method'>] [S.capitalize() -> string    Return a copy of the string S with only its first character  capitalized.]
    #center [<type 'builtin_function_or_method'>] [S.center(width[, fillchar]) -> string    Return S centered in a string of length width. Padding is  done using the specified fill character (default is a space)]
    #count [<type 'builtin_function_or_method'>] [S.count(sub[, start[, end]]) -> int    Return the number of non-overlapping occurrences of substring sub in  string S[start:end].  Optional arguments start and end are interpreted  as in slice notation.]
    #decode [<type 'builtin_function_or_method'>] [S.decode([encoding[,errors]]) -> object    Decodes S using the codec registered for encoding. encoding defaults  to the default encoding. errors may be given to set a different error  handling scheme. Default is 'strict' meaning that encoding errors raise  a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'  as well as any other name registered with codecs.register_error that is  able to handle UnicodeDecodeErrors.]
    #encode [<type 'builtin_function_or_method'>] [S.encode([encoding[,errors]]) -> object    Encodes S using the codec registered for encoding. encoding defaults  to the default encoding. errors may be given to set a different error  handling scheme. Default is 'strict' meaning that encoding errors raise  a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and  'xmlcharrefreplace' as well as any other name registered with  codecs.register_error that is able to handle UnicodeEncodeErrors.]
    #endswith [<type 'builtin_function_or_method'>] [S.endswith(suffix[, start[, end]]) -> bool    Return True if S ends with the specified suffix, False otherwise.  With optional start, test S beginning at that position.  With optional end, stop comparing S at that position.  suffix can also be a tuple of strings to try.]
    #expandtabs [<type 'builtin_function_or_method'>] [S.expandtabs([tabsize]) -> string    Return a copy of S where all tab characters are expanded using spaces.  If tabsize is not given, a tab size of 8 characters is assumed.]
    #find [<type 'builtin_function_or_method'>] [S.find(sub [,start [,end]]) -> int    Return the lowest index in S where substring sub is found,  such that sub is contained within S[start:end].  Optional  arguments start and end are interpreted as in slice notation.    Return -1 on failure.]
    #format [<type 'builtin_function_or_method'>] [S.format(*args, **kwargs) -> string    Return a formatted version of S, using substitutions from args and kwargs.  The substitutions are identified by braces ('{' and '}').]
    #index [<type 'builtin_function_or_method'>] [S.index(sub [,start [,end]]) -> int    Like S.find() but raise ValueError when the substring is not found.]
    #isalnum [<type 'builtin_function_or_method'>] [S.isalnum() -> bool    Return True if all characters in S are alphanumeric  and there is at least one character in S, False otherwise.]
    #isalpha [<type 'builtin_function_or_method'>] [S.isalpha() -> bool    Return True if all characters in S are alphabetic  and there is at least one character in S, False otherwise.]
    #isdigit [<type 'builtin_function_or_method'>] [S.isdigit() -> bool    Return True if all characters in S are digits  and there is at least one character in S, False otherwise.]
    #islower [<type 'builtin_function_or_method'>] [S.islower() -> bool    Return True if all cased characters in S are lowercase and there is  at least one cased character in S, False otherwise.]
    #isspace [<type 'builtin_function_or_method'>] [S.isspace() -> bool    Return True if all characters in S are whitespace  and there is at least one character in S, False otherwise.]
    #istitle [<type 'builtin_function_or_method'>] [S.istitle() -> bool    Return True if S is a titlecased string and there is at least one  character in S, i.e. uppercase characters may only follow uncased  characters and lowercase characters only cased ones. Return False  otherwise.]
    #isupper [<type 'builtin_function_or_method'>] [S.isupper() -> bool    Return True if all cased characters in S are uppercase and there is  at least one cased character in S, False otherwise.]
    #join [<type 'builtin_function_or_method'>] [S.join(iterable) -> string    Return a string which is the concatenation of the strings in the  iterable.  The separator between elements is S.]
    #ljust [<type 'builtin_function_or_method'>] [S.ljust(width[, fillchar]) -> string    Return S left-justified in a string of length width. Padding is  done using the specified fill character (default is a space).]
    #lower [<type 'builtin_function_or_method'>] [S.lower() -> string    Return a copy of the string S converted to lowercase.]
    #lstrip [<type 'builtin_function_or_method'>] [S.lstrip([chars]) -> string or unicode    Return a copy of the string S with leading whitespace removed.  If chars is given and not None, remove characters in chars instead.  If chars is unicode, S will be converted to unicode before stripping]
    #partition [<type 'builtin_function_or_method'>] [S.partition(sep) -> (head, sep, tail)    Search for the separator sep in S, and return the part before it,  the separator itself, and the part after it.  If the separator is not  found, return S and two empty strings.]
    #replace [<type 'builtin_function_or_method'>] [S.replace(old, new[, count]) -> string    Return a copy of string S with all occurrences of substring  old replaced by new.  If the optional argument count is  given, only the first count occurrences are replaced.]
    #rfind [<type 'builtin_function_or_method'>] [S.rfind(sub [,start [,end]]) -> int    Return the highest index in S where substring sub is found,  such that sub is contained within S[start:end].  Optional  arguments start and end are interpreted as in slice notation.    Return -1 on failure.]
    #rindex [<type 'builtin_function_or_method'>] [S.rindex(sub [,start [,end]]) -> int    Like S.rfind() but raise ValueError when the substring is not found.]
    #rjust [<type 'builtin_function_or_method'>] [S.rjust(width[, fillchar]) -> string    Return S right-justified in a string of length width. Padding is  done using the specified fill character (default is a space)]
    #rpartition [<type 'builtin_function_or_method'>] [S.rpartition(sep) -> (head, sep, tail)    Search for the separator sep in S, starting at the end of S, and return  the part before it, the separator itself, and the part after it.  If the  separator is not found, return two empty strings and S.]
    #rsplit [<type 'builtin_function_or_method'>] [S.rsplit([sep [,maxsplit]]) -> list of strings    Return a list of the words in the string S, using sep as the  delimiter string, starting at the end of the string and working  to the front.  If maxsplit is given, at most maxsplit splits are  done. If sep is not specified or is None, any whitespace string  is a separator.]
    #rstrip [<type 'builtin_function_or_method'>] [S.rstrip([chars]) -> string or unicode    Return a copy of the string S with trailing whitespace removed.  If chars is given and not None, remove characters in chars instead.  If chars is unicode, S will be converted to unicode before stripping]
    #split [<type 'builtin_function_or_method'>] [S.split([sep [,maxsplit]]) -> list of strings    Return a list of the words in the string S, using sep as the  delimiter string.  If maxsplit is given, at most maxsplit  splits are done. If sep is not specified or is None, any  whitespace string is a separator and empty strings are removed  from the result.]
    #splitlines [<type 'builtin_function_or_method'>] [S.splitlines(keepends=False) -> list of strings    Return a list of the lines in S, breaking at line boundaries.  Line breaks are not included in the resulting list unless keepends  is given and true.]
    #startswith [<type 'builtin_function_or_method'>] [S.startswith(prefix[, start[, end]]) -> bool    Return True if S starts with the specified prefix, False otherwise.  With optional start, test S beginning at that position.  With optional end, stop comparing S at that position.  prefix can also be a tuple of strings to try.]
    #strip [<type 'builtin_function_or_method'>] [S.strip([chars]) -> string or unicode    Return a copy of the string S with leading and trailing  whitespace removed.  If chars is given and not None, remove characters in chars instead.  If chars is unicode, S will be converted to unicode before stripping]
    #swapcase [<type 'builtin_function_or_method'>] [S.swapcase() -> string    Return a copy of the string S with uppercase characters  converted to lowercase and vice versa.]
    #title [<type 'builtin_function_or_method'>] [S.title() -> string    Return a titlecased version of S, i.e. words start with uppercase  characters, all remaining cased characters have lowercase.]
    #translate [<type 'builtin_function_or_method'>] [S.translate(table [,deletechars]) -> string    Return a copy of the string S, where all characters occurring  in the optional argument deletechars are removed, and the  remaining characters have been mapped through the given  translation table, which must be a string of length 256 or None.  If the table argument is None, no translation is applied and  the operation simply removes the characters in deletechars.]
    #upper [<type 'builtin_function_or_method'>] [S.upper() -> string    Return a copy of the string S converted to uppercase.]
    #zfill [<type 'builtin_function_or_method'>] [S.zfill(width) -> string    Pad a numeric string S with zeros on the left, to fill a field  of the specified width.  The string S is never truncated.]
def is_even(x):
    return x != ''


def _lktest():
    x = "abc"
    print(x)
#     laok.dump_description_help(x)
    index= x.find("a")
    print(index)
    
    if "a" in x:
        print "contain"
        
    keyword = "营业总收入单季同比"
    compare_str = '单季|单季度|同比|环比'
    laok.dump_description_help(re)
    
    m=re.search(compare_str,keyword)
    print(m.group())
    all = re.findall(compare_str,keyword)
    print(all[1])
    if re.search(compare_str,keyword):
        print "OK"
    spli = re.split(compare_str,keyword)
    sp = filter(is_even,spli)
    print(sp)
    for s in set(sp):
        print(s)
#     bt = 'bat|bet|bit'
#     m = re.match(bt,'bat')
#     if m is not None:
#         print m.group()
#     print '1>>>>>>>>>>>>>>'
#     
#     
#     m = re.match(bt,'blt')
#     if m is not None:
#         print m.group()
#     print '2>>>>>>>>>>>>>>'
#     
#     
#     m = re.match(bt,'He bit me!')
#     if m is not None:
#         print m.group()
#     print '3>>>>>>>>>>>>>>'
#     
#     
#     m = re.search(bt,'He bit me!')
#     if m is not None:
#         print m.group()
#     print '4>>>>>>>>>>>>>>'
#     
#     text = u'\xe9\x95\xbf\xe5\x9f\x8e'
#     text = text.encode('unicode-escape')
#     print(text)
#     text = text.decode('string-escape')
#     print(text)
#     text = text.decode("utf-8")
#     print(text)
    
#     m = ' jafefefe '
#     minfo = m.strip()
#     print minfo
    
    keyword = "单季度净利润"
    str = "单季度"
    index1=keyword.find(str)
    print index1
    index2 = keyword.rfind(str)
    print index2
    
    one = ' '.join(['r','i'])
    print(one)
    print("%s return error code is %s" % (one,one))

if __name__ == '__main__':
    laok.lktest_run()#catch_except = True