class Node:
    def __init__(self, player_name, ranking):
        self.player_name = player_name
        self.ranking = ranking
        self.next = None

class ChessTournament:
    def __init__(self):
        self.head = None

    def register_player(self, player_name, ranking):
        new_player = Node(player_name, ranking)
        if self.head is None:
            self.head = new_player
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_player

    def eliminate_player(self, player_name):
        if self.head is None:
            return
        
        if self.head.player_name == player_name:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.player_name == player_name:
                    current.next = current.next.next
                    return
                current = current.next

    def print_players_by_ranking(self):
        if self.head is None:
            print("Belum ada peserta terdaftar.")
            return

        players = []
        current = self.head
        while current is not None:
            players.append((current.player_name, current.ranking))
            current = current.next
        
        players = sorted(players, key=lambda x: x[1], reverse=True)
        print("Daftar peserta berdasarkan peringkat:")
        for player in players:
            print("Nama: {}, Peringkat: {}".format(player[0], player[1]))


# Contoh penggunaan program
tournament = ChessTournament()

# Mendaftarkan peserta turnamen
tournament.register_player("Sri", 3)
tournament.register_player("Yuni", 1)
tournament.register_player("Wangi", 2)

# Mencetak daftar peserta berdasarkan peringkat
tournament.print_players_by_ranking()

# Menghapus peserta yang telah kalah
tournament.eliminate_player("Sri")

# Mencetak daftar peserta setelah penghapusan
tournament.print_players_by_ranking()
