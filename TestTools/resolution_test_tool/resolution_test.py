# -*- coding: utf-8 -*-
# @Time    : 2021-02-03 21:51
# @Author  : yingrinsing
# @File    : resolution_test.py

"""

功能说明

"""
from codecs import open
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



resolution480 = 480
resolution1920 = 1920
resolution1080 = 1080
resolution720 = 720
resolution1280 = 1280
resolution960 = 960
resolution540 = 540
resolution2160 = 2160 #4K 视频宽
resolution3840 = 3840 #4K 视频高



def read_csv(filename, delimiter=';'):
    """
        读取csv 格式的文件
        :filename:输入读文件的路径
        :return:
    """
    names = []
    with open(filename=filename, mode='r', encoding='utf-8-sig') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        for row in spam_reader:
            if not names:
                names = row
            else:
                assert len(names) == len(row), row
                val_dict = {
                    name if '.' not in name else name.replace('.', '_'): row[i]
                    for i, name in enumerate(names)
                }
                yield val_dict


def write_csv(filename, iter_data):
    u"""写入csv 格式的文件
    filename:输入写文件的路径
    iter_data:输入可迭代的字典
    """
    fmt_line = None
    with open(filename=filename, mode='w', encoding='utf8') as f:
        for data in iter_data:
            if not fmt_line:
                fmt_line = u",".join(u"{%s}" % k for k in data) + u'\n'
                f.write(fmt_line.replace('{', '').replace('}', ''))
            #             print(fmt_line.format(**data))
            f.write(fmt_line.format(**data))


def read_csv_lktest():
    iter_data = read_csv(u"../../文件读写/指标表元数据信息.csv")
    for i, data in enumerate(iter_data):
        print i, u" ".join(u"%s:%s" % item for item in data.iteritems())


def write_csv_lktest():
    iter_data = read_csv(u"../../文件读写/指标表元数据信息.csv")
    write_csv(u"../../文件读写/指标表元数据信息-write.csv", iter_data)


# 写文件

_cache_file = {}


def write_file(filename, msg):
    if filename not in _cache_file:
        _cache_file[filename] = open(filename, mode='a', encoding='utf-8')
    # print(filename)
    # _cache_file[filename].write(codecs.BOM_UTF8)
    _cache_file[filename].write("%s\n" % msg)
    _cache_file[filename].flush()


def min(x,y):
    return x if x<y else y

def max(x,y):
    return x if x>y else y

def is4K_old(videoWidth, videoHeight):
    width = min(videoWidth, videoHeight)
    height = max(videoWidth, videoHeight)
    if (width > (resolution1080 + (resolution2160 - resolution1080) / 2) and height > (
            resolution1920 + (resolution3840 - resolution1920) / 2)):
        return True
    return False

def is1080p_old(videoWidth, videoHeight):
    width = min(videoWidth, videoHeight)
    height = max(videoWidth, videoHeight)
    if((resolution720 + (resolution1080 - resolution720) / 2) < width  <= (
            resolution1080 + (resolution2160 - resolution1080) / 2) and (
            resolution1280 + (resolution1920 - resolution1280) / 2) < height <= (resolution1920 + (resolution3840 - resolution1920) / 2)) :
        return True
    return False

def is720p_old(videoWidth, videoHeight):
    width = min(videoWidth, videoHeight)
    height = max(videoWidth, videoHeight)
    if (resolution540 + (resolution720 - resolution540) / 2 < width<= (
        resolution720 + (resolution1080 - resolution720) / 2) and (
        resolution960 + (resolution1280 - resolution960) / 2) < height  <= (resolution1280 + (resolution1920 - resolution1280) / 2)) :
        return True
    return False

def is540p_old(videoWidth, videoHeight):
    if ((videoHeight <= resolution960 + (resolution1280 - resolution960) / 2 and
     videoWidth <= resolution540 + (resolution720 - resolution540) / 2) or
        (videoWidth <= resolution960 + (resolution1280 - resolution960) / 2 and
         videoHeight <= resolution540 + (resolution720 - resolution540) / 2)):
        return True
    return False

def is_resolution_old(videoWidth, videoHeight):
    if is540p_old(videoWidth, videoHeight):
        return '540p',8000000
    elif is720p_old(videoWidth, videoHeight):
        return '720p',11000000
    elif is1080p_old(videoWidth, videoHeight):
        return '1080p',20000000
    elif is4K_old(videoWidth, videoHeight):
        return '4k',110000000
    else:
        return 'other',videoHeight * videoWidth * 3 * 4

def isBelow720p(videoWidth, videoHeight):

    if videoHeight <= resolution1280 and videoWidth <= resolution1280:
        return True
    return False

def getNearLeast4k():
    return (resolution3840 * resolution2160 + resolution1920 * resolution1080) / 2


def is4K(videoWidth, videoHeight):
    allPixelCurrent = videoHeight * videoWidth
    return allPixelCurrent >= getNearLeast4k()

def getNearLeast1080P():
    return (resolution1920 * resolution1080 + resolution1280 * resolution720) / 2

  #
  # /**
  #  * 面积法用于判断是否支持1080P，用于获取码率档位，较为合适
  #  */
def is1080p(videoWidth, videoHeight):
    allPixelCurrent = videoHeight * videoWidth
    return  getNearLeast1080P() <= allPixelCurrent < getNearLeast4k()


def getNearLeast720P():
    return (resolution1280 * resolution720 + resolution960 * resolution540) / 2

  # /**
  #  * 面积法用于判断是否支持720P，用于获取码率档位，较为合适
  #  */
def is720p(videoWidth, videoHeight):
    allPixelCurrent = videoHeight * videoWidth
    return getNearLeast720P() <= allPixelCurrent < getNearLeast1080P()


   #
   # * 面积法用于判断是否支持540P，用于获取码率档位，较为合适
   # */
def is540p(videoWidth, videoHeight):
    allPixelCurrent = videoHeight * videoWidth
    return allPixelCurrent < getNearLeast720P()

def is_resolution(videoWidth, videoHeight):
    if is540p(videoWidth, videoHeight):
        return '540p', 8000000
    elif is720p(videoWidth, videoHeight):
        return '720p', 11000000
    elif is1080p(videoWidth, videoHeight):
        return '1080p', 20000000
    elif is4K(videoWidth, videoHeight):
        return '4k', 110000000
    else:
        return 'other', -1

if __name__ == '__main__':
    a= 1296
    b = 480
    print(is_resolution(a,b))
    print(is_resolution_old(a, b))
    iter_resolution = read_csv('导入分辨率.csv', ',')
    fmt_line = False
    filename = '../../文件读写/result.csv'
    header = 'width,height,is_resolution_new,is_resolution_old,result,malv_new,malv_old,result1\n'
    with open(filename=filename, mode='w', encoding='utf8') as f:
        for data in iter_resolution:
            if not fmt_line:
                f.write(header)
                fmt_line = True
            new_data=[]
            width = int(data['width'])
            height =int(data['height'])
            resolution_new,malv_new = is_resolution(width, height)
            resolution_old,malv_old = is_resolution_old(width, height)
            result = 'same' if resolution_new == resolution_old else 'different'
            new_data.append(str(width))
            new_data.append(str(height))
            new_data.append(resolution_new)
            new_data.append(resolution_old)
            new_data.append(result)
            new_data.append(str(malv_new))
            new_data.append(str(malv_old))
            new_data.append('yes' if malv_new < malv_old else 'no')
            f.write(','.join(new_data)+"\n")



    # print(a*b)
    # print(getNearLeast720P())
    # print(getNearLeast1080P())
    # print(getNearLeast4k())

