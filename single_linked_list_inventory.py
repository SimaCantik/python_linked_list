class Node:
    def __init__(self, product_name, product_code, stock_quantity):
        self.product_name = product_name
        self.product_code = product_code
        self.stock_quantity = stock_quantity
        self.next = None

class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, product_name, product_code, stock_quantity):
        new_product = Node(product_name, product_code, stock_quantity)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, product_code):
        if self.head is None:
            return
        
        if self.head.product_code == product_code:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.product_code == product_code:
                    current.next = current.next.next
                    return
                current = current.next

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
            return

        current = self.head
        print("Daftar produk dan jumlah stok:")
        while current is not None:
            print("Nama Produk: {}, Kode Produk: {}, Jumlah Stok: {}".format(current.product_name, current.product_code, current.stock_quantity))
            current = current.next


# Contoh penggunaan program
inventory = InventoryManagement()

# Menambahkan produk ke inventaris
inventory.add_product("Buku", "BK001", 100)
inventory.add_product("Senter", "SN001", 50)
inventory.add_product("Pulpen", "PL001", 75)

# Mencetak daftar produk beserta jumlah stoknya
inventory.print_inventory()

# Menghapus produk dari inventaris
inventory.remove_product("PL001")

# Mencetak daftar produk setelah penghapusan
inventory.print_inventory()
