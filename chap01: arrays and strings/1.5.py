"""
Cracking the coding interview 6th
1.5
"""

# Use Hashmap
# time complexity: O(n)
# space complexity: O(256)
def one_away(str1,str2):
	hashmap ={}
	for i in str1:
		if i in hashmap:
			hashmap[i]+=1
		else:
			hashmap[i]=1
	
	for j in str2:
		if j in hashmap:
			hashmap[j]+=1
		else:
			hashmap[j]=1
	
	if(len(hashmap)-len(str1) >=2):
		return False
	return True
if __name__=="__main__":

	str1 = "pale"
	str2 = "bake"
	print one_away(str1,str2)
