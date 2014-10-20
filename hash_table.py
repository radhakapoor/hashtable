
"""allocate a bucket for keyword"""

# def bad_hash_string(keyword, buckets):
# 	return ord(keyword[0]%buckets)

def hash_string(keyword, buckets):
	count = 0
	for k in keyword:				
		count = count + ord(k)	
	allocated_bucket = count%buckets	
	return allocated_bucket



"""make the hashtable"""

# def make_hashtable(nbuckets):
# 	count = 0
# 	hashtable=[]
# 	while count < nbuckets:
# 		hashtable.append([])
# 		count = count + 1
# 	return hashtable	

def make_hashtable_refactored(nbuckets):
	hashtable = []
	for i in range(0, nbuckets): 	  
	    hashtable.append([])
	print len(hashtable)
	return hashtable


"""find bucket for keyword"""

def hashtable_get_bucket(htable, keyword):
	print htable[hash_string(keyword, len(table))]
	return htable[hash_string(keyword, len(table))]



"""add key, value to hashtable"""

def hashtable_add(htable, key, value):
	bucket = hashtable_get_bucket(htable, key)
	bucket.append([key, value])
	#hashtable_get_bucket(htable, key).append([key, value])
	return htable



"""look up key in hashtable and return value"""

def hashtable_lookup(htable, key):
	bucket = hashtable_get_bucket(htable, key)
	print bucket
	for entry in bucket:
		if entry[0]==key:
			return entry[1]
	else:
		return None

#print hashtable_lookup(table, 'radha')



"""update key, value"""

def hashtable_update(htable, key, value):
	bucket = hashtable_get_bucket(htable, key)	
	for entry in bucket:
		if entry[0]==key:
			entry[1]=value
			return						
	bucket.append([key, value])

#very similar to lookup. Can we avoid repeating code? 	

# def hashtable_update(htable, key, value):
# 	bucket = hashtable_get_bucket(htable, key)	
# 	for entry in bucket:
# 		if entry[0]==key:
# 			bucket.remove(entry)			
# 	return bucket.append([key, value])			
	
table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]			

hashtable_get_bucket(table, 'Zoe')
hashtable_get_bucket(table, 'Brick')

#hashtable_update(table, 'Bill', 42)
#hashtable_update(table, 'Rochelle', 94)
#hashtable_update(table, 'Zed', 68)
#print table



# def bad_hash_string(keyword, buckets):
# 	return ord(keyword[0]%buckets)

# def make_hashtable(nbuckets):
# 	count = 0
# 	hashtable=[]
# 	while count < nbuckets:
# 		hashtable.append([])
# 		count = count + 1
# 	return hashtable


