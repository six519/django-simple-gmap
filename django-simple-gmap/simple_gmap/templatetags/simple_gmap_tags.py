from django import template
register = template.Library()

@register.inclusion_tag("simple_gmap/gmap_init.html")
def gmap_init(lat, lon, zoom=18, canvas_height=400, canvas_width=500):

    return {
        "canvas_width": canvas_width,
        "canvas_height": canvas_height,
        "gmap_lat": lat,
        "gmap_lon": lon,
        "gmap_zoom": zoom
    }