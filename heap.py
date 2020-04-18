def swap(l,i,j):
	temp = l[i]
	l[i] = l[j]
	l[j] = temp
	return l

def print_mini(l):
	return l[0]

def insert(l,data):
	l.insert(0,0)
	l.append(data)
	if len(l) == 1:
		print("data is inserted as node")
	else:
		temp = l[-1]
		i = (len(l)-1)
		# print(i)
		while(i>1):
			if l[i]<l[i//2]:
				l = swap(l,i,i//2)
				i = i//2
			else:
				break
	return l[1:]
	

def delete(l):
	
	k = len(l)
	if k == 0:
		return -9999999
	elif k==1:
		return(l.pop())
	elif k==2:
		temp = l.pop(0)
		return temp, l

	else:
		l = swap(l,0,len(l)-1)
		l.pop()
		# print(l)
		i = 0
		left = i*2+1
		right = i*2+2
		if l[left]>l[right]:
			mini = right
		else:
			mini = left

		while(left<len(l) or right<len(l)):

			if right>=len(l):

				l = swap(l,i,left)
				# print(l)
				i = left
			else:
				if l[left]>l[right]:
					mini = right
				else:
					mini = left

				if l[i]>l[mini]:
					l = swap(l,i, mini)
					# print(l)
					i = mini
				else:
					i = mini


			left = i*2+1
			right = i*2+2


	return l
			# if i*2+1 < len(l):
			# 	left = i*2+1
			# else:
			# 	break

			# if i*2+2 < len(l):
			# 	right = i*2+2
			# else:

















l = []
l = insert(l,5)
print(l)
l = insert(l,9)
print(l)
l = delete(l)
print(l)
