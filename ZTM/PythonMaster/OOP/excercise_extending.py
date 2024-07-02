# Create a superlist
class SuperList(list):  # Inheritance is from the built in object list
    def __len__(self):
        return 1000
    
    def show_list(self):
        return self.list
    
super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

print(issubclass(SuperList,list))