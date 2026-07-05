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

#print(tabulate(customers, headers="keys", tablefmt="simple"))

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
    
    from tabulate import tabulate
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
    
    # Jika pilih 2, langsung kembali ke menu utama
    if choice == "2":
        return
    # Jika pilih 1, Lanjutkan Proses Input Data Customer

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

    from tabulate import tabulate
    new_data = {"Customer ID":cid,"Customer":nama,"Produk":produk,"Item Code":pid,
                "Jenis Customer":seg,"Payment Terms":pay,"Garansi":garansi,
                "Discount":disc,"Order Qty (pcs)":qty}
    
    # tampilkan data baru dalam bentuk tabel rapi
    print(tabulate([new_data], headers="keys", tablefmt="simple"))

    if not validate_business_rules(new_data):
        print("data inputted is not match")
        return

    confirm = input(f"Apakah anda yakin untuk memasukkan data {new_data}? (Y/N): ")
    if confirm.upper() == "Y":
        customers.append(new_data)
        print("Data successfully saved")

# Menu Update Data
def update_menu():
    print("\n=== Update Data Customer ===")
    print("1. Edit Data Customer")
    print("2. Kembali ke Main Menu")
    choice = input("Pilih: ")
    
   # Jika pilih 2, langsung kembali ke menu utama
    if choice == "2":
        return
    
    # Jika pilih 1, Lanjutkan Proses Input Data Customer    
    if choice == "1":
        cid = input("Masukkan Customer ID: ")
    found = [c for c in customers if c["Customer ID"] == cid]
    if not found:
        print("The data you are looking for does not exist")
        return

    data = found[0]
    #print("Data lama:", data)
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

# Menu Delete Data
def delete_menu():
    print("\n=== Delete Data Customer ===")
    print("1. Hapus Data Customer")
    print("2. Kembali ke Main Menu")
    choice = input("Pilih: ")
    
   # Jika pilih 2, langsung kembali ke menu utama
    if choice == "2":
        return
    
    # Jika pilih 1, Lanjutkan Proses Input Data Customer to delete
    if choice == "1":
        cid = input("Masukkan Customer ID: ")
    found = [c for c in customers if c["Customer ID"] == cid]
    if not found:
        print("The data you are looking for does not exist")
        return
    else:
        # tampilkan hasil pencarian dalam bentuk tabel rapi
        print(tabulate(found, headers="keys", tablefmt="simple"))

    #print(found[0])
    confirm = input("Apakah anda yakin untuk menghapus data ini? (Y/N): ")
    if confirm.upper() == "Y":
        customers.remove(found[0])
        print("Data successfully deleted")

# Main Menu
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Lihat Data Customer")
        print("2. Menambahkan Data Customer")
        print("3. Edit Data Customer")
        print("4. Menghapus Data Customer")
        print("5. Exit")
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
            print("Program selesai.")
            break
        else:
            print("The option you entered is not valid")

# Jalankan program
main_menu()
