# --------------------------------------------------------------------------------------------------------
# In string change (space) with (-)
# Split the string with (space) and then join with (-)
def fun(line):
    arr = line.split(" ")
    ans = "-".join(arr)
    return ans


x = "Today is a beautiful day"
ans = fun(x)
print(x, "=>", ans)
# --------------------------------------------------------------------------------------------------------
'''
Sample Input =>  chris alan
Sample Output => Chris Alan
'''


def solve(s):
    x = s.split(" ")
    c = []
    for i in x:
        c.append(i.capitalize())
    ans = " ".join(c)
    return ans


s = "chris alan"
ans = solve(s)
print(s, "=>", ans)
# --------------------------------------------------------------------------------------------------------
