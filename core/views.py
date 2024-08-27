"""
Core Views Module

This module contains the views for the core pages of the website, including:

1. Home Page (`index`): The landing page of the website, providing an overview
   of the site's offerings.
2. API Information Page (`api_info`): Details about the RESTful API, including
   how developers can start using it and access the API documentation.
3. About Page (`about`): Information about the website and its developers,
   explaining the purpose and background of the site.
4. Contact Page (`contact`): A form allowing users to contact the website
   administrators for inquiries, support, or feedback.

Each view is responsible for rendering a specific template, and these views
form the foundational pages of the website.

Functions:
    - index(request): Renders the home page.
    - api_info(request): Renders the API information page.
    - about(request): Renders the About page.
    - contact(request): Renders the Contact page.
"""


from django.shortcuts import render

# Create your views here.


def index(request):
    """Render the home page (landing page) of the website.

    This view provides the main landing page for the website, where
    users can find an overview of what the site offers. It renders
    the 'core/home.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'core/home.html')


def api_info(request):
    """
    Render the API information page.

    This view provides information about the website's RESTful API,
    including details on how developers can get started with the
    API and access the API documentation. It renders the
    'core/api_info.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered API information page.
    """
    return render(request, 'core/api_info.html')


def api_terms_of_use(request):
    """
    Render the API Terms of use page.

    This view provides information about the website's RESTful API
    Terms of use.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered API information page.
    """
    return render(request, 'core/terms_of_use.html')


def about(request):
    """
    Render the About page of the website.

    This view provides information about the website, including details
    about the developers and the purpose of the site. It renders the
    'core/about.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered About page.
    """
    return render(request, 'core/about.html')


def contact(request):
    """
    Render the Contact page of the website.

    This view provides a contact form that allows users to get in touch
    with the website administrators. It renders the 'core/contact.html'
    template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered Contact page.
    """
    return render(request, 'core/contact.html')
