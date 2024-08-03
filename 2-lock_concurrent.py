import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance) -> None:
        self.balance = balance


def draw(account, amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            print(threading.current_thread().name, "success")
            account.balance -= amount
            print(threading.current_thread().name, "amount: ", account.balance)
        else:
            print(threading.current_thread().name, "error")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 600))

    ta.start()
    tb.start()
