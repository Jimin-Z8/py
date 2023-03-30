import codecs
import os, sys
import glob
import time
from datetime import datetime
from datetime import timedelta
import argparse

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

def end_of_article(line):
#    if (line == unicode("翻译：纽约时报中文网", "utf-8")):
#        return True
#    if (line == unicode("点击查看本文英文版。", "utf-8")):
#        return True
#    if (line == unicode("相关报道", "utf-8")):
#        return True
#    print("相关报道")
#    if (line == "相关报道")
#        return True
    if (-1 != line.find('翻译：纽约时报中文网')):
        return True
    if (-1 != line.find('点击查看本文英文版')):
        return True
    if (-1 != line.find('相关报道')):
        return True
    return False


# @file_name is a full path name
def handle_an_article(file_name):
    #file_name=sys.argv[1]
    print(file_name, "\n")
    if not os.path.exists(file_name) :
        print("file not exist")
        return

    #old_file_name = "old " + file_name
    old_file_name = file_name+"old"
    if os.path.isfile(old_file_name) :
        os.remove(old_file_name)
    os.rename(file_name, old_file_name)
    #file_name = "NYT_01.txt"
    #file_name_new = "new " + file_name
    file_name_new = file_name
    with codecs.open(file_name_new, 'w+', 'utf-8') as outstream:
        with codecs.open(old_file_name, 'r+', 'utf-8') as instream:
            for line in instream.readlines():
                #line = line.rstrip()
                line = line.strip()
                if (end_of_article(line)):
                    break
                if (line == '广告' or
                    line == '中文' or
                    line == '中英双语' or
                    line == '英文') :
                    #print(line)
                    continue
                if (len(line)):
                    #outstream.write(str(len(line)))
                    if (len(line) > 40) : 
                        outstream.write('\n')
                    outstream.write(line+'\n')
                #if is_chinese(line[0]):
                    #outstream.write("yes\n")
                    #pass
    os.remove(old_file_name)

# Handle one file copied from new york times cn web, largely adding blank lines between English and Chinese paragraphs.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest='file', default=r"C:\\x\\_NYTimes\\example.txt", required=False, type=str, action='store', help="which file to be handled.")
    args = parser.parse_args()
    #print(args)

    handle_an_article(args.file)
    time.sleep(3)

if __name__ == "__main__":
    sys.exit(main())
    