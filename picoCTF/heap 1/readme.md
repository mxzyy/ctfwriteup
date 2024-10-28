># PicoCTF Write-Up Binary Exploitation : heap 1
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul heap 1 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1.  Diberikan 2 file yaitu file executeable dan source code nya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%201/img/Screenshot%202024-10-28%20144857.png)
2. Jika kita liat pada source code nya terdapat 1 perbedaan dari source code sebelumya (heap 0), yaitu pada fungsi check_win.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%201/img/Screenshot%202024-10-28%20144716.png)

   Disini kita diminta agar variabel safe_var di overwrite menjadi string `pico`.
3. Untuk exploitnya kita hanya perlu mengubah yang awalnya 32 + 1 bit menjadi 32 + "pico". Langsung saja kita eksekusikan.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/heap%201/img/Screenshot%202024-10-28%20145052.png)

Flag: ```picoCTF{starting_to_get_the_hang_e9fbcea5}```

Ez!
