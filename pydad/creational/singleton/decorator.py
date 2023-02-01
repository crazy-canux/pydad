def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            print("do once")
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass(object):
    def __init__(self, *args, **kwargs):
        print("do init")


if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1, obj2)
