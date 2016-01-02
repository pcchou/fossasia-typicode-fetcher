#!/usr/bin/env python3

import utils
import pathlib
import os

print("Let's fetch data from Typicode!")

user_id = int(input("Enter your user_id: "))

with open("index.html", "w") as f:
    f.write(utils.fetch_to_table(user_id))

print("Done! View at: " + pathlib.Path(os.path.abspath("index.html")).as_uri())
