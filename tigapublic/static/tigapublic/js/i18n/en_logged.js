var trans = trans || {};

add = {
    'layer.trash_layer': 'Other observations',
    'layer.unclassified': 'To validate',

    'expertinfo.tiger_mosquito': ' According to experts, the pictures of this observation could be tiger mosquito (<i>Aedes albopictus</i>). \
      <br/>If their taxonomic features can be clearly seen, especially the white stripe on head and thorax, it will be "confirmed". If some features cannot be observed, it will be "possible".',
    'expertinfo.yellow_fever_mosquito':' According to experts, the pictures of this observation could be yellow fever mosquito (<i>Aedes aegypti</i>). \
      <br/>If their taxonomic features can be clearly seen, especially the lyre in the head and thorax, it will be "confirmed". If some features cannot be seen, it will be "possible".',
    'expertinfo.site': 'Citizens’ observations of possible breeding sites (storm drain or sewer) of tiger or yellow fever mosquitoes. It includes observations that have not yet been filtered by experts.',
    'expertinfo.unclassified':'Observations with photo that have not yet been validated by experts.',
    'expertinfo.trash_layer':'Observations that do not correspond to any other category but which may contain information of interest to managers.',

    'map.controlshare_view_description': 'Share this private map view',
    'share.private_layer_warn': 'Attention! The private data and some of its layers of the current view will only be visible to registered users.',

    //download
    'map.text_description_download': '<p>Only observation citizen data displayed in the current map view will be downloaded. Verify your current active layers, temporal filters and zoom.</p><p>Once verified, press the download button.</p>',

    //Notification
  'usernotification.not-predefined':'Not predefined',
  'check_notifications': 'Notifications',
  'map.control_notifications': 'Issue notification',
  'map.notification.notified': 'To',
  'map.notification.notifier': 'From',
  'map.notification.predefined.title': 'You can use a predefined notification if you want:',
  'map.notification.preset0.body': '<p>This is predefined notification number 1</p><p>Fill the message body as needed.</p>',
  'map.notification.preset0.title': 'Predefined notification 1',
  'map.notification.preset1.body': '<p>This is predefined notification number 2</p><p>There\'s a little bit more text in the message body.</p>',
  'map.notification.preset1.title': 'Predefined notification 2',
  'map.notification.type.none': 'Notification type',
  'map.notification.type.private': 'Private notification',
  'map.notification.type.public': 'Public notification',
  'map.notification_add': 'New notification',
  'map.notification_select_polygon_btn': 'Select territory',
  'map.text_description_notification': '<p>Click <span class="fa fa-pencil"></span> "Select territory" to select the observations which will be sent a notification.</p><p>You can close the polygon double clicking a new vertex, or single clicking an existing vertex (...)',
  'notif.saved': 'Notification successfully sent',
  'notif.notification_cancel': 'Cancel',
  'notif.observations_none': 'No observations selected',
  'notif.sendig_notifications': 'Data is being sent...',

  //modal
  'map.users_found_text': 'Users',
  'info.notifications': 'Notifications',
  'notif.all_field_requiered': 'All fields are required',
  'map.results_found_text': 'Observations',
  'map.title_notification': 'Notification',

  //Draw
  'map.text_description_notification': '<p>Click <span class="fa fa-pencil"></span> "Select territory" to select the observations which will be sent a notification.</p><p>You can close the polygon double clicking a new vertex, or single clicking the starting vertex.<br/><br/>When finishing the polygon, the number of affected observations will be shown on top of this panel and the notification creation form will pop up.</p><p>When the notification form is closed the territory selection must start again.</p>',
  'leaflet.draw.toolbar.cancel.title': 'Cancel notification',

  //Storm Drain
  'stormdrain.send': 'Send',
  'layer.drainstorm': 'Storm drains',
  'drainstorm.nowater': 'Without water',
  'drainstorm.water': 'With water',
  'stormdrain.categories-helper1':'Categories will be evaluated by order of definition.',
  'stormdrain.categories-helper2':'A storm drain will be assigned to a category only if it meets all the specified conditions.',
  'stormdrain.categories-helper3':'Every condition is made out of an attribute and a value.',
  'stormdrain.categories-helper4':'Storm drains which are already assigned to a category will not be evaluated again.',
  'stormdrain.field-activity': 'Activity',
  'stormdrain.field-date': 'Date',
  'stormdrain.field-sand': 'Sand',
  'stormdrain.field-species1': 'Species A',
  'stormdrain.field-species2': 'Species B',
  'stormdrain.field-treatment': 'Treatment',
  'stormdrain.field-type': 'Type',
  'stormdrain.field-water': 'Water',
  'stormdrain.import-finished': 'Import completed successfully',
  'stormdrain.import-started': 'Importing data. This could take a while.',
  'stormdrain.label-categories': 'Categories',
  'stormdrain.label-color': 'Color',
  'stormdrain.label-conditions': 'Conditions',
  'stormdrain.label-field': 'Field',
  'stormdrain.label-value': 'Value',
  'stormdrain.label-versions': 'Version',
  'stormdrain.main-title': 'Storm drain visualization setup',
  'stormdrain.none-txt': 'None',
  'stormdrain.operator-<=': ' up to',
  'stormdrain.operator-<>': ' not equal to',
  'stormdrain.operator-=': ' equal to',
  'stormdrain.operator->=': ' from',
  'stormdrain.setup.submit.ok': 'New configuration has been saved',
  'stormdrain.setup-later': 'Configure storm drains later',
  'stormdrain.setup-now': 'Continue with storm drain configuration',
  'stormdrain.upload-button': 'Select file',
  'stormdrain.get-template':'Download template',
  'stormdrain.upload-comment': 'Title (30 characters max)',
  'stormdrain.upload-error': 'There has been an error:',
  'stormdrain.upload-newversion': 'Version number:',
  'stormdrain.upload-required': 'All fields are required',
  'stormdrain.upload-title': 'Storm drain upload',
  'stormdrain.user-txt': 'User',
  'stormdrain.value-0': 'No',
  'stormdrain.value-1': 'Yes',
  'stormdrain.value-E': 'Storm drain',
  'stormdrain.value-F': 'Fountain',
  'stormdrain.value-false': 'No',
  'stormdrain.value-R': 'Grating',
  'stormdrain.value-true': 'Yes',
  'stormdrain.value-null': 'No value',
  'stormdrain.version-helper': 'Select version to setup',
  'stormdrain.version-txt': 'Version',
  'stormdrain.water': 'Water',
  'stormdrain.example-title': 'Storm drain configuration example',
  'stormdrain.example-body-1': 'We want to represent and color-code storm drains in the following two categories:',
  'stormdrain.example-body-2': 'With water and treated. Green-coloured',
  'stormdrain.example-body-3': 'With water and non-treated. Red-coloured',
  'stormdrain.example-body-4': 'We would need to do this:',
  'stormdrain.example-body-5': 'img/stormdrain_example_1_en.png',
  'stormdrain.example-body-6': 'If we configured the visualization using the following settings, this would <strong>NOT</strong> work: ',
  'stormdrain.example-body-7': 'img/stormdrain_example_2_en.png',
  'stormdrain.example-body-8': 'Why in this case we would not see two types of storm drains (with water and treated; and with water and non-treated)?, What would we be seeing?',
  'stormdrain.example-body-9': 'Green-coloured storm drains with the attribute «water» = «Yes». Independently of the values of other attributes (treatment, date, etc.).',
  'stormdrain.example-body-10': 'Purple-coloured, storm drains that don’t fit with the first category and have the attribute «Treatment» = «Yes».',
  'stormdrain.example-body-11': 'Blue-coloured, storm drains that don’t fit neither the two categories and have the column «Treatment» = «No».',
  'stormdrain.example-body-12': 'Each colour is associated with a category. Each category can have one or more conditions. Each condition refers to an attribute, an operator (equal to, not equal to, etc.) and a «value».',
  'stormdrain.example-body-13': 'Storm drains must have all the conditions of the categories in order to fit in each one (logical operator AND).',
  'stormdrain.example-body-14': 'When a storm drain fits in one category, it is not evaluated in the other categories. For example, when one storm drain has the column «water»= «Yes» and «treatment» = «Yes» is will be represented in Green, because it’s the first category that matches all the conditions (in this case there is only one).',

  //configuración de la capa epidemiologia
  'layer.epidemiology': 'Epidemiology',
  'epidemiology.upload-title': 'Epidemiology upload',
  'epidemiology.get-template': 'Epidemiology template',
  'epidemiology.upload-button': 'Select file',
  'epidemiology.import-started': 'Importing data. This could take a while.',
  'epidemiology.import-finished': 'Import completed successfully',
  'epidemiology.setup-now': 'Continue with data configuration',
  'epidemiology.setup-later': 'Configure later',
  'epi.tpl-title':'Epidemiology data',
  'epi.date_symptom': 'Date first symptoms',
  'epi.date_arribal': 'Arribal date',
  'epi.age': 'Age',
  'epi.country': 'Country',
  'epi.patient_state':'State',
  'epi.province':'Province',
  'epi.health_center':'Center',
  'epi.year':'Year',
  'epidemiology.setup-title': 'Epidemiology. View setup',
  'epidemiology.update': 'Update',
  'epidemiology.period': 'By',
  'epidemiology.field-map': 'Map type',
  'epidemiology.patient_state': 'Patient state',
  'epidemiology.age_band': 'Age ranges',
  'epidemiology.date_symptom': 'Sympthoms date',
  'epidemiology.date_arribal': 'Arribal date',
  'epidemiology.years': 'years',
  'epidemiology.patient-filter': 'Patient states',
  'epidemiology.likely': 'Likely',
  'epidemiology.suspected': 'Suspected',
  'epidemiology.confirmed': 'Confirmed',
  'epidemiology.undefined': 'Undefined',
  'epidemiology.nocase': 'No case',
  'epidemiology.all': 'All states',
  'epidemiology.filter-explanation':'If a date filter is applied to the map, it will also be applied to this layer on *date_arribal* field',
  'epidemiology.upload-explanation': 'WARNING!! The upload proces will delete all previouly stored data for the epidemiology layer',
  'epidemiology.empty-layer': 'There is no epidemiology data available at the moment',
  'epidemiology.upload-error': 'An error occurred while importing data',
};
_.extend(trans.en, add);
