class ChainingHashTable:
    # Constructor, takes in parameter of length of list
    # Then pass the length to LargestPrimeFactor function for hash table's capacity
    # Then assigns all buckets with empty list.
    def __init__(self, list_length):
        self.table = []
        initial_capacity = int(LargestPrimeFactor(list_length))
        for i in range(initial_capacity):
            self.table.append([])

    # Insert package into the hash table
    def insert(self, key, package):
        # Get bucket list
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None


def LargestPrimeFactor(num):
    """Calculate greatest prime factor using length of list

    It is best practice to use greatest prime factor for hash table's
    capacity. This method calculates the greatest prime factor using the
    int passed in and returns the prime integer.
    """
    p_factor = 1
    i = 2

    while i <= num / i:
        if num % i == 0:
            p_factor = i
            num /= i
        else:
            i += 1

    if p_factor < num:
        p_factor = num

    return p_factor
