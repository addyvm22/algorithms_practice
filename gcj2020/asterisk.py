"""


Problem
Many terminals use asterisks (*) to signify "any string", including the empty string. 
For example, when listing files matching BASH*, a terminal may list BASH, BASHER and 
BASHFUL. For *FUL, it may list BEAUTIFUL, AWFUL and BASHFUL. When listing B*L, BASHFUL, 
BEAUTIFUL and BULL may be listed.

In this problem, formally, a pattern is a string consisting of only uppercase English letters and asterisks (*), 
and a name is a string consisting of only uppercase English letters. A pattern p matches a name m if there is a 
way of replacing every asterisk in p with a (possibly empty) string to obtain m. Notice that each asterisk may be 
replaced by a different string.

Given N patterns, can you find a single name of at most 104 letters that matches all those patterns at once, or report
 that it cannot be done?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line 
with a single integer N: the number of patterns to simultaneously match. Then, N lines follow, each one containing a 
single string Pi representing the i-th pattern.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is 
any name containing at most 104 letters such that each Pi matches y according to the definition above, or * 
(i.e., just an asterisk) if there is no such name.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 50.
2 ≤ length of Pi ≤ 100, for all i.
Each character of Pi is either an uppercase English letter or an asterisk (*), for all i.
At least one character of Pi is an uppercase English letter, for all i.

"""

def a():
        
    t=int(input())


    for case in range(1, t+1):

        n= int(input())

        lmax = ""
        rmax = ""
        impossible = False
        returnString = ""
        for i in range(n):
            if impossible:
                s= input()
                continue

            s= input()

            splitList = s.split("*")
            ls=splitList[0]
            rs=splitList[-1]
            if lmax=="":
                lmax = ls
            if rmax == "":
                rmax = rs
            lnlmax=len(lmax)
            lnrmax=len(rmax)

            if len(ls) > lnlmax:
                if ls[:lnlmax] == lmax:
                    lmax = ls
                    # print(lmax)
                else:
                    impossible = True
                    # break

            elif ls!=lmax[:len(ls)]:
                impossible = True
                # break

            if len(rs)>=lnrmax and rs[-lnrmax:]==rmax:
                rmax = rs
                # print(rmax)
            elif rs=="" or  len(rs)<lnrmax and rs == rmax[-len(rs):]:
                pass
            else:
                impossible = True
                # break

            for j in range(1,len(splitList)-1):
                returnString+= splitList[j]


        if impossible:
            print("Case #"+ str(case) +": "+ "*")
        else:
            print("Case #"+ str(case) +": "+lmax+returnString+rmax)

# if __name__ == '__a__':
#     a()

a()











