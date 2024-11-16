friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

cats = {"Bob", "Rolf", "Anne"}
dogs = {"Charlie", "Bob", "Frankie"}
animals = cats.union(dogs)
print(animals)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)