'''write a code to get maximum size of substring which has vowels,
where window size is constant 3'''
def max_vowels(s,k):
    vowels= 'aeiouAEIOU'
    count =0
    for i in range(k):
        if s[i]in vowels:
         count+=1
    max_count = count
    for i in range(k,len(s)):
        if s[i] in vowels:
            count+=1
        if s[i-k] in vowels:
            count-=1
        max_count=max(max_count,count)
    return max_count
s= input("Enter a string :")
k= int(input("Enter the window size :"))
print("maximum vowelssubstring sizeis",max_vowels(s,k))