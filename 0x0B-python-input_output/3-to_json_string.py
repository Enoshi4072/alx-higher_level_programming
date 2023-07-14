#!/usr/bin/python3

import json
""" Returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    """ Utilization of the dumps function for conversion """

    j_string = json.dumps(my_obj)
    return j_string
