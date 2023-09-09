from person import Person
from graph import create_graph

# Objects of the Person class
person1 = Person("João", 30)
person2 = Person("João", 29)
person3 = Person("Maria", 22)
person4 = Person("Mariana", 29)
person5 = Person("Matheus", 22)
person6 = Person("John", 22)
person7 = Person("Gustavo", 19)

# A list containing all the objects
people = [person1, person2, person3, person4, person5, person6, person7]

# Loop to greet each person
for i in people:
    text = i.greet()
    print(text)

# Call the function to create a graph
create_graph(people)
