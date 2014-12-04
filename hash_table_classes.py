

class Hashtable(object):

	# all_entries = []
	
	def __init__(self, size):
		"""initializes hashtable"""		
		self.size = size
		self.hashtable = []
		for i in xrange(self.size):
		    self.hashtable.append([])
		self.all_entries = []

	def __repr__(self):
		return "size: {}, draw hashtable: {}".format(self.size, self.hashtable)	

	def __getitem__(self, index):
		return self.hashtable[index]  
		
	def hash_string(self, key):
		"""hashing algorithm to determine bucket no"""
		count = 0		
		for k in key:
			count = count + ord(k)						
		bucket_no = count%self.size						
		return bucket_no
		
	def hashtable_get_bucket(self, key):
		"""fetches bucket for a given key"""
		bucket_no = self.hash_string(key)		
		return self.hashtable[bucket_no]
		
	def hashtable_get_entry(self, bucket, key):
		""""fetches entry in bucket for a key"""
		for entry in bucket:
			if entry[0]==key:
				return entry
		return None

	def hashtable_insert(self, key, value):	
		"""updates / inserts entries"""	
		bucket_no = self.hash_string(key)
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_get_entry(bucket, key)
		if entry:		
			entry[1] = value
			self.update_all_entries(key, value)
			return self.hashtable
		elif len(bucket)==0:
			bucket.append([key, value])			
		else:
			collision = self.collision_handling(key, bucket_no)					
			if collision:
				collision[1] = value
				self.update_all_entries(key, value)	
				return self.hashtable
			else:								
				collision.append([key, value])
		self.all_entries.append([key, value]) 			
		self.check_load()

	def collision_handling(self, key, bucket_no):
		for bucket in self.hashtable:
			bucket_no += 1
			if bucket_no >= len(self.hashtable):
				bucket_no = 0
			check_bucket = self.hashtable[bucket_no]
			if len(check_bucket)==0:
				return check_bucket
			else: 
				for entry in check_bucket:
					if entry[0]==key:
						return entry
		raise ValueError
		
	def update_all_entries(self, key, value):
		"""updates storage of all key, values. necessary for resizing mechanics"""
		for each in self.all_entries:
			if each[0]==key:
				each[1]=value
		
	def hashtable_lookup(self, key):
		"""looks up value"""
		bucket_no = self.hash_string(key)
		entry = self.hashtable_get_entry(self.hashtable_get_bucket(key), key)
		if entry:					
			return entry[1]
		else:
			collision = self.collision_handling(key, bucket_no)
			if collision:
				return collision[1]			
		return "Error! {} is not a key in the hashtable".format(key)
		
	def check_load(self):
		"""checks load to see if resizing required"""		
		load_factor = float(len(self.all_entries)) / float(self.size)		
		if load_factor > 0.66:			
			return self.enlarge_hashtable()
		elif load_factor < 0.33:			
			return self.shrink_hashtable()
		else:
			return self.hashtable
		
	def enlarge_hashtable(self):
		"""doubles size of hashtable"""		
		existing_buckets = self.size		
		self.size = self.size * 2	
		add_new_buckets = self.size - existing_buckets		
		for i in xrange(add_new_buckets):
			self.hashtable.append([])				
		self.re_distribute()							
		return self.hashtable

	def shrink_hashtable(self):
		""""halves size of hashtable"""		
		existing_buckets = self.size
		self.size = self.size / 2
		remove_buckets = existing_buckets - self.size		
		for i in xrange(remove_buckets):
			self.hashtable.remove([])
		self.re_distribute()		
		return self.hashtable

	def clear_buckets(self):
		"""clears all buckets in preparation for re-hashing pursuant to resizing"""
		for bucket in self.hashtable:					
			bucket[:] = []			
		return bucket

	def re_distribute(self):
		"""re-hashes key, values upon resizing"""
		self.clear_buckets()		
		for each in self.all_entries:			
			bucket = self.hashtable_get_bucket(each[0])			
			if len(bucket)==0:
				bucket.append([each[0], each[1]])
			else:
				bucket_no = self.hash_string(each[0])
				collision = self.collision_handling(each[0], bucket_no)
				collision.append([each[0], each[1]])								
			
	#rewrite to mark deleted items as 'deleted' so as not to disrupt lookups based on open addressing
	def hashtable_delete(self, key):
		"""deletes entries from hashtable"""
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_get_entry(bucket, key) 		
		if entry:
			bucket.remove(entry[:2])
			self.all_entries.remove(entry[:2])			
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
hashtable1.hashtable_insert('rabbit', 9)

"""check lookup"""
print hashtable1.hashtable_lookup('cat')
print hashtable1.hashtable_lookup('dog')
print hashtable1.hashtable_lookup('fish')
print hashtable1.hashtable_lookup('pigeon')
print hashtable1.hashtable_lookup('whale')
print hashtable1.hashtable_lookup('crocodile')
print hashtable1.hashtable_lookup('elephant')
print hashtable1.hashtable_lookup('lizard')
print hashtable1.hashtable_lookup('rabbit')

"""check lookup of non-existing key"""
print hashtable1.hashtable_lookup('donkey')
print hashtable1.hashtable_lookup('rhino')

"""check update of value"""
hashtable1.hashtable_insert('elephant', 1000)
hashtable1.hashtable_insert('lizard', 2000)
hashtable1.hashtable_insert('rabbit', 3000)
print hashtable1.hashtable_lookup('elephant')
print hashtable1.hashtable_lookup('lizard')
print hashtable1.hashtable_lookup('rabbit')

# """check deletion"""
# hashtable1.hashtable_delete('crocodile')
# hashtable1.hashtable_delete('lizard')
# hashtable1.hashtable_delete('cat')

print hashtable1








