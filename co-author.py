import urllib.request
import re

author = input('input author: ')
author = re.sub(' ', '+',author.strip())


page = 0

pattern_coauthor = "<span class=\"search-hit\">Authors:</span>[\s\S]*?</p>"

# Find all elements
result = []
while(True):
    url = "https://arxiv.org/search/?query=" + author + "&searchtype=author&start=" + str(page)
    content = urllib.request.urlopen(url)
    html_str = content.read().decode('utf-8')

    temp = re.findall(pattern_coauthor, html_str)
    if (len(temp) == 0):
        break
    else :
        result.extend(temp)
        page = page + 50



count = 0
d = dict()
for r in result:
    info = r.split("<span class=\"search-hit\">Authors:</span>")[1].split("</p>")[0].strip()
    
    pattern_indiv = "(\">(.+)<\/a>)"
    all_author = re.findall(pattern_indiv, info)

    count = count + 1

    for co_author in all_author:
        key = co_author[1].strip()
        
        if key != author:
            if key in d:
                d[key] += 1
            else:
                d[key] = 1

    
for key,value in sorted(d.items()):
    print("[" + key + "]:"+ str(value) +" times")