a = 10
b = 12.5
c = "python"
d = [1, 2, 3]
e = {"name": "kishore", "age": 29}
f = {1, 2, 3}
g = (10, 20, 30)

# Print values and their types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))

# 2. Sales data
sales = [12000, 0, 8500, 15000, -200, 9800]

total = 0
target = 30000

# 3. Process sales
for sale in sales:
    # Skip zero or negative values
    if sale <= 0:
        print("skipped invalid value" ,sale)
        continue
    # Add valid sales
    total += sale
    print("Added", sale, "total", total)
    # Stop when total exceeds target 
    if total> total:
        print("Target reached.Stoped at , total")

    # 4. Check tarket status 
    else:
        if total >= target:
            print("Target reached")
        else: 
            print("Target not reached")