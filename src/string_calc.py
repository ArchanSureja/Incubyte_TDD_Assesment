class StringCalculator:
    def add(input):
        if len(input)==0:
            return 0
        elif len(input)==1:
            return int(input)
        else:
            nums = input.split(",")
            nums = [int(num) for num in nums]
            return sum(nums)

