class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Create a dictionary to store the frequency of each number
        dictt = {}
        
        # 2. Iterate through the array to count occurrences
        for i in range(len(nums)):
            # Check if the number is already in the dictionary
            if nums[i] not in dictt:
                # If not, initialize its count to 0
                dictt[nums[i]] = 0
            # Increment the count for this number
            dictt[nums[i]] += 1
            
        # 3. Sort the dictionary items based on their values (frequencies)
        # dictt.items() returns a list of (key, value) tuples like [(1, 3), (2, 2)]
        # key=lambda x: x[1] tells Python to sort based on the second item (the count)
        # reverse=True ensures the most frequent items come first
        # Time complexity of this step: O(m log m) where m is number of unique elements
        sorted_items = sorted(dictt.items(), key=lambda x: x[1], reverse=True)
        
        # 4. Use a list comprehension to extract the keys from the first 'k' items
        # item[0] is the number itself (the key from our original dictionary)
        # [:k] slices the list to only take the top 'k' elements
        return [item[0] for item in sorted_items[:k]]