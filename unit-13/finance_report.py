import math

sales = [125000, 98500, 143250, 110750]

total = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total / len(sales)
vat = total * 0.075
vat_payable = math.ceil(vat)

print("=== Quarterly Sales Report ===")
print(f"Total sales: NGN {total:,}")
print(f"Highest sale: NGN {highest:,}")
print(f"Lowest sale: NGN {lowest:,}")
print(f"Average sale: NGN {average:,.2f}")
print(f"VAT payable (7.5%, rounded up): NGN {vat_payable:,}")
