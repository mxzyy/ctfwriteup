># PicoCTF Write-Up Binary Exploitation : format string 1
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul format string 0 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1. Diberikan 2 file yaitu file executeable dan source codenya berikut gambarnya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%201/img/Screenshot%202024-10-29%20114741.png)
2. Disini saya melihat source code yang diberikan, disini input akan dilimit sebanyak 1024 byte, dan juga tedapat printf(buf) disini printf tidak menggunakan format specifier sehingga
3. memungkinkan untuk di inputkan format specifier seperti %s %x %d %p, disini kita akan melihat pointer nya yang berisi flag kemudian mengambil pointer lalu mengubahnya menjadi string. 
   
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20085846.png)


4. Langsung saja kita eksekusi menggunakan exploit.py (liat sendiri kodenya).
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20114813.png)

   Flag : ```picoCTF{4n1m41_57y13_4x4_f14g_64277116}```

   CIHHUI
