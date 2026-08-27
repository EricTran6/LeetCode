class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range (1, n + 1):
            num = i
            if num % 5 == 0 and num % 3 == 0:
                res.append("FizzBuzz")
            elif num % 5 == 0:
                res.append("Buzz")
            elif num % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(num))
        return res

                    