import hashlib
mdp='poire'
mdp=mdp.encode()
x=hashlib.sha1(mdp).hexdigest()
print(x)
