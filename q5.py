a = "The quick brown fox jumps over the lazy dog"
index = a.find("fox")
if index == -1:
    print("not present")
else:
    print("present at",index,"position")
