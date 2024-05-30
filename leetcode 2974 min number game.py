nums = [5,4,2,3]
new_nums = []
while nums:
            alice=min(nums)
            nums.remove(min(nums))
            bob=min(nums)
            nums.remove(min(nums))
            new_nums.append(bob)
            new_nums.append(alice)
print(new_nums)     