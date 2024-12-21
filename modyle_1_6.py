my_dict = { "Михаил": 1997,"Никита":1988,"Анна":2010}
print(my_dict)
print(my_dict["Анна"])
my_dict["Андрей"]=1962
print(my_dict["Андрей"])
my_dict.update({"Юра":1963, "Сергей": 1967})
print(my_dict.get("Сергей"))
print(my_dict.get("Елена"))
a = my_dict. pop("Никита")
print(a)
print(my_dict)

my_set_={1,2,3,'a','c',2,4,1,'a','b','c'}
print(my_set_)
my_set_.add(8)
my_set_.discard(1)
print(my_set_)