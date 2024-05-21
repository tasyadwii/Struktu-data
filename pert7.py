# tabel kebenaran (logika bolean)
# and or not xor

# NOT
print("LOGIKA NOT*")
x = False
y = not x
print("Nilai dari x =", x)
print("Nilai dari y =", y)

# and (hanya bernilai True, ketika keduanya True)
#jika ada salah satu saja yang False, maka nilai False
print("\n**LOGIKA AND*")
x = False
y = False
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x = False
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = True
z = x and y
print(x, "and", y, "=", z)

# or (akan bernilai true selama ada satu aja yang true)
# bernilai salah ketika keduanya salah
print("\n**LOGIKA OR*")
x = False
y = False
z = x or y
print(x, "or", y, "=", z)

x = True
y = False
z = x or y
print(x, "or", y, "=", z)

x = False
y = True
z = x or y
print(x, "or", y, "=", z)

x = True
y = True
z = x or y
print(x, "or", y, "=", z)

# xor(akan bernilai )
#
print("\n**LOGIKA XOR*")
x = False
y = False
z = x ^ y
print(x, "xor", y, "=", z)

x = True
y = False
z = x ^ y
print(x, "xor", y, "=", z)

x = False
y = True
z = x ^ y
print(x, "xor", y, "=", z)

x = True
y = True
z = x ^ y
print(x, "xor", y, "=", z)
