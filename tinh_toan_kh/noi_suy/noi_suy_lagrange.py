from scipy.interpolate import lagrange
x = [1,5]
y = [3,6]
result = lagrange(x, y)
print("ham noi suy lagrange: ")
print(result)