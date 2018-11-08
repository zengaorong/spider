# a = {"A":"123","B":"456"}
#
# for key in a:
#     if key == "A":
#         del a[key]
#
# print a

a={'a':1,'b':2,'c':3}
print a.keys()
for k in list(a.keys()):
    if a[k]>2:
        del a[k]

print a