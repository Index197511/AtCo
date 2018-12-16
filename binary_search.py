import bisect

li = [1, 9, 15, 32]
x = 15

print (bisect.bisect_left(li, x))
# => 2

print (bisect.bisect_right(li, x))
# => 3
