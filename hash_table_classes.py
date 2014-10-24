

class Hashtable(object):

	hashtable = []
	total_keys = 0

	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.table = self.make_hashtable()
		
		
	def __getitem__(self, index):
		print self.hashtable[index]

	def __repr__(self):
		return "name: {}, size: {}, draw hashtable: {}".format(self.name, self.size, self.table)

	def make_hashtable(self):		
		for i in range(0, self.size):
			self.hashtable.append([])
		return self.hashtable

	def hash_string(self, key):
		count = 0
		for k in key:
			count = count + ord(k)
		allocated_bucket = count%self.size
		print key
		print "initial bucket is:"
		print allocated_bucket		
		return allocated_bucket

	def hashtable_get_bucket(self, key):
		bucket_number = self.hash_string(key)
		return self.hashtable[bucket_number]

	def hashtable_bucket_find(self, bucket, key):
		for entry in bucket:
			if entry[0]==key:
				print "entry is"
				print entry				
				return entry
			else:
				return None

	def hashtable_insert(self, key, value):
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_bucket_find(bucket, key)
		if entry:				
			entry[1]=value
			return
		bucket.append([key, value])
		self.total_keys = self.total_keys + 1		
		return self.total_keys	

	def hashtable_lookup(self, key):
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_bucket_find(bucket, key)
		if entry:
			return entry[1]
		else:
			return "Error! {} is not a key in the hashtable".format(key)

	def check_load(self):
		load_factor = float(self.total_keys) / float(self.size)
		if load_factor > 0.66:
			print "enlarge table"
			self.enlarge_hashtable()
		if load_factor < 0.33:
			print "shrink table"
			self.shrink_hashtable()

	def enlarge_hashtable(self):
		existing_buckets = self.size		
		self.size = self.size * 2	
		add_new_buckets = self.size - existing_buckets		
		for i in range(0, add_new_buckets):
			self.hashtable.append([])		
		self.re_distribute()					
		return self.hashtable

	def re_distribute(self):
		for bucket in self.hashtable:
			for entry in bucket:				
				key = entry[0]
				value = entry[1]
				new_bucket = self.hashtable_get_bucket(entry[0])
				#print "entry[0] is"
				#print entry[0]
				#even though this prints initial bucket it is the new bucket
				if ([key, value]) in new_bucket:
				    break
				else:
					if ([key, value]) in bucket:
						bucket.remove([key, value])					
					new_bucket.append([key, value])				
	
					
	def shrink_hashtable(self):
		existing_buckets = self.size
		self.size = self.size / 2
		remove_buckets = existing_buckets - self.size		
		for i in range(0, remove_buckets):
			self.hashtable.remove([])
		self.re_distribute()
		return self.hashtable			
		
	def hashtable_delete(self, key):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:
			if entry[0]==key:
				bucket.remove(entry[:2])
		return 	

hashtable1 = Hashtable('test', 40)

hashtable1.hashtable_insert('cat', 1)
hashtable1.hashtable_insert('dog', 2)
hashtable1.hashtable_insert('fish', 3)
hashtable1.hashtable_insert('pigeon', 4)
hashtable1.hashtable_insert('whale', 5)
hashtable1.hashtable_insert('crocodile', 6)
hashtable1.hashtable_insert('elephant', 7)
hashtable1.hashtable_insert('lizard', 8)
hashtable1.hashtable_insert('snake', 9)
hashtable1.hashtable_insert('killer whale', 10)
hashtable1.hashtable_insert('duck',11)
hashtable1.hashtable_insert('suraj', 13)

print "hashtable without resizing:"
print hashtable1.hashtable

print hashtable1.check_load()

print "hashtable with new buckets"
print hashtable1.hashtable

print hashtable1.size
hashtable1.re_distribute()

print hashtable1.hashtable_insert('radha', 12)
print hashtable1.hashtable_insert('zebra', 13)

print hashtable1.hashtable_lookup('snake')

print hashtable1.hashtable

print hashtable1.hashtable_lookup('zebra')



# Problems with current code:
# Seeing some repetition of entries. need to delete the existing first?
# needs refactoring as there is general code repetition
# hashtable_lookup - there is a bug whereby if the entry is not the first in the bucket. 









