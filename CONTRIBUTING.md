# Com contribuir
## Afegir paraules
Actualment, hi ha 2 opcions:
- A través del [Formulari](https://docs.google.com/forms/d/e/1FAIpQLSfaUMh9FfrHljv75PoBfhMX-3EK5Fn8CoukRFBO5fl0eYxjlQ/viewform?usp=sf_link)
- Modificant el JSON (Aquells acostumats a GitHub, s'agraeix que utilitzeu aquesta):

Per a afegir paraules a la base de dades, hauràs de modificar [insults.json](insults.json), afegint una paraula amb el següent format:
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
- No deixar-se cap coma ni posar-ne de més, [ací](https://docs.openstack.org/doc-contrib-guide/json-conv.html) teniu un bon exemple sobre com és el format d'un JSON.
- Introduir la paraula dintre de la llista "insults".

Una vegada afegida la paraula, cliqueu el botó de commit i seleccioneu l'opció de suggerir canvis.

Quan puga, revisaré la vostra aportació i l'afegiré a la base de dades.

## Modificar el codi de la pàgina
TODO
