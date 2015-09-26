def checkEqual(lst):
	return lst[1:] == lst[:-1]

def unique_list(nums):
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique

s = raw_input()
numbers_list = map(int, s.split())

string_list=[]


multi_list=[]


for i in numbers_list:
	temp_list=[]
	
	z= len(str(i))
	
	string_list.append(z)
	k=pow(10,z-1)
	n=int(i/k)
	if z==1:
		temp_list.append(i)
	else:
		temp_list.append(n)
	temp_list.append(i)
	multi_list.append(temp_list)
	temp_list=None

string_list=unique_list(string_list)
string_list.sort()

new_multi_list=[]

for i in numbers_list:
	temp_list=[]
	z= len(str(i))
	k=pow(10,z-1)
	n=int(i/k)
	if z==1:
		temp_list.append(i)
	else:
		temp_list.append(n)
	z= len(str(i))
	for j in string_list:
		if len(str(i))==j and j-2>-1:
			
			k=pow(10,j-2)
			n=int(i/k)
			temp_list.append(n)
		else:
			
			if(temp_list[len(temp_list)-1]<i and temp_list[len(temp_list)-1]>10):
				temp_list.append(temp_list[len(temp_list)-1])
			else:
				temp_list.append(i)
			
	new_multi_list.append(temp_list)
	temp_list=None


for j in xrange(1, len(string_list)):
	
	new_multi_list= sorted(new_multi_list,key=lambda x:x[j+1])
	
	new_multi_list= sorted(new_multi_list,key=lambda x:x[0])
	

for i in xrange(len(new_multi_list)):
	
	
	for j in xrange(i,len(new_multi_list)):
		t1=new_multi_list[i][1]
		t1_1en=len(str(t1))
		
		t2=new_multi_list[j][1]
		t2_len=len(str(t2))
		len_diff=t1_1en-t2_len
		if(len_diff<0):
			len_diff=t2_len+len_diff
			temp=str(t2)
			
			if int(temp[0:len_diff])<t1:
				temp_list=new_multi_list[i]
				new_multi_list[i]=new_multi_list[j]
				new_multi_list[j]=temp_list
			

appending_number=''
for item in new_multi_list:
	appending_number=appending_number+str(item[1])

print int(appending_number)

