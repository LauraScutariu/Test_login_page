"""
xemplu:

Vrem sa cautam un element cu id-ul  username pe  un site.
Sistemul va cauta acel element, si daca  il va gasi va trece instant la instructiunea
urmatoare.

a) implicit wait
Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in
implicit wait, dupa care va da eroare.
Daca nu am avea acel implicit wait, ar da eroare instant.

b) sleep
Daca avem sleep inainte de element, atunci sistemul va astepta 5 secunde inainte sa
caute elementul apoi il va cauta,
iar daca nu il va gasi, va da eroare instant.

Daca avem sleep dupa element, o sa returneze eroare instant, pentru ca sistemul nu mai
ajunge sa execute instructiunea de sleep

c) explicit wait
Daca avem explicit wait pe elementul cautat si acesta va fi gasit, va fi actionat asupra
 lui instant
Daca avem explicit wait pe elementul cautat si acesta nu va fi gasit instant, atunci se
 va astepta numarul de secunde definit, dupa care se va returna eroare in cazul in care
 nu s-a gasit nici dupa numarul de secunde alocat.
Daca avem explicit wait pe un alt element decat elementul cautat si acesta va fi gasit,
 va fi actionat asupra lui instant
Daca avem explicit wait pe  un alt element decat elementul cautat si acesta nu va fi
gasit, sistemul va returna eroare instant

"""