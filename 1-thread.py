import threading


def do_craw(a, b):
    print(a, b)


def my_func(a, b):
    do_craw(a, b)


if __name__ == "__main__":

    # 传递函数名，对应参数用 元组传递，如果只有一个参数，用 (arg, ) 表示
    t = threading.Thread(target=my_func, args=(100, 200))

    t.start()

    t.join()
