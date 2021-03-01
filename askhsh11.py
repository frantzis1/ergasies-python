my_dict={
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
     },
    }
pl=[]

totalkeys=[]
keys=[]
def find_keys(d):
 for k,v in d.items():
  keys.append(k)
  if type(v) is dict:
      find_keys(v)

find_keys(my_dict)

print(keys)
i=1
singlekeys=[]
singlekeys.append(keys[0])

for i in range(len(keys)):
    done=True
    for j in range(len(singlekeys)):
        if singlekeys[j]==keys[i]:
            done=False
    if done==True:

        singlekeys.append(keys[i])
print(singlekeys)
pl=[]
for i in range(len(singlekeys)):
    pl.append(0)

for x in range(len(keys)) :
    for y in range(len(singlekeys)):
        if keys[x] ==singlekeys[y]:
            pl[y]=pl[y]+1
print(pl)
max=0
for m in range(len(pl)):
    if pl[m]>max:
        max=pl[m]
for b in  range(len(pl)):
    if pl[b]==max:
        print("dhmofilhsterokleidh/kleidia")
        print(singlekeys[b])
