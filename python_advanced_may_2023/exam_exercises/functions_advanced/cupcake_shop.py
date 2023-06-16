from collections import deque


def stock_availability(cupcakes, command, *info):
    cupcakes = deque(cupcakes)

    def remove_from_list(n):
        for _ in range(n):
            cupcakes.popleft()

    def remove_flavours():
        if el in cupcakes:
            for i in range(cupcakes.count(el)):
                cupcakes.remove(el)

    if command == "delivery":
        cupcakes.extend(info)

    if command == "sell":
        if info:
            for el in info:
                el = str(el)

                if el.isdigit():
                    remove_from_list(int(el))
                else:
                    remove_flavours()
        else:
            cupcakes.popleft()

    return list(cupcakes)


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
