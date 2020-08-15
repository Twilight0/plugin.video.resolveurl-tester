# -*- coding: utf-8 -*-

'''
    ResolveURL Tester Addon
    Author Twilight0

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
'''

from tulip.init import params

action = params.get('action')
url = params.get('url')
query = params.get('query')
title = params.get('title')


if action is None:
    from resources.lib.indexers import navigator
    navigator.root()

elif action == 'play':
    from resources.lib.modules import player
    if query:
        query = {'title': query}
    player.play(url, query)

elif action == 'add':
    from resources.lib.modules import tools
    tools.add_to_history()

elif action == 'readme':
    from resources.lib.modules import tools
    tools.readme()

elif action == 'refresh':
    from tulip.control import refresh
    refresh()

elif action == 'clear_history':
    from resources.lib.modules import tools
    tools.clear_history()

elif action == 'delete_from_history':
    from resources.lib.modules import tools
    tools.delete_from_history(query)

elif action == 'resolveurl_settings':
    from resolveurl import display_settings
    display_settings()
