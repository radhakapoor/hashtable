

def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]


def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
    	entry[1] = value
    else:
    	bucket.append([key, value])
    #can we update the key this way or is this only to update values? 

def hashtable_lookup(htable, key):
	bucket = hashtable_get_bucket(htable, key)
	entry = bucket_find(bucket, key)
	if entry:
		return entry[1]
	else:
		return None

def bucket_find(bucket, key):
	for entry in bucket:
		if entry[0] == key:
			return entry
	return None


table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python')
print hashtable_lookup(table, 'JavaScript')


