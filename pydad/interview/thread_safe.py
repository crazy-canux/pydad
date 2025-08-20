import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance
        
def draw(account, amount):
    with lock:
        if account.balance >= amount:
            # time.sleep(1)
            print(threading.current_thread().name, "draw succeed")
            account.balance -= amount
            print(threading.current_thread().name, "new balance:", account.balance)
        else:
            print(threading.current_thread().name, "draw failed, insufficient balance")
        
if __name__ == "__main__":
    account = Account(1000)
    threads = [
        threading.Thread(target=draw, args=(account, 800))
        for i in range(10)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()