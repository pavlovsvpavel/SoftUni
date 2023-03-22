import re

count_barcodes = int(input())
regex = r"@\#+(?P<product>[A-Z][A-Za-z\d]{4,}[A-Z])@\#+"
for _ in range(count_barcodes):
    barcode = input()
    match = re.findall(regex, barcode)
    if not match:
        print("Invalid barcode")
        continue
    product_group = ""
    valid_barcode = "".join(match)
    for char in valid_barcode:
        if char.isdigit():
            product_group += char
    if not product_group:
        product_group = "00"
    print(f"Product group: {product_group}")
