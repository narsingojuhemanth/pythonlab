# 20. Write a Python class to reverse a string word by word.
class Solution:
    def solve(self, s):
        temp = s.split(' ')
        temp = list(reversed(temp))
        print(temp)
        return ' '.join(temp)

ob = Solution()
sentence = "Hello world, I love python programming"
print(ob.solve(sentence))