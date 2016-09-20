from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.exceptions import ParseError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import django_filters
from datetime import datetime, timedelta
import pytz
import calendar
import json
from operator import attrgetter
from tigaserver_app.serializers import NotificationSerializer, UserSerializer, ReportSerializer, MissionSerializer, PhotoSerializer, FixSerializer, ConfigurationSerializer, MapDataSerializer, SiteMapSerializer, CoverageMapSerializer, CoverageMonthMapSerializer, TagSerializer, NearbyReportSerializer
from tigaserver_app.models import Notification, TigaUser, Mission, Report, Photo, Fix, Configuration, CoverageArea, CoverageAreaMonth
from math import ceil
from taggit.models import Tag
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.contrib.gis.geos import Point, GEOSGeometry



class ReadOnlyModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, and 'list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class WriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides`create` action.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


class ReadWriteOnlyModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    A viewset that provides `retrieve`, 'list`, and `create` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """
    pass


@api_view(['GET'])
def get_current_configuration(request):
    """
API endpoint for getting most recent app configuration created by Movelab.

**Fields**

* id: Auto-incremented primary key record ID.
* samples_per_day: Number of randomly-timed location samples to take per day.
* creation_time: Date and time when this configuration was created by MoveLab. Automatically generated when
record is saved.
    """
    if request.method == 'GET':
        current_config = Configuration.objects.order_by('creation_time').last()
        serializer = ConfigurationSerializer(current_config)
        return Response(serializer.data)


@api_view(['GET'])
def get_new_missions(request):
    """
API endpoint for getting most missions that have not yet been downloaded.

**Fields**

* id: Unique identifier of the mission. Automatically generated by server when mission created.
* title_catalan: Title of mission in Catalan.
* title_spanish: Title of mission in Spanish.
* title_english: Title of mission in English.
* short_description_catalan: Catalan text to be displayed in mission list.
* short_description_spanish: Spanish text to be displayed in mission list.
* short_description_english: English text to be displayed in mission list.
* long_description_catalan: Catalan text that fully explains mission to user.
* long_description_spanish: Spanish text that fully explains mission to user.
* long_description_english: English text that fully explains mission to user.
* help_text_catalan: Catalan text to be displayed when user taps mission help button.
* help_text_spanish: Spanish text to be displayed when user taps mission help button.
* help_text_english: English text to be displayed when user taps mission help button.
* platform: What type of device is this mission is intended for? It will be sent only to these devices.
* creation_time: Date and time mission was created by MoveLab. Automatically generated when mission saved.
* expiration_time: Optional date and time when mission should expire (if ever). Mission will no longer be displayed to users after this date-time.
* photo_mission: Should this mission allow users to attach photos to their responses? (True/False).
* url: Optional URL that wll be displayed to user for this mission. (The entire mission can consist of user going to that URL and performing some action there. For security reasons, this URL must be within a MoveLab domain.
* mission_version: Optional integer that can be used to ensure that new mission parameters that we may create in the
future do not cause problems on older versions of the app. The Android app is currently set to respond only to
missions with mission_version=1 or null.
* triggers:
    * lat_lower_bound:Optional lower-bound latitude for triggering mission to appear to user. Given in decimal degrees.
    * lat_upper_bound: Optional upper-bound latitude for triggering mission to appear to user. Given in decimal degrees.
    * lon_lower_bound: Optional lower-bound longitude for triggering mission to appear to user. Given in decimal
    degrees.
    * lon_upper_bound: Optional upper-bound longitude for triggering mission to appear to user. Given in decimal degrees.
    * time_lowerbound: Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as [ISO 8601](http://www.w3.org/TR/NOTE-datetime) time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)
    * time_upperbound: Lower bound of optional time-of-day window for triggering mission. If location trigger also is specified, mission will be triggered only if user is found in that location within the window; if location is not specified, the mission will be triggered for all users who have their phones on during the time window. Given as time without date, formatted as [ISO 8601](http://www.w3.org/TR/NOTE-datetime) time string (e.g. "12:34:00") with no time zone specified (trigger is always based on local time zone of user.)
* items:
    * question_catalan: Question displayed to user in Catalan.
    * question_spanish: Question displayed to user in Spanish.
    * question_english: Question displayed to user in English.
    * answer_choices_catalan: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * answer_choices_spanish: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * answer_choices_english: Response choices, with each choice surrounded by square brackets (e.g. _[Yes][No]_).
    * help_text_catalan: Help text displayed to user for this item.
    * help_text_spanish: Help text displayed to user for this item.
    * help_text_english: Help text displayed to user for this item.
    * prepositioned_image_reference: Optional image displayed to user within the help message. Integer reference to image prepositioned on device.')
    * attached_image: Optional Image displayed to user within the help message. File.

**Query Parameters**

* id_gt: Returns records with id greater than the specified value. Use this for getting only those missions that have not yet been downloaded. Default is 0.
* platform: Returns records matching exactly the platform code or those with 'all' or null. Default is 'all'.
* version_lte: returns records with mission_version less than or equal to the value specified or those with
mission_version null. Defaults to 100.
    """
    if request.method == 'GET':
        these_missions = Mission.objects.filter(Q(id__gt=request.QUERY_PARAMS.get('id_gt', 0)),
                                                Q(platform__exact=request.QUERY_PARAMS.get('platform', 'all')) | Q(platform__isnull=True) | Q(platform__exact='all'),
                                                Q(mission_version__lte=request.QUERY_PARAMS.get('version_lte',100)) | Q(mission_version__isnull=True)).order_by('id')
        serializer = MissionSerializer(these_missions)
        return Response(serializer.data)


@api_view(['GET'])
def get_photo(request):
    if request.method == 'GET':
        user_id = request.QUERY_PARAMS.get('user_id', -1)
        #get user reports by user id
        these_reports = Report.objects.filter(user_id=user_id).values('version_UUID').distinct()
        these_photos = Photo.objects.filter(report_id__in=these_reports)
        serializer = PhotoSerializer(these_photos)
        return Response(serializer.data)


@api_view(['POST'])
def post_photo(request):
    """
API endpoint for uploading photos associated with a report. Data must be posted as multipart form,
with with _photo_ used as the form key for the file itself, and _report_ used as the key for the report
version_UUID linking this photo to a specific report version.

**Fields**

* photo: The photo's binary image data
* report: The version_UUID of the report to which this photo is attached.
    """
    if request.method == 'POST':
        this_report = Report.objects.get(version_UUID=request.DATA['report'])
        instance = Photo(photo=request.FILES['photo'], report=this_report)
        instance.save()
        return Response('uploaded')


# For production version, substitute WriteOnlyModelViewSet
class UserViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting user registration. The only information required is a 36 digit UUID generated on
user's
device. (Registration time is also added by server automatically and included in the database, but is not accessible
through the API.)

**Fields**

* user_UUID: UUID randomly generated on phone to identify each unique user. Must be exactly 36 characters (32 hex digits plus 4 hyphens).
    """
    queryset = TigaUser.objects.all()
    serializer_class = UserSerializer


class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        return JSONRenderer()


# For production version, substitute WriteOnlyModelViewSet
class ReportViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting new reports and report versions. (Every time a user edits a report,
a new version is
posted; user keeps only most recent version on phone but server retains all versions.) Note that photos attached to the
report must be uploaded separately through the [photo](/api/photos/) endpoint. (Also note that the HTML form, below,
for testing posts does not work for including responses in posted reports; use the raw/JSON format instead.)

**Fields**

* version_UUID: UUID randomly generated on phone to identify each unique report version. Must be exactly 36 characters (32 hex digits plus 4 hyphens).
* version_number: The report version number. Should be an integer that increments by 1 for each repor version. Note
that the user keeps only the most recent version on the device, but all versions are stored on the server. To
delete a report, submit a version with version_number = -1. This will cause the report to no longer be displated on
the server map (although it will still be retained internally).
* user: user_UUID for the user sending this report. Must be exactly 36 characters (32 hex digits plus 4 hyphens) and user must have already registered this ID.
* report_id: 4-digit alpha-numeric code generated on user phone to identify each unique report from that user. Digits should lbe randomly drawn from the set of all lowercase and uppercase alphabetic characters and 0-9, but excluding 0, o, and O to avoid confusion if we ever need user to be able to refer to a report ID in correspondence with MoveLab (as was previously the case when we had them sending samples).
* phone_upload_time: Date and time on phone when it uploaded fix. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56.123+01:00".
* creation_time:Date and time on phone when first version of report was created. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string
(e.g. "2014-05-17T12:34:56.123+01:00".
* version_time:Date and time on phone when this version of report was created. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e
.g. "2014-05-17T12:34:56.123+01:00".
* type: Type of report: 'adult', 'site', or 'mission'.
* mission: If this report was a response to a mission, the unique id field of that mission.
* location_choice: Did user indicate that report relates to current location of phone ("current") or to a location selected manually on the map ("selected")?
* current_location_lon: Longitude of user's current location. In decimal degrees.
* current_location_lat: Latitude of user's current location. In decimal degrees.
* selected_location_lon: Latitude of location selected by user on map. In decimal degrees.
* selected_location_lat: Longitude of location selected by user on map. In decimal degrees.
* note: Note user attached to report.
* package_name: Name of tigatrapp package from which this report was submitted.
* package_version: Version number of tigatrapp package from which this report was submitted.
* device_manufacturer: Manufacturer of device from which this report was submitted.
* device_model: Model of device from which this report was submitted.
* os:  Operating system of device from which this report was submitted.
* os_version: Operating system version of device from which this report was submitted.
* os_language: Language setting of operating system on device from which this report was submitted. 2-digit [ISO 639-1](http://www.iso.org/iso/home/standards/language_codes.htm) language code.
* app_language:Language setting, within tigatrapp, of device from which this report was submitted. 2-digit [ISO 639-1](http://www.iso.org/iso/home/standards/language_codes.htm) language code.
* responses:
    * question: Question that the user responded to.
    * answer: Answer that user selected.

**Query Parameters**

* user_UUID: The user_UUID for a particular user.
* version_number: The report version number.
* report_id: The 4-digit report ID.
* type: The report type (adult, site, or mission).
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_fields = ('user', 'version_number', 'report_id', 'type')


# For production version, substitute WriteOnlyModelViewSet
class PhotoViewSet(ReadWriteOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


# For production version, substitute WriteOnlyModelViewSet
class FixViewSet(ReadWriteOnlyModelViewSet):
    """
API endpoint for getting and posting masked location fixes.

**Fields**

* user: The 36-digit user_UUID for the user sending this location fix.
* fix_time: Date and time when fix was recorded on phone. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56'
                                              '.123+01:00".
* server_upload_time: Date and time registered by server when it received fix upload. Automatically generated by server.'
* phone_upload_time: Date and time on phone when it uploaded fix. Format as [ECMA 262](http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15) date time string (e.g. "2014-05-17T12:34:56.123+01:00".
* masked_lon: Longitude rounded down to nearest 0.05 decimal degree (floor(lon/.05)*.05).
* masked_lat: Latitude rounded down to nearest 0.05 decimal degree (floor(lat/.05)*.05).
* power: Power level of phone at time fix recorded, expressed as proportion of full charge. Range: 0-1.

**Query Parameters**

* user_UUID: The UUID of the user sending this fix.
    """
    queryset = Fix.objects.all()
    serializer_class = FixSerializer
    filter_fields = ('user_coverage_uuid', )


def lookup_photo(request, token, photo_uuid, size):
    if token == settings.PHOTO_SECRET_KEY:
        this_photo = Photo.objects.get(uuid=photo_uuid)
        if size == 'small':
            url = this_photo.get_small_url()
        elif size == 'medium':
            url = this_photo.get_medium_url()
        else:
            url = this_photo.photo.url
        return HttpResponseRedirect(url)


def get_data_time_info(request):
    # setting fixed start time based on release date to avoid the pre-release beta reports
    start_time = settings.START_TIME
    end_time = Report.objects.latest('creation_time').creation_time
    days = (end_time - start_time).days + 1
    weeks = ceil(days / 7.0)
    months = ceil(days / 28.0)
    json_response = {'start_time_posix': calendar.timegm(start_time.utctimetuple()), 'end_time_posix': calendar.timegm(end_time.utctimetuple()), 'n_days': days, 'n_weeks': weeks, 'n_months': months}
    return HttpResponse(json.dumps(json_response))


def get_n_days():
    # setting fixed start time based on release date to avoid the pre-release beta reports
    start_time = settings.START_TIME
    end_time = Report.objects.latest('creation_time').creation_time
    # adding 1 to include the last dayin the set
    return (end_time - start_time).days + 1


def get_n_months():
    # setting fixed start time based on release date to avoid the pre-release beta reports
    start_time = settings.START_TIME
    end_time = Report.objects.latest('creation_time').creation_time
    # adding 1 to include the last dayin the set
    return ((end_time - start_time).days / 28) + 1


def filter_creation_day(queryset, days_since_launch):
    if not days_since_launch:
        return queryset
    try:
        target_day_start = settings.START_TIME + timedelta(days=int(days_since_launch))
        target_day_end = settings.START_TIME + timedelta(days=int(days_since_launch)+1)
        result = queryset.filter(creation_time__range=(target_day_start, target_day_end))
        return result
    except ValueError:
        return queryset


def filter_creation_week(queryset, weeks_since_launch):
    if not weeks_since_launch:
        return queryset
    try:
        target_week_start = settings.START_TIME + timedelta(weeks=int(weeks_since_launch))
        target_week_end = settings.START_TIME + timedelta(weeks=int(weeks_since_launch)+1)
        result = queryset.filter(creation_time__range=(target_week_start, target_week_end))
        return result
    except ValueError:
        return queryset


def filter_creation_month(queryset, months_since_launch):
    if not months_since_launch:
        return queryset
    try:
        target_month_start = settings.START_TIME + timedelta(weeks=int(months_since_launch)*4)
        target_month_end = settings.START_TIME + timedelta(weeks=(int(months_since_launch)*4)+4)
        result = queryset.filter(creation_time__range=(target_month_start, target_month_end))
        return result
    except ValueError:
        return queryset


def filter_creation_year(queryset, year):
    if not year:
        return queryset
    try:
        result = queryset.filter(creation_time__year=year)
        return result
    except ValueError:
        return queryset


class MapDataFilter(django_filters.FilterSet):
    day = django_filters.Filter(action=filter_creation_day)
    week = django_filters.Filter(action=filter_creation_week)
    month = django_filters.Filter(action=filter_creation_month)
    year = django_filters.Filter(action=filter_creation_year)

    class Meta:
        model = Report
        fields = ['day', 'week', 'month', 'year']


class CoverageMapFilter(django_filters.FilterSet):
    id_range_start = django_filters.NumberFilter(name='id', lookup_type='gte')
    id_range_end = django_filters.NumberFilter(name='id', lookup_type='lte')

    class Meta:
        model = CoverageArea
        fields = ['id_range_start', 'id_range_end']


class CoverageMonthMapFilter(django_filters.FilterSet):
    id_range_start = django_filters.NumberFilter(name='id', lookup_type='gte')
    id_range_end = django_filters.NumberFilter(name='id', lookup_type='lte')

    class Meta:
        model = CoverageAreaMonth
        fields = ['id_range_start', 'id_range_end']


def get_latest_reports_qs(reports, property_filter=None):
    if property_filter == 'movelab_cat_ge1':
        unique_report_ids = set(r.report_id for r in filter(lambda x: hasattr(x, 'movelab_annotation') and x.movelab_annotation is not None and 'tiger_certainty_category' in x.movelab_annotation and x.movelab_annotation['tiger_certainty_category'] >= 1, reports.iterator()))
    elif property_filter == 'movelab_cat_ge2':
        unique_report_ids = set(r.report_id for r in filter(lambda x: hasattr(x, 'movelab_annotation') and x.movelab_annotation is not None and 'tiger_certainty_category' in x.movelab_annotation and x.movelab_annotation['tiger_certainty_category'] == 2, reports.iterator()))
    elif property_filter == 'embornals_fonts':
        unique_report_ids = set(r.report_id for r in filter(lambda x: x.embornals or x.fonts, reports.iterator()))
    elif property_filter == 'basins':
        unique_report_ids = set(r.report_id for r in filter(lambda x: x.basins, reports.iterator()))
    elif property_filter == 'buckets_wells':
        unique_report_ids = set(r.report_id for r in filter(lambda x: x.buckets or x.wells, reports.iterator()))
    elif property_filter == 'other':
        unique_report_ids = set(r.report_id for r in filter(lambda x: x.other, reports.iterator()))
    else:
        unique_report_ids = set([r.report_id for r in reports])
    result_ids = list()
    for this_id in unique_report_ids:
        these_reports = sorted([report for report in reports if report.report_id == this_id], key=attrgetter('version_number'))
        if these_reports[0].version_number > -1:
            # taking the version with the highest movelab score, if this is a adult report cat_ge1 or cat_ge2 request, otherwise most recent version
            if property_filter in ('movelab_cat_ge1', 'movelab_cat_ge2'):
                movelab_sorted_reports = sorted(filter(lambda x: hasattr(x, 'movelab_annotation') and x.movelab_annotation is not None and 'tiger_certainty_category' in x.movelab_annotation, these_reports), key=attrgetter('movelab_score'))
                this_version_UUID = movelab_sorted_reports[-1].version_UUID
            else:
                this_version_UUID = these_reports[-1].version_UUID
            result_ids.append(this_version_UUID)
    return Report.objects.filter(version_UUID__in=result_ids)


def get_latest_validated_reports(reports):
    reports = filter(lambda x: x.show_on_map(), reports.iterator())
    unique_report_ids = set([r.report_id for r in reports])
    result_ids = list()
    for this_id in unique_report_ids:
        these_reports = sorted([report for report in reports if report.report_id == this_id], key=attrgetter('version_number'))
        if these_reports[0].version_number > -1:
            this_version_UUID = these_reports[-1].version_UUID
            result_ids.append(this_version_UUID)
    return Report.objects.filter(version_UUID__in=result_ids)


class AllReportsMapViewSet(ReadOnlyModelViewSet):
    queryset = Report.objects.exclude(hide=True).filter(Q(package_name='Tigatrapp', creation_time__gte=settings.IOS_START_TIME) | Q(package_name='ceab.movelab.tigatrapp', package_version__gt=3)).exclude(package_name='ceab.movelab.tigatrapp', package_version=10)
    serializer_class = MapDataSerializer
    filter_class = MapDataFilter


def lon_function(this_lon, these_lons, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    n_fixes = len([l for l in these_lons if l == this_lon])
    if CoverageAreaMonth.objects.filter(lat=this_lat[0], lon=this_lon[0], year=this_lat[1],month=this_lat[2]).count() > 0:
        this_coverage_area = CoverageAreaMonth.objects.get(lat=this_lat[0], lon=this_lon[0], year=this_lat[1],month=this_lat[2])
        this_coverage_area.n_fixes += n_fixes
    else:
        this_coverage_area = CoverageAreaMonth(lat=this_lat[0], lon=this_lon[0], year=this_lat[1],month=this_lat[2], n_fixes=n_fixes)
    if fix_list and fix_list.count() > 0:
        this_coverage_area.latest_fix_id = fix_list.order_by('id').last().id
    else:
        this_coverage_area.latest_fix_id = latest_fix_id
    if report_list and report_list.count() > 0:
        this_coverage_area.latest_report_server_upload_time = report_list.order_by('server_upload_time').last().server_upload_time
    else:
        this_coverage_area.latest_report_server_upload_time = latest_report_server_upload_time
    this_coverage_area.save()


def lon_function_m0(this_lon, these_lons_m0, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    n_fixes = len([l for l in these_lons_m0 if l == this_lon])
    if CoverageAreaMonth.objects.filter(lat=this_lat[0], lon=this_lon[0], year=this_lat[1], month=0).count() > 0:
        this_coverage_area = CoverageAreaMonth.objects.get(lat=this_lat[0], lon=this_lon[0], year=this_lat[1], month=0)
        this_coverage_area.n_fixes += n_fixes
    else:
        this_coverage_area = CoverageAreaMonth(lat=this_lat[0], lon=this_lon[0], year=this_lat[1], month=0, n_fixes=n_fixes)
    if fix_list and fix_list.count() > 0:
        this_coverage_area.latest_fix_id = fix_list.order_by('id').last().id
    else:
        this_coverage_area.latest_fix_id = latest_fix_id
    if report_list and report_list.count() > 0:
        this_coverage_area.latest_report_server_upload_time = report_list.order_by('server_upload_time').last().server_upload_time
    else:
        this_coverage_area.latest_report_server_upload_time = latest_report_server_upload_time
    this_coverage_area.save()


def lon_function_y0(this_lon, these_lons_y0, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    n_fixes = len([l for l in these_lons_y0 if l == this_lon])
    if CoverageAreaMonth.objects.filter(lat=this_lat[0], lon=this_lon[0], month=this_lat[1], year=0).count() > 0:
        this_coverage_area = CoverageAreaMonth.objects.get(lat=this_lat[0], lon=this_lon[0], month=this_lat[1], year=0)
        this_coverage_area.n_fixes += n_fixes
    else:
        this_coverage_area = CoverageAreaMonth(lat=this_lat[0], lon=this_lon[0], month=this_lat[1], year=0, n_fixes=n_fixes)
    if fix_list and fix_list.count() > 0:
        this_coverage_area.latest_fix_id = fix_list.order_by('id').last().id
    else:
        this_coverage_area.latest_fix_id = latest_fix_id
    if report_list and report_list.count() > 0:
        this_coverage_area.latest_report_server_upload_time = report_list.order_by('server_upload_time').last().server_upload_time
    else:
        this_coverage_area.latest_report_server_upload_time = latest_report_server_upload_time
    this_coverage_area.save()


def lat_function(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    these_lons = [(f.masked_lon, f.fix_time.year, f.fix_time.month) for f in fix_list if (f.masked_lat == this_lat[0] and f.fix_time.year == this_lat[1] and f.fix_time.month == this_lat[2])] + [(r.masked_lon, r.creation_time.year, r.creation_time.month) for r in report_list if (r.masked_lat is not None and r.masked_lat == this_lat and r.creation_time.year == this_lat[1] and r.creation_time.month == this_lat[2])]
    unique_lons = set(these_lons)
    [lon_function(this_lon, these_lons, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lon in unique_lons]


def lat_function_m0(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    these_lons_m0 = [(f.masked_lon, f.fix_time.year) for f in fix_list if (f.masked_lat == this_lat[0] and f.fix_time.year == this_lat[1])] + [(r.masked_lon, r.creation_time.year) for r in report_list if (r.masked_lat is not None and r.masked_lat == this_lat and r.creation_time.year == this_lat[1])]
    unique_lons_m0 = set(these_lons_m0)
    [lon_function_m0(this_lon, these_lons_m0, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lon in unique_lons_m0]


def lat_function_y0(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time):
    these_lons_y0 = [(f.masked_lon, f.fix_time.month) for f in fix_list if (f.masked_lat == this_lat[0] and f.fix_time.month == this_lat[1])] + [(r.masked_lon, r.creation_time.month) for r in report_list if (r.masked_lat is not None and r.masked_lat == this_lat and r.creation_time.month == this_lat[1])]
    unique_lons_y0 = set(these_lons_y0)
    [lon_function_y0(this_lon, these_lons_y0, this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lon in unique_lons_y0]


def update_coverage_area_month_model_manual():
    json_response = {'updated': False}
    # turning off for now
    if True:
        if CoverageAreaMonth.objects.all().count() > 0:
            latest_report_server_upload_time = CoverageAreaMonth.objects.order_by('latest_report_server_upload_time').last().latest_report_server_upload_time
            latest_fix_id = CoverageAreaMonth.objects.order_by('latest_fix_id').last().latest_fix_id
        else:
            latest_report_server_upload_time = pytz.utc.localize(datetime(1970, 1, 1))
            latest_fix_id = 0
        if CoverageAreaMonth.objects.all().count() == 0 or latest_report_server_upload_time < Report.objects.order_by('server_upload_time').last().server_upload_time or latest_fix_id < Fix.objects.order_by('id').last().id:
            report_list = get_latest_reports_qs(Report.objects.exclude(hide=True).filter(Q(package_name='Tigatrapp',  creation_time__gte=settings.IOS_START_TIME) | Q(package_name='ceab.movelab.tigatrapp', package_version__gt=3)).filter(server_upload_time__gt=latest_report_server_upload_time))
            fix_list = Fix.objects.filter(fix_time__gt=settings.START_TIME, id__gt=latest_fix_id)
            full_lat_list = [(f.masked_lat, f.fix_time.year, f.fix_time.month) for f in fix_list] + [(r.masked_lat, r.creation_time.year, r.creation_time.month) for r in report_list if r.masked_lat is not None]
            full_lat_list_m0 = [(f.masked_lat, f.fix_time.year) for f in fix_list] + [(r.masked_lat, r.creation_time.year) for r in report_list if r.masked_lat is not None]
            full_lat_list_y0 = [(f.masked_lat, f.fix_time.month) for f in fix_list] + [(r.masked_lat, r.creation_time.month) for r in report_list if r.masked_lat is not None]
            unique_lats = set(full_lat_list)
            unique_lats_m0 = set(full_lat_list_m0)
            unique_lats_y0 = set(full_lat_list_y0)
            [lat_function(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lat in unique_lats]
            [lat_function_m0(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lat in unique_lats_m0]
            [lat_function_y0(this_lat, fix_list, latest_fix_id, report_list, latest_report_server_upload_time) for this_lat in unique_lats_y0]
            json_response['updated'] = True
    return json.dumps(json_response)


class CoverageMonthMapViewSet(ReadOnlyModelViewSet):
    queryset = CoverageAreaMonth.objects.all()
    serializer_class = CoverageMonthMapSerializer
    filter_class = CoverageMonthMapFilter

def filter_partial_name(queryset, name):
    if not name:
        return queryset
    return queryset.filter(name__icontains=name)

class TagFilter(django_filters.FilterSet):
    name = django_filters.Filter(action=filter_partial_name)

    class Meta:
        model = Tag
        fields = ['name']

class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_class = TagFilter

def string_par_to_bool(string_par):
    if string_par:
        string_lower = string_par.lower()
        if string_lower == 'true':
            return True
    return False

@api_view(['GET','POST'])
def user_notifications(request):
    if request.method == 'GET':
        user_id = request.QUERY_PARAMS.get('user_id', -1)
        acknowledged = 'ignore'
        if request.QUERY_PARAMS.get('acknowledged') != None:
            acknowledged = request.QUERY_PARAMS.get('acknowledged', False)
        all_notifications = Notification.objects.all()
        if user_id != -1:
            all_notifications = all_notifications.filter(user_id=user_id)
        if acknowledged != 'ignore':
            all_notifications = all_notifications.filter(acknowledged=acknowledged)
        serializer = NotificationSerializer(all_notifications)
        return Response(serializer.data)
    if request.method == 'POST':
        id = request.QUERY_PARAMS.get('id', -1)
        try:
            int(id)
        except ValueError:
            raise ParseError(detail='Invalid id integer value')
        queryset = Notification.objects.all()
        this_notification = get_object_or_404(queryset,pk=id)
        ack = request.QUERY_PARAMS.get('acknowledged', True)
        ack_bool = string_par_to_bool(ack)
        this_notification.acknowledged = ack_bool
        this_notification.save()
        serializer = NotificationSerializer(this_notification)
        return Response(serializer.data)

@api_view(['GET'])
def nearby_reports(request):
    if request.method == 'GET':
        dwindow = request.QUERY_PARAMS.get('dwindow', 30)
        try:
            int(dwindow)
        except ValueError:
            raise ParseError(detail='Invalid dwindow integer value')
        if int(dwindow) > 365:
            raise ParseError(detail='Values above 365 not allowed for dwindow')

        date_N_days_ago = datetime.now() - timedelta(days=int(dwindow))

        center_buffer_lat = request.QUERY_PARAMS.get('lat', None)
        center_buffer_lon = request.QUERY_PARAMS.get('lon', None)
        radius = request.QUERY_PARAMS.get('radius', '2500')
        if center_buffer_lat is None or center_buffer_lon is None:
            return Response(status=400,data='invalid parameters')

        center_point_4326 = GEOSGeometry('SRID=4326;POINT(' + center_buffer_lon + ' ' + center_buffer_lat + ')')
        center_point_3857 = center_point_4326.transform(3857,clone=True)

        swcorner_3857 = GEOSGeometry('SRID=3857;POINT(' + str(center_point_3857.x - float(radius)) + ' ' + str(center_point_3857.y - float(radius)) + ')')
        nwcorner_3857 = GEOSGeometry('SRID=3857;POINT(' + str(center_point_3857.x - float(radius)) + ' ' + str(center_point_3857.y + float(radius)) + ')')
        secorner_3857 = GEOSGeometry('SRID=3857;POINT(' + str(center_point_3857.x + float(radius)) + ' ' + str(center_point_3857.y - float(radius)) + ')')
        necorner_3857 = GEOSGeometry('SRID=3857;POINT(' + str(center_point_3857.x + float(radius)) + ' ' + str(center_point_3857.y + float(radius)) + ')')

        swcorner_4326 = swcorner_3857.transform(4326,clone=True)
        nwcorner_4326 = nwcorner_3857.transform(4326, clone=True)
        secorner_4326 = secorner_3857.transform(4326, clone=True)
        necorner_4326 = necorner_3857.transform(4326, clone=True)

        min_lon = swcorner_4326.x
        min_lat = swcorner_4326.y

        max_lon = necorner_4326.x
        max_lat = necorner_4326.y

        all_reports = Report.objects.exclude(creation_time__year=2014).exclude(note__icontains="#345").exclude(hide=True).exclude(photos__isnull=True).filter(type='adult').annotate(n_annotations=Count('expert_report_annotations')).filter(n_annotations__gte=3).exclude(creation_time__lte=date_N_days_ago)
        #Broad square filter
        all_reports = all_reports.filter(Q(location_choice='selected', selected_location_lon__range=(min_lon,max_lon),selected_location_lat__range=(min_lat, max_lat)) | Q(location_choice='current', current_location_lon__range=(min_lon,max_lon), current_location_lat__range=(min_lat, max_lat)))
        classified_reports = filter(lambda x: x.simplified_annotation is not None and x.simplified_annotation['score'] > 0,all_reports)
        serializer = NearbyReportSerializer(classified_reports)
        return Response(serializer.data)
