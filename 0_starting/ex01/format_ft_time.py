import time

seconds = time.time()

#print(seconds)

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")

"""
:, - adds comma as thousand separator
:.2f - fixed point with 2 decimal places
:.2e - scientific notation with 2 decimal places
:>10 - right align in 10 character width
:0>5 - pad with zeros (00123)
"""

# convert seconds to a struct
time_struct = time.localtime(seconds)

#print(time_struct)

# print struct
# print(time_struct)

# b - locale month abreviated
# d - day as decimal
# Y - year as decimal
str_time = time.strftime("%b %d %Y", time_struct)

print(str_time)


