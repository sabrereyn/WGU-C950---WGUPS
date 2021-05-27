# Hashtables have a space complexity of O(n)
class ChainingHashTable:
    def __init__(self, list_length):
        """ Constructor

        Passes passed in parameter to LargestPrimeFactor function for hash table's capacity
        Then assigns all buckets with empty list.

        :param list_length: length of a list
        """
        self.table = []
        initial_capacity = int(LargestPrimeFactor(list_length))
        for i in range(initial_capacity):
            self.table.append([])

    def Get_Bucket_List(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list

    def insert(self, key, package):
        """ Insert package into the hash table.

        Time complexity of O(1)

        :param key: Key to find specific value
        :param package: Value
        :return: true when value is inserted
        """

        # Get bucket list
        bucket_list = self.Get_Bucket_List(key)

        # insert the item to the end of the bucket list
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    def update(self, key, value):
        """ Update value in hashtable.

        Time complexity of O(1)

        :param key: Key to find specific value
        :param value: Value
        :return: true when value is updated
        """
        bucket_list = self.Get_Bucket_List(key)  # get the bucket list where this key would be.

        # Search for key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

    # Searches for an item with matching
    def search(self, key):
        """ Searches for a value with matching key

        Time complexity of O(1)

        :param key: The key to find a specific value with
        :return: None if value couldn't be found or the value itself
        """

        bucket_list = self.Get_Bucket_List(key)  # get the bucket list where this key would be.

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]  # value
        return None


def LargestPrimeFactor(num):
    """Calculate greatest prime factor using length of list

    It is best practice to use greatest prime factor for hash table's
    capacity. This method calculates the greatest prime factor using the
    int passed in and returns the prime integer.

    :param num: length of list
    :return: prime number for hashtable capacity
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