#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)
        rating = data.get("rating")
        if rating is not None:
            print(f"{int(float(rating))}\t1")
    except:
        continue
