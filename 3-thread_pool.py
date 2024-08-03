from concurrent.futures import ThreadPoolExecutor, as_completed


with ThreadPoolExecutor() as pool:

    # map函数，简单，注意map的结果和入参是顺序对应的
    results = pool.map(craw, urls)

    for result in results:
        print(result)

    # 第二种 future模式，更强大
    futures = [pool.submit(craw, url) for url in urls]

    for future in futures:
        print(future.result())

    # as_completed 顺序是不固定的
    for future in as_completed(futures):
        print(future.result())

    # 用字典对应保存
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    for future in as_completed(futures):
        url = futures[future]
        print(url, future.result())
