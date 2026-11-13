#!/usr/bin/env python3
import sys

current_product = None
total = 0
count = 0

for line in sys.stdin:
    product, rating = line.strip().split("\t")

    if current_product != product:
        if current_product is not None:
            print(f"{current_product}\t{count}\t{total/count:.2f}")

        current_product = product
        total = 0
        count = 0

    total += float(rating)
    count += 1

if current_product is not None:
    print(f"{current_product}\t{count}\t{total/count:.2f}")
