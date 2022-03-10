# TecHack Roteiro 2
### Por Victor Vergara

#### 1) 

1.1a)
![alt_text](imgs/1-1a.png)

1.1b)
![alt_text](imgs/1-1b.png)

1.1c) 

![alt_text](imgs/1-1c.png)


1.1d) 

Arquivo portScanner.py


1.1e) 

![alt_text](imgs/1-1e.png)


1.1f) 

Exploit encontrado na Porta 21

![alt_text](imgs/1-1f.png)


1.1g) 

Na porta 3306 foram encontrados 2 CVEs classificados como altos:

CVE-2009-2446   8.5     https://vulners.com/cve/CVE-2009-2446

CVE-2008-0226   7.5     https://vulners.com/cve/CVE-2008-0226

![alt_text](imgs/1-1g-3306.png)


Na porta 5432 foram encontrados 2 CVEs classificados como Crítico:

CVE-2013-1903   10.0    https://vulners.com/cve/CVE-2013-1903

CVE-2013-1902   10.0    https://vulners.com/cve/CVE-2013-1902

Também foram encontrados 4 CVEs classificados como Altos:

POSTGRESQL:CVE-2013-1900        8.5     https://vulners.com/postgresql/POSTGRESQL:CVE-2013-1900

POSTGRESQL:CVE-2010-1169        8.5     https://vulners.com/postgresql/POSTGRESQL:CVE-2010-1169

CVE-2010-1447   8.5     https://vulners.com/cve/CVE-2010-1447

CVE-2010-1169   8.5     https://vulners.com/cve/CVE-2010-1169


![alt_text](imgs/1-1g-5432.png)

1.1h) 

a) 104.16.44.99

![alt_text](imgs/1-1ha.png)


b) CloudFlare, mostrado no comando acima e no abaixo

![alt_text](imgs/1-1hb.png)


c) Sim, há um servidor de email no domínio: mail.ietf.org no IP 4.31.198.44 

Os dados foram pegos utilizando o site IPOk (https://ipok.com.br/tools.php?valor=ietf.org&tool=info) e NetCraft(https://sitereport.netcraft.com/?url=mail.ietf.org)


1.1i) 

a) Site escolhido: www.rodolfoavelino.com.br


![alt_text](imgs/1-1i-a.png)


b) Sim é um IP do CloudFlare, assim é utilizado por vários outros serviços.
Esses podem ser encontrados fazendo um reverse IP Lookup (https://hackertarget.com/reverse-ip-lookup/ utilizando o IP 104.21.57.232)


c) Via o nmap -O não é possível ter certeza do OS, ele acredita ser o British Gas GS-Z3 data logger

![alt_text](imgs/1-1i-c1.png)

Mas ao pingar o site, o ttl é de 52, indicando ser linux, mas mesmo assim por ser distante de 64 não podemos ter certeza.

![alt_text](imgs/1-1i-c2.png)

Mas ao olhar no seu histórico de Hospedagem é possível ver que o servidor roda Linux com Apache

![alt_text](imgs/1-1i-c3.png)
d) 

![alt_text](imgs/14.png)


1.1j) 

![alt_text](imgs/15.png)
