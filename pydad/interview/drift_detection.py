#!/usr/bin/env python3

def drift(expected, actual: dict) -> dict:
    missing = [name for name in expected if name not in actual]
    extra = [name for name in actual if name not in expected]
    modified = {
        k: (expected[k], actual[k])
        for k in expected
        if k in actual and expected[k] != actual[k]
    }
    return {
        "missing": missing,
        "extra": extra,
        "modified": modified
    }


if __name__ == "__main__":
    expected = {"nginx": "1.18", "redis": "6.2"}
    actual = {"nginx": "1.20", "mysql": "8.0"}
    print(drift(expected, actual))