word="banana"
def bananas(s):
    return helper(s, [], "", len(word))
def helper(s, arr, remain, length):
    if length==0:
        arr.append(remain+len(s)*"-")
        return
    for i,j in enumerate(s):
        if j==word[len(word)-length]:
            helper(s[i+1:], arr, remain+"-"*i+j, length-1)
    return arr