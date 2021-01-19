class Person :
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age      = age
        
    def intro(self): # class içinde olduğundan self referansının verilmesi gereklidir.
        print("Hello there. I am ", self.firstName)
        
        
person1 = Person('Hamza','Yüksel',19)

print(person1.firstName)

print(person1.lastName)

person1.intro()


#### Inheritance(kalıtım): Classların birbirinden miras alması.
#### Self. == class için oluşturulan objelerin yerini almasını sağlar. xd = Personx() dediğimizde
#### xd objesinin self yerine geçmesi sağlanır.


class Personx :
    def __init__(self,fname,sname):
        self.firstName = fname
        self.surName = sname
        print("Person created")
    
    def who_am_i(self):
        print("I am a person!")



class Student(Personx):
    def __init__(self,fname,sname):
        Personx.__init__(self, fname, sname) ### Burası çokomelli.
        print("Student created.")

    def who_am_i(self):
        print("I am a student!")  ### temel class taki metod persondakini override etti.

s1=Student("almet", "yüksel")