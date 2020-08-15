# -*- coding: utf-8 -*-

'''
    ResolveURL Tester Addon
    Author Twilight0

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
'''

from tulip import control


history_size = int(control.setting('history.size'))
history_file = control.join(control.dataPath, 'urls.lst')


def trim_history(file_=history_file):

    """
    Trims history to what is set in settings
    """

    f = open(file_, 'r')
    text = [i.rstrip('\n') for i in f.readlines()]
    f.close()

    if len(text) > history_size:

        f = open(file_, 'w')

        dif = history_size - len(text)
        result = text[:dif]

        f.write('\n'.join(result))
        f.close()


def add_to_history(file_=history_file):

    if not control.exists(file_):
        control.makeFiles(control.dataPath)

    txt = control.dialog.input(control.name())

    if not txt:
        return

    if txt not in read_from_history():

        with open(file_, 'a') as f:
            f.writelines(txt + '\n')

        trim_history(file_)
        control.sleep(200)
        control.refresh()


def read_from_history(file_=history_file):

    """
    Reads from history file which is stored in plain text, line by line
    :return: List
    """

    if control.exists(file_):

        with open(file_, 'r') as f:
            text = [i.rstrip('\n') for i in f.readlines()][::-1]

        return text

    else:

        return ''


def delete_from_history(txt, file_=history_file):

    with open(file_, 'r') as f:
        text = [i.rstrip('\n') for i in f.readlines()]

    text.remove(txt)

    with open(file_, 'w') as f:
        if not text:
            text = ''
        else:
            text = '\n'.join(text) + '\n'
        f.write(text)

    control.sleep(200)
    control.refresh()


def clear_history(file_=history_file):

    if control.exists(file_):

        with open(file_, 'w') as f:
            f.write('')

    control.infoDialog(control.lang(30011))
    control.sleep(200)
    control.refresh()


def readme():

    text = control.addonInfo('disclaimer')

    control.dialog.textviewer(control.name(), text=text)
