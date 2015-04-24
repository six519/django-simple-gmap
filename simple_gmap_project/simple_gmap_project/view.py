from django.template import RequestContext
from django.shortcuts import render_to_response

def test_page(request):

    return render_to_response('simple_gmap/test_usage.html',{},RequestContext(request))