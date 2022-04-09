class OrderedStream:

    def __init__(self, n: int):
        self.iter = 0
        self.order_list = [None]*n


    def insert(self, idKey: int, value: str) -> list[str]:

        self.order_list[idKey-1] = value

        res = []
        n = len(self.order_list)

        #print(self.order_list)

        while self.iter < n:
            if (self.order_list[self.iter] != None):
                res.append(self.order_list[self.iter])
                self.iter+=1
            else:
                break

        return res


def main():

    order = OrderedStream(5)
    print(order.insert(3, "ccccc"))
    print(order.insert(1, "aaaaa"))
    print(order.insert(2, "bbbbb"))
    print(order.insert(5, "eeeee"))
    print(order.insert(4, "ddddd"))


    

if __name__ == "__main__":
    main()

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)