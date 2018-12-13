var trans = trans || {};

add = {
  'layer.trash_layer': 'Altres observacions',
  'layer.unclassified': 'Per validar',

  'expertinfo.tiger_mosquito': ' Segons els experts, les fotos d\'aquesta observació podrien ser de mosquit tigre (<i>Aedes albopictus</i>). \
      <br/>Si es veuen molt clarament els seus trets taxonòmics, especialment la ratlla blanca al cap i tòrax, serà "confirmat". Si no s\'aprecien alguns trets, serà "possible".',
  'expertinfo.yellow_fever_mosquito':' Segons els experts, les fotos d\'aquesta observació podrien ser de mosquit de la febre groga (<i>Aedes aegypti</i>). \
    <br/>Si es veuen molt clarament els seus trets taxonòmics, especialment la lira al cap i tòrax, serà "confirmat". Si no s\'aprecien alguns trets, serà "possible".',
  'expertinfo.site': 'Observacions ciutadanes de possibles llocs de cria (embornals i altres) de mosquit tigre o de la febre groga. Inclou observacions que encara no han estat filtrades per experts.',
  'expertinfo.unclassified':'Observacions amb foto que encara no han estat validades per experts.',
  'expertinfo.trash_layer':'Observacions que no corresponen a cap altra categoria però que podrien contenir informació d\'interès per a gestors.',

  'map.controlshare_view_description': 'Comparteix la vista privada d\'aquest mapa',
  'share.private_layer_warn': 'Atenció! Les dades privades de la vista actual i algunes de les capes només seran visibles pels usuaris registrats.',
  'map.notification_add':'Nova notificació',
  'notif.observations_none':'Cal seleccionar alguna observació',
  'notif.all_field_requiered':' Tots els camps són obligatoris',
  'notif.saved':'La notificació s\'ha enviat correctament',
  'notif.notification_cancel':'Cancel·la',

  //Descarregar
  'map.text_description_download': '<p>La descàrrega es realitzarà a partir dels elements que es visualitzen al mapa i només per a les dades relatives a les observacions ciutadanes. Comprova que tens actives les capes de la llegenda que desitges, els filtres temporals i el nivell de zoom.</p><p>Un cop definida la vista desitjada, fes clic al botó de descàrrega.</p>',
  //Notificacions
  'usernotification.not-predefined':'No predefinides',
  'all_notifications': 'Totes les notificacions',
  'check_notifications': 'Notificacions',
  'map.notification.notified': 'A',
  'map.notification.notifier': 'De',
  'map.notification.predefined.title': 'Si ho prefereixes pots fer servir una notificació predefinida:',
  'map.notification.preset0.body': '<p>Aquesta és la notificació predefinida número 1</p><p>Al cos del missatge posem el que convingui.</p>',
  'map.notification.preset0.title': 'Notificació predefinida 1',
  'map.notification.preset1.body': '<p>Aquesta és la notificació predefinida número 2</p><p>Al cos del missatge hi ha una mica més de text.</p>',
  'map.notification.preset1.title': 'Notificació predefinida 2',
  'map.notification.type.none': 'Tipus de notificació',
  'map.notification.type.private': 'Notificació privada',
  'map.notification.type.public': 'Notificació pública',
  'map.notification_add': 'Nova notificació',
  'map.notification_select_polygon_btn': 'Selecciona territori',
  'leaflet.draw.toolbar.cancel.title': 'Cancel·lar notificació',
  'map.control_notifications': 'Emetre notificació',
  'map.title_notification': 'Notificació',
  'notif.all_field_requiered': 'Tots els camps són obligatoris',
  'notif.notification_cancel': 'Cancel·lar',
  'notif.observations_none': 'No hi ha cap observació seleccionada',
  'notif.saved': 'Notificació enviada correctament',
  'notif.sendig_notifications': 'Les dades s\'estan enviant...',


  //Dibuix
  'map.text_description_notification': '<p>Fes clic a <span class="fa fa-pencil"></span> "Seleccionar territori" per seleccionar les observacions a les que vols enviar una notificació.</p><p>Pots tancar el polígon amb un doble clic sobre nou vèrtex, o amb un sol clic sobre el vèrtex inicial.<br/><br/>En finalitzar el polígon s\'indicarà el nombre d\'observacions afectades a la part superior d\'aquest panell i es mostrarà el formulari per crear la notificació.</p><p>En tancar el formulari de notificació caldrà tornar a començar la selecció del territori.</p>',

  //Select
    //Modal
  'map.users_found_text': 'Usuaris',
  'map.results_found_text': 'Observacions',

  'map.text_description_notification': '<p>Fes clic a <span class="fa fa-pencil"></span> "Seleccionar territori" per seleccionar les observacions a les que vols enviar una notificació.</p><p>Pots tancar el polígon amb un doble clic sobre nou vèrtex, o amb un sol clic sobre el vèrtex inicial.<br/><br/>Al finalitzar el polígon s\'indicarà el número d\'observacions afectades en la part superior del panell i es mostrarà el formulario para crear la notificació.</p><p>Al tancar el formulari de notificació serà necessari començar de nou amb la selecció del territori.</p>',

  //configuración de imbornales'stormdrain.label-versions': 'Número de versión',
  'layer.drainstorm': 'Embornals',
  'drainstorm.nowater': 'Sense aigua',
  'drainstorm.water': 'Amb aigua',
  'stormdrain.send': 'Enviar',
  'stormdrain.categories-helper1': 'Les categories seran avaluades per ordre de definició.',
  'stormdrain.categories-helper2': 'Només es representaran els embornals que compleixin totes les condicions.',
  'stormdrain.categories-helper3': 'Cada condició està formada per un atribut i un valor.',
  'stormdrain.categories-helper4': 'Els embornals ja assignats a una categoria no tornaran a ser avaluats.',
  'stormdrain.field-activity': 'Activitat',
  'stormdrain.field-date': 'Data',
  'stormdrain.field-sand': 'Sorra',
  'stormdrain.field-species1': 'Espècie A',
  'stormdrain.field-species2': 'Espècie B',
  'stormdrain.field-treatment': 'Tractament',
  'stormdrain.field-type': 'Tipus',
  'stormdrain.field-water': 'Aigua',
  'stormdrain.import-finished': 'La importació ha finalitzat correctament',
  'stormdrain.import-started': 'Important dades. Aquest procés pot tardar una estona.',
  'stormdrain.label-categories': 'Categories',
  'stormdrain.label-color': 'Color',
  'stormdrain.label-conditions': 'Condicions',
  'stormdrain.label-field': 'Atribut',
  'stormdrain.label-value': 'Valor',
  'stormdrain.label-versions': 'Versió',
  'stormdrain.main-title': 'Configuració de la visualització d\'embornals',
  'stormdrain.none-txt': 'Cap',
  'stormdrain.operator-<=': ' fins a',
  'stormdrain.operator-<>': ' diferent de',
  'stormdrain.operator-=': ' igual a',
  'stormdrain.operator->=': ' des de',
  'stormdrain.setup.submit.ok': 'S\'ha desat la nova configuració',
  'stormdrain.setup-later': 'Configurar embornals més tard',
  'stormdrain.setup-now': 'Continuar amb la configuració d\'embornals',
  'stormdrain.upload-button': 'Selecciona un fitxer',
  'stormdrain.get-template':'Descarregar plantilla',
  'stormdrain.upload-comment': 'Titol (max 30 caràcters)',
  'stormdrain.upload-error': 'S\'ha produït un error:',
  'stormdrain.upload-newversion': 'Versió número:',
  'stormdrain.upload-required': 'Tots els camps són obligatoris',
  'stormdrain.upload-title': 'Càrrega d\'embornals',
  'stormdrain.user-txt': 'Usuari',
  'stormdrain.value-0': 'No',
  'stormdrain.value-1': 'Si',
  'stormdrain.value-E': 'Embornal',
  'stormdrain.value-F': 'Font',
  'stormdrain.value-false': 'No',
  'stormdrain.value-R': 'Reixeta',
  'stormdrain.value-true': 'Sí',
  'stormdrain.value-null': 'Sense valor',
  'stormdrain.version-helper': 'Selecciona la versió que vols configurar',
  'stormdrain.version-txt': 'Versió',
  'stormdrain.water': 'Aigua',
  'stormdrain.example-title': 'Exemple de configuració de la visualització d\'embornals',
  'stormdrain.example-body-1': 'Es vol pintar, representar els embornals en dos categories, segons:',
  'stormdrain.example-body-2': 'Tenen aigua i han estat tractats. Representats de color verd',
  'stormdrain.example-body-3': 'Tenen aigua i no han estat tractats. Representats de color vermell',
  'stormdrain.example-body-4': 'En aquest cas, el que s’hauria de fer seria:',
  'stormdrain.example-body-5': 'img/stormdrain_example_1_ca.png',
  'stormdrain.example-body-6': 'El que <strong>NO</strong> funcionaria, seria configurar la visualització amb aquests paràmetres:',
  'stormdrain.example-body-7': 'img/stormdrain_example_2_ca.png',
  'stormdrain.example-body-8': 'Perquè no representaríem en aquest cas, dos tipus d’embornals (els que tenen aigua i estan tractats;  els que tenen aigua i no han estat tractats?), que estaríem representant en aquest cas?',
  'stormdrain.example-body-9': 'En color verd els embornals que tenen l’atribut «aigua» = «Sí». Independentment dels valors que tinguin els altres atributs (tractament, data, etc.).',
  'stormdrain.example-body-10': 'En color morat, els embornals que no han encaixat en la primera categoria, i que tenen l’atribut «Tractament» = «sí».',
  'stormdrain.example-body-11': 'En color blau, els embornals que no encaixen en cap de les dues categories anteriors, i que tenen la columna «Tractament» = «no».',
  'stormdrain.example-body-12': 'És a dir, cada color s’associa a una categoria. Cada categoria pot tenir una o més condicions. I cada condició fa referència a un «atribut» un operador (igual ,diferent de, etc.) i un «valor». ',
  'stormdrain.example-body-13': 'Perquè un embornal pertanyi a una categoria, cal que es compleixen totes les condicions de la categoria (operador lògic AND).',
  'stormdrain.example-body-14': 'També cal tenir present que quan un embornal «cau» dins d’una categoria, aquest embornal ja no s’avalua amb la resta de categories que venen a continuació. És a dir, un embornal que tingui la columna «aigua» = «si» i «tractament» = «si» es representarà de color verd perquè és la primera categoria de la quan en compleix totes les condicions (en aquest cas només n’hi ha una).',

  //configuración de la capa epidemiologia
  'layer.epidemiology': 'Epidemiologia',
  'epidemiology.upload-title': 'Carga de dades epidemiològiques',
  'epidemiology.get-template': 'Descarregar plantilla',
  'epidemiology.upload-button':'Selecciona un arxiu',
  'epidemiology.import-started': 'Important dades. Aquest procés pot tardar una estona',
  'epidemiology.import-finished': 'La importació ha finalitzat correctament',
  'epidemiology.setup-now': 'Continuar amb la configuració',
  'epidemiology.setup-later': 'Configurar més tard',
  'epi.tpl-title': 'Dades epidemiològiques',
  'epi.date_symptom':'Data primers simptomes',
  'epi.date_arribal': 'Data d\'arribada',
  'epi.age': 'Edat',
  'epi.country':'País visitat',
  'epi.patient_state':'Estat',
  'epi.province':'Provincia',
  'epi.health_center':'Centre',
  'epi.year':'Any',
  'epidemiology.setup-title': 'Epidemiologia. Configuració de la visualització',
  'epidemiology.update': 'Actualitzar',
  'epidemiology.period': 'Per',
  'epidemiology.field-map': 'Tipus de mapa',
  'epidemiology.patient_state': 'Estat del pacient',
  'epidemiology.age_band': 'Franges d\'edat',
  'epidemiology.date_symptom': 'Data dels primers simptomes',
  'epidemiology.date_arribal': 'Data d\'arribada',
  'epidemiology.years': 'anys',
  'epidemiology.patient-filter': 'Estats dels pacients',
  'epidemiology.likely': 'Probable',
  'epidemiology.suspected': 'Sospitós',
  'epidemiology.confirmed': 'Confirmat',
  'epidemiology.group-confirmat': 'Confirmat',
  'epidemiology.confirmed-not-specified': 'Virus no especificat',
  'epidemiology.confirmed-den': 'Dengue',
  'epidemiology.confirmed-zk': 'Zika',
  'epidemiology.confirmed-yf': 'Febre groga',
  'epidemiology.confirmed-chk': 'Chikungunya',
  'epidemiology.confirmed-wnv': 'Virus de l\'oest del nil',

  'epidemiology.form.confirmed-not-specified': 'Confirmat. Virus no especificat',
  'epidemiology.form.confirmed-den': 'Confirmat. Dengue',
  'epidemiology.form.confirmed-zk': 'Confirmat. Zika',
  'epidemiology.form.confirmed-yf': 'Confirmat. Febre groga',
  'epidemiology.form.confirmed-chk': 'Confirmat. Chikungunya',
  'epidemiology.form.confirmed-wnv': 'Confirmat. Virus de l\'oest del nil',

  'epidemiology.undefined': 'Indefinit',
  'epidemiology.nocase': 'No hi ha cas',
  'epidemiology.all': 'Tots els estats',
  'epidemiology.filter-explanation':'Els filtres temporas del mapa també aplicaran a aquesta capa a partir del camp *data_arribada*',
  'epidemiology.upload-explanation': 'ATENCIÓ!! Aquest procés d\'importació eliminarà totes les dades prèviament emmagatzemades de la capa d\'Epidemiologia',
  'epidemiology.empty-layer': 'En aquests moments no hi ha dades d\'epidemiologia',
  'epidemiology.upload-error': 'S\'ha produït un error durant el procés d\'importació',
};
_.extend(trans.ca, add);
