class LRU_cache(object):
	def __init__(self,size):
		self.size=size
		self.cache={}
		self.lru={}
		self.count=0
		
	def get_ele(self,k):
		#pdb.set_trace()
		if k in self.cache:
			self.lru[k]=self.count
			self.count+=1
			return self.cache[k]
		else:
			return "Not found"
			
	def set_ele(self,k,val):
		#pdb.set_trace()
		if(len(self.cache))>=self.size:
			#remove least recently used entry
			#The lambda function accesses keys value and selects minimum value among the values as minimum key.
			least_rec_key=min(self.lru.keys(),key=lambda x:self.lru[x])
			self.cache.pop(least_rec_key)
			self.lru.pop(least_rec_key)
		self.cache[k]=val
		self.lru[k]=self.count
		self.count+=1
			
lru=LRU_cache(5)
lru.set_ele(1,100)
lru.set_ele(2,200)
lru.set_ele(3,250)
lru.set_ele(4,300)
lru.set_ele(5,350)
lru.get_ele(4)
lru.get_ele(1)
lru.get_ele(2)
lru.get_ele(5)
lru.set_ele(6,90)
print(lru.cache)
print(lru.lru)