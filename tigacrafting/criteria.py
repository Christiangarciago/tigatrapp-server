from tigaserver_app.models import Photo,Report,TigaUser

def filter_users_by_score(score):
    if score == 'score_bronze':
        score_user_ids = TigaUser.objects.filter(score__gt=0).filter(score__lte=33)
    elif score == 'score_silver':
        score_user_ids = TigaUser.objects.filter(score__gt=33).filter(score__lte=66)
    elif score == 'score_gold':
        score_user_ids = TigaUser.objects.filter(score__gt=66)
    else:
        score_user_ids = TigaUser.objects.filter(score__gt=0).filter(score__lte=33)
    return score_user_ids

def filter_users_with_storm_drain_pictures(reports):
    reports_filtered = filter(lambda x: not x.deleted and x.latest_version and x.embornals, reports)
    return reports_filtered

def filter_users_with_pictures(reports):
    reports_filtered = filter(lambda x: not x.deleted and x.latest_version, reports)
    return reports_filtered

def users_with_pictures():
    return filter_reports('users_with_pictures')

def users_with_score_range(min,max):
    return TigaUser.objects.filter(score__gte=int(min)).filter(score__lte=int(max))

def users_with_score(score):
    return filter_reports(score)

def users_with_storm_drain_pictures():
    return filter_reports('users_with_storm_drain_pictures')

def filter_reports(type):
    photos = Photo.objects.filter(hide=False)
    report_ids = set(photos.values_list('report_id', flat=True))
    reports_site = Report.objects.filter(hide=False).filter(version_UUID__in=report_ids).filter(type='site')
    reports_all = Report.objects.filter(hide=False).filter(version_UUID__in=report_ids)
    if type == 'users_with_storm_drain_pictures':
        reports_filtered = filter_users_with_storm_drain_pictures(reports_site)
    elif type == 'users_with_pictures':
        reports_filtered = filter_users_with_pictures(reports_all)
    elif type.startswith('score'):
        return filter_users_by_score(type)
    user_ids = []
    for r in reports_filtered:
        user_ids.append(r.user_id)
    unique_user_ids = set(user_ids)
    return TigaUser.objects.filter(user_UUID__in=unique_user_ids)
