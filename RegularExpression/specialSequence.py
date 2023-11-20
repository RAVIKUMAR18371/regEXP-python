import re
a="harry potter"
match=re.search(r"\Apot",a)
print(match)
#output--->None--> because it is not starting with "pot"

match=re.search(r"\Ahar",a)
print(match)
#output---->   <re.Match object; span=(0, 3), match='har'>

match=re.search(r"\Ah",a)
print(match)
#output--->  <re.Match object; span=(0, 1), match='h'>

match=re.search(r"\bh",a)
print(match)
#output----><re.Match object; span=(0, 1), match='h'>--> use of --> \b