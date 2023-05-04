#####   ♡〜٩( ˃́▿˂̀ )۶〜♡   #####
# Amazon Question Bank

# 1. Contains Duplicate ʕ´•ᴥ•`ʔ
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def main():
    print(containsDuplicate([1,2,3,4]))
main()


# Time: O(N) 
# Space: 0(N)
#### ᕕ༼✿•̀︿•́༽ᕗ ####



# 2. Missing Number ʕ´•ᴥ•`ʔ
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

def missingNumber(nums):
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

def main():
    print(missingNumber([3,0,1]))
main()


# Time: O(N) 
# Space: 0(1)
#### ᕕ༼✿•̀︿•́༽ᕗ ####