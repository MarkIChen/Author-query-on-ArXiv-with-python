import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

author = input('input author: ')
author = re.sub(' ', '+',author.strip())

# author = 'Ian+Goodfellow'
# author = 'Jan+Kautz'
page = 0

pattern_year = 'originally announced</span>[\s\S]*?</p>'

# Find all elements
result = []
while(True):
    url = "https://arxiv.org/search/?query=" + author + "&searchtype=author&start=" + str(page)
    content = urllib.request.urlopen(url)
    html_str = content.read().decode('utf-8')

    temp = re.findall(pattern_year, html_str)
    if (len(temp) == 0):
        break
    else :
        result.extend(temp)
        page = page + 50

print('No. of result: '+str(len(result)))

d = dict()
for r in result:
    info = r.split("originally announced</span> ")[1].split("</p>")[0].strip()
    year = re.search('[0-9][0-9][0-9][0-9]', info)
    # print(year.group(0))
    key = year.group(0)
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print(d)

x = list(d.keys())
x.reverse()
y = list(d.values())
y.reverse()

plt.bar(x, y, align = 'center',alpha =1)
plt.yticks(np.arange(0, max(d.values())+ 1, 1))
plt.title('Papers been published each year')
plt.ylabel('number of papers')
plt.show()