![alt text](https://raw.githubusercontent.com/Twilight0/plugin.video.resolveurl-tester/master/icon.png "Woof woof!")
# ResolveURL Tester

The purpose of this addon is to test links supported by resolveurl resolver library.
- It does not provide any content on its own.

### You can install it from [repository.twilight0](https://github.com/Twilight0/repo.twilight0)

## Features:

- Add a url menu item appears when no cached url are present. Use context menu to add additional urls
- Keeps history of added urls (limited by a setting)
- Can play arbitrary links via plugin route call

## Plugin route playback

You can arbitrarily play any url with the following **sample** snippet:

    import xbmc
    
    try:
        from urllib import quote
    except ImportError:
        from urllib.parse import quote
    
    web_url = 'https://www.youtube.com/watch?v=XIMLoLxmTDw'
    title = 'Black Screen'
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.resolveurl-tester/?action=play&url={0}&title={1}")'.format(quote(web_url), quote(title)))

Or feed it into xbmc.Player()

    xbmc.Player().play('plugin://plugin.video.resolveurl-tester/?action=play&url={0}'.format(web_url))

Or as resolved url:

    url = 'plugin://plugin.video.resolveurl-tester/?action=play&url={0}'.format(web_url)'

    item = xbmcgui.ListItem(path=url)

    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
