># PicoCTF Write-Up Web Exploitation : Insp3ct0r
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul Insp3t0r yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Web Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Mozilla Firefox](https://www.mozilla.org/id/firefox/new/)

## Write Up
1. Diberikan Soal yang berisi suatu url, disini soalnya memiliki 2 hints, berikut gambar2nya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-25.png)
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-11.png)
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-45-55.png)

2. Langsung coba cek websitenya, disni terdapat tulisan untuk melakukan inspect me.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-30.png)
   
3. Untuk melakukan inspect kita dapat melihat source code dari web tersebut dengan mengklik kanan pada web, berikut hasilnya.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-38.png)
   Dapat dilihat bahwa terdapat 1 part dari 3 part flag. Langsung saja kita cek file CSSnya. 

4. Jika kita scroll kebawah kita akan menemukan part 2 dari flag diatas. kini kita memiliki 2 part flag dan perlu mencari 1 lagi.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-48.png)
   Kembali ke html, dan kita cek file Javascriptnya.
   
5. Berikut hasilnya
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/main/picoCTF/Insp3ct0r/img/Screenshot%20from%202023-11-09%2018-46-53.png)
   Terlihat bahwa tedapat part terakhir dari flag, maka kita sudah menemukan semuanya
   
6. Berikut flagnya
   ```picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}```
   

 Langsung nemu coy, yak sekian dari write up yang tidak begitu jelas ini kurang lebihnya mohon mff. terimaksih
   
