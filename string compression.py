class Solution(object):
    def compress(self, chars):
        index=0 #new array format index
        count=0 #count of consecutive elements
        for i in range(len(chars)):
            count+=1
            if(i+1==len(chars) or chars[i]!=chars[i+1]): #if the end or next and previous not equal its time to write count or element(count=1)
                chars[index]=chars[i]
                index+=1 #once written always moves next
                if count>1 :
                    for ch in str(count): #the count of consecutive element
                        chars[index]=ch
                        index+=1
                count=0 #restore of count into 0 for checking next consecutive element
        return index
