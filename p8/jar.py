class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.cookies = 0
        self.capacity = capacity



    def __str__(self):
        return self.cookies*"🍪"

    def deposit(self, n):
        self.cookies = self.cookies + n
        if self.cookies > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.cookies = self.cookies - n
        if 0 > self.cookies:
            raise ValueError

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


    @property
    def size(self):
        return self.cookies





def main():
    jar = Jar(int(input("capacity: ")))
    jar.deposit(int(input("deposit: ")))
    jar.withdraw(int(input("withdraw: ")))
    for i in range(jar.size):
        print("🍪", end="")
    print()

if __name__ == "__main__":
    main()