 # percabangan dan perulangan
def main():
    # Input nilai
    nilai = float(input("Masukkan nilai Anda: "))

    # Percabangan
    if nilai >= 80:
        print("Nilai Anda adalah A")
    elif nilai >= 70:
        print("Nilai Anda adalah B")
    elif nilai >= 60:
        print("Nilai Anda adalah C")
    elif nilai >= 50:
        print("Nilai Anda adalah D")
    else:
        print("Anda tidak lulus")

    # Perulangan
    for i in range(1, 6):
        if i % 2 == 0:
            print(f'Iterasi ke-{i}: Bilangan genap')
        else:
            print(f'Iterasi ke-{i}: Bilangan ganjil')

if __name__ == "__main__":
    main()
