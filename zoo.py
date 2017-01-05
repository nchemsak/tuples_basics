# Create a tuple named zoo that contains your favorite animals.
zoo = ("lions", "tigers", "bears")
print(zoo)
# Find one of your animals using the .index(value) method on the tuple.
zoo.index("tigers")

print(zoo.index("tigers"))

# Determine if an animal is in your tuple by using "for value in tuple"
for animal in zoo:
    if animal == "bears":
        print(animal)

# Create a variable for each of the animals in your tuple with this cool feature of Python.

# example
# (lizard, fox, mammoth) = zoo
# print(lizard)
(lions, tigers, bears) = zoo
print(tigers)

# Convert your tuple into a list.
zoo=list(zoo)
print(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(["snakes", "badgers", "narwhal"])
print(type(zoo))
print(zoo)

# Convert the list back into a tuple.
zoo=tuple(zoo)
print(type(zoo))
print(zoo)
