import re

content = "Xiaoshuaib has 100 bananas"
#贪婪匹配
res = re.match('^X.*(\d+).*$', content)
print(res)
print(res.group(1))
#非贪婪匹配
res = re.match('^X.*?([0-9]+).*$', content)
print(res)
print(res.group(1))