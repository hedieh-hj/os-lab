a=input("insert:")

h, m, s =a.split(":")
sec=int(h)*3600 + int(m)*60+ int(s)
print(sec)