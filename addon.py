import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon

my_addon = xbmcaddon.Addon('plugin.video.hello-world')

# Retrieve settings
my_bool_setting = my_addon.getSetting('my_bool_setting')
my_text_setting = my_addon.getSetting('my_text_setting')
my_number_setting = my_addon.getSetting('my_number_setting')
my_ip_address_setting = my_addon.getSetting('my_ip_address_setting')
# Set setting
# my_addon.setSetting('my_number_setting', '5')

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:]) #Skip initial ?

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
	return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
	url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
	li = xbmcgui.ListItem('Folder One', iconImage="DefaultFolder.png")
	li.setArt({'fanart': my_addon.getAddonInfo('fanart')})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

	url = build_url({'mode': 'folder', 'foldername': 'Folder Two'})
	li = xbmcgui.ListItem('Folder Two', iconImage="DefaultFolder.png")
	li.setArt({'fanart': my_addon.getAddonInfo('fanart')})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

	xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
	foldername = args['foldername'][0]
	url = 'http://localhost/a-video.mkv'
	li = xbmcgui.ListItem(foldername + ' Video')
	li.setIconImage(my_addon.getAddonInfo('icon'))
	li.setArt({'fanart': my_addon.getAddonInfo('fanart')})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	xbmcplugin.endOfDirectory(addon_handle)