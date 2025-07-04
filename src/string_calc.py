class NegetiveNumberException(Exception):
    def __init__(self,negetive_nums):
        num_str=""
        for i in range(len(negetive_nums)-1):
            num_str += f"{str(negetive_nums[i])}, "
        num_str += f"{str(negetive_nums[-1])}"
        msg = f"negetive numbers not allowed {num_str}"
        super().__init__(msg)

class StringCalculator:

    @staticmethod
    def _negetives(nums):
        return [num for num in nums if num<0]

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
            negetive_nums = StringCalculator._negetives(nums)
            if negetive_nums:
                raise NegetiveNumberException(negetive_nums)
            return sum(nums)

