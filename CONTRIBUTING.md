# Com contribuir
## Afegir paraules
Actualment, el sistema és un poc complicat:

Per a afegir paraules a la base de dades, haurás de modificar [insults.json](insults.json), afegint una paraula amb el seguent format:
```
{
    "paraula": "Carallot",
    "definicio": "Encantat, aturat. Persona que no fa res.",
    "tags": [
        "despectiu",
        "vegetal"
    ],
    "font": {
        "nom": "Atzucac.cat",
        "url": "https://atzucac.cat/insultem-i-blasfemem-pero-en-catala/"
    }
},
```
És molt important:
- No deixar-se cap coma ni posar-ne de més, [ací](https://docs.openstack.org/doc-contrib-guide/json-conv.html) teniu un bon exemple sobre com és el format d'un json.
- Introduir la paraula dintre de la llista "insults".

Una vegada affegida la paraula, cliqueu el baoó de commit i seleccioneu l'opció de sugerrir canvis.

Quan puga, revisaré la vostra aportació i l'afegiré a la base de dades.

## Modificar el codi de la pàgina
TODO
