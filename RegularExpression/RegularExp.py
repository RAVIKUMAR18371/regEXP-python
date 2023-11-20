import re
a="ayushi@gmail.com"
match=re.search(r"\.",a)
print(match)
# output--><re.Match object; span=(12, 13), match='.'>

b="hello"
catch=re.search(r"[@]",a)
print(catch)
#output--><re.Match object; span=(6, 7), match='@'>

c="hello"
patch=re.search(r"[l]",a)
print(patch)
#output----><re.Match object; span=(11, 12), match='l'>

d="hello"
p=re.findall(r"[l]",d)
print(p)
# output---->['l', 'l']

R="ayushi@gmail.com"
v= re.search(r"^ayu",R)
print(v)
#output---><re.Match object; span=(0, 3), match='ayu'>
# ^ --------> means match from the beginning

N=re.search(r"^shi",R)
print(N)
#output---->None

T=re.search(r"com$",R)
print(T)
#output--><re.Match object; span=(13, 16), match='com'>

Look = "Ravikumarparasar"
G=re.findall(r"mar|avi",Look)
print(G)
#output--->['avi', 'mar']

#Here -->ren---> it is not present in LOOK
C=re.findall(r"avi|ren",Look)
print(C)

K = "charlie chchapman"
over=re.findall(r"ch?a",K)
print(over)
#output-->['cha', 'cha']
#  ? --->it means that 0 times or 1 times occurence it will show-->['cha', 'cha']

dock="charlie chachaplin"
cure=re.findall(r"ch*a",dock)
print(cure)
# --->['cha', 'cha', 'cha'] ---> it can be as number of times it is present

check = "xyz,xyyz,xxyyzz,xyxyzz,xxyzyy"
core=re.findall(r"xy+z",check)
print(core)
#---->['xyz', 'xyyz', 'xyyz', 'xyz', 'xyz']--> here y can be anynumber of times

checked="xyyyyzzz,xyxyxzz,xyzzzx,xyyxyyy,xxxyyxyxxz"
cow=re.findall(r"y{2,4}",checked)
print(cow)
#------>['yyyy', 'yy', 'yyy', 'yy']-->here y will get printed if it is in range from 2 to 4

chock="xyyyyzzz,xyxyxzz,xyzzzx,xyyxyyy,xxxyyxyxxz"
mat=re.findall(r"(x|z)yz",chock)
print(mat)
# output---> ['x'] here only one occurences in -->xyzzzx