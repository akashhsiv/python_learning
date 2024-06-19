squares =[value**2 for value in range(1, 11)]
print(squares)
squares = []
for value in range(1,11):
    squares.append(value**3)
dimensions =(200,50)
print(dimensions[0])
print(dimensions[1])
dimensions = (400,20)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,200,130)
print("\nmodified dimensions:")
for dimension in dimensions:
    print(dimension)
    