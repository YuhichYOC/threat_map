#
# models.py
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

from django.db import models


class Item(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    @classmethod
    def create(cls, name):
        item = Item()
        max_id = Item.objects.all().aggregate(models.Max('id'))['id__max']
        item.id = 1 if max_id is None else max_id + 1
        item.name = name
        return item


class Position(models.Model):
    item = models.OneToOneField(Item, primary_key=True, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()

    @classmethod
    def create(cls, item, lat, lng):
        pos = Position()
        pos.item = item
        pos.lat = lat
        pos.lng = lng
        return pos


class ThreatInfo(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rate = models.SmallIntegerField()
    text = models.CharField(max_length=1000)

    @classmethod
    def create(cls, item, rate, text):
        ti = ThreatInfo()
        max_id = ThreatInfo.objects.all().aggregate(models.Max('id'))['id__max']
        ti.id = 1 if max_id is None else max_id + 1
        ti.item = item
        ti.rate = rate
        ti.text = text
        return ti


class PeerReview(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    threat_info = models.ForeignKey(ThreatInfo, on_delete=models.CASCADE)
    rate = models.SmallIntegerField()
    text = models.CharField(max_length=1000)

    @classmethod
    def create(cls, ti, rate, text):
        pr = PeerReview()
        max_id = PeerReview.objects.all().aggregate(models.Max('id'))['id__max']
        pr.id = 1 if max_id is None else max_id + 1
        pr.threat_info = ti
        pr.rate = rate
        pr.text = text
        return pr
