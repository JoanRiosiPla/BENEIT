# [B.E.N.E.I.T. FLASK en Desenvolupamnet](https://joanriosipla.github.io/BENEIT/)
[Visista la branca main per a la versió estable](https://github.com/JoanRiosiPla/BENEIT/tree/main)
## Base Enriquida de Nocions Enfocades en Insults i Trets
Web i base de dades amb tots els insults en valencià/català/balear on tothom pot afegir-ne de nous.
(En desenvolupament)

[beneit.cat](http://beneit.cat)

### Objectiu
Els insults a la nostra llengua s'estan castellanitzant i molts dels nostres propis es queden en l'oblit.
Aquest projecte busca conservar la nostra meravellosa cultura dels insults.

### Com afegir paraules
Actualment, hi ha 2 opcions:
- A través del [Formulari](https://docs.google.com/forms/d/e/1FAIpQLSfaUMh9FfrHljv75PoBfhMX-3EK5Fn8CoukRFBO5fl0eYxjlQ/viewform?usp=sf_link)
- Modificant el Json (Aquells acostumats a GitHub, s'agraeix que utilitzeu aquesta.) [Guia de contribució](CONTRIBUTING.md)


### Llicències i codi obert
- S'ha utilitzat la llibreria de c++ de Niels Lohmann [JSON for Modern C++](https://github.com/nlohmann/json) sota la llicència [MIT](https://github.com/nlohmann/json/blob/develop/LICENSE.MIT)
- S'ha utilitzat el jQuerry Highlight Plugin de Johann Burkard sota la llicència [MIT](https://opensource.org/license/mit/)
- S'ha utilitzat Flask, una llibreria de Python sota la llicència [BSD](https://opensource.org/licenses/BSD-3-Clause)

### Correr el servidor flask
#### Desenvolupament (Windows)
- Iniciar un venv: `python3 -m venv venv`
- Activar el venv: `venv\Scripts\activate`
- Instal·lar les dependencies: `pip install -r requirements.txt`
- Executar el servidor: ` flask run --host="0.0.0.0" --debug`