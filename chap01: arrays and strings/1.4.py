"""
Cracking the coding interview 6th
1.4
"""

# Hashmap
# time complexity: O(n)
# space complexity: O(256)

def palindrome_permutation(string):
	hashmap ={}
	string_low = "".join(string.lower().split())
	for i in string_low:
		if i in hashmap:
			hashmap[i]+=1
		else:
			hashmap[i]=1
			
	count_odd=0
	for key,value in hashmap.items():
		if(value %2 !=0):
			count_odd +=1
		if(count_odd > 1):
			return False
	return True

if __name__=="__main__":

	string = "Tact Coa"
	print palindrome_permutation(string)
