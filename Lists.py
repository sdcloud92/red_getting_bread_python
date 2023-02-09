# List is a "Data Structure" = a way of organising and storing data in 
# eg a = 3

# storing group data:
# Storing order data 

# List code

# fruit = []

# fruits = [item1, item2]

# fruits = ["cherry", "apple", "pear"]

states_america = ["New York", "virginia", "California", "Florida", "Pennsylvania", "New Jersey", "Tennesse"]
# print(states_america)

# EG lets say we need an order of which the states joined the union
print(states_america[0])

print(states_america[-1]) #COUNTS FROM THE END OF THE LIST

#How to change items in a list
states_america[-1] = "Tunassesey"
print (states_america)

#How to add to the list
states_america.append("Shomarriland") #Adds single item to the end of the list
print(states_america)

states_america.extend(["New Mexico", "Arizona", "Hawaii", "Utah"]) #Adds a whole bunch of items to list
print(states_america)






