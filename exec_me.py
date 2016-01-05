#!/usr/bin/env python3

import utils

print("Let's fetch data from Typicode!")

user_id = int(input("Enter your user_id: "))

result = utils.fetch_to_table(user_id)

print("Done!\n")
print(result)
