#
# views.py
#
# Copyright 2024 Yuichi Yoshii
#     吉井雄一 @ 吉井産業  you.65535.kir@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import urllib.request

from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Item

YOUR_MAPS_API_KEY = ""


def index(request):
    item_list = Item.objects.all()
    ctx = {'info': item_list}
    return render(request, 'map_view.html', ctx)


def get_gmap_js(request):
    url = ''.join([
        'https://maps.googleapis.com/maps/api/js?key=',
        YOUR_MAPS_API_KEY,
        '&language=ja&v=weekly&libraries=marker',
        '&callback=prepare',
    ])
    with urllib.request.urlopen(urllib.request.Request(url)) as target_js:
        return HttpResponse(target_js.read(), content_type='text/javascript')
