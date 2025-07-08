#!/usr/bin/python3

def process(value):
    """ process the value == <key name>=<value>"""
    if '=' not in value:
        return None, None

    data = value.split('=', 1)
    key = data[0]
    value = data[1]
    if value[0] == '"' and value[-1] == '"':
        value = value[1: -1].replace('\\"', '\"')
        value = value.replace("_", " ")
    elif '.' in value:
        try:
            value = float(value)
        except ValueError:
            pass
    else:
        try:
            value = int(value)
        except ValueError:
            pass
    return key, value
