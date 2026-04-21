nums = list(map(int, input("Enter numbers: ").split()))
n=len(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])
for i in range(2):
    for j in range(n-1-i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted List:", nums)

if n >= 2:
    largest=nums[-1]
    for i in range(n-2,-1,-1):
        if nums[i]<largest:
            print("second largest unique number:",nums[i])
            break
        else:
            print(" No Second Largest Unique Number Exists")
else:
    print("List must contain at least two elements.")
