# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

v = set()
v.add(20)
v.add(20.0)
v.add('20')
print(v.__len__())
# The length of this Set will be 2