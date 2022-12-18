import streamlit as st
import interface

def convert(lst):
    return ([i for i in lst.split()])

def CYK(sentence):
    rule = [["K", "X","O"],
            ["K", "X", "X"],
            ["K", "Q", "Ket"],
            ["Q", "X", "Z"],
            ["K", "X", "Y"],
            ["K", "X", "Z"],
            ["K", "X", "Pel"],
            ["K", "X", "Ket"],
            ["K", "S", "P"],
            ["X", "S", "P"],
            ["Y", "O", "Ket"],
            ["Z", "O", "Pel"],
            ["NP", "Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Sepatu", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas",    "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras",
                "Itu", "Saya", "Kami", "Dia", "Kita", "Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"],
            ["NP", "Noun", "NP"],
            ["NP", "NP", "Adj"],
            ["NP", "NP", "Pronoun"],
            ["NP", "NP", "PropNoun"],
            ["NP", "Adj", "NP"],
            ["VP", "Adv", "VP"],
            ["VP", "Verb", "VP"],
            ["VP", "Adj", "VP"],
            ["VP", "Membersihkan", "Mencintai", "Memperlancar", "Memberlakukan", "Mencari", "Memperbaiki", "Membeli", "Mencuci",
                "Menanam", "Melukis", "Mencarikan", "Membelikan", "Menamai", "Menghadiahi", "Mengajarkan", "Membuatkan", "Mengirimi",
                "Mencicipi", "Memberi", "Berjumalh", "Mengemukakan", "Menjadi", "Merupakan", "Kehilangan", "Kedapatan",
                "Merokok", "Kejatuhan", "Pergi", "Tidur", "Membusuk", "Duduk", "Bernyanyi", "Membangun", "Bertani", "Terkejut",
                "Kedinginan", "Mandi", "Bekerja", "Mulai", "Terus"],
            ["PP", "Prep", "VP"],    
            ["PP", "Prep", "NP"],
            ["PP", "Prep", "PP"],
            ["PP", "Noun", "VP"],

            ["S", "Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Sepatu", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas",    "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras",
                "Itu", "Saya", "Kami", "Dia", "Kita", "Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"], 
            ["S", "Noun", "NP"],
            ["S", "NP", "Adj"],
            ["S", "NP", "Pronoun"],
            ["S", "NP", "PropNoun"],
            ["S", "Adj", "NP"],

            ["P", "Adv", "VP"],
            ["P", "Verb", "VP"],
            ["P", "Adj", "VP"],
            ["P", "Membersihkan", "Mencintai", "Memperlancar", "Memberlakukan", "Mencari", "Memperbaiki", "Membeli", "Mencuci",
                "Menanam", "Melukis", "Mencarikan", "Membelikan", "Menamai", "Menghadiahi", "Mengajarkan", "Membuatkan", "Mengirimi",
                "Mencicipi", "Memberi", "Berjumalh", "Mengemukakan", "Menjadi", "Merupakan", "Kehilangan", "Kedapatan",
                "Merokok", "Kejatuhan", "Pergi", "Tidur", "Membusuk", "Duduk", "Bernyanyi", "Membangun", "Bertani", "Terkejut",
                "Kedinginan", "Mandi", "Bekerja", "Mulai", "Terus"],

            ["O", "Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Sepatu", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas",    "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras",
                "Itu", "Saya", "Kami", "Dia", "Kita", "Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"],
            ["O", "Noun", "NP"],
            ["O", "NP", "Adj"],
            ["O", "NP", "Pronoun"],
            ["O", "NP", "PropNoun"],
            ["O", "Adj", "NP"],

            ["Ket", "Prep", "VP"],    
            ["Ket", "Prep", "NP"],
            ["Ket", "Prep", "PP"],
            ["Ket", "Noun", "VP"],
            ["Ket", "Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Sepatu", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas",    "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras",
                "Itu", "Saya", "Kami", "Dia", "Kita","Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"],            

            ["Pel", "Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas",    "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras",
                "Itu", "Saya", "Kami", "Dia", "Kita","Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"],
            ["Pel", "Noun", "NP"],
            ["Pel", "NP", "Adj"],
            ["Pel", "NP", "Pronoun"],
            ["Pel", "NP", "PropNoun"],
            ["Pel", "Adj", "NP"],
            ["Pel", "Num", "NP"],
            ["Pel", "Adv", "VP"],
            ["Pel", "Verb", "VP"],
            ["Pel", "Membersihkan", "Mencintai", "Memperlancar", "Memberlakukan", "Mencari", "Memperbaiki", "Membeli", "Mencuci",
                "Menanam", "Melukis", "Mencarikan", "Membelikan", "Menamai", "Menghadiahi", "Mengajarkan", "Membuatkan", "Mengirimi",
                "Mencicipi", "Memberi", "Berjumalh", "Mengemukakan", "Menjadi", "Merupakan", "Kehilangan", "Kedapatan",
                "Merokok", "Kejatuhan", "Pergi", "Tidur", "Membusuk", "Duduk", "Bernyanyi", "Membangun", "Bertani", "Terkejut",
                "Kedinginan", "Mandi", "Bekerja", "Mulai", "Terus"],

            ["Noun", "Atas" ,"Adik", "Ibu", "Kamar", "Rakyat", "Pemimpin", "Rumah", "Polisi", "Arus", "Lalu-Lintas",
                "Pemerintah", "Peraturan", "Orang", "Pekerjaan", "Tukang", "Jalan", "Sepatu", "Kamar", "Mandi", "Bibi",
                "Sayur", "Bayam", "Ayah", "Kangkung", "Akar", "Penari", "Kanvas", "Tidur", "Kakak", "Baju", "Kucing",
                "Tiket", "Pesawat", "Anak", "Pelajaran", "Matematika", "Bolu", "Kukus", "Bapak", "Guru", "Kado", "Masakan",
                "Nenek", "Motivasi", "Paman", "Belas", "Buah", "Gagasan", "Kota", "Nasi", "Bubur", "Kelapa", "Buku", "Sumber",
                "Ilmu", "Kunci", "Aktor", "Mobil", "Pagi", "Negara", "Mata", "Pencaharian", "Penduduk", "Gunung", "Hari", "Buah-buahan",
                "Pinggir", "Sungai", "Depan", "Kelas","Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila", "Sekarang"],
            ["Verb", "Membersihkan", "Mencintai", "Memperlancar", "Memberlakukan", "Mencari", "Memperbaiki", "Membeli", "Mencuci",
                "Menanam", "Melukis", "Mencarikan", "Membelikan", "Menamai", "Menghadiahi", "Mengajarkan", "Membuatkan", "Mengirimi",
                "Mencicipi", "Memberi", "Berjumalh", "Mengemukakan", "Menjadi", "Merupakan", "Kehilangan", "Kedapatan",
                "Merokok", "Kejatuhan", "Pergi", "Tidur", "Membusuk", "Duduk", "Bernyanyi", "Membangun", "Bertani", "Terkejut",
                "Kedinginan", "Mandi", "Bekerja", "Mulai", "Terus"],
            ["Adv", "Sedang", "Sudah", "Pasti", "Akan", "Segera", "Selalu", "Telah", "Harus"], 
            ["Adj", "Jujur", "Sukar", "Rusak", "Baru", "Kecil", "Bagus", "Kaya", "Besar", "Terkenal", "Keras"],
            ["PropNoun", "Arya", "Bali", "Putri", "Tino", "Intan", "David", "Adel", "Gita", "Devit", "Teja", "Mario", "Momo",
                "Ary", "Duta", "Deva", "Sukamandi", "Farel", "Bayu", "Dila"],
            ["Pronoun", "Itu", "Saya", "Kami", "Dia", "Kita"],    
            ["Prep", "Di", "Sejak", "Untuk", "Ketika", "Ke"],
            ["Num", "Beberapa", "Dua", "Satu"]]
    cnf = rule.copy()
    word = convert(sentence)
    product = list()
    combinedCNF = list()
    for i in range(len(cnf)):
        product.append(cnf[i].pop(0))
    for i in range(len(cnf)):
        j = (len(cnf[i]))
        if j == 2:
            combinedCNF.append(cnf[i][0]+cnf[i][1])
        elif j == 1:
            combinedCNF.append(cnf[i][0])
        else:
            combinedCNF.append("")

    variabel = dict()

    Table = [["" for x in range(len(word))] for y in range(len(word))]

    for i in range(1,len(word)+1):
        j = i
        variabel[i,j] = []
        for k in range(len(cnf)):
            if word[i-1] in cnf[k]:
                variabel[i,j].append(product[k])
                Table[i-1][j-1] = "V"

    for k in range(len(word)-1):
        for i in range(1,len(word)-k):
            j = i+k+1
            result = list()
            if i != j and i < j and j <= len(word) and Table[i-1][j-1] != "V":   
                if j - i == k+1:
                    for l in range(j-i):        
                        for p in range(len(variabel[i,i+l])):
                            for q in range(len(variabel[i+1+l,j])):
                                result.append(variabel[i,i+l][p]+variabel[i+1+l,j][q])

                variabel[i,j] = []
                for x in range(len(combinedCNF)):
                    if combinedCNF[x] in result:
                        variabel[i,j].append(product[x])
            if j != len(word):
                del result
        
    if "K" in variabel[1,len(word)]:
        interface.valid = 'y'
        interface.result = result.copy()
    else:
        interface.valid = 'x' 
 
        
    
