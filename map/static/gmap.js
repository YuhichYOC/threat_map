/*
 * gmap.js
 *
 * Copyright 2024 Yuichi Yoshii
 *     吉井雄一 @ 吉井産業  you.65535.kir@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

class GmapOperator {

    #map;
    #info;
    #markers = [];
    #defaultMarkersCount;

    constructor() {
        this.#map = new google.maps.Map(document.getElementById('map'), {
            mapId: "MAP", zoom: 12, center: {lat: 34.66311, lng: 135.49579},
        });
        this.#info = new google.maps.InfoWindow();
    }

    init(args) {
        args.map(i => this.#markers.push(this.#createMarker(i)));
        this.#defaultMarkersCount = this.#markers.length;
        this.#map.addListener('click', (ev) => {
            if (this.#markers.length > this.#defaultMarkersCount) {
                this.#markers.pop().map = null;
            }
            this.#markers.push(
                this.#createMarker({lat: ev.latLng.lat(), lng: ev.latLng.lng(), name: '', threat_info: []})
            );
        });
    }

    #createMarker(info) {
        const m = new google.maps.marker.AdvancedMarkerElement({
            map: this.#map, position: {lat: info.lat, lng: info.lng}, title: info.name,
        });
        m.addListener('click', () => this.#openInfoWindow(m, info));
        return m;
    }

    #openInfoWindow(marker, info) {
        this.#info.close();
        this.#info.setContent(this.#createInfoWindowContent(info));
        this.#info.open(this.#map, marker);
    }

    #createInfoWindowContent(info) {
        if (!info.name) {
            return this.#createForm(true, false, info.lat, info.lng, 0);
        }
        const threat_info = info.threat_info.reduce((seed, i) => {
            return [seed,
                `<hr><ul><li>リスク評価 : ${'☠'.repeat(i.rate)}</li><li>コメント : ${i.text}</li>`,
                i.peer_review.reduce((seed, r) => {
                    return [seed,
                        `<hr><ul><li>レビュースコア : ${'☆'.repeat(r.rate)}</li>`,
                        `<li>コメント : ${r.text}</li></ul>`].join("");
                }, ''),
                '</ul>',
                this.#createForm(false, true, 0, 0, i.id)].join("");
        }, '');
        return [`<div><h1>${info.name}</h1><div>`,
            this.#createForm(false, false, 0, 0, info.id),
            threat_info,
            '</div></div>'].join("");
    }

    #createForm(isNew, isPeerReview, lat, lng, id) {
        const csrf_token = this.#getCookie('csrftoken');
        if (isNew) {
            return ['<form action="/post/new_threat_view/" method="post">',
                `<input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">`,
                `<input type="hidden" name="lat" value="${lat}">`,
                `<input type="hidden" name="lng" value="${lng}">`,
                '<input type="submit" value="危険度情報を記入">',
                '</form>'].join("");
        }
        if (isPeerReview) {
            return ['<form action="/post/add_peer_review_view/" method="post" style="text-align: right">',
                `<input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">`,
                `<input type="hidden" name="id" value="${id}">`,
                '<input type="submit" value="ピアレビューを記入">',
                '</form>'].join("");
        }
        return ['<form action="/post/add_threat_view/" method="post">',
            `<input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">`,
            `<input type="hidden" name="id" value="${id}">`,
            '<input type="submit" value="危険度情報を記入">',
            '</form>'].join("");
    }

    #getCookie(name) {
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                if (cookies[i].trim().startsWith(name)) {
                    return decodeURIComponent(cookies[i].substring(name.length + 1));
                }
            }
        }
        return '';
    }

}
