# -*- coding: utf-8 -*-

'''
    License summary below, for more details please read license.txt file

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from tulip import directory, control
from resolveurl import HostedMediaFile, resolve, add_plugin_dirs


def router(url):

    try:

        add_plugin_dirs([control.join(control.addonPath, 'resources', 'lib', 'resolvers')])

        if HostedMediaFile(url).valid_url():

            stream = resolve(url)

            return stream

        else:

            raise Exception

    except Exception:

        return url


def play(url, meta=None):

    if meta:

        control.busy()

    stream = router(url)

    if isinstance(meta, dict):

        control.idle()

        if meta['title'] == 'custom':

            title = control.inputDialog()

            meta['title'] = title

    directory.resolve(stream, meta=meta, resolved_mode=meta is None)
