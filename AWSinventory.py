# This code creates a list of services using Python

# 1) The list should be empty initially.

AWS_services = []

print (AWS_services)
print ("Hey, this list is empty. where are the AWS services???")

# 2) Populate the list 

AWS_services.insert(0, 'vpc')
AWS_services.insert(1, 'ec2')
AWS_services.insert(2, 'lambda')
AWS_services.insert(3, 'route53')
AWS_services.insert(4, 'cloudformation')

# print list

print (AWS_services)

# Print the list and the length of the list

print("This list is", len(AWS_services), "items long")

# Remove two specific services from the list by name or by index.

del AWS_services [1:3] # deletes values from 1-3

# Print the new list and the new length of the list.

print (AWS_services)

print("Oh no! This list is now", len(AWS_services), "items long")
