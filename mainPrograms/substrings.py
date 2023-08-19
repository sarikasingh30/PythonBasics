# --------------------------------------------------------------------------------------------------------
# Check how many times this substring comes in the given string
def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):
        s = str()
        for j in range(i, len(string)):
            s += string[j]
            if (s == sub_string):
                c += 1
    return c


string = "ABCDCDC"
sub_string = "CDC"
ans = count_substring(string, sub_string)
print(ans)
# --------------------------------------------------------------------------------------------------------
