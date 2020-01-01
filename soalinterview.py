# Author Felix Aristo

# Number 1

    def palindromeDetection(s):
        wordsReversed = s[::-1]

        if (s == wordsReversed):
            return True
        return False

    palindromeDetection("abcba") # Run the function

    # Return True

    palindromeDetection("Abcba") # Run the function

    # Return False
    
    # Big O Notation
    
    # Untuk nilai Time Complexity bernilai O(1) 
    # karena function itu menjalankan hanya sekali instuksi return.
    # Dan untuk nilai Space Complexity bernilai O(N) 
    # karena variable 'wordsReversed' membutuhkan sebuah unit ruang yang bergantung pada panjangnya data yang diberikan.

# End Number 1

# ======================================================

# Number 2

    def countChar(c):
        all_freq = {} 
        for i in c: 
            if i in all_freq: 
                all_freq[i] += 1
            else: 
                all_freq[i] = 1
        return sorted(all_freq.items())
    
    a = countChar("abdbcdeapd")

    for k, v in a:
        print(k)
        print(v)
        
    # Result 
    
    # a
    # 2
    # b
    # 2
    # c
    # 1
    # d
    # 3
    # e
    # 1
    # p
    # 1

# End Number 2

# ======================================================

# Number 3

    # HTTP POST
        # Cara kerja HTTP POST adalah mengirimkan data secara langsung untuk ditampung pada suatu action.
    
    # HTTP GET
        # Cara kerja HTTP GET adalah mengirimkan/menampilkan data berdasarkan URL yang terdeteksi dan 
        # kemudian ditampung pada suatu action.
    
# End Number 3

# ======================================================

# Number 4

    # 3 Types of Design Pattern
    
    # 1. Creational Pattern
    # Pola pada desain ini lebih mengutamakan pada pembuatan suatu objek atau instansi pada suatu kelas.
    # Contoh: Singleton, satu class hanya satu instance.
    
    # 2. Structural Pattern
    # Pola pada desain ini lebih berhubungan dengan komposisi suatu class dan object.
    # Contoh: Composite, penyusunan object pada suatu class menjadi sebuah hirarki atau tree.
    
    # 3. Behavioral Pattern
    # Pola pada desain ini lebih berhubungan dengan komunikasi antar object (tingkah laku suatu object).
    # Contoh: Overriding, Overloading, etc.

# End Number 4
