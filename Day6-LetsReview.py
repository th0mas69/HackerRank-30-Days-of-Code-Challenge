# Enter your code here. Read input from STDIN. Print output to ST
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
