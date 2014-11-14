

class Hashtable(object):
	
	total_keys = 0
	all_entries = []

	def __init__(self, size):		
		self.size = size
		self.hashtable = []
		for i in xrange(self.size):
		    self.hashtable.append([])	

	def __repr__(self):
		return "size: {}, draw hashtable: {}".format(self.size, self.hashtable)	

	def __getitem__(self, index):
		return self.hashtable[index]       

	def hash_string(self, key):
		count = 0		
		for k in key:
			count = count + ord(k)						
		bucket_no = count%self.size						
		return bucket_no

	def hashtable_get_bucket(self, key):
		bucket_no = self.hash_string(key)		
		return self.hashtable[bucket_no]

	def hashtable_get_entry(self, bucket, key):
		for entry in bucket:
			if entry[0] == key:
				return entry
		return None

	def hashtable_insert(self, key, value):		
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_get_entry(bucket, key)
		if entry:		
			entry[1] = value
			for each in self.all_entries:
			    if each[0]==key:
			    	each[1]=value
			    	return
		else:			
			bucket.append([key, value])
		self.all_entries.append([key, value]) 
		print self.all_entries				
		self.total_keys = self.total_keys + 1		
		self.check_load()		
			

	def hashtable_lookup(self, key):
		entry = self.hashtable_get_entry(self.hashtable_get_bucket(key), key)
		if entry:					
			return entry[1]			
		else:
			return "Error! {} is not a key in the hashtable".format(key)

	def check_load(self):		
		load_factor = float(self.total_keys) / float(self.size)		
		if load_factor > 0.66:			
			self.enlarge_hashtable()
		elif load_factor < 0.33:			
			self.shrink_hashtable()

	def enlarge_hashtable(self):		
		existing_buckets = self.size		
		self.size = self.size * 2	
		add_new_buckets = self.size - existing_buckets		
		for i in xrange(add_new_buckets):
			self.hashtable.append([])				
		self.re_distribute()							
		return self.hashtable

	def clear_buckets(self):
		for bucket in self.hashtable:					
			bucket[:] = []			
		return bucket

	def re_distribute(self):
		self.clear_buckets()		
		for each in self.all_entries:
			print "each in self.all_entries"
			print each
			bucket = self.hashtable_get_bucket(each[0])
			entry = self.hashtable_get_entry(bucket, each[0])
			bucket.append([each[0], each[1]])
					
	def shrink_hashtable(self):		
		existing_buckets = self.size
		self.size = self.size / 2
		remove_buckets = existing_buckets - self.size		
		for i in xrange(remove_buckets):
			self.hashtable.remove([])
		self.re_distribute()		
		return self.hashtable			
		
	def hashtable_delete(self, key):
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_get_entry(bucket, key) 		
		if entry:
			bucket.remove(entry[:2])
			self.all_entries.remove(entry[:2])
		self.total_keys = self.total_keys - 1	
		self.check_load()
		return	
	
hashtable1 = Hashtable(10)

"""check insert"""
hashtable1.hashtable_insert('cat', 1)
hashtable1.hashtable_insert('dog', 2)
hashtable1.hashtable_insert('fish', 3)
hashtable1.hashtable_insert('pigeon', 4)
hashtable1.hashtable_insert('whale', 5)
hashtable1.hashtable_insert('crocodile', 6)
hashtable1.hashtable_insert('elephant', 7)
hashtable1.hashtable_insert('lizard', 8)

"""check lookup"""
print "check lookup"
print hashtable1.hashtable_lookup('cat')
print hashtable1.hashtable_lookup('dog')
print hashtable1.hashtable_lookup('fish')
print hashtable1.hashtable_lookup('pigeon')
print hashtable1.hashtable_lookup('whale')
print hashtable1.hashtable_lookup('crocodile')
print hashtable1.hashtable_lookup('elephant')
print hashtable1.hashtable_lookup('lizard')

# """check deletion"""
# hashtable1.hashtable_delete('crocadile')
# hashtable1.hashtable_delete('lizard')

"""check lookup of non-existing key"""
print hashtable1.hashtable_lookup('donkey')

"""check update of value"""
hashtable1.hashtable_insert('elephant', 'super')
hashtable1.hashtable_insert('lizard', 1000)
print hashtable1.hashtable_lookup('lizard')
print hashtable1.hashtable_lookup('elephant')

print hashtable1

print "all_entries at the end"
print hashtable1.all_entries
print hashtable1.total_keys






