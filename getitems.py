class Hashtable(object):

	table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]		


	def __getitem__(self, index):
		print ('getitem', index)
		print self.table[index]

a_hashtable = Hashtable()

a_hashtable[0]