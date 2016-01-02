#!/usr/bin/env python3

import requests

def get_to_dict(user_id):
    if not (user_id > 0 and user_id <= 100):
        raise ValueError("user_id not allowed.")

    response = requests.get("http://jsonplaceholder.typicode.com/posts/" + str(user_id))
    return response.json()

def fetch_to_table(user_id):
    data = get_to_dict(user_id)
    return """<!DOCTYPE html>
    <html lang="en">

    <head>
        <title>""" + data["title"] + """</title>
    </head>

    <body>
        <h1>""" + data["title"] + """</h1>

        <p style=\"font-size: 16px; line-height: 1.2; color: #262626; font-family: \"Helvetica\",Helvetica,Arial,sans-serif; font-weight: 400;\">""" + data["body"] + """
        </p>
    </body></html>"""
