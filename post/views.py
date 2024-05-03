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

from django.shortcuts import render, HttpResponseRedirect

from map.models import Item, Position, ThreatInfo, PeerReview
from . import forms


def new_threat_view(request):
    return render(request, 'new_threat_view.html', {
        'lat': request.POST.get('lat'),
        'lng': request.POST.get('lng'),
        'form': forms.NewThreatInfoPost(),
    })


def post_new_threat(request):
    item = Item.create(request.POST.get('name'))
    item.save()
    pos = Position.create(item, request.POST.get('lat'), request.POST.get('lng'))
    pos.save()
    threat_info = ThreatInfo.create(item, request.POST.get('rate'), request.POST.get('text'))
    threat_info.save()
    return HttpResponseRedirect('/map/')


def add_threat_view(request):
    return render(request, 'add_threat_view.html', {
        'id': request.POST.get('id'),
        'form': forms.AddThreatInfoPost(),
    })


def post_add_threat(request):
    item = Item.objects.get(id__exact=request.POST.get('id'))
    threat_info = ThreatInfo.create(item, request.POST.get('rate'), request.POST.get('text'))
    threat_info.save()
    return HttpResponseRedirect('/map/')


def add_peer_review_view(request):
    return render(request, 'add_peer_review_view.html', {
        'id': request.POST.get('id'),
        'form': forms.AddPeerReviewPost(),
    })


def post_add_peer_review(request):
    threat_info = ThreatInfo.objects.get(id__exact=request.POST.get('id'))
    peer_review = PeerReview.create(threat_info, request.POST.get('rate'), request.POST.get('text'))
    peer_review.save()
    return HttpResponseRedirect('/map/')
