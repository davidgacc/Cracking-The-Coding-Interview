"""
Cracking the coding interview 6th
1.2
"""

# Hashmap
# time complexity: O(n)
# space complexity: O(n)

def check_permutation_1(str1,str2):
	hashmap_str1 ={}
	hashmap_str2 ={}
	for i in str1:
		if i in hashmap_str1:
			hashmap_str1[i]+=1
		else:
			hashmap_str1[i]=1
			
	for j in str2:
		if j in hashmap_str2:
			hashmap_str2[j]+=1
		else:
			hashmap_str2[j]=1

	return hashmap_str1==hashmap_str2

# Sorting
# Time complexity : O(n*logn)
# Space complexity : O(1)
def check_permutation_2(str1,str2):
	temp_1 = sorted(str1)
	temp_2 = sorted(str2)
	return temp_1==temp_2
	
if __name__=="__main__":

	string1 = "abcdefghi"
	string2 = "ihgfedcba"
	print check_permutation_1(string1,string2)
	print check_permutation_2(string1,string2)
