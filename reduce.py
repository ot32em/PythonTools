# Author @ OT Chen
# What @ reducing duplicated directory ex: "C:\aa\aa\aa"  to "C\aa"
# Why @ It is created because I accidentally created the same name 
#       for each torrent file which already has its name in free download
#       manager

import os
def hasDuplicated(wd, name):
	loc = os.path.join(wd, name)
	if not os.path.isdir(loc):
		raise IOError(loc + " is not dir")
	locloc = os.path.join(loc, name)
	return os.path.isdir(locloc)
	
def reduceDuplicated(wd, name):
	loc_old = os.path.join(wd, name)
	loc_new = os.path.join(wd, name + "_tmp")	
	subloc_old = os.path.join(loc_old, name)
	subloc_new = os.path.join(loc_new, name)
	if not os.path.isdir(loc_old):
		raise IOError(loc_old + " not found")
	if not os.path.isdir(subloc_old):		
		raise IOError(subloc_old + " not found")
	print("reducing " + subloc_old + " to " + loc_old)
	os.rename(loc_old, loc_new)
	os.rename(subloc_new, loc_old)
	os.rmdir(loc_new)

def listOnlyDir(loc):
	if not os.path.isdir(loc):
		raise RuntimeError(loc + " not a dir")
	return [(loc, e) for e in os.listdir(loc) if os.path.isdir(os.path.join(loc, e))]
	
if __name__ == "__main__":
	q = listOnlyDir(os.getcwd())	
	while q:
		d = q.pop(0)
		while hasDuplicated(d[0], d[1]):
			reduceDuplicated(d[0], d[1])
		q.extend(listOnlyDir(os.path.join(d[0], d[1])))
