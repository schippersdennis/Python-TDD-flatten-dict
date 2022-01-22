from hashlib import new
from pytest import Instance


def get_none():
    pass


def flatten_dict(dict2, item=[]):
    for key, value in dict2.items():
        if isinstance(value, dict):
            flatten_dict(value, item)
        else:
            item.append(value)
    return item


