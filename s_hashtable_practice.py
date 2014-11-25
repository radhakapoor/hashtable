

hashtable = [[], [], [], [], [], [], [], [], [], []]


def hashtable_insert(self, key, value):		
		bucket_no = self.hash_string(key)		
		bucket = self.hashtable_get_bucket(key)
		entry = self.hashtable_get_entry(bucket, key)		
		if entry:
			entry[1] = value			
			self.update_all_entries(key, value)		    	
			return			
		elif len(bucket)==0:
			bucket.append([key, value])
		else:
			collision_entry = self.collision_lookup(key, bucket_no)
			if collision_entry:				
				collision_entry[1] = value
				self.update_all_entries(key, value)
				return
			else:
				empty_bucket = self.find_empty_bucket(bucket_no)			
				empty_bucket.append([key, value])			
		self.all_entries.append([key, value])					
		self.total_keys = self.total_keys + 1		
		self.check_load()

def find_empty_bucket(self, bucket_no):
		for bucket in self.hashtable:
			bucket_no += 1
			if bucket_no < len(self.hashtable):
				check_bucket = self.hashtable[bucket_no]
				if len(check_bucket)==0:
					return check_bucket
			else:				
				bucket_no = 0
				check_bucket = self.hashtable[bucket_no]
				if len(check_bucket)==0:
					return check_bucket	

def hashtable_lookup(self, key):
		bucket_no = self.hash_string(key)
		entry = self.hashtable_get_entry(self.hashtable_get_bucket(key), key)
		if entry:					
			return entry[1]	
		else:
	 		entry = self.collision_lookup(key, bucket_no)
			if entry:
				return entry[1]
		return "{} is not a key in the hashtable".format(key)	

def collision_lookup(self, key, bucket_no):
		# print "collision lookup is getting triggered"
		for bucket in self.hashtable:
			while len(bucket) !=0:
				bucket_no +=  1
				if bucket_no < len(self.hashtable):				
					check_bucket = self.hashtable[bucket_no]								 
					for entry in check_bucket:
						if entry:					
							if entry[0]==key:												
								return entry
				else:
					bucket_no = 0
					check_bucket = self.hashtable[bucket_no]
					for entry in check_bucket:
						if entry[0]==key:
							return entry		