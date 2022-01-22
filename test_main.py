from main import get_none, flatten_dict


def test_get_none():
    assert get_none() == None


def test_flatten_dict():
    assert (
        flatten_dict(
            {
                "a": {"inner_a": 42, "inner_b": {"a": 1, "b": 2, "c": {"a": 1000}}},
                "b": 3.14,
                "c": {"a": 2000, "b": {"a": 30000, "b": 150}},
            }
        )
        == [42, 1, 2, 1000, 3.14, 2000, 30000, 150]
    )
