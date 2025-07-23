import bisect

my_list = [2, 4, 6]
x = 4

idx_left  = bisect.bisect_left(my_list, x)
idx_right = bisect.bisect_right(my_list, x)
print(idx_left)
print(idx_right)