import copy

def create_inventory():
    return [
        {
            "items": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"name": "Dell", "rating": 4.5}
            }
        },
        {
            "items": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"name": "Samsung", "rating": 4.2}
            }
        }
    ]

def apply_discount(data, roll):
    index = roll % len(data)
    for i in range(len(data)):
        data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.9)
        if i == index:
            data[i]["details"]["stock"] -= 5
            data[i]["details"]["supplier"]["rating"] += 0.1

def compare_data(original, modified):
    changed = 0
    unchanged = 0
    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1
    return (changed, unchanged)

roll = 24110011545

original = create_inventory()
backup = copy.deepcopy(original)

shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

apply_discount(shallow_copy, roll)
apply_discount(deep_copy, roll)

print("\n---- ORIGINAL INVENTORY ----")
for i, item in enumerate(original):
    print(f"{i} -> {item}")

print("\n---- SHALLOW COPY ----")
for i, item in enumerate(shallow_copy):
    print(f"{i} -> {item}")

print("\n---- DEEP COPY ----")
for i, item in enumerate(deep_copy):
    print(f"{i} -> {item}")

shallow_result = compare_data(backup, shallow_copy)
deep_result = compare_data(backup, deep_copy)

print("\n---- DIFFERENCES ----")
print(f"Shallow Copy : {shallow_result}")
print(f"Deep Copy : {deep_result}")

print("\n---- EXPLANATION ----")
print("Shallow copy shares nested objects, so original data also gets affected.")
print("Deep copy creates a completely separate structure, so original data stays unchanged.")