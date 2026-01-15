ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set= {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# work like a array, but alow to store multiple types
ft_list[1] = "World!"

# tupples are immutable, here we reuse the reference to create a new object
ft_tuple = ("Hello", "Portugal!") 

# clear set, to re-define in different order.
# set's are unordered, but it's values are unique
ft_set = set()
ft_set.add("Porto!")
ft_set.add("Hello")

# ditionaries work as a std::map
ft_dict["Hello"] = "42Porto!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
