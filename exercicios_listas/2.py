temperaturas = [0, 10, 20, 30, 40]
fahrenheit = [((temp * 9/5) + 32) for temp in temperaturas]

print('celsius:    ', *temperaturas)
print('fahrenheit: ', *fahrenheit)
