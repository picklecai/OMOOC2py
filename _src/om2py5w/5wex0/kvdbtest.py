#_*_coding:utf-8_*_
import sae.kvdb

kv = sae.kvdb.KVClient()

kv.set("some_key","Some value")
kv.set("another_key", 3)
kv.delete("another_key")
kv.set('a',{'aa':[1,2,3,5]})

kv.set('c:1','a')
kv.set('c:2','b')
kv.set('c:3','c')
kv.set('c:4','d')

for k in kv.getkeys_by_prefix('c:'):
	print k
	print kv.get(k)