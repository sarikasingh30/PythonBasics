'''
Q. => Consider a list (list = [ ]).You can perform the following commands:
        insert i e: Insert integer at the position.
        print: Print the list.
        remove i.e: Delete the first occurrence of integer.
        append i.e: Insert integer at the end of the list.
        sort: Sort the list.
        pop: Pop the last element from the list.
        reverse: Reverse the list.
        Initialize your list and read in the value followed by lines of commands where each command will be of
        the types listed above. Iterate through each command in order and perform the corresponding
        operation on your list.
        Example 1 =>
        N = 4
        Append 1
        Append 2
        Insert 3 1
        Print
        ########################################################################################
        Output: [1, 3, 2]
        ----------------------------------------------------------------------------------------
        Example 2 =>
        12
        insert 0 5
        insert 1 10
        insert 0 6
        print
        remove 6
        append 9
        append 1
        sort
        print
        pop
        reverse
        print
        ###################################################################################
        Output =>
        [6, 5, 10]
        [1, 5, 9, 10]
        [9, 5, 1]
        ----------------------------------------------------------------------------------
'''
# Solution
# insert(index,element)
l = []
N = int(input())
for i in range(N):
    inputAll = list(map(str, input().split()))
    if "insert" in inputAll:
        l.insert(int(inputAll[1]), int(inputAll[2]))
    if "print" in inputAll:
        print(l)
    if "remove" in inputAll:
        l.remove(int(inputAll[1]))
    if "append" in inputAll:
        l.append(int(inputAll[1]))
    if "sort" in inputAll:
        l.sort()
    if "pop" in inputAll:
        l.pop()
    if "reverse" in inputAll:
        l.reverse()
# --------------------------------------------------------------------------------------------------------
