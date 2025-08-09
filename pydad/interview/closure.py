def outer(arg):
    print("outer called")
    v1 = arg
    print(f"outer v1: {v1}")
    def inner(value):
        nonlocal v1
        print("inner called: ", v1)
        v1 += 1
        print(f"inner v1: {v1}")
        return v1
    return inner

if __name__ == "__main__":
    call = outer(10)
    print(call(1))
    print(call(2))
