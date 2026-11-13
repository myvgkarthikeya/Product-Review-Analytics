#!/usr/bin/env python3
import sys

current_rating = None
count = 0

for line in sys.stdin:
    rating, value = line.strip().split("\t")
    value = int(value)

    if current_rating != rating:
        if current_rating is not None:
            print(f"{current_rating}\t{count}")
        current_rating = rating
        count = 0

    count += value

if current_rating is not None:
    print(f"{current_rating}\t{count}")
