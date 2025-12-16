ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

country_name = "UAE!"
city_name = "AbuDhabi!"
campus_name = "42AbuDhabi!"

# modify the list to hello world
ft_list[1] = "World!\t"

# modify the tuple to hello country_name
ft_tuple = (ft_tuple[0], country_name)

# modify the set to remove tutu! and add city_name
ft_set.remove("tutu!")
ft_set.update([city_name])

# modify the dict to change the value of hello to campus name
ft_dict["Hello"] = campus_name

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
