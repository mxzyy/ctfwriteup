># PicoCTF Write-Up Binary Exploitation : heap 0
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul heap 0 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1. Diberikan 2 file yaitu file executeable dan source codenya berikut gambarnya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20141747.png)
2. Disini saya melihat source code yang diberikan, dan terdapat variabel input dan safe_var
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20142107.png)

   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20142056.png)
3. Yang perlu kita lakukan adalah melakukan overflow dari input ke safe_var, maka dari itu kita perlu mencari offset yang ada untuk melakukan overwrite,disini kita coba jalankan programnya.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20141358.png)
   Terlihat terdapat perbedaan antara pointer input dan safe_var, disini kita coba bisa mengurangi pointernya untuk menemukan offsetnya. (%p safe_var - $p input).

4. ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20141423.png)
   Terlihat bahwa hasilnya adalah 32 byte. Maka kita bisa membuat input sebanyak >32 byte agar program menjadi overflow dan mendapatkan flagnya. Disini saya telah membuat exploitnya (liat sendiri di exploit.py) jadi langsung saja dijalankan.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%200/img/Screenshot%202024-10-28%20143505.png)

   Flag : ```picoCTF{my_first_heap_overflow_c3935a08}```

   PWNED COY!!

