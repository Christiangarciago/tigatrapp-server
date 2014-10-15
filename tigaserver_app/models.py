from django.db import models
import uuid
import os
import os.path
from PIL import Image
import datetime
from math import floor
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from django.db.models import Max, Min
from tigacrafting.models import CrowdcraftingTask
from django.db.models import Count


class TigaUser(models.Model):
    user_UUID = models.CharField(max_length=36, primary_key=True, help_text='UUID randomly generated on '
                                                                            'phone to identify each unique user. Must be exactly 36 '
                                                                            'characters (32 hex digits plus 4 hyphens).')
    registration_time = models.DateTimeField(auto_now=True, help_text='The date and time when user '
                                                                      'registered and consented to sharing '
                                                                 'data. Automatically set by '
                                                                 'server when user uploads registration.')

    def __unicode__(self):
        return self.user_UUID

    def number_of_reports_uploaded(self):
        return Report.objects.filter(user=self).count()

    def is_ios(self):
        return self.user_UUID.isupper()

    n_reports = property(number_of_reports_uploaded)
    ios_user = property(is_ios)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Mission(models.Model):
    id = models.AutoField(primary_key=True, help_text='Unique identifier of the mission. Automatically generated by ' \
                                                  'server when mission created.')
    title_catalan = models.CharField(max_length=200, help_text='Title of mission in Catalan')
    title_spanish = models.CharField(max_length=200, help_text='Title of mission in Spanish')
    title_english = models.CharField(max_length=200, help_text='Title of mission in English')
    short_description_catalan = models.CharField(max_length=200, help_text='Catalan text to be displayed '
                                                                                       'in mission '
                                                                           'list.')
    short_description_spanish = models.CharField(max_length=200, help_text='Spanish text to be displayed '
                                                                                      'in mission '
                                                                           'list.')
    short_description_english = models.CharField(max_length=200, help_text='English text to be displayed '
                                                                                      'in mission '
                                                                           'list.')
    long_description_catalan = models.CharField(max_length=1000, blank=True, help_text='Catalan text that fully ' \
                                                                                     'explains '
                                                                             'mission '
                                                                           'to '
                                                                           'user')
    long_description_spanish = models.CharField(max_length=1000, blank=True, help_text='Spanish text that fully ' \
                                                                                     'explains mission '
                                                                           'to user')
    long_description_english = models.CharField(max_length=1000, blank=True, help_text='English text that fully ' \
                                                                                     'explains mission '
                                                                           'to user')
    help_text_catalan = models.TextField(blank=True, help_text='Catalan text to be displayed when user taps mission '
                                                               'help '
                                                               'button.')
    help_text_spanish = models.TextField(blank=True, help_text='Spanish text to be displayed when user taps mission '
                                                               'help '
                                                               'button.')
    help_text_english = models.TextField(blank=True, help_text='English text to be displayed when user taps mission '
                                                               'help '
                                                               'button.')
    PLATFORM_CHOICES = (('none', 'No platforms (for drafts)'), ('and', 'Android'), ('ios', 'iOS'), ('html', 'HTML5'), ('beta', 'beta versions only'), ('all',
                                                                                               'All platforms'),)
    platform = models.CharField(max_length=4, choices=PLATFORM_CHOICES, help_text='What type of device is this '
                                                                                   'mission is intended for? It will '
                                                                                   'be sent only to these devices')
    creation_time = models.DateTimeField(auto_now=True, help_text='Date and time mission was created by MoveLab. '
                                                                  'Automatically generated when mission saved.')
    expiration_time = models.DateTimeField(blank=True, null=True, help_text='Optional date and time when mission '
                                                                            'should expire (if ever). Mission will no longer be displayed to users after this date-time.')

    photo_mission = models.BooleanField(help_text='Should this mission allow users to attach photos to their '
                                                  'responses? (True/False).')
    url = models.URLField(blank=True, help_text='Optional URL that wll be displayed to user for this mission. (The '
                                                'entire mission can consist of user going to that URL and performing '
                                                'some action there. For security reasons, this URL must be within a '
                                                'MoveLab domain.')
    mission_version = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title_catalan

    def active_missions(self):
        return self.expiration_time >= datetime.datetime.utcnow().replace(tzinfo=utc)


class MissionTrigger(models.Model):
    mission = models.ForeignKey(Mission, related_name='triggers')
    lat_lower_bound = models.FloatField(blank=True, null=True, help_text='Optional lower-bound latitude for '
                                                                         'triggering mission to appear to user. Given in decimal degrees.')
    lat_upper_bound = models.FloatField(blank=True, null=True, help_text='Optional upper-bound latitude for '
                                                                         'triggering mission to appear to user. Given in decimal degrees.')
    lon_lower_bound = models.FloatField(blank=True, null=True, help_text='Optional lower-bound longitude for '
                                                                         'triggering mission to appear to user. Given in decimal degrees.')
    lon_upper_bound = models.FloatField(blank=True, null=True, help_text='Optional upper-bound longitude for '
                                                                         'triggering mission to appear to user. Given in decimal degrees.')
    time_lowerbound = models.TimeField(blank=True, null=True, help_text='Lower bound of optional time-of-day window '
                                                                        'for triggering mission. If '
                                                                        'location trigger also is specified, mission will '
                                                                        'be triggered only '
                                                                        'if user is found in that location within the window; if '
                                                                        'location is not specified, the mission will '
                                                                        'be triggered for all users who have their phones on during the '
                                                                        'time window. Given as time without date, '
                                                                        'formatted as ISO 8601 time string (e.g. '
                                                                        '"12:34:00") with no time zone specified (trigger '
                                                                        'is always based on local time zone of user.)')
    time_upperbound = models.TimeField(blank=True, null=True, help_text='Lower bound of optional time-of-day window '
                                                                        'for triggering mission. If '
                                                                        'location trigger also is specified, mission will '
                                                                        'be triggered only if user is found in that location within the window; if '
                                                                        'location is not specified, the mission will be '
                                                                        'triggered for all users who have their phones on during the '
                                                                        'time window. Given as time without date, '
                                                                        'formatted as ISO 8601 time string (e.g. '
                                                                        '"12:34:00") with no time zone specified (trigger '
                                                                        'is always based on local time zone of user.)')


class MissionItem(models.Model):
    mission = models.ForeignKey(Mission, related_name='items', help_text='Mission to which this item is associated.')
    question_catalan = models.CharField(max_length=1000, help_text='Question displayed to user in Catalan.')
    question_spanish = models.CharField(max_length=1000, help_text='Question displayed to user in Spanish.')
    question_english = models.CharField(max_length=1000, help_text='Question displayed to user in English.')
    answer_choices_catalan = models.CharField(max_length=1000, help_text='Response choices in Catalan, wrapped in '
                                                                         'square '
                                                                         'brackets '
                                                                       '(e.g., [yes][no]).')
    answer_choices_spanish = models.CharField(max_length=1000, help_text='Response choices in Spanish, wrapped in '
                                                                         'square '
                                                                         'brackets (e.g., [yes][no]).')
    answer_choices_english = models.CharField(max_length=1000, help_text='Response choices in English, wrapped in '
                                                                         'square '
                                                                         'brackets (e.g., [yes][no]).')
    help_text_catalan = models.TextField(blank=True, help_text='Catalan help text displayed to user for this item.')
    help_text_spanish = models.TextField(blank=True, help_text='Spanish help text displayed to user for this item.')
    help_text_english = models.TextField(blank=True, help_text='English help text displayed to user for this item.')
    prepositioned_image_reference = models.IntegerField(blank=True, null=True, help_text='Optional image '
                                                                                         'displayed to user '
                                                                                         'within the help '
                                                                                         'message. Integer '
                                                                                         'reference to image '
                                                                                         'prepositioned on device.')
    attached_image = models.ImageField(upload_to='tigaserver_mission_images', blank=True, null=True,
                                       help_text='Optional Image displayed to user within the help message. File.')


class Report(models.Model):
    version_UUID = models.CharField(max_length=36, primary_key=True, help_text='UUID randomly generated on '
                                                'phone to identify each unique report version. Must be exactly 36 '
                                                'characters (32 hex digits plus 4 hyphens).')
    version_number = models.IntegerField(db_index=True, help_text='The report version number. Should be an integer that increments '
                                                   'by 1 for each repor version. Note that the user keeps only the '
                                                   'most recent version on the device, but all versions are stored on the server.')
    user = models.ForeignKey(TigaUser, help_text='user_UUID for the user sending this report. Must be exactly 36 '
                                                 'characters (32 hex digits plus 4 hyphens) and user must have '
                                                 'already registered this ID.')
    report_id = models.CharField(db_index=True, max_length=4, help_text='4-digit alpha-numeric code generated on user phone to '
                                                         'identify each unique report from that user. Digits should '
                                                         'lbe randomly drawn from the set of all lowercase and '
                                                         'uppercase alphabetic characters and 0-9, but excluding 0, '
                                                         'o, and O to avoid confusion if we ever need user to be able to refer to a report ID in correspondence with MoveLab (as was previously the case when we had them sending samples).')
    server_upload_time = models.DateTimeField(auto_now_add=True, help_text='Date and time on server when report '
                                                                           'uploaded. (Automatically generated by '
                                                                           'server.)')
    phone_upload_time = models.DateTimeField(help_text='Date and time on phone when it uploaded fix. Format '
                                                       'as ECMA '
                                                       '262 date time string (e.g. "2014-05-17T12:34:56'
                                                       '.123+01:00".')
    creation_time = models.DateTimeField(help_text='Date and time on phone when first version of report was created. '
                                                   'Format '
                                                       'as ECMA '
                                                       '262 date time string (e.g. "2014-05-17T12:34:56'
                                                       '.123+01:00".')
    version_time = models.DateTimeField(help_text='Date and time on phone when this version of report was created. '
                                                  'Format '
                                                       'as ECMA '
                                                       '262 date time string (e.g. "2014-05-17T12:34:56'
                                                       '.123+01:00".')
    TYPE_CHOICES = (('adult', 'Adult'), ('site', 'Breeding Site'), ('mission', 'Mission'),)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, help_text="Type of report: 'adult', 'site', "
                                                                         "or 'mission'.", )
    mission = models.ForeignKey(Mission, blank=True, null=True, help_text='If this report was a response to a '
                                                                          'mission, the unique id field of that '
                                                                          'mission.')
    LOCATION_CHOICE_CHOICES = (('current', "Current location detected by user's device"), ('selected',
                                                                                           'Location selected by '
                                                                                           'user from map'),
                               ('missing', 'No location choice submitted - should be used only for missions'))
    location_choice = models.CharField(max_length=8, choices=LOCATION_CHOICE_CHOICES, help_text='Did user indicate '
                                                                                                'that report relates '
                                                                                                'to current location '
                                                                                                'of phone ("current") or to a location selected manually on the map ("selected")? Or is the choice missing ("missing")')
    current_location_lon = models.FloatField(blank=True, null=True, help_text="Longitude of user's current location. "
                                                                              "In decimal degrees.")
    current_location_lat = models.FloatField(blank=True, null=True, help_text="Latitude of user's current location. "
                                                                              "In decimal degrees.")
    selected_location_lon = models.FloatField(blank=True, null=True, help_text="Latitude of location selected by "
                                                                               "user on map. "
                                                                              "In decimal degrees.")
    selected_location_lat = models.FloatField(blank=True, null=True, help_text="Longitude of location selected by "
                                                                               "user on map. "
                                                                              "In decimal degrees.")
    note = models.TextField(blank=True, help_text='Note user attached to report.')
    package_name = models.CharField(db_index=True, max_length=400, blank=True, help_text='Name of tigatrapp package from which this '
                                                                          'report was submitted.')
    package_version = models.IntegerField(db_index=True, blank=True, null=True, help_text='Version number of tigatrapp package from '
                                                                           'which this '
                                                                          'report was submitted.')
    device_manufacturer = models.CharField(max_length=200, blank=True, help_text='Manufacturer of device from which '
                                                                                'this '
                                                                          'report was submitted.')
    device_model = models.CharField(max_length=200, blank=True, help_text='Model of device from '
                                                                         'which this '
                                                                          'report was submitted.')
    os = models.CharField(max_length=200, blank=True, help_text='Operating system of device from which this '
                                                                          'report was submitted.')
    os_version = models.CharField(max_length=200, blank=True, help_text='Operating system version of device from '
                                                                        'which this '
                                                                          'report was submitted.')
    os_language = models.CharField(max_length=2, blank=True, help_text='Language setting of operating system on '
                                                                         'device from '
                                                                        'which this '
                                                                          'report was submitted. 2-digit '
                                                                        'ISO-639-1 language code.')
    app_language = models.CharField(max_length=2, blank=True, help_text='Language setting, within tigatrapp, '
                                                                        'of device '
                                                                          'from '
                                                                        'which this '
                                                                          'report was submitted. 2-digit '
                                                                        'ISO-639-1 language code.')

    hide = models.BooleanField(default=False, help_text='Hide this report from public views?')

    def __unicode__(self):
        return self.version_UUID

    def get_lat(self):
        if self.location_choice == 'selected' and self.selected_location_lat is not None:
            return self.selected_location_lat
        else:
            return self.current_location_lat

    def get_lon(self):
        if self.location_choice == 'selected' and self.selected_location_lon is not None:
            return self.selected_location_lon
        else:
            return self.current_location_lon

    def get_tigaprob(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = 0
        total = 0
        for this_response in these_responses:
            total += 1
            if 'Y' in this_response.answer or 'S' in this_response.answer:
                result += 1
            if this_response.answer == 'No':
                result -= 1
        if total == 0:
            total = 1
        return float(result)/total

    def get_response_html(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID).order_by('question')
        result = ''
        for this_response in these_responses:
            result = result + '<br/>' + this_response.question + '&nbsp;' + this_response.answer
        return result

    def get_response_string(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID).order_by('question')
        result = ''
        for this_response in these_responses:
            result = result + '{' + this_response.question + ' ' + this_response.answer + '}'
        return result

    def get_tigaprob_text(self):
        if self.tigaprob == 1.0:
            return _('High')
        elif 0.0 < self.tigaprob < 1.0:
            return _('Medium')
        else:
            return _('Low')

    def get_site_type(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer
        return result

    def get_site_type_trans(self):
        if self.embornals:
            return _('Storm drain')
        if self.fonts:
            return _('Fountain')
        if self.basins:
            return _('Basin')
        if self.wells:
            return _('Well')
        if self.other:
            return _('Other')

    def get_site_embornals(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Embornals' or this_response.answer == 'Sumideros' or \
                    'Storm' in this_response.answer
        return result

    def get_site_fonts(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Fonts' or this_response.answer == 'Fountain' or \
                    this_response.answer == "Fuentes"
        return result

    def get_site_basins(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Basin' or this_response.answer == 'Basses' or \
                    'balsas' in this_response.answer
        return result

    def get_site_buckets(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Bucket' or this_response.answer == 'Bidones' or \
                    'Bidons' in this_response.answer
        return result

    def get_site_wells(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Well' or this_response.answer == 'Pozos' or \
                    this_response.answer == 'Pous'
        return result

    def get_site_other(self):
        these_responses = ReportResponse.objects.filter(report__version_UUID=self.version_UUID)
        result = ''
        for this_response in these_responses:
            if this_response.question.startswith('Tipo') or this_response.question.startswith('Selecciona') or \
                    this_response.question.startswith('Type'):
                result = this_response.answer == 'Other' or this_response.answer == 'Altres' or \
                    this_response.answer == 'Otros'
        return result

    def get_masked_lat(self):
        if self.lat is not None:
            return floor(self.lat/.05)*.05
        else:
            return None

    def get_masked_lon(self):
        if self.lon is not None:
            return floor(self.lon/.05)*.05
        else:
            return None

    def get_n_photos(self):
        these_photos = Photo.objects.filter(report__version_UUID=self.version_UUID)
        return len(these_photos)

    def get_photo_html(self):
        these_photos = Photo.objects.filter(report__version_UUID=self.version_UUID).exclude(hide=True)
        result = ''
        for photo in these_photos:
            result = result + photo.small_image_() + '&nbsp;'
        return result

    def get_formatted_date(self):
        return self.version_time.strftime("%d-%m-%Y %H:%M")

    def get_is_deleted(self):
        result = False
        all_versions = Report.objects.filter(report_id=self.report_id).order_by('version_number')
        if all_versions[0].version_number == -1:
            result = True
        return result

    def get_other_versions(self):
        all_versions = Report.objects.filter(report_id=self.report_id).exclude(version_UUID=self.version_UUID).order_by('version_number')
        result = ''
        for this_version in all_versions:
            result += '<a href="/admin/tigaserver_app/report/%s">Version %s</a> ' % (this_version.version_UUID, this_version.version_number)
        return result

    def get_is_latest(self):
        if self.version_number == -1:
            return False
        elif Report.objects.filter(report_id=self.report_id).count() == 1:
            return True
        else:
            all_versions = Report.objects.filter(report_id=self.report_id).order_by('version_number')
            if all_versions[0].version_number == -1:
                return False
            elif all_versions.reverse()[0].version_number == self.version_number:
                return True

    def get_crowdcrafting_score(self):
        if self.type not in ('site', 'adult'):
           scores = None
        else:
            these_tasks = CrowdcraftingTask.objects.filter(photo__report__version_UUID=self.version_UUID).annotate(n_responses=Count('responses')).filter(n_responses__gte=30).exclude(photo__report__hide=True).exclude(photo__hide=True)
            these_tasks_filtered = filter(lambda x: not x.photo.report.deleted and x.photo.report.latest_version, these_tasks)
            if len(these_tasks_filtered) == 0:
                scores = None
            elif self.type == 'site':
                scores = map(lambda x: x.site_validation_score, these_tasks_filtered)
            else:
                scores = map(lambda x: x.tiger_validation_score, these_tasks_filtered)
        return scores

    lon = property(get_lon)
    lat = property(get_lat)
    tigaprob = property(get_tigaprob)
    tigaprob_text = property(get_tigaprob_text)
    site_type = property(get_site_type)
    site_type_trans = property(get_site_type_trans)
    embornals = property(get_site_embornals)
    fonts = property(get_site_fonts)
    basins = property(get_site_basins)
    buckets = property(get_site_buckets)
    wells = property(get_site_wells)
    other = property(get_site_other)
    masked_lat = property(get_masked_lat)
    masked_lon = property(get_masked_lon)
    n_photos = property(get_n_photos)
    photo_html = property(get_photo_html)
    formatted_date = property(get_formatted_date)
    response_html = property(get_response_html)
    response_string = property(get_response_string)
    deleted = property(get_is_deleted)
    other_versions = property(get_other_versions)
    latest_version = property(get_is_latest)
    crowdcrafting_score = property(get_crowdcrafting_score)

    class Meta:
        unique_together = ("user", "version_UUID")


class ReportResponse(models.Model):
    report = models.ForeignKey(Report, related_name='responses', help_text='Report to which this response is ' \
                                                                          'associated.')
    question = models.CharField(max_length=1000, help_text='Question that the user responded to.')
    answer = models.CharField(max_length=1000, help_text='Answer that user selected.')

    def __unicode__(self):
        return str(self.id)


def make_image_uuid(path):
    def wrapper(instance, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join(path, filename)
    return wrapper


def make_uuid():
    return str(uuid.uuid4())


class Photo(models.Model):
    """
    Photo uploaded by user.
    """
    photo = models.ImageField(upload_to=make_image_uuid('tigapics'), help_text='Photo uploaded by user.')
    report = models.ForeignKey(Report, related_name='photos', help_text='Report and version to which this photo is associated (36-digit '
                                                 'report_UUID).')
    hide = models.BooleanField(default=False, help_text='Hide this photo from public views?')
    uuid = models.CharField(max_length=36, default=make_uuid)

    def __unicode__(self):
        return self.photo.name

    def get_user(self):
        return self.report.user

    def get_date(self):
        return self.report.version_time.strftime("%d-%m-%Y %H:%M")

    def get_small_path(self):
        return self.photo.path.replace('tigapics/', 'tigapics_small/')

    def get_small_url(self):
        if os.path.isfile(self.photo.path):
            if not os.path.isfile(self.get_small_path()):
                im = Image.open(self.photo.path)
                try:
                    im.thumbnail((120, 120), Image.ANTIALIAS)
                except IOError:
                    im.thumbnail((120, 120), Image.NEAREST)
                im.save(self.get_small_path())
            return self.photo.url.replace('tigapics/', 'tigapics_small/')

    def small_image_(self):
        return '<a href="{0}"><img src="{1}"></a>'.format(self.photo.url, self.get_small_url())

    small_image_.allow_tags = True

    def get_medium_path(self):
        return self.photo.path.replace('tigapics/', 'tigapics_medium/')

    def get_medium_url(self):
        if os.path.isfile(self.photo.path):
            if not os.path.isfile(self.get_medium_path()):
                im = Image.open(self.photo.path)
                try:
                    im.thumbnail((460, 460), Image.ANTIALIAS)
                except IOError:
                    im.thumbnail((460, 460), Image.NEAREST)
                im.save(self.get_medium_path())
            return self.photo.url.replace('tigapics/', 'tigapics_medium/')

    def medium_image_(self):
        return '<a href="{0}"><img src="{1}"></a>'.format(self.photo.url, self.get_medium_url())

    medium_image_.allow_tags = True

    user = property(get_user)
    date = property(get_date)


class Fix(models.Model):
    """
    Location fix uploaded by user.
    """
    user_coverage_uuid = models.CharField(blank=True, null=True, max_length=36, help_text='UUID randomly generated on '
                                                                            'phone to identify each unique user, '
                                                                            'but only within the coverage data so '
                                                                            'that privacy issues are not raised by '
                                                                            'linking this to the report data.'
                                                                            '. Must be exactly 36 '
                                                                            'characters (32 hex digits plus 4 hyphens).')

    fix_time = models.DateTimeField(help_text='Date and time when fix was recorded on phone. Format as ECMA '
                                              '262 date time string (e.g. "2014-05-17T12:34:56'
                                              '.123+01:00".')
    server_upload_time = models.DateTimeField(auto_now_add=True, help_text='Date and time registered by server when '
                                                                           'it received fix upload. Automatically '
                                                                           'generated by server.')
    phone_upload_time = models.DateTimeField(help_text='Date and time on phone when it uploaded fix. Format '
                                                       'as ECMA '
                                                       '262 date time string (e.g. "2014-05-17T12:34:56'
                                                       '.123+01:00".')
    masked_lon = models.FloatField(help_text='Longitude rounded down to nearest 0.5 decimal degree (floor(lon/.5)*.5)'
                                             '.')
    masked_lat = models.FloatField(help_text='Latitude rounded down to nearest 0.5 decimal degree (floor(lat/.5)*.5).')
    power = models.FloatField(null=True, blank=True, help_text='Power level of phone at time fix recorded, '
                                                               'expressed as proportion of full charge. Range: 0-1.')

    def __unicode__(self):
        result = 'NA'
        if self.user_coverage_uuid is not None:
            result = self.user_coverage_uuid
        return result

    class Meta:
        verbose_name = "fix"
        verbose_name_plural = "fixes"


class Configuration(models.Model):
    id = models.AutoField(primary_key=True, help_text='Auto-incremented primary key record ID.')
    samples_per_day = models.IntegerField(help_text="Number of randomly-timed location samples to take per day.")
    creation_time = models.DateTimeField(help_text='Date and time when this configuration was created by MoveLab. '
                                                   'Automatically generated when record is saved.',
                                         auto_now_add=True)

    def __unicode__(self):
        return str(self.samples_per_day)