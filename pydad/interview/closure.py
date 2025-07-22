def outer():
    # data = []
    v1 = 10
    def inner(value):
        # data.append(value)
        nonlocal v1
        v1 += 1
        # return data
        return v1
    return inner

if __name__ == "__main__":
    call = outer()
    print(call(1))
    print(call(2))
