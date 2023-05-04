#####   ♡〜٩( ˃́▿˂̀ )۶〜♡   #####
# Amazon Question Bank

# 1. Contains Duplicate ʕ´•ᴥ•`ʔ

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

# 2. 