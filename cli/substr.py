'''write a code to print the number of substrings in a given string using sliding window range
example
abcabcbb
output=3'''
def count_most(s,k):
    left, count=0,0
    freq={}
    for right in range(len(s)):
        freq[s[right]]= freq.get(s[right],0)+1
        while len(freq)>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
        count+= right-left+1
    return count

s= input("enter a string: ")
k= int(input("enter a size of slide: "))
result= count_most(s,k)
print("number of substrings with at most",k,"distinct characters is:",result)   
