class Node:
    def __init__(self, item_name, importance_level):
        self.item_name = item_name
        self.importance_level = importance_level
        self.next = None

class AdventureBag:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, importance_level):
        new_item = Node(item_name, importance_level)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_item

    def remove_item(self, item_name):
        if self.head is None:
            return
        
        if self.head.item_name == item_name:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.item_name == item_name:
                    current.next = current.next.next
                    return
                current = current.next

    def print_items_by_importance(self):
        if self.head is None:
            print("Tas kosong.")
            return

        items = []
        current = self.head
        while current is not None:
            items.append((current.item_name, current.importance_level))
            current = current.next
        
        items = sorted(items, key=lambda x: x[1], reverse=True)
        print("Daftar item dalam tas berdasarkan tingkat kepentingan:")
        for item in items:
            print("Item: {}, Tingkat Kepentingan: {}".format(item[0], item[1]))


# Contoh penggunaan program
adventure_bag = AdventureBag()

# Menambahkan item ke dalam tas
adventure_bag.add_item("New Default Skin", 10)
adventure_bag.add_item("item Bambu", 5)
adventure_bag.add_item("Kunci Emas", 8)

# Mencetak daftar item dalam tas berdasarkan tingkat kepentingan
adventure_bag.print_items_by_importance()

# Menghapus item dari dalam tas
adventure_bag.remove_item("Kunci Emas")

# Mencetak daftar item setelah penghapusan
adventure_bag.print_items_by_importance()
