

"""How to modify the code?"""
# - you can initialize the table with whatever size you want
# - upon 'update', hashtable will automatically resize (enlarge or shrink)
# - load factor = total number of keys / size

class Hashtable(object):

	hashtable = []	

	def __init__(self, name, size):
		self.name = name
		self.size = size

		#can __init__ have methods? ie the growing and shrinking? 

	def __getitem__(self, index):		
		print self.hashtable[index]

	def __repr__(self):
		return "name of hashtable: {}, size of hashtable: {}".format(self.name, self.size)

	def make_hashtable(self):		
		for i in range(0, self.size):
		    self.hashtable.append([])	        
		#print len(self.hashtable)
		#print self.hashtable		
		return self.hashtable

	def hash_string(self, key):
		count = 0
		for k in key:				
			count = count + ord(k)	
		allocated_bucket = count%self.size	
		#print allocated_bucket
		return allocated_bucket	

	def hashtable_get_bucket(self, key):		
		bucket_number = self.hash_string(key)
		return self.hashtable[bucket_number]

	def hashtable_insert(self, key, value):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:
			if entry[0]==key:
				entry[1] = value
				return
		bucket.append([key, value])
		print bucket

	def hashtable_delete(self, key):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:
			if entry[0]==key:
				bucket.remove(entry[:2])
		print bucket
		return

	def hashtable_lookup(self, key):
		bucket = self.hashtable_get_bucket(key)
		for entry in bucket:			
			if entry[0] == key:
				return entry[1]
		return "{} is not a key in the hashtable".format(key)		
		
		
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

"""Insert entries into the hashtable"""
print "Insert entries into the hashtable:"
phone_hashtable.hashtable_insert('asha', '0208 998 3443')
phone_hashtable.hashtable_insert('radha', '646 641 7999')
phone_hashtable.hashtable_insert('paresh', '0776 468 5109')

"""Print the hashtable"""
print "Print the hashtable"
print phone_hashtable.hashtable

"""Delete from the hashtable"""
print "Delete from the hashtable:"
phone_hashtable.hashtable_delete('radha')

"""Print the hashtable"""
print "Print the hashtable"
print phone_hashtable.hashtable

"""Look up 'suraj' in the hashtable"""
print "Lookup 'suraj' in the hashtable:"
print phone_hashtable.hashtable_lookup('suraj')

"""Features of a good hashing function"""
# Makes use of all info provided by key
# Uniformly distributes output across table
# Maps similar keys to very different hash values
# Uses only very fast operations

"""Dynamic Resizing"""
# - A general purpose hashtable class will almost always have some ways to resize
# and it is good practice to include even for simple custom tables. 
# - An implementation should check the load factor and do something if it becomes too large. 
# - load factor = number of entries / number of buckets (n/k)
# - This needs to be done only on inserts since that is the only thing that would increase it. 
# in Python dict, table size is resized when the load factor is greater than 2/3. 
# - resizing is accompanied by a full or incremental table rehash whereby existing items are mapped to new bucket locations. 

"""Shrinking"""
# - when load factor falls below a second threshold, all entries are moved to a new smaller table. 
# - should that load factor be 1/3? 

"""Add ability to delete entries"""
# - that is the only time when shrinking is relevant

"""Whether to deal with collisions"""

"""Whether to improve the hashing function"""

"""This whole thing about prime numbers"""

"""Test the hashtable by having it pick up words from a book chapter?"""








