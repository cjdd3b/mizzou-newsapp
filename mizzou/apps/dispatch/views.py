from django.shortcuts import render_to_response, get_object_or_404
from mizzou.apps.dispatch.models import Dispatch, Type

########## THE BASICS ##########

def dispatch_list(request):
    '''
    View to list all dispatch types.
    '''
    # Return all types of dispatch calls for display in a list
    types = Type.objects.all().order_by('name')

    # Use the render-to-response shortcut to send the data to a template
    # See: https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#render-to-response
    return render_to_response('basic/index.html', {'types': types})


def dispatch_detail(request, slug):
    '''
    View all calls for a specific dispatch type.
    '''
    # Use the get_object_or_404 shortcut to return a specific type
    type = get_object_or_404(Type, slug=slug)

    # Now get all the dispatches associated with that type
    dispatches = type.dispatch_set.all()

    # Again, use render_to_response
    return render_to_response('basic/crime_detail.html', {'type': type, 'dispatches': dispatches})


########## ADVANCED ##########

def index(request):
    '''
    Main view for the index page!
    '''
    # Return all types of dispatch calls for display in a list
    types = Type.objects.all().order_by('name')

    # Use the render-to-response shortcut to send the data to a template
    # See: https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#render-to-response
    return render_to_response('advanced/index.html', {'types': types})


def map_api(request):
    '''
    A view that generates a JSON file that feeds points into our
    map. JSON is a common platform-agnostic format for sending data
    to things like AJAX calls.

    More on JSON here: http://en.wikipedia.org/wiki/JSON
    And AJAX here: http://www.w3schools.com/ajax/default.asp
    '''
    # By default, get all of the dispatch objects in the database 
    points = Dispatch.objects.all()

    # The GET query string passed at the end of any URL ins your project can
    # be accessed like this (for example, in www.website.com/?type=1), "type=1"
    # is the GET string.
    if request.GET: # If your request has a GET string ...

        # Variables passed in via GET are made accessible via dictionary object.
        # In the example above, the Django representation of the type=1 GET string
        # would be {'type': 1}
        if request.GET.has_key('type'): # Check for a dictionary key called type

            # If it's there, get the value corresponding with that key and use it to
            # get the corresponding Type object from the database.
            type_slug = request.GET.get('type')
            filter_type = Type.objects.get(slug=type_slug)

            # Finally, filter the points based on that type
            points = points.filter(type=filter_type)

    # Render to response is the same here, with one addition. Because we're rendering a JSON
    # file and not an HTML page, we want browsers and other clients to see it as the correct
    # type of file. That's where the optional mimetype argument comes in.
    # Reference here: http://en.wikipedia.org/wiki/Internet_media_type
    return render_to_response('advanced/points.json', {'points': points}, mimetype="application/json")
