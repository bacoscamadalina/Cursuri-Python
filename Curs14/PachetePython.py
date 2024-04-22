# PIP = Preferred Installer Program
'''
CELE MAI UTILIZATE PACHETE PYTHON

1. MachineLearning: O bibliotecă fundamentală pentru calcul științific în Python. Oferă suport pentru array-uri
multidimensionale, operații matriceale și o colecție largă de funcții matematice de înalt nivel.
2. Pandas: O bibliotecă care oferă structuri de date și unelte de analiză de date flexibile și rapide,
ideală pentru manipularea și analiza datelor tabulare și de serie temporală.
3. Requests: O bibliotecă simplă pentru a efectua cereri HTTP. Este utilizată pentru a trimite cereri
în rețea și a interacționa cu API-uri web.
4. Flask: Un micro-framework web pentru Python. Este ușor și flexibil, fiind potrivit pentru dezvoltarea
rapidă a aplicațiilor web.
5, Django: Un framework web de nivel înalt care încurajează dezvoltarea rapidă și un design curat, pragmatic.
Este cunoscut pentru robustețea sa.
6. TensorFlow: O bibliotecă open-source dezvoltată de Google pentru calcul numeric folosind grafice de flux de date.
Este folosită în mod special pentru aplicații de învățare automată și învățare profundă (deep learning).
7. Keras: O interfață de nivel înalt pentru rețele neuronale, care rulează deasupra TensorFlow, CNTK sau Theano.
Este concentrată pe experimentare rapidă.
8. SciPy: Bazată pe MachineLearning, SciPy este o colecție de algoritmi matematici și funcții de conveniență
construite pe extensia MachineLearning a Python.
9. Matplotlib: O bibliotecă pentru crearea de vizualizări statice, animate și interactive în Python.
10. Scikit-learn: O bibliotecă simplă și eficientă pentru învățare automată și analiza de date, construită
pe MachineLearning, SciPy și matplotlib.
11. Pillow: O extensie a bibliotecii PIL (Python Imaging Library), Pillow este utilizată pentru deschiderea,
manipularea și salvarea multor formate diferite de fișiere imagine.
12. SQLAlchemy: O bibliotecă SQL toolkit și Object-Relational Mapping (ORM) care oferă un set complet de
modele persistente cu baze de date SQL.
13. Beautiful Soup: O bibliotecă destinată pentru web scraping, care facilitează extragerea datelor
din fișiere HTML și XML.
14. PyTorch: O bibliotecă de învățare automată open source dezvoltată de Facebook, oferind o
flexibilitate mare și o platformă optimă pentru cercetarea în deep learning.
15. Jupyter: O aplicație web open-source care permite crearea și partajarea documentelor care conțin
cod live, ecuații, vizualizări și text narativ.
16. Pygame: O set de module Python proiectate pentru scrierea jocurilor video. Include grafică și
sunet, și este utilizat pentru a crea jocuri rapide și ușoare.
17. Plotly: O bibliotecă de grafică care produce figuri interactive și de calitate publicistică,
în diverse formate, și le integrează în aplicații web
18. Selenium: O unealtă pentru testarea aplicațiilor web care permite automatizarea browser-ului
web pentru testarea paginilor.
19. PyTest: Un framework care facilitează scrierea de teste simple, dar puternice și scalabile,
pentru aplicații și biblioteci Python.
20. Docker: Deși nu este un pachet Python în sens tradițional, Docker are o integrare importantă
cu Python, permițând containerizarea aplicațiilor Python pentru dezvoltare, livrare și implementare eficiente.
21. lxml: O bibliotecă eficientă și ușor de folosit pentru procesarea XML și HTML, foarte populară
pentru web scraping.
22. Tornado: Un framework web și o bibliotecă de rețea asincronă, folosită pentru construirea
aplicațiilor web scalabile și performante.
23. Celery: Un sistem distribuit de cozi de mesaje, folosit pentru a procesa lucrări în paralel
bazat pe distribuirea mesajelor.
24. Fabric: O bibliotecă care oferă un set de operații de nivel înalt pentru administrarea serverelor
prin utilizarea comenzilor SSH.
25. Nltk (Natural Language Toolkit): O platformă lider pentru construirea de programe Python care
lucrează cu datele limbajului uman.
26. FastAPI: Un framework web modern, rapid (de nivel înalt) pentru construirea de API-uri cu Python 3.7+,
bazat pe standardele Python type hints.
27. Twisted: Un motor de evenimente asincron pentru Python, care facilitează construirea de aplicații
de rețea scalabile și performante.
28. wxPython: O bibliotecă pentru crearea interfețelor grafice de utilizator (GUI) native pe
diferite platforme.
29. Scrapy: Un framework rapid și de înalt nivel pentru crawling web și scraping, folosit pentru
a extrage datele de pe site-uri web.
30. PyQt/PySide: Două seturi de legături Python pentru biblioteca de interfață grafică Qt. Sunt
folosite pentru a crea aplicații GUI complexe și atractive.
'''
'''
                                         COMMAND PROMPT
Pt start : deactivate         
Pt activare myenv :   
->python -m venv .\myenv
->myenv\Scripts\activate.bat 
                             
Verificarea versiunii Python se face cu comanda : python -V sau python3 -V sau py - V
Daca nu ne este cunoscuta versiunea de python procedam astfel:
1. START : Python -> click dreapta + selectam unde este situat Python in C
2. Run + comanda sysdm.cpl + enter
3. Advanced + Environmend Variables + Use variables + click Path + new CtrlV+ new CtrlV + \Scripts + OK
4. Advanced + Environmend Variables + System + click Path + new CtrlV+ new CtrlV + \Scripts + OK
5. Restart Pycharm
Instalare pip : pip install pytest
Ca sa vedem ce pachete avem instalate: pip freeze
Ca sa ruleze comanda : pip freeze >requirements.txt
'''
'''
python --version  > Afișează versiunea curentă de Python instalată pe sistem.
pip  > pachet care ne ofera posibliattea de a instala librarii externe
pip help  > arata toate comenzile disponibile
pip install <nume_pachet>  > Instalează pachetul specificat prin <nume_pachet> folosind pip.(ultima viersiune)
pip uninstall <nume_pachet>  > Dezinstalează pachetul specificat.
pip freeze  > Afișează o listă a tuturor pachetelor Python instalate în mediul curent, împreună cu versiunile lor.
pip freeze > requirements.txt  > Redirecționează ieșirea comenzii pip freeze într-un fișier numit requirements.txt.
    Fișierul va conține o listă a pachetelor instalate și versiunile lor, util pentru replicarea mediului.
pip list -o  > Afișează o listă a pachetelor instalate care au versiuni mai noi disponibile.
pip install -U <nume_pachet>  > Actualizează pachetul specificat la cea mai recentă versiune disponibilă.
pip install <nume_pachet>==versiune  > Instalează o versiune specifică a unui pachet.
pip install -r requirements.txt  > Instalează pachetele specificate în fișierul requirements.txt.
'''
