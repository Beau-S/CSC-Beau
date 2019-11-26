#11_26_1

def bubble(unsort):
	bubblels = unsort
	n = len(bubblels)
	print('initial', bubblels)
	for i in range(n):
		#for every loop that happens, the last value sorted will be in the correct place. it won't be needed to be iterated over again
		for j in range(0,n-1-i):
			if (bubblels[j] > bubblels[j+1]):
				temp = bubblels[j]
				bubblels[j] = bubblels[j+1]
				bubblels[j+1] = temp
				print(bubblels)
	print('final:', bubblels)
def main():
	list_1 = [1,10,-2,5,0]
	bubble(list_1)
if __name__ == '__main__':
	main()