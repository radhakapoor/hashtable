
class Hashtable(object):

	hashtable = []	

	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __getitem__(self, index):		
		print self.hashtable[index]

	def __repr__(self):
		return "name of hashtable: {}, size of hashtable: {}".format(self.name, self.size)

	def hash_string(self, key):
		count = 0
		for k in key:				
			count = count + ord(k)	
		allocated_bucket = count%self.size	
		#print allocated_bucket
		return allocated_bucket

	def make_hashtable(self):		
		for i in range(0, self.size):
		    self.hashtable.append([])	        
		#print len(self.hashtable)
		#print self.hashtable		
		return self.hashtable

	def hashtable_get_bucket(self, key):		
		bucket_number = self.hash_string(key)
		return self.hashtable[bucket_number]

	def hashtable_update(self, key, value):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:
			if entry[0]==key:
				entry[1] = value
				return
		bucket.append([key, value])
		print bucket

	def hashtable_lookup(self, key):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:
			if entry[0] == key:
				return entry[1]
		return None

"""initialize the hashtable"""
phone_hashtable = Hashtable('phonenumbers', 10)

"""Get bucket number for 'Asha'"""
print "Get bucket number for Asha:"
print phone_hashtable.hash_string('asha')

"""Create the empty hashtable"""
print "Print the empty hashtable:"
print phone_hashtable.make_hashtable()

"""Index the hashtable"""
print "Index the hashtable:"
phone_hashtable[2]

"""Get the bucket for keyword 'asha'"""
print "Get the bucket for keyword 'asha':"
print phone_hashtable.hashtable_get_bucket('asha')

"""Update the hashtable with two entries"""
print "Update the hashtable with two entries:"
phone_hashtable.hashtable_update('asha', '0208 998 3443')
phone_hashtable.hashtable_update('radha', '646 641 7999')

"""Print the hashtable"""
print "Print the hashtable"
print phone_hashtable.hashtable

"""Look up 'Asha' in the hashtable"""
print "Lookup 'Asha' in the hashtable:"
print phone_hashtable.hashtable_lookup('asha')






