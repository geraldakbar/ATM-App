import tkinter as tk

transaksi_lagi = True

transfer = False
penarikan = False
cek_saldo = False
masukkan_nominal = False

nama = {'a': '0000', 'b': '1111', 'c': '2222'}

jumlah_saldo = {'a': 500000, 'b': 1000000, 'c': 2000000}
saldo = 0
nomor_rekening = ""

def main():
    root = tk.Tk()
    root.geometry("350x350")
    root.configure(bg="white")
    root.winfo_toplevel().title("ATM")

    def kurang(jumlah):
        global saldo
        saldo -= jumlah

    def choice_window():
        global choice
        choice = tk.Tk()
        choice.geometry("350x350")
        choice.winfo_toplevel().title("ATM")
        choice.configure(bg="white")
        pilih_transaksi = tk.Label(master=choice, text="Pilih Transaksi", bg="white", font=('Arial', 24))
        pilih_transaksi.pack()
        transfer_button = tk.Button(master=choice, text="Pengiriman tunai", height=3, width=15, pady=5,
                                    command=lambda: transfer_window())
        transfer_button.pack(pady=8)
        withdraw_button = tk.Button(master=choice, text="Penarikan Tunai", height=3, width=15, pady=5,
                                    command=lambda: withdraw_window())
        withdraw_button.pack(pady=8)
        savings_button = tk.Button(master=choice, text="Saldo", height=3, width=15, pady=5,
                                   command=lambda: savings_window())
        savings_button.pack(pady=8)
        choice.mainloop()

    def transfer_window():
        global tf
        global transfer
        transfer = True
        tf = tk.Tk()
        tf.geometry("350x350")
        tf.winfo_toplevel().title("ATM")
        antar_rekening = tk.Button(master=tf, text="Antar Rekening", height=3, width=15, pady=5,
                                   command=lambda: no_rekening())
        antar_rekening.place(x=125, y=50)
        antar_bank = tk.Button(master=tf, text="Antar Bank", height=3, width=15, pady=5,
                               command=lambda: input_kode_bank())
        antar_bank.place(x=125, y=150)
        tf.mainloop()

    def input_kode_bank():
        global bank_lain
        bank_lain = True
        global kb
        kb = tk.Tk()
        kb.geometry("350x350")
        Label = tk.Label(master=kb, text="Masukkan Kode Bank Tujuan", bg="white", font=('Arial', 18))
        Label.pack(pady=10)
        kode_bank = tk.Entry(master=kb, font=('Arial', 16))
        kode_bank.pack()
        global kode
        kode = kode_bank.get()
        enter = tk.Button(master=kb, text="Enter", command=lambda: no_rekening())
        enter.pack(pady=10)
        kb.mainloop()

    def no_rekening():
        global rek
        rek = tk.Tk()
        rek.geometry("350x350")
        tk.Label(master=rek, text="Masukkan no rekening tujuan").pack()
        global no_rek_entry
        no_rek_entry = tk.Entry(master=rek, font=('Arial', 16))
        no_rek_entry.pack(pady=10)
        enter_rek = tk.Button(master=rek, text="Enter", command=lambda: trf_amount())
        enter_rek.pack()
        global nomor_rekening
        nomor_rekening = str(no_rek_entry.get())
        rek.mainloop()

    def withdraw_window():
        global wd
        global penarikan
        penarikan = True
        wd = tk.Tk()
        wd.geometry("350x350")
        global saldo
        seratus_ribu = tk.Button(master=wd, text="100.000", width=20, command=lambda: tb1_window())
        seratus_ribu.place(x=0, y=50)
        duaratus_ribu = tk.Button(master=wd, text="200.000", width=20, command=lambda: tb2_window())
        duaratus_ribu.place(x=0, y=150)
        tigaratus_ribu = tk.Button(master=wd, text="300.000", width=20, command=lambda: tb3_window())
        tigaratus_ribu.place(x=0, y=250)
        empatratus_ribu = tk.Button(master=wd, text="400.000", width=20, command=lambda: tb4_window())
        empatratus_ribu.place(x=200, y=50)
        limaratus_ribu = tk.Button(master=wd, text="500.000", width=20, command=lambda: tb5_window())
        limaratus_ribu.place(x=200, y=150)
        pilihan_lain = tk.Button(master=wd, text="Pilihan lain", width=20, command=lambda: wd_pilihan_lain())
        pilihan_lain.place(x=200, y=250)
        wd.mainloop()

    def trf_amount():
        global ta
        ta = tk.Tk()
        ta.geometry("350x350")
        seratus_ribu = tk.Button(master=ta, text="100.000", width=20, command=lambda: konfirmasi_transfer1())
        seratus_ribu.place(x=0, y=50)
        duaratus_ribu = tk.Button(master=ta, text="200.000", width=20, command=lambda: konfirmasi_transfer2())
        duaratus_ribu.place(x=0, y=150)
        tigaratus_ribu = tk.Button(master=ta, text="300.000", width=20, command=lambda: konfirmasi_transfer3())
        tigaratus_ribu.place(x=0, y=250)
        empatratus_ribu = tk.Button(master=ta, text="400.000", width=20, command=lambda: konfirmasi_transfer4())
        empatratus_ribu.place(x=200, y=50)
        limaratus_ribu = tk.Button(master=ta, text="500.000", width=20, command=lambda: konfirmasi_transfer5())
        limaratus_ribu.place(x=200, y=150)
        pilihan_lain = tk.Button(master=ta, text="Pilihan lain", width=20, command=lambda: trf_pilihan_lain())
        pilihan_lain.place(x=200, y=250)
        ta.mainloop()

    def trf_pilihan_lain():
        global pl
        global masukkan_nominal
        masukkan_nominal = True
        pl = tk.Tk()
        tk.Label(master=pl, text="Masukkan nominal transfer").pack()
        global jumlah_trf
        jumlah_trf = tk.Entry(master=pl, font=("Arial", 16))
        jumlah_trf.pack(pady=10)
        enter_trf = tk.Button(master=pl, text="Enter", command=lambda: konfirmasi_transfer_lain())
        enter_trf.pack()
        pl.mainloop()

    def wd_pilihan_lain():
        global masukkan_nominal
        masukkan_nominal = True
        pl = tk.Tk()
        pl.geometry("350x350")
        tk.Label(master=pl, text="Masukkan nominal transfer").pack()
        global jumlah_wd
        jumlah_wd = tk.Entry(master=pl, font=('Arial', 16))
        jumlah_wd.pack(pady=10)
        enter_trf = tk.Button(master=pl, text="Enter", command=lambda: cek_nominal())
        enter_trf.pack()
        global feedback_wd
        feedback_wd = tk.Label(master=pl, text='', font=('Arial', 14))
        feedback_wd.pack()
        pl.mainloop()

    def konfirmasi_transfer_lain():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        global nominal
        nominal = int(jumlah_trf.get())
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp{nominal}")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb_lain_trf())
        benar.pack(pady=40)
        batal = tk.Button(master=kt, text="BATAL", font=('Arial', 18), command=lambda: kt.destroy())
        batal.pack(pady=10)
        kt.mainloop()

    def konfirmasi_transfer1():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp100.000")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb1_window())
        benar.pack(pady=40)
        batal = tk.Button(master=kt, text="BATAL", font=('Arial', 18), command=lambda: kt.destroy())
        batal.pack(pady=10)
        kt.mainloop()

    def konfirmasi_transfer2():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp200.000")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb2_window())
        benar.pack(pady=40)
        batal = tk.Button(master=kt, text="BATAL", font=('Arial', 18), command=lambda: kt.destroy())
        batal.pack(pady=10)
        kt.mainloop()

    def konfirmasi_transfer3():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp300.000")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb3_window())
        benar.pack(pady=40)
        batal = tk.Button(master=kt, text="BATAL", font=('Arial', 18), command=lambda: kt.destroy())
        batal.pack(pady=10)
        kt.mainloop()

    def konfirmasi_transfer4():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp400.000")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb4_window())
        benar.pack(pady=40)
        batal = tk.Button(master=kt, text="BATAL", font=('Arial', 18), command=lambda: kt.destroy())
        batal.pack(pady=10)
        kt.mainloop()

    def konfirmasi_transfer5():
        global kt
        kt = tk.Tk()
        kt.geometry("350x350")
        global nomor_rekening
        nomor_rekening = no_rek_entry.get()
        label = tk.Label(master=kt, bg='white', font=('Arial', 16), text=f"KONFIRMASI TRANSFER:\n"
                                                                         f"Rekening Tujuan: {nomor_rekening}\n"
                                                                         f"Nominal Transfer: Rp500.000")
        label.pack(pady=30)
        benar = tk.Button(master=kt, text="KONFIRMASI", font=('Arial', 18), command=lambda: tb5_window())
        benar.place(x=50, y=200)
        kt.mainloop()

    def tb1_window():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah_saldo[nama_entry.get()] -= 100000
        if saldo >= 100000:
            kurang(100000)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n {saldo}", font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb2_window():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah_saldo[nama_entry.get()] -= 200000
        if saldo >= 200000:
            kurang(200000)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n {saldo}", font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb3_window():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah_saldo[nama_entry.get()] -= 300000
        if saldo >= 300000:
            kurang(300000)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n {saldo}", font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb4_window():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah_saldo[nama_entry.get()] -= 400000
        if saldo >= 400000:
            kurang(400000)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n {saldo}", font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb5_window():
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah_saldo[nama_entry.get()] -= 500000
        if saldo >= 500000:
            kurang(500000)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n Rp.{saldo}",
                                font=('Arial', 14))
            berhasil.pack()

        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb_lain_wd():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah = int(jumlah_wd.get())
        jumlah_saldo[nama_entry.get()] -= jumlah

        if saldo >= jumlah:
            kurang(jumlah)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n Rp.{saldo}",
                                font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def tb_lain_trf():
        global tb
        tb = tk.Tk()
        tb.geometry("350x350")
        global saldo
        saldo = jumlah_saldo[nama_entry.get()]
        jumlah = int(jumlah_trf.get())
        jumlah_saldo[nama_entry.get()] -= jumlah
        if saldo >= jumlah:
            kurang(jumlah)
            berhasil = tk.Label(master=tb, text=f"TRANSAKSI BERHASIL sisa saldo anda: \n Rp.{saldo}",
                                font=('Arial', 14))
            berhasil.pack()
        else:
            gagal = tk.Label(master=tb, text="Saldo anda tidak mencukupi")
            gagal.configure(font=('Arial', 16))
            gagal.pack()
        label = tk.Label(master=tb, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=tb, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=tb, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        tb.mainloop()

    def savings_window():
        global sav
        global cek_saldo
        cek_saldo = True
        sav = tk.Tk()
        sav.geometry("350x350")
        sav.winfo_toplevel().title("ATM")
        judul = tk.Label(master=sav, text="Jumlah Saldo Anda")
        judul.configure(font=("Arial", 30))
        judul.pack()
        saldo = tk.Label(master=sav, text=str(jumlah_saldo[nama_entry.get()]))
        saldo.configure(font=("Arial", 30))
        saldo.pack()
        label = tk.Label(master=sav, text="Apakah Anda igin melakukan \ntransaksi lagi?", font=('Arial', 16))
        label.pack()
        Transaksi_lagi = tk.Button(master=sav, text="Tidak", font=('Arial', 16), command=lambda: selesai())
        Transaksi_lagi.pack(pady=40)
        tidak_transaksi_lagi = tk.Button(master=sav, text="Ya", font=("Arial", 16), command=lambda: ulang())
        tidak_transaksi_lagi.pack(pady=10)

        sav.mainloop()

    def cek_nominal():
        if int(jumlah_wd.get()) % 100000 == 0:
            tb_lain_wd()
        else:
            feedback_wd.configure(text="Mohon masukkan nominal kelipatan 100.000")

    def cek_pin():
        try:
            int(pin_entry.get())
            false_pin = 0
            pin_benar = False
            user_benar = False
            if nama_entry.get() in nama.keys():
                user_benar = True
                if pin_entry.get() == nama[nama_entry.get()]:
                    pin_benar = True
                else:
                    false_pin += 1
                    feedback_pin.configure(text="PIN tidak valid")
            if false_pin == 3:
                feedback_pin.configure(text="Kartu diblokir")
            if user_benar and pin_benar:
                choice_window()
        except ValueError:
            feedback_pin.configure(text="PIN hanya mengandung angka")

    def selesai():
        global transaksi_lagi
        terimakasih = tk.Tk()
        terimakasih.geometry("350x350")
        label = tk.Label(master=terimakasih, text="TERIMA KASIH\n SAMPAI JUMPA KEMBALI", font=('Arial', 14))
        label.pack(pady=75)
        if transfer == True:
            rek.destroy()
            if masukkan_nominal == True:
                pl.destroy()
            tf.destroy()
            ta.destroy()
            tb.destroy()
            kt.destroy()
        if penarikan == True:
            if masukkan_nominal == True:
                pl.destroy()
            wd.destroy()
            tb.destroy()
        if cek_saldo == True:
            sav.destroy()
        transaksi_lagi = False
        root.destroy()
        choice.destroy()

    def ulang():
        if transfer == True:
            rek.destroy()
            if masukkan_nominal == True:
                pl.destroy()
            tf.destroy()
            ta.destroy()
            tb.destroy()
            kt.destroy()
        if penarikan == True:
            wd.destroy()
            if masukkan_nominal == True:
                pl.destroy()
            tb.destroy()
        if cek_saldo == True:
            sav.destroy()

    title = tk.Label(master=root, bg="white", text="ATM")
    title.config(font=("Arial", 44))
    title.pack()

    username = tk.Label(master=root, bg="white", text="Masukkan Username Anda")
    username.config(font=("Arial", 16))
    username.pack()

    nama_entry = tk.Entry(master=root, bg="white", width=10)
    nama_entry.config(font=("Arial", 24))
    nama_entry.pack()

    pin_label = tk.Label(master=root, bg="white", text="Masukkan PIN anda")
    pin_label.config(font=("Arial", 16))
    pin_label.pack()

    pin_entry = tk.Entry(master=root, bg="white", text="mohon masukkan PIN anda", width=10)
    pin_entry.config(font=("Arial", 24))
    pin_entry.pack()

    enter = tk.Button(master=root, text="Enter", command=lambda: cek_pin())
    enter.pack()

    feedback_pin = tk.Label(master=root, text='', bg='white')
    feedback_pin.pack()

    root.mainloop()

while transaksi_lagi == True:
    main()

