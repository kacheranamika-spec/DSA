#check for Anagrams:
#Write a code to check if two strings are anagrams of each other or not.
s1 = "listen"
s2 = "silent"
count1 = {}
count2 = {}
for ch in s1:
    if ch in count1:
        count1[ch] += 1
    else:
        count1[ch] = 1
for ch in s2:
    if ch in count2:
        count2[ch] += 1
    else:
        count2[ch] = 1
 
if count1 == count2:
    print("Anagrams")
else:
    print("Not Anagrams")