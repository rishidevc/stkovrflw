
	>>> arr
	['[1,2,3]', '[4,5,6]', '[7,8,9]', '[10,11,12]']
	>>>
	>>> '+'.join(arr)
	'[1,2,3]+[4,5,6]+[7,8,9]+[10,11,12]'
	>>>
	>>> eval('+'.join(arr))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	>>>

Another approach using **reduce()** and **lambda**

	>>> import json
	>>>
	>>> arr = ['[1,2,3]','[4,5,6]','[7,8,9]','[10,11,12]']
	>>>
	>>> arr2 = reduce(lambda list1, list2: list1 + '+' + list2, arr)
	>>>
	>>> arr2
	'[1,2,3]+[4,5,6]+[7,8,9]+[10,11,12]'
	>>>
	>>> eval(arr2)
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]