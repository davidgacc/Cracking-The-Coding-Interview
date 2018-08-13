"""
Cracking the coding interview 
1.3
"""
def urlify(string,length):
    temp = list(string)
    index = len(temp)
    for i in range(length-1,-1,-1):
        if(temp[i] != " "):
            temp[index-1] = temp[i]
            index -=1
        else:
            temp[index-1] = '0'
            temp[index-2] = '2'
            temp[index-3] = '%'
            index-=3
    return "".join(temp)
            
if __name__=="__main__":

	string = "Mr John Smith    "
	truth_length = 13
	print urlify(string,truth_length)
