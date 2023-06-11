class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return
        
        if self.head.description == description:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.description == description:
                    current.next = current.next.next
                    return
                current = current.next

    def print_tasks_by_priority(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        tasks = []
        current = self.head
        while current is not None:
            tasks.append((current.description, current.priority))
            current = current.next
        
        tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
        print("Daftar tugas berdasarkan prioritas:")
        for task in tasks:
            print("Deskripsi: {}, Prioritas: {}".format(task[0], task[1]))


# Contoh penggunaan program
task_list = TaskList()

# Menambahkan tugas baru
task_list.add_task("Mengerjakan tugas rumah", 3)
task_list.add_task("Belajar untuk ujian", 2)
task_list.add_task("Olahraga", 1)

# Mencetak daftar tugas berdasarkan prioritas
task_list.print_tasks_by_priority()

# Menghapus tugas
task_list.remove_task("Belajar untuk ujian")

# Mencetak daftar tugas setelah penghapusan
task_list.print_tasks_by_priority()
