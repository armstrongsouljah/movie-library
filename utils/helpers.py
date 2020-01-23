from django.utils.text import slugify


def generate_slug(field):
    """takes in a field a returns a slug"""
    return slugify(field)
