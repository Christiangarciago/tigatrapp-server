from django.shortcuts import render

# Create your views here.


def show_about(request, platform, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/about_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/about_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/about_en.html', context)


def show_help(request, platform, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/help_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/help_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/help_en.html', context)


def show_license(request, platform, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/license_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/license_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/license_en.html', context)


def show_policies(request, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/policies_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/policies_ca.html', context)
    if language == 'en':
        return render(request, 'tigahelp/policies_ca.html', context)