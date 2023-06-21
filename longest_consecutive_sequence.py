#from typing import List

def longestConsecutive(nums) -> int:
    hashSet = set()
    for num in nums:
        hashSet.add(num)
   # print(hashSet)
    longestStreak = 0
    for num in nums:
        if (num - 1) not in hashSet:
            currentNum = num
            currentStreak = 1
            while (currentNum + 1) in hashSet:
                currentNum += 1
                currentStreak += 1
            longestStreak = max(longestStreak, currentStreak)
    return longestStreak


if __name__ == "__main__":
    arr = [100, 200, 1, 2, 3]
    lon = longestConsecutive(arr)
    print("The longest consecutive sequence is", lon)