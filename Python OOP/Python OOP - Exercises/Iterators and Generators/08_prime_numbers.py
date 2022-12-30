def get_primes(nums: list):
    for num in nums:
        if num <= 1:
            continue

        for digit in range(2, num):
            if num % digit == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
