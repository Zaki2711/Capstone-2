# Dataset awal (list of dict) sesuai file The Armoury Sales
#from tabulate import tabulate

from tabulate import tabulate

customers = [
    {"Customer ID":"A001","Customer":"Sport Direct","Produk":"Jacket","Item Code":"AR001","Jenis Customer":"Strategic","Payment Terms":"30 hari","Garansi":"Ya","Discount":0.15,"Order Qty (pcs)":200},
    {"Customer ID":"A002","Customer":"Planet Sport","Produk":"Jersey Home","Item Code":"AR002","Jenis Customer":"Core","Payment Terms":"15 hari","Garansi":"Ya","Discount":0.1,"Order Qty (pcs)":150},
    {"Customer ID":"A003","Customer":"Foot Locker","Produk":"Jersey Away","Item Code":"AR003","Jenis Customer":"Priority","Payment Terms":"30 hari","Garansi":"Tidak","Discount":0.0,"Order Qty (pcs)":100},
    {"Customer ID":"A004","Customer":"Sport Station","Produk":"Jacket","Item Code":"AR001","Jenis Customer":"Others","Payment Terms":"Cash","Garansi":"Tidak","Discount":0.0,"Order Qty (pcs)":50},
    {"Customer ID":"A005","Customer":"Top Skor","Produk":"Jersey Home","Item Code":"AR002","Jenis Customer":"Strategic","Payment Terms":"45 hari","Garansi":"Ya","Discount":0.15,"Order Qty (pcs)":300},
    {"Customer ID":"A006","Customer":"JD Sport","Produk":"Jersey Away","Item Code":"AR003","Jenis Customer":"Core","Payment Terms":"30 hari","Garansi":"Ya","Discount":0.1,"Order Qty (pcs)":120},
    {"Customer ID":"A007","Customer":"Jerseyzone","Produk":"Jacket","Item Code":"AR001","Jenis Customer":"Priority","Payment Terms":"15 hari","Garansi":"Tidak","Discount":0.0,"Order Qty (pcs)":80},
    {"Customer ID":"A008","Customer":"RankSports","Produk":"Jersey Home","Item Code":"AR002","Jenis Customer":"Others","Payment Terms":"Cash","Garansi":"Tidak","Discount":0.0,"Order Qty (pcs)":60},
    {"Customer ID":"A009","Customer":"The Athlete's Foot","Produk":"Jersey Away","Item Code":"AR003","Jenis Customer":"Core","Payment Terms":"Cash","Garansi":"Ya","Discount":0.1,"Order Qty (pcs)":20},
    {"Customer ID":"A010","Customer":"Footgear","Produk":"Jacket","Item Code":"AR001","Jenis Customer":"Strategic","Payment Terms":"Cash","Garansi":"Ya","Discount":0.15,"Order Qty (pcs)":15}
]

# Recycle bin
recycle_bin = []

# Validasi aturan bisnis
def validate_business_rules(data):
    seg = data["Jenis Customer"]
    qty = data["Order Qty (pcs)"]
    pay = data["Payment Terms"]
    disc = data["Discount"]
    garansi = data["Garansi"]

    if seg == "Strategic":
        if qty < 25 and (disc > 0 or pay != "Cash"):
            return False
        if pay not in ["Cash","15 hari","30 hari","45 hari"]:
            return False
        if disc > 0.15 or garansi != "Ya":
            return False

    elif seg == "Core":
        if qty < 50 and (disc > 0 or pay != "Cash"):
            return False
        if pay not in ["Cash","15 hari","30 hari"]:
            return False
        if disc > 0.1 or garansi != "Ya":
            return False

    elif seg == "Priority":
        if qty < 50 and (disc > 0 or pay != "Cash"):
            return False
        if pay not in ["Cash","15 hari"]:
            return False
        if disc > 0.05 or garansi != "Ya":
            return False

    elif seg == "Others":
        if qty < 50 and pay != "Cash":
            return False
        if disc != 0 or garansi != "Tidak":
            return False
        if pay not in ["Cash","15 hari"]:
            return False

    return True

# Menu Lihat Data
def read_menu():
    print("\n=== Lihat Data Customer ===")
    print("1. All customer list")
    print("2. Specific Customer")
    print("3. Kembali ke Main Menu")
    choice = input("Pilih: ")

    if choice == "1":
        print(tabulate(customers, headers="keys", tablefmt="simple"))
    elif choice == "2":
        cid = input("Masukkan Customer ID: ")
        found = [c for c in customers if c["Customer ID"] == cid]
        if not found:
            print("The data you are looking for does not exist")
        else:
            print(tabulate(found, headers="keys", tablefmt="simple"))
    elif choice == "3":
        return

# Menu Tambah Data Customer
def create_menu():
    print("\n=== Tambah Data Customer ===")
    print("1. Menambahkan Data Customer")
    print("2. Kembali ke Main Menu")
    choice = input("Pilih: ")

    if choice == "2":
        return

    if choice == "1":
        cid = input("Masukkan Customer ID: ")
        if any(c["Customer ID"] == cid for c in customers):
            print("Data already exist")
            return

    nama = input("Nama Customer: ")
    produk = input("Product name: ")
    pid = input("Product ID: ")
    seg = input("Segmentasi Customer (Strategic/Core/Priority/Others): ")
    pay = input("Payment Terms (hari): ")
    garansi = input("Garansi (Ya/Tidak): ")
    disc = float(input("Discount (0 jika tidak ada): "))
    qty = int(input("Order Qty (pcs): "))

    new_data = {"Customer ID":cid,"Customer":nama,"Produk":produk,"Item Code":pid,
                "Jenis Customer":seg,"Payment Terms":pay,"Garansi":garansi,
                "Discount":disc,"Order Qty (pcs)":qty}

    print(tabulate([new_data], headers="keys", tablefmt="simple"))

    if not validate_business_rules(new_data):
        print("data inputted is not match")
        return

    confirm = input("Apakah anda yakin untuk memasukkan data ini? (Y/N): ")
    if confirm.upper() == "Y":
        customers.append(new_data)
        print("Data successfully saved")

# Menu Update Data
def update_menu():
    print("\n=== Update Data Customer ===")
    print("1. Edit Data Customer")
    print("2. Kembali ke Main Menu")
    choice = input("Pilih: ")

    if choice == "2":
        return

    if choice == "1":
        cid = input("Masukkan Customer ID: ")

    found = [c for c in customers if c["Customer ID"] == cid]
    if not found:
        print("The data you are looking for does not exist")
        return

    data = found[0]
    print(tabulate([data], headers="keys", tablefmt="simple"))

    field = input("Masukkan nama kolom yang ingin diubah: ")
    if field not in data:
        print("Kolom tidak ditemukan")
        return

    new_val = input("Masukkan nilai baru: ")
    if field == "Discount":
        new_val = float(new_val)
    elif field == "Order Qty (pcs)":
        new_val = int(new_val)

    data[field] = new_val

    if not validate_business_rules(data):
        print("data inputted is not match")
        return

    confirm = input("Apakah anda yakin untuk mengupdate data? (Y/N): ")
    if confirm.upper() == "Y":
        print("Data successfully saved")

# Menu Delete Data + Recycle Bin
def delete_menu():
    print("\n=== Delete Data Customer ===")
    print("1. Hapus Data Customer (pindah ke Recycle Bin)")
    print("2. Kembali ke Main Menu")
    choice = input("Pilih: ")

    if choice == "2":
        return

    if choice == "1":
        cid = input("Masukkan Customer ID: ")

    found = [c for c in customers if c["Customer ID"] == cid]
    if not found:
        print("The data you are looking for does not exist")
        return

    print(tabulate(found, headers="keys", tablefmt="simple"))

    confirm = input("Apakah anda yakin untuk menghapus data ini? (Y/N): ")
    if confirm.upper() == "Y":
        customers.remove(found[0])
        recycle_bin.append(found[0])
        print("Data moved to Recycle Bin")

# Menu Recycle Bin
def recycle_menu():
    print("\n=== Recycle Bin ===")
    print("1. Lihat Recycle Bin")
    print("2. Restore Data")
    print("3. Hapus Permanen")
    print("4. Kembali ke Main Menu")
    choice = input("Pilih: ")

    if choice == "1":
        print(tabulate(recycle_bin, headers="keys", tablefmt="simple"))

    elif choice == "2":
        cid = input("Masukkan Customer ID untuk restore: ")
        found = [c for c in recycle_bin if c["Customer ID"] == cid]
        if not found:
            print("Data tidak ditemukan di Recycle Bin")
        else:
            recycle_bin.remove(found[0])
            customers.append(found[0])
            print("Data restored")

    elif choice == "3":
        cid = input("Masukkan Customer ID untuk hapus permanen: ")
        found = [c for c in recycle_bin if c["Customer ID"] == cid]
        if not found:
            print("Data tidak ditemukan")
        else:
            recycle_bin.remove(found[0])
            print("Data permanently deleted")

    elif choice == "4":
        return

# Laporan Custom Grouping
def report_menu():
    print("\n=== Laporan Grouping ===")
    print("Pilih kolom untuk grouping:")
    print("1. Jenis Customer")
    print("2. Produk")
    print("3. Payment Terms")
    print("4. Garansi")
    print("5. Kembali ke Main Menu")
    choice = input("Pilih: ")

    mapping = {
        "1": "Jenis Customer",
        "2": "Produk",
        "3": "Payment Terms",
        "4": "Garansi"
    }

    if choice == "5":
        return

    if choice not in mapping:
        print("Pilihan tidak valid")
        return

    col = mapping[choice]

    # Grouping
    groups = {}
    for c in customers:
        key = c[col]
        if key not in groups:
            groups[key] = []
        groups[key].append(c)

    # Tampilkan laporan per grup
    for key, items in groups.items():
        print(f"\n=== Group: {key} ===")
        print(tabulate(items, headers="keys", tablefmt="simple"))

# Main Menu
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Lihat Data Customer")
        print("2. Menambahkan Data Customer")
        print("3. Edit Data Customer")
        print("4. Menghapus Data Customer")
        print("5. Recycle Bin")
        print("6. Laporan Grouping")
        print("7. Exit")
        choice = input("Pilih menu: ")

        if choice == "1":
            read_menu()
        elif choice == "2":
            create_menu()
        elif choice == "3":
            update_menu()
        elif choice == "4":
            delete_menu()
        elif choice == "5":
            recycle_menu()
        elif choice == "6":
            report_menu()
        elif choice == "7":
            print("Program selesai.")
            break
        else:
            print("The option you entered is not valid")

# Jalankan program
main_menu()