print("hello")
#datatypes
age=18
print(type(age))
my_list=[12,"OneTeam",[3,'Kochi',17],23]
print(my_list[2][1])   #  Output --> Kochi
my_list=[12,"OneTeam",9,23]
my_list[2]="Kochi"
print(my_list)


t=("Python",7,"Ebin",56)

# t[1]=89   --->  Error because tuple is immutable 

s={67,"Python",12,"Ebin",9,12,'Dell'}
print(s)