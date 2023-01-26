def generateParenthesis(n):
    if n <= 0:
        return []
    res = []
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    backtrack("", 0, 0)
    return res

print(generateParenthesis(3)) 
print(generateParenthesis(1)) 
print(generateParenthesis(5))
print(generateParenthesis(-1)) 
