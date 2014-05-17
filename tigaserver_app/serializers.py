from rest_framework import serializers
from tigaserver_app.models import Report, TigaUser, Mission, Photo, Fix, Configuration, ReportResponse, MissionItem


class UserSerializer(serializers.ModelSerializer):
    user_UUID = serializers.CharField()

    def validate_user_UUID(self, attrs, source):
        """
        Check that the user_UUID has exactly 36 characters.
        """
        value = attrs[source]
        if len(str(value)) != 36:
            raise serializers.ValidationError("Make sure user_UUID is EXACTLY 36 characters.")
        return attrs

    class Meta:
        model = TigaUser
        fields = ['user_UUID']


class MissionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionItem


class MissionSerializer(serializers.ModelSerializer):
    items = MissionItemSerializer(many=True)
    title = serializers.CharField()
    short_description = serializers.CharField(help_text='Text to be displayed in mission list.')
    long_description = serializers.CharField(help_text='Text that fully explains mission to user')
    help_text = serializers.CharField(help_text='Text to be displayed when user taps mission help button.')
    language = serializers.CharField(help_text='What language is mission displayed in?')
    platform = serializers.CharField()
    creation_time = serializers.DateTimeField()
    expiration_time = serializers.DateTimeField()
    location_trigger_lat = serializers.FloatField()
    location_trigger_lon = serializers.FloatField()
    time_trigger_lower_bound = serializers.TimeField()
    time_trigger_upper_bound = serializers.TimeField()
    button_left_visible = serializers.BooleanField()
    button_middle_visible = serializers.BooleanField()
    button_right_visible = serializers.BooleanField()
    button_left_text = serializers.CharField()
    button_left_action = serializers.IntegerField()
    button_left_url = serializers.URLField()
    button_middle_text = serializers.CharField()
    button_middle_action = serializers.IntegerField()
    button_middle_url = serializers.URLField()
    button_right_text = serializers.CharField()
    button_right_action = serializers.IntegerField()
    button_right_url = serializers.URLField()

    class Meta:
        model = Mission


class UserListingField(serializers.RelatedField):
    def to_native(self, value):
        return value.user_UUID


class MissionListingField(serializers.RelatedField):
    def to_native(self, value):
        return value.mission_id


class ReportSerializer(serializers.ModelSerializer):
    report_UUID = serializers.CharField(max_length=36)
    user = UserListingField
    mission = MissionListingField
    type = serializers.CharField(help_text="Type of report: 'adult', 'site', or 'mission'.")

    def validate_report_UUID(self, attrs, source):
        """
        Check that the user_UUID has exactly 36 characters.
        """
        value = attrs[source]
        if len(str(value)) != 36:
            raise serializers.ValidationError("Make sure report_UUID is EXACTLY 36 characters.")
        return attrs

    def validate_type(self, attrs, source):
        """
        Check that the report type is either 'adult', 'site', or 'mission'.
        """
        value = attrs[source]
        if value not in ['adult', 'type', 'mission']:
            raise serializers.ValidationError("Make sure type is 'adult', 'site', or 'mission'.")
        return attrs


    class Meta:
        model = Report
        depth = 0
        fields = ['version_UUID',
                  'version_number',
                  'user',
                  'report_id',
                  'server_upload_time',
                  'phone_upload_time',
                  'creation_time',
                  'version_time',
                  'type',
                  'mission',
                  'location_choice',
                  'current_location_lon',
                  'current_location_lat',
                  'selected_location_lon',
                  'selected_location_lat',
                  'note',
                  'package_name',
                  'package_version',
                  'phone_manufacturer',
                  'phone_model',
                  'os',
                  'os_version', ]

class ReportListingField(serializers.RelatedField):
    def to_native(self, value):
        return value.version_UUID


class ReportResponseSerializer(serializers.ModelSerializer):
    report = ReportListingField

    class Meta:
        model = ReportResponse
        fields = ['report', 'question', 'answer']


class PhotoSerializer(serializers.ModelSerializer):
    report = ReportListingField

    class Meta:
        model = Photo
        depth = 0
        fields = ['photo', 'report']


class FixSerializer(serializers.ModelSerializer):
    user = UserListingField(help_text='esting')

    class Meta:
        model = Fix
        depth = 0
        fields = ['user', 'fix_time', 'phone_upload_time', 'masked_lon', 'masked_lat', 'power']


class ConfigurationSerializer(serializers.ModelSerializer):
    """
    Test doc
    param -- descrip
    """
    samples_per_day = serializers.IntegerField(help_text='Number of samples.')
    creation_time = serializers.DateTimeField(help_text='Creation time help', read_only=True)

    class Meta:
        model = Configuration
