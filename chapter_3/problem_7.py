import re

def make_slug(string):
    slug = re.sub('\s+', '-', string)
    slug = re.sub('-+', '-', slug)
    slug = re.sub('^-', '', slug)
    slug = re.sub('-$', '', slug)
    return slug

print make_slug('  --hello world hello-')
