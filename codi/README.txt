Codi principal:
- TFG - Aleix Solanes.ipynb

En aquesta carpeta es troben els fitxers que es necessiten per a l'execució del projecte. S'han de posar a la mateixa arrel que el fitxer iPython. Són els següents:
- antropònims.txt: conté una llista de noms de persona catalans.
- CartoCat.xlsx: conté la informació relativa a les poblacions catalanes.
- cities15000.txt: conté la informació de totes les poblacions a nivell mundial.
- common_names.txt: conté els noms de persona amb anglès i espanyol.
- countryInfo.txt: conté informació de cada país.
- iso-languagecodes.txt: conté informació dels codis ISO dels idiomes per exemple.

A més s'adjunta la carpeta dump, que conté les bases de dades de notícies i de ciutats utilitzades.
Per a la seva execució s'ha de fer un backup de les dades en el sistema MongoDB instalat. Per a fer-ho s'ha d'executar el següent codi:

- mongorestore --db nom_database path_al_fitxer_bson

Per a l'execució del projecte també es necessita un fitxer anomenat alternateNames.txt, però degut a la seva mida se n'adjunta el link de
descàrrega:
Enllaç personal - https://mega.nz/#!HlwEiJ6R!CFrNG2m3NOkJwJ2lC3yis1CQljQ8V_C_rbmkmuNT2nk
Enllaç original - http://download.geonames.org/export/dump/alternateNames.zip (s'haurà de descomprimir primer)
