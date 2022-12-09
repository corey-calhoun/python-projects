# Python script that erases all browser history, cookies, and cache from the system
# Prints out the number of files deleted for each browser

import os
import shutil

# Firefox
firefox_path = os.path.expanduser('~') + '/.mozilla/firefox'
firefox_cache = firefox_path + '/Cache'
firefox_cookies = firefox_path + '/cookies.sqlite'
firefox_history = firefox_path + '/places.sqlite'
firefox_downloads = firefox_path + '/downloads.sqlite'

# Chrome
chrome_path = os.path.expanduser('~') + '/.config/google-chrome'
chrome_cache = chrome_path + '/Cache'
chrome_cookies = chrome_path + '/Default/Cookies'
chrome_history = chrome_path + '/Default/History'
chrome_downloads = chrome_path + '/Default/History'

# Safari
safari_path = os.path.expanduser('~') + '/Library/Safari'
safari_cache = safari_path + '/Caches'
safari_cookies = safari_path + '/Cookies.binarycookies'
safari_history = safari_path + '/History.db'
safari_downloads = safari_path + '/Downloads.db'

# Erase Firefox cache
def erase_firefox_cache():
    if os.path.exists(firefox_cache):
        shutil.rmtree(firefox_cache)
        print('Firefox cache deleted')
    else:
        print('Firefox cache not found')

# Erase Firefox cookies
def erase_firefox_cookies():
    if os.path.exists(firefox_cookies):
        os.remove(firefox_cookies)
        print('Firefox cookies deleted')
    else:
        print('Firefox cookies not found')

# Erase Firefox history
def erase_firefox_history():
    if os.path.exists(firefox_history):
        os.remove(firefox_history)
        print('Firefox history deleted')
    else:
        print('Firefox history not found')

# Erase Firefox downloads
def erase_firefox_downloads():
    if os.path.exists(firefox_downloads):
        os.remove(firefox_downloads)
        print('Firefox downloads deleted')
    else:
        print('Firefox downloads not found')

# Erase Chrome cache
def erase_chrome_cache():
    if os.path.exists(chrome_cache):
        shutil.rmtree(chrome_cache)
        print('Chrome cache deleted')
    else:
        print('Chrome cache not found')

# Erase Chrome cookies
def erase_chrome_cookies():
    if os.path.exists(chrome_cookies):
        os.remove(chrome_cookies)
        print('Chrome cookies deleted')
    else:
        print('Chrome cookies not found')

# Erase Chrome history
def erase_chrome_history():
    if os.path.exists(chrome_history):
        os.remove(chrome_history)
        print('Chrome history deleted')
    else:
        print('Chrome history not found')

# Erase Chrome downloads
def erase_chrome_downloads():
    if os.path.exists(chrome_downloads):
        os.remove(chrome_downloads)
        print('Chrome downloads deleted')
    else:
        print('Chrome downloads not found')

# Erase Safari cache
def erase_safari_cache():
    if os.path.exists(safari_cache):
        shutil.rmtree(safari_cache)
        print('Safari cache deleted')
    else:
        print('Safari cache not found')

# Erase Safari cookies
def erase_safari_cookies():
    if os.path.exists(safari_cookies):
        os.remove(safari_cookies)
        print('Safari cookies deleted')
    else:
        print('Safari cookies not found')

# Erase Safari history
def erase_safari_history():
    if os.path.exists(safari_history):
        os.remove(safari_history)
        print('Safari history deleted')
    else:
        print('Safari history not found')

# Erase Safari downloads
def erase_safari_downloads():
    if os.path.exists(safari_downloads):
        os.remove(safari_downloads)
        print('Safari downloads deleted')
    else:
        print('Safari downloads not found')

# Erase all browser history
def erase_all():
    erase_firefox_cache()
    erase_firefox_cookies()
    erase_firefox_history()
    erase_firefox_downloads()
    erase_chrome_cache()
    erase_chrome_cookies()
    erase_chrome_history()
    erase_chrome_downloads()
    erase_safari_cache()
    erase_safari_cookies()
    erase_safari_history()
    erase_safari_downloads()

# Main
erase_all()

# End of script
