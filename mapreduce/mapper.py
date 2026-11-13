#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        product = data.get("parent_asin") or data.get("asin")
        rating = data.get("rating")

        if product and rating is not None:
            print(f"{product}\t{float(rating)}")
    except:
        continue
