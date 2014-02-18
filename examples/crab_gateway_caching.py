# -*- coding: utf-8 -*-
'''
This script demonstrates querying the crab gateway while maintaining a cache.
'''

import os

from crabpy.client import crab_factory, crab_request


from crabpy.gateway.crab import CrabGateway

root = "./dogpile_data/"

if not os.path.exists(root):
    os.makedirs(root)

g = CrabGateway(
    crab,
    cache_config = {
        'permanent.backend': 'dogpile.cache.dbm',
        'permanent.expiration_time': 604800,
        'permanent.arguments.filename': os.path.join(root, 'capakey_permanent.dbm'),
        'long.backend': 'dogpile.cache.dbm',
        'long.expiration_time': 86400,
        'long.arguments.filename': os.path.join(root, 'capakey_long.dbm'),
    }
)

gent = g.get_gemeente_by_id(44021)

print 'Straten in Gent'
print '------------------'

print [str(a) for a in g.list_straten(gent)]

print 'Huisnummers in GENT Straat1'
print '---------------------'

print [str(s) for s in g.list_huisnummers_by_straat(a)]


p = g.get_gemeente_by_niscode(11001)

print 'gemeente: %s' % p.id
print 'naam: %s' % p.naam
print 'niscode: %s' % p.niscode
print 'gewest: %s' % p.gewest
print 'taal: %s' % p.taal
print 'centroid: %s' % p.centroid
print 'bounding_box: %s' % p.bounding_box
