nmax = 0
try:
    value = input("Masukkan max length = ")
    nmax = int(value)
except Exception as ex:
    print("Format salah, input harus berupa angka")

nstart = 0
n = 1
nextn = n

for i in range(nmax):
    if nstart > 1:
        print(nextn)

        nstart, n = n, nextn
        nextn = nstart + n

    elif n <= 1:
        print(nstart)

    nstart += 1