class HashData:
    """Represents a hash table that stores key/value pairs."""
    #  Initialize a list of 10 items
    def __init__(self, size=10):
        """Initialize the hash table with given size. Defaults size is `10`."""
        self.size: int = size
        self.table: list[None | int] = [None] * self.size
        self.lf_threshold: float = 0.7
        self.count = 0

    def hash_function(self, key: int) -> int:
        """Computes the hash.

        Args:
            key (int): The key to be hashed.

        Returns:
            int: The hash value.
        """
        return key % self.size

    def put(self, key: int) -> None:
        """Inserts a key into the hash table.

        For avoiding collisions the method uses the linear probing.

        Args:
            key (int): The key to be inserted into the hash table.
        """
        self.count += 1
        if self.count / self.size >= self.lf_threshold:
            self.rehash()

        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = key
        else:
            while self.table[index]:
                index = (index + 1) % self.size
            self.table[index] = key

    def rehash(self) -> None:
        """Rehashes the hash table by doubling its size and re-inserting the elements."""
        self.size = self.size * 2
        old_table = self.table
        self.table = [None] * self.size

        for key in old_table:
            if key is not None:
                self.put(key)

    def display(self) -> None:
        """Displays the current state of the hash table with indices and their values."""
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")


if __name__ == "__main__":
    hash1 = HashData()

    # keys
    keys = [int(x) for x in input().split(', ')]

    # apply hash function to each key
    for key in keys:
        hash1.put(key)
        print(hash1.count)

    hash1.display()
