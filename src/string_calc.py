class StringCalculator:
    def add(input):
        if not input:
            return 0
        else:
            nums = input.split(",")
            nums = [int(num) for num in nums]
            return sum(nums)

