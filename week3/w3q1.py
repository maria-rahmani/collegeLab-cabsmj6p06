
prices = input("Enter list of numbers: ")
print(prices)
updatedPrices = list(map(float, prices.split()))

print("SUM = ", sum(updatedPrices))

product = 1
for i in updatedPrices:
    product *= i

print("PRODUCT = ", product)
print("AVERAGE = ", sum(updatedPrices)/len(updatedPrices))
