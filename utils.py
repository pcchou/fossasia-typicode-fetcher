#!/usr/bin/env python3

import requests

def get_to_dict(user_id):
    if not (user_id > 0 and user_id <= 100):
        raise ValueError("user_id not allowed.")

    response = requests.get("http://jsonplaceholder.typicode.com/posts/" + str(user_id))
    return response.json()

def fetch_to_table(user_id):
    data = get_to_dict(user_id)
    return "Title: {0}\nText: {1}".format(data["title"], data["body"])
