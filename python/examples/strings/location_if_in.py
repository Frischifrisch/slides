sub = "cat"
txt = "The black cat climbed the green tree"

if sub in txt:
    loc = txt.index(sub)
    print(f"{sub} is at {loc}")

sub = "dog"
if sub in txt:
    loc = txt.index(sub)
    print(f"{sub} is at {loc}")
    
# cat is at 10
