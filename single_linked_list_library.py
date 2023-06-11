class Node:
    def __init__(self, visitor_name, book_title):
        self.visitor_name = visitor_name
        self.book_title = book_title
        self.next = None

class LibraryRecord:
    def __init__(self):
        self.head = None

    def add_record(self, visitor_name, book_title):
        new_record = Node(visitor_name, book_title)
        if self.head is None:
            self.head = new_record
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_record

    def print_records(self):
        if self.head is None:
            print("Tidak ada catatan peminjaman.")
            return

        current = self.head
        while current is not None:
            print("Pengunjung: {}, Judul Buku: {}".format(current.visitor_name, current.book_title))
            current = current.next


# Contoh penggunaan program
library_records = LibraryRecord()

# Menambahkan catatan peminjaman buku
library_records.add_record("Sima", "Putri salju")
library_records.add_record("Dario", "Si Kancil")
library_records.add_record("Ibnu", "25 Nabi")

# Mencetak daftar catatan peminjaman
library_records.print_records()
