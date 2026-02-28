def lst(s):
    left = max_len= start=0
    seen= {}
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
    return s[start:start+ max_len]
s = input("Enter a string :")
print("longest unique substring :", lst(s))

