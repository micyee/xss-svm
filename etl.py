import re



def get_len(url):
    return len(url)

def get_url_count(url):
    if re.search('(http://)|(https://)', url, re.IGNORECASE) :
        return 1
    else:
        return 0

def get_evil_char(url):
    return len(re.findall("[<>,\'\"]", url, re.IGNORECASE))

def get_evil_word(url):
    return len(re.findall("(alert)|(script)|(%3c)|(%3e)|(%20)|(onerror)|(onload)|(eval)|(src=)|(prompt)",url,re.IGNORECASE))



def etl(filename):
    try:
        file_object = open(filename)
        for line in file_object:
            f1=get_len(line)
            f2=get_url_count(line)
            f3=get_evil_char(line)
            f4=get_evil_word(line)
            if f3 > 0:
                print line
    finally:
        file_object.close( )


etl('xss-200000.txt')
#etl('good-xss-200000.txt')