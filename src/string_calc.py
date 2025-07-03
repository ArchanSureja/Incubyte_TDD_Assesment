class StringCalculator:
    def add(input):
        if len(input)==0:
            return 0
        elif len(input)==1:
            return int(input)
        else:
            nums = input.split(",")
            return int(nums[0]) + int(nums[1])
            
