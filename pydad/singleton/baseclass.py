import threading


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        print("call new")
        if not hasattr(cls, '_instance'):
            print("do once")
            Singleton._instance = super().__new__(cls, *args, **kwargs)
        return Singleton._instance


class SingletonWithLock(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        print("call new")
        if not hasattr(cls, '_instance'):
            print("do once")
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton._instance = super().__new__(cls, *args, **kwargs)
        return Singleton._instance

    def __init__(self, *args, **kwargs):
        print("call base init")


def task(arg):
    obj = SingletonWithLock()
    print(obj)


class MyClass(Singleton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("call my init")


if __name__ == "__main__":
    # obj1 = MyClass()
    # obj2 = MyClass()
    # print(obj1, obj2)

    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1, obj2)

    # for i in range(10):
    #     t = threading.Thread(target=task, args=[i, ])
    #     t.start()
