"""
Cracking the coding interview 6th
1.6
"""

# time complexity: O(n)
# space complexity: O(1)

def string_compression(str1):
	count=1
	new_str= ""
	for i in range(1,len(str1)):
		if (str1[i]!=str1[i-1]):
			new_str +=str1[i-1]+str(count)
			count=1
		else:
			count +=1
	new_str += str1[len(str1)-1]+str(count)
	if(len(new_str)>len(str1)):
		return str1
	return new_str
			
if __name__=="__main__":

	str1 = "aaabbccccccccdde"
	print string_compression(str1)
