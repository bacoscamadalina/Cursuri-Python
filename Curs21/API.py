'''
                                                 - API -

API - MESAGER care face ca doua interfate sa comunice intre ele
Ex: App Pizza -> comunica cu pizzeria ->alt API aduce inapoi informatiile pizzeriei
API - comunica si trimite date de la o aplicatie la alta
API - permit aplicatiilor sa interactioneze intre ele fara ca utilizatorul sa intervina in partea de backend

API = Interfete de programare a aplicatiilor (Application Programming Interface) permit aplicatiilor software sa
comunice intre ele
    - actioneaza ca un mediator intre doua aplicatii, permitand uneia sa solicite date sau servicii de la cealalta
si sa primeasca servicii in schimb
    - fac posibil ca aplicatiile sa acceseze functii sau alte date ale altor platforme, deschizand posibilitati infinite
de inovare si integrare

REST (REpresentational State Transfer) = un stil arhitectural pentru furnizarea de standarde intre sisteme computerizate
de pe web, facilitand comunicarea intre ele
Sistemele compatibile REST, numite si RESTFul se caracterizeaza prin modul in care sunt independente si separa
preocuparile clientului si ale serverului
Pentru ca un API sa fie considerat RESTFul tebuie sa respecte urmatoarele restrangeri:
1.Arhitectura client server : clientul si serverul sunt separate si actioneazza independent, permitand utilizarea diferitor
tehnologii pentru fiecare
2. Stateless (Fara stare): serverul nu stocheaza nici un context pentru client intre cereri, a.i. fiecare cere recontine
toate informatiile necesare pentru a o finaliza
3. Capacitatea de cache (stocheaza orice date) : clientii pot stoca in chace datele de raspuns, reducand numarul de
solicitari catre server si astfel se imbunatateste performanta
4. Utilizarea metodelor HTTP
5. Utilizarea codurilor de stare HTTP: API, RESTFul folosesc aceste coduri pentru a inica rezultatul statusului unei
solicitari, cum ar fi Succes (are codul 200)

                                                     - METODELE HTTP -

- sunt verbe standard de utilizare pentru a indica actiunea dorita care trebuie efectuata dintr-o resursa API
Cele patru metode prinicipale sunt
1. GET - preia date dintr-o resursa, si este folosit pt citire
2. POST - creaza o noua resursa si este folosita pentru a trimite date in Server
3. PUT - actualizeaza o resursa curenta si este folosita pt a modifica datele existente
4. DELETE - sterge o resursa si este folosit pt a elimina date


'''