#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from __init__ import create_app
from libs.links import get_all_groups

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
