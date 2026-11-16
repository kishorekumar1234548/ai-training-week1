prices = [500, 1200, 800, 2500, 300]

# 1. Apply Discount Function
def apply_discount(price, discount=10):
    return price - (price * discount / 100)


print("Discount 10%:", apply_discount(1000))
print("Discount 25%:", apply_discount(1000, 25))


# 2. Total Function using *args
def total(*args):
    return sum(args)


print("Total:",  total(5, 10, 15))


# 3. Describe Function using **kwargs
def describe(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print("\nDescription:")
describe(name="kishore", age=29, city="Chennai")  


# 4. List Comprehension - Prices Above 1000
above_1000 = [price for price in prices if price > 1000]

print("\nAbove 1000:", above_1000)

# 5. Map() with Lambda - Add 18% GST
with_gst = list(map(lambda price: round(price * 1.18, 2),prices))

print("With GST:", with_gst)


# 6. Filter() - Prices Below 1000
below_1000 = list(filter(lambda price: price < 1000, prices))

print("Below 1000:", below_1000)

