#!/usr/bin/python3
""" Returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """ Utilization of the dumps function for conversion """

    j_string = json.dumps(my_obj)
    return j_string
