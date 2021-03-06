var trans = trans || {};

add = {
    'layer.trash_layer': 'Otras observaciones',
    'layer.unclassified': 'Por validar',

    'expertinfo.tiger_mosquito': ' Según los expertos, las fotos de esta observación podrían ser de mosquito tigre (<i>Aedes albopictus</i>). \
      <br/>Si se ven muy claramente sus rasgos taxonómicos, especialmente la raya blanca en cabeza y tórax, será “confirmado”. Si no se aprecian algunos rasgos, será “posible”.',
    'expertinfo.yellow_fever_mosquito':' Según los expertos, las fotos de esta observación podrían ser de mosquito de la fiebre amarilla (<i>Aedes aegypti</i>). \
      <br/>Si se ven muy claramente sus rasgos taxonómicos, especialmente la lira en cabeza y tórax, será “confirmado”. Si no se aprecian algunos rasgos, será “posible”.',
    'expertinfo.site': 'Observaciones ciudadanas de posibles lugares de cría (imbornales y otros) de mosquito tigre o de la fiebre amarilla. Incluye observaciones que aún no han sido filtradas por expertos.',
    'expertinfo.unclassified':'Observaciones con foto que aún no han sido validadas por expertos.',
    'expertinfo.trash_layer':'Observaciones que no corresponden a ninguna otra categoría pero que podrían contener información de interés para gestores.',

    'map.controlshare_view_description': 'Comparte esta vista privada',
    'share.private_layer_warn': '¡Atención! Los datos privados de la vista actual y algunas de las capas solo serán visibles para los usuarios registrados.',

    //descargas
    'map.text_description_download': '<p>La descarga se realizará a partir de los elementos que se visualizan en el mapa y solo para los datos relativos a las observaciones ciudadanas. Comprueba que estén activas las capas de la leyenda que deseas así como los filtros temporales y el nivel de zoom.</p><p>Una vez definida la vista deseada pulsa en el botón de descarga.</p>',
    //NOFIFICATIONS
    'map.notification_add':'Nueva notificación',
    'notif.observations_none':'No hay ninguna observación seleccionada',
    'notif.all_field_requiered':'Todos los campos son obligatorios',
    'notif.saved':'Notificación enviada correctamente',
    'notif.notification_cancel':'Cancelar',
    'map.control_notifications': 'Emitir notificación',
    'map.title_notification': 'Notificación',
    'map.results_found_text': 'Observaciones',
    'map.users_found_text': 'Usuarios',
    'map.notification_form_open': 'Crear notificación',
    'map.notification_select_polygon_btn': 'Seleccionar territorio',
    'map.notification.notifier': 'De',
    'map.notification.notified': 'A',
    'map.notification.type.none': 'Tipo de notificación',
    'map.notification.type.public': 'Notificación pública',
    'map.notification.type.private': 'Notificación privada',
    'map.notification.predefined.title': 'Si lo prefieres puedes usar una notificación predefinida:',
    'map.notification.preset0.title': 'Notificación predefinida 1',
    'map.notification.preset0.body': '<p>Esta es la notificación predefinida número 1</p><p>En el cuerpo del mensaje ponemos lo que convenga.</p>',
    'map.notification.preset1.title': 'Notificación predefinida 2',
    'map.notification.preset1.body': '<p>Esta es la notificación predefinida número 2</p><p>En el cuerpo de este mensaje hay un poco más de texto.</p>',
    'notif.sendig_notifications': 'Se está enviando la información...',

     //NOTIFICATIONS DRAW
    'leaflet.draw.toolbar.cancel.title': 'Cancelar edición',

    'layer.drainstorm':'Imbornales',
    'drainstorm.water': 'Con agua',
    'drainstorm.nowater': 'Sin agua',
    'map.text_description_notification': '<p>Pulsa en <span class="fa fa-pencil"></span> "Seleccionar territorio" para seleccionar las observaciones a las que deseas enviar una notificación.</p><p>Puedes cerrar el polígono con un doble click sobre nuevo vértice, o con un solo click sobre el vértice inicial.<br/><br/>Al finalizar el polígono se indicará el número de observaciones afectadas en la parte superior de este panel y se mostrará el formulario para crear la notificación.</p><p>Al cerrar el formulario de notificación será necesario empezar de nuevo con la selección del territorio.</p>',

    'observations.filters.title': 'Observaciones',
    'usernotification.not-predefined':'No predefinidas',

    // FIN NOTIFICACIONES

    //STORM DRAIN
    'stormdrain.main-title':'Configuración de la visualización de imbornales',
    'stormdrain.version-helper':'Selecciona los imbornales que deseas visualizar',
    'stormdrain.label-categories':'Categorías',
    'stormdrain.categories-helper1':'Las categorías se evaluarán por orden de definición.',
    'stormdrain.categories-helper2':'Los imbornales se asignarán a una categoría sólo si cumplen todas las condiciones especificadas.',
    'stormdrain.categories-helper3':'Cada condición se compone de un atributo y un valor.',
    'stormdrain.categories-helper4':'Los imbornales ya asignados a una categoría no volverán a ser evaluados.',
    'stormdrain.label-versions':'Versión',
    'stormdrain.label-color':'Color',
    'stormdrain.exclude-text':'El color blanco excluirá del mapa estos elementos',
    'stormdrain.label-conditions':'Condiciones',
    'stormdrain.label-field':'Atributo',
    'stormdrain.label-value':'Valor',
    'stormdrain.send':'Enviar',
    'stormdrain.water':'Agua',
    'stormdrain.treatment':'Tratamiento',
    'stormdrain.value-true':'Sí',
    'stormdrain.value-false':'No',
    'stormdrain.value-1':'Sí',
    'stormdrain.value-0':'No',
    'stormdrain.value-F':'Fuente',
    'stormdrain.value-E':'Imbornal',
    'stormdrain.value-R':'Rejilla',
    'stormdrain.value-null': 'Sin valor',
    'stormdrain.field-water':'Agua',
    'stormdrain.field-sand':'Arena',
    'stormdrain.field-treatment':'Tratamiento',
    'stormdrain.field-species1':'Especie A',
    'stormdrain.field-species2':'Especie B',
    'stormdrain.field-activity':'Actividad',
    'stormdrain.field-date':'Fecha',
    'stormdrain.field-type':'Tipo',
    'stormdrain.operator-=':' igual a ',
    'stormdrain.operator-<>':' distinto de ',
    'stormdrain.operator-<=':' hasta ',
    'stormdrain.operator->=':' desde ',
    'stormdrain.setup.submit.ok':'La nueva configuración ha sido almacenada',
    'stormdrain.upload-title':'Carga de imbornales',
    'stormdrain.upload-newversion':'Versión número: ',
    'stormdrain.import-started': 'Importando datos. Este proceso puede tardar unos segundos.',
    'stormdrain.import-finished': 'La importación ha finalizado correctamente',
    'stormdrain.upload-error':'Se ha producido un error : ',
    'stormdrain.upload-required':'Todos los campos son obligatorios',
    'stormdrain.setup-now':'Continuar con la configuración de imbornales',
    'stormdrain.setup-later':'Configurar imbornales más tarde',
    'stormdrain.upload-button':'Selecciona un archivo',
    'stormdrain.get-template':'Descargar plantilla',
    'stormdrain.version-txt':'Versión',
    'stormdrain.user-txt':'Usuario',
    'stormdrain.none-txt':'Ninguna',
    'stormdrain.upload-comment':'Título (max 30 caracteres)',
    'stormdrain.example-title': 'Ejemplo de configuración de la visualización de imbornales',
    'stormdrain.example-body-1': 'Se quiere pintar, representar los imbornales en dos categorías, según si:',
    'stormdrain.example-body-2': 'Tienen agua y han sido tratados. Representados en color verde ',
    'stormdrain.example-body-3': 'Tienen agua y no han sido tratados. Representados en color rojo',
    'stormdrain.example-body-4': 'En este caso lo que habría que hacer es:',
    'stormdrain.example-body-5': 'img/stormdrain_example_1_es.png',
    'stormdrain.example-body-6': 'Lo que <strong>NO</strong> funcionaría, sería configurar la visualización con estos parámetros:',
    'stormdrain.example-body-7': 'img/stormdrain_example_2_es.png',
    'stormdrain.example-body-8': '¿Por qué no representaríamos en este caso dos tipos de imbornales (los que tienen agua y se han tratado; los que tienen agua y no se han tratado)? ¿Qué estaríamos representando en este caso?',
    'stormdrain.example-body-9': 'En color verde los imbornales que tienen el atributo <agua> = «Sí». Independientemente de los valores que tengan los otros atributos (tratamiento, fecha, etc.).',
    'stormdrain.example-body-10': 'En color morado, los imbornales que no han encajado en la primera categoría y que tienen el atributo «Tratamiento» = «sí».',
    'stormdrain.example-body-11': 'En color azul, los imbornales que no encajan en ninguna de las dos categorías anteriores y que tienen la columna «Tratamiento» = «no».',
    'stormdrain.example-body-12': 'Es decir, de cada color se asocia a una categoría. Cada categoría puede tener una o más condiciones. Y cada condición hace referencia a un «atributo» un operador (igual, distinto, etc.) y un «valor».',
    'stormdrain.example-body-13': 'Para que un imbornal pertenezca a una categoría es necesario que se cumplan todas las condiciones de la categoría (operador lógico AND).',
    'stormdrain.example-body-14': 'También hay que tener en cuenta que cuando un imbornal «cae» dentro de una categoría, éste ya no se evalúa con el resto de categorías que vienen a continuación. Es decir, un imbornal que tenga la columna «agua» = «sí» y «tratamiento» = «sí» se representará en color verde porque es la primera categoría de la que cumple todas las condiciones (en este caso sólo hay una).',

    //configuración de la capa epidemiologia
    'layer.epidemiology': 'Epidemiología',
    'epidemiology.upload-title': 'Carga de datos epidemiológicos',
    'epidemiology.get-template': 'Descargar plantilla',
    'epidemiology.upload-button':'Selecciona un archivo',
    'epidemiology.import-started': 'Importando datos. Este proceso puede tardar unos segundos',
    'epidemiology.import-finished': 'La importación ha finalizado correctamente',
    'epidemiology.setup-now':'Continuar con la configuración',
    'epidemiology.setup-later':'Configurar más tarde',
    'epi.tpl-title': 'Datos epidemiologicos',
    'epi.date_symptom':'Fecha primeros síntomas',
    'epi.date_arribal': 'Fecha de llegada',
    'epi.date_notification': 'Fecha de notificación',
    'epi.date_nodate': 'Sin fecha (llegada/notificación)',
    'epi.age': 'Edad',
    'epi.country':'País visitado',
    'epi.patient_state':'Estado',
    'epi.province':'Provincia',
    'epi.health_center':'Centro',
    'epi.year':'Año',
    'epidemiology.setup-title': 'Epidemiología. Configuración de la visualización',
    'epidemiology.update': 'Actualizar',
    'epidemiology.period': 'Por',
    'epidemiology.field-map': 'Tipo de mapa',
    'epidemiology.patient_state': 'Estado del paciente',
    'epidemiology.age_band': 'Franjas de edad',
    'epidemiology.date_symptom': 'Fecha primeros síntomas',
    'epidemiology.date_arribal': 'Fecha de llegada',
    'epidemiology.years': 'años',
    'epidemiology.patient-filter': 'Estado de los pacientes',
    'epidemiology.likely': 'Probable',
    'epidemiology.suspected': 'Sospechoso',
    'epidemiology.group-confirmat': 'Confirmado',
    'epidemiology.confirmed': 'Confirmado',
    'epidemiology.confirmed-not-specified': 'Virus no especificado',
    'epidemiology.confirmed-den': 'Dengue',
    'epidemiology.confirmed-zk': 'Zika',
    'epidemiology.confirmed-yf': 'Fiebre amarilla',
    'epidemiology.confirmed-chk': 'Chikunguña',
    'epidemiology.confirmed-wnv': 'Virus del oeste del nilo',
    'epidemiology.form.confirmed-not-specified': 'Confirmado. Virus no especificado',
    'epidemiology.form.confirmed-den': 'Confirmado. Dengue',
    'epidemiology.form.confirmed-zk': 'Confirmado. Zika',
    'epidemiology.form.confirmed-yf': 'Confirmado. Fiebre amarilla',
    'epidemiology.form.confirmed-chk': 'Confirmado. Chikunguña',
    'epidemiology.form.confirmed-wnv': 'Confirmado. Virus del oeste del nilo',
    'epidemiology.undefined': 'Indefinido',
    'epidemiology.nocase': 'No hay caso',
    'epidemiology.all': 'Todos los estados',
    'epidemiology.filter-explanation':'Los filtros temporales del mapa también se aplicarán a esta capa a partir del campo *Fecha de llegada* o "Fecha de notificación* según aplique',
    'epidemiology.upload-explanation': 'ATENCIÓN!! Este proceso de importación eliminará todos los datos previamente almacenados de la capa de Epidemiología',
    'epidemiology.empty-layer': 'En estos momentos la capa Epidemiología no contiene datos.',
    'epidemiology.upload-error': 'Se ha producido un error durante el proceso de importación',
};
_.extend(trans.es, add);
