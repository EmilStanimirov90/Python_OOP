n = input()
qty_max = 0
qty_min = 0
qty_ideal = 0
qty_legal_range = 0
max_size = 22.05
min_size = 21.75
requested = 21.90
total_entries = 0
qty_above_req = 0
qty_below_req = 0
qty_exact_req= 0

while n != "end":
    n = float(n)
    if n > max_size:
        qty_max += 1
    elif n < min_size:
        qty_min += 1
    else:
        qty_legal_range += 1

    if max_size >= n > requested:
        qty_above_req +=1
    elif min_size <= n < requested:
        qty_below_req += 1
    elif n == requested:
        qty_exact_req += 1


    if min_size <= n <= requested:
        qty_ideal += 1

    total_entries += 1
    n = input()
print(f"Requested size by client {requested:.2f}mm")
print(f"Cork items above {requested:.2f}mm - {qty_above_req}")
print(f"Cork items below {requested:.2f}mm - {qty_below_req}")
print(f"Cork items exactly {requested:.2f}mm - {qty_exact_req}")
print(f"Ideal size (between {min_size}-{requested:.2f} mm) - {qty_ideal}")
print()

print(f"Above the Maximum size({max_size}mm) - {qty_max}")
print(f"Below the Minimum size({min_size}mm) - {qty_min}")
print(f"Total correct size according to clients specs - {qty_legal_range}")
print(f"Measured quantity: {total_entries}")
