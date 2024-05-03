#
# forms.py
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

from django import forms


class NewThreatInfoPost(forms.Form):
    name = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rate = forms.ChoiceField(
        choices=((1, '☠'), (2, '☠☠'), (3, '☠☠☠'), (4, '☠☠☠☠'), (5, '☠☠☠☠☠')),
        required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    text = forms.CharField(
        max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))


class AddThreatInfoPost(forms.Form):
    rate = forms.ChoiceField(
        choices=((1, '☠'), (2, '☠☠'), (3, '☠☠☠'), (4, '☠☠☠☠'), (5, '☠☠☠☠☠')),
        required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    text = forms.CharField(
        max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))


class AddPeerReviewPost(forms.Form):
    rate = forms.ChoiceField(
        choices=((1, '☆'), (2, '☆☆'), (3, '☆☆☆'), (4, '☆☆☆☆'), (5, '☆☆☆☆☆')),
        required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    text = forms.CharField(
        max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
