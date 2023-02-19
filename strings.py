# --------------------------------------------------------------------------------------------------------
# In string change (space) with (-)
# Split the string with (space) and then join with (-)
def fun(line):
    arr = line.split(" ")
    ans = "-".join(arr)
    return ans


x = "Today is a beautiful day"
ans = fun(x)
print(ans)
# --------------------------------------------------------------------------------------------------------
