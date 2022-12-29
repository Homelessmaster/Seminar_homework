with open('2Project_1file.txt', 'r') as data:
    firstPolynomial = data.read()

with open('2Project_2file.txt', 'r') as data:
    secondPolynomial = data.read()

print(firstPolynomial, secondPolynomial)

firstPolynomial = firstPolynomial.split(' = 0')

resultPolynomial = firstPolynomial[0] + " + " + secondPolynomial

print('')
print(resultPolynomial)