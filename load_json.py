# -*- coding: utf-8 -*-

import json
import codecs

class Import():

    def json_file(self, name):
        imported_file = json.loads(open(name).read())
        return (imported_file)
