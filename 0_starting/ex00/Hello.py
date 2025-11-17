ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "UAE")

# You'll have to remove the element from the set, and add a new element with that value updated.
# That's because sets use hashing to efficiently eliminate duplicates.
# If mutating the elements directly was allowed you'd break this model.
# without the sqare brackets update treats the string as a list of letters, update takes only iterable objects
ft_set.remove("tutu!")
ft_set.update(["Abu Dhabi"])

ft_dict["Hello"]= "42AbuDhabi"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)