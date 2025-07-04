class StringCalculator:
    def add(input):
        if not input:
            return 0
        else:
            # custom delimeter
            if input.startswith("//"):
                custom_delimeter , input = input.split("\n",1)
                custom_delimeter=custom_delimeter[2] # skipping first two /
                input = input.replace(custom_delimeter,",")

            input = input.replace("\n",",")
            nums = input.split(",")
            nums = [int(num) for num in nums]
            return sum(nums)

