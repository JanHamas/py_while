class Mobile:
    fp = "yes"
    
    @classmethod
    def is_fp(cls):
        print("finger print ",cls.fp)
    
realme = Mobile()
redme = Mobile()
geek = Mobile()

print("realme:",Mobile.fp)
print("redme:",Mobile.fp)
print("geek:",Mobile.fp)
print()
Mobile.fp = "no"
print("realme:",Mobile.fp)
print("redme:",Mobile.fp)
print("geek:",Mobile.fp)