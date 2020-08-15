# -*- coding: utf-8 -*-

'''
    ResolveURL Tester Addon
    Author Twilight0

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
'''

from tulip import directory, control
from resolveurl import HostedMediaFile, resolve, add_plugin_dirs, relevant_resolvers
from resolveurl.resolver import ResolverError


def router(url):

    try:

        add_plugin_dirs([control.join(control.addonPath, 'resources', 'lib', 'resolvers')])

        forced_host = control.setting('force_host')

        rr = relevant_resolvers()
        domains = [r.domains for r in rr][1:]
        domain_list = [d for dm in domains for d in dm]

        if forced_host in domain_list:

            stream = HostedMediaFile(media_id=url, host=forced_host).resolve()

            return stream

        elif HostedMediaFile(url).valid_url():

            stream = resolve(url)

            return stream

        else:

            return url

    except ResolverError:

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
