># PicoCTF Write-Up Binary Exploitation : format string 2
Pada kesempatan kali ini, saya akan berbagi pengalaman dan solusi dari tantangan Capture The Flag (CTF) yang baru saja saya selesaikan. Soal CTF kali ini berjudul format string 2 yang berasal dari website [PicoCTF](https://picoctf.org), dengan kategori Binary Exploitation. 

## Tools

Berikut Alat & Bahan yang saya gunakan pada Soal CTF ini.

* [Python](https://www.python.org/)
* [Pwntools](https://docs.pwntools.com/en/stable/)

### Write-up
1. Diberikan 2 file yaitu file executeable dan source codenya berikut gambarnya.
   ![Soal](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%202/img/Screenshot%202024-10-30%20100652.png)
2. Disini pada source code yang diberikan diberikan variabel sus dengan isi `0x21737573`, kita perlu menggantinya dengan `0x67616c66`, pada input yang ada terdapat kerentanan
   format string pada print(buf), dengan memanfaatkan kerentanan tersebut kita bisa melakukan arbirary memory write, dibantu dengan pwntools akan jauh lebih mudah.
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%202/img/Screenshot%202024-10-29%20114813.png)
3.  Langsung saja eksekusi (exploit.py liat sendiri)
   ![](https://raw.githubusercontent.com/mxzyy/ctfwriteup/refs/heads/main/picoCTF/format%20string%202/img/Screenshot%202024-10-30%20100804.png)

   Flag : ```picoCTF{f0rm47_57r?_f0rm47_m3m_e371fb20}```

   ANJAS
