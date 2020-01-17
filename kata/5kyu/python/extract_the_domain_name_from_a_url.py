import re


def domain_name(url):
    return re.search(r'(https?\:\/\/(www.)?|www.)?(.*?)\.', url).group(3)
