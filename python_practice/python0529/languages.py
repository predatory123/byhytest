from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['ken'] = 'C'
favorite_languages['jack'] = 'PHP'
favorite_languages['ben'] = 'JAVA'
favorite_languages['phile'] = 'R'

for k, v in favorite_languages.items():
    print(k + '___' + v)
