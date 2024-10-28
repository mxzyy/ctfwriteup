># PicoCTF Write-Up Binary Exploitation : heap 2
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul heap 2 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1.  Diberikan 2 file yaitu file executeable dan source code nya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%202/img/Screenshot%202024-10-28%20164809.png)
2. Pada source code yang diberikan terdapat perbedaan dari sebelumnya yaitu fungsi win dan check_win, intinya fungsi check_win merupakan type casting yang mengubah input menjadi address untuk direturn. 
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%202/img/Screenshot%202024-10-28%20164839.png)

   Sehingga kita perlu mencari address dari win function, lalu kita inputkan address tadi setelah byte 32 agar melakukan overwrite.
3. Untuk exploitnya kita hanya perlu mengubah yang awalnya 32 + "address dari win function". Jadi kita gunakan gdb untuk mencari win functionnya.
   
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%202/img/Screenshot%202024-10-28%20164937.png)

   Setelah menemukan alamat dari fungsi win nya kita dapat menggunakanya di exploit nya. Langsung saja kita eksekusi

   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%202/img/Screenshot%202024-10-28%20170916.png)
   
Flag: ```picoCTF{and_down_the_road_we_go_dbb7ff66}```

DONE BG!
