># PicoCTF Write-Up Web Exploitation : Cookies
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul Cookies yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Web Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Mozilla Firefox](https://www.mozilla.org/id/firefox/new/)
* [Python](https://www.python.org/)

## Write Up
1. Diberikan Soal yang berisi suatu url, disini soalnya tidak memiliki hints.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-25-11.png)

2. Langsung coba cek websitenya, disni terdapat input 'snickerdoodle' langsung saja saya klik
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-28-08.png)
   
3. Berikut hasil dari inputan snickerdoodle
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-30-06.png)
   Dapat dilihat terdapat tulisan 'I Love snickerdoodle cookies!', saya tau bahwa kata cookies ini merujuk pada cookies web, langsung saja kita cek menggunakan Inspect Tool dari Mozilla Firefox.

4. Terlihat disini terdapat cookies dengan value 0
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-44-40.png)
   Saya pun mencoba untuk mengganti valuenya menjadi 1.
   
6. Berikut hasilnya jika menggunakan value 1
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-35-44.png)
   Terlihat bahwa tulisanya berganti menjadi 'I love chocolate chip cookies!', lalu saya ganti lagi value nya menjadi 2
   
8. Berikut hasilnya jika valuenya 2
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Cookies/img/Screenshot%20from%202023-11-04%2007-45-16.png)
   Terlihat juga tulisanya berganti menjadi 'I love oatmeal raisin cookies!', bisa dilihat bahwa hal ini menandakan suatu pola dengan kondisi jika kita terus mengganti valuenya, maka saya coba untuk membuat script untuk melihat tulisan apa yang akan keluar berdasarkan value dari cookies tadi.
   
10. 
   

11. Lalu saya coba juga tombol yang biru
   ![WebBlue](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-52-05.png)
   
   ![ResBlue](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-51-50.png)

11. Dari kedua tombol tersebut, terdapat suatu perbedaan pada Requestnya, yaitu ditombol merah menggunakan HTTP Method GET, sedangkan yang biru menggunakan HTTP Method POST. Dipikir2 method GET ini sesuai dengan nama soalnya, tetapi tidak dengan POST. yang seharusnya HEAD malah POST. ywdah sih tinggal coba aj pake Repeater burpsuite.

 ![HEAD](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-57-17.png)

 Langsung nemu coy, yak sekian dari write up yang tidak jelas ini kurang lebihnya mohon mff. terimaksih
   
