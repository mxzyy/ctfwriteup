># PicoCTF Write-Up Binary Exploitation : format string 0
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul format string 0 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1. Diberikan 2 file yaitu file executeable dan source codenya berikut gambarnya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20092438.png)
2. Disini saya melihat source code yang diberikan, dan terdapat beberapa point penting, pertama flag akan di print ketika program mengalami segmentation vault.
   
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20085846.png)

3. Kemudian kita lihat input yang diberikan akan masuk kedalam function dan terdapat if !on_menu.

   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20085919.png)

   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20085859.png)

   Pada fungsi itu input yang dimasukan perlu melebihi 2x dari buffer size, jika kita perhatikan pada menu ke-2 terdapat char `%114d`, char tersebut merupakan format desimal dari angka `114`.
   maka dari itu kita bisa menggunakan menu ke-2 sebagai input, namun karena scanf yang tidak membatasi char yang diinputkan kita akan memasukan input yang lebih dari buffer dan jumlah char dari menu ke-2.
   

4. Langsung saja kita eksekusi menggunakan exploit.py (liat sendiri kodenya).
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%200/img/Screenshot%202024-10-29%20092649.png)

   Flag : ```picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_74f6c0e7}```

   LOGINKAN!!
