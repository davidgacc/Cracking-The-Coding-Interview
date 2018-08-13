"""
Cracking the coding interview 6th
1.1
"""

# Hashmap
# time complexity: O(n)
# space complexity: O(1), is constant because the size of hashmap have to be 128(character alphabet) or 256(ASCII)

def isUnique_1(string):
	hashmap ={}
	for i in string:
		if i in hashmap:
			hashmap[i]+=1
		else:
			hashmap[i]=1
	for key,value in hashmap.items():
		if(value != 1):
			return False
	return True

# Sorting
# Time complexity : O(n*logn)
# Space complexity : O(1)
def isUnique_2(string):
	temp = sorted(string)
	for i in range(1,len(temp)):
		if(temp[i-1] == temp[i]):
			return False
	return True
	
            
if __name__=="__main__":

	string = "abcdefghi"
	print isUnique_1(string)
	print isUnique_2(string)s
