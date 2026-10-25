class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Behavior karakter mulai berlari
        self.is_running = True
        print(f"{self.nama} mulai berlari menghindari kejaran inspektur!")

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin dan tingkatkan skor
        self.koin += jumlah
        self.skor += jumlah * 10
        print(f"{self.nama} mendapatkan {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Kondisi menabrak rintangan / game over
        self.is_running = False
        print(f"BAM! {self.nama} menabrak rintangan. Game Over!")

    def info_player(self):
        # TODO 5: Cetak status terkini pemain
        status = "Sedang Berlari" if self.is_running else "Berhenti / Game Over"
        print(f"--- Status Player ---")
        print(f"Nama       : {self.nama}")
        print(f"Skor       : {self.skor}")
        print(f"Jumlah Koin: {self.koin}")
        print(f"Status     : {status}\n")

# --- PENGUJIAN OBJEK ---
player1 = KarakterSurfer("Jake")
player1.berlari()
player1.ambil_koin(5)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()