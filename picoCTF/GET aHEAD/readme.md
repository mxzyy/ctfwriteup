># PicoCTF Write-Up Web Exploitation : GET aHEAD 
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul GET a Head yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Web Exploitation. 

## Tools

Berikut Tools yang saya gunakan pada Soal CTF ini.

* [BurpSuite](https://portswigger.net/burp)

## Write Up
1. Diberikan Soal berupa sebuah website yang terdapat sebuah Flag
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-30-26.png)

2. Coba cek websitenya
   ![Web](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-31-26.png)
   
3. Dari web tersebut dapat saya coba liat packet datanya menggunakan burpsuite
   ![BurpWeb](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-50-30.png)

4. Setelah diliat2 di webnya ada 2 tombol, lalu ketika ditekan yang warna merah maka hasil responya akan seperti gambar dibawah.
   ![ResRed](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-51-31.png)

5. Lalu saya coba juga tombol yang biru
   ![WebBlue](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-52-05.png)
   
   ![ResBlue](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-51-50.png)

6. Dari kedua tombol tersebut, terdapat suatu perbedaan pada Requestnya, yaitu ditombol merah menggunakan HTTP Method GET, sedangkan yang biru menggunakan HTTP Method POST. Dipikir2 method GET ini sesuai dengan nama soalnya, tetapi tidak dengan POST. yang seharusnya HEAD malah POST. ywdah sih tinggal coba aj pake Repeater burpsuite.

 ![HEAD](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/GET%20aHEAD/img/Screenshot%20from%202023-08-25%2020-57-17.png)

 Langsung nemu coy, yak sekian dari write up yang tidak jelas ini kurang lebihnya mohon mff. terimaksih
   



