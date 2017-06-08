#!/usr/bin/python
# Copyright (c) 2016 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pprint import pprint
import os, sys, re
import logging
import cmdln
import json

LANGS = {
        # SLE main languages
        'Arabic': 'ar',
        'Brazilian Portugese': 'pt_BR',
        'Chinese Simplified': 'zh_CN',
        'Chinese Traditional': 'zh_TW',
        'Czech': 'cs',
        'Dutch': 'nl',
        'French': 'fr',
        'German': 'de',
        'Hungarian': 'hu',
        'Italian': 'it',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Polish': 'pl',
        'Russian': 'ru',
        'Spanish': 'es',
        'Swedish': 'sv',
        # strong openSUSE languages
        'Catalan': 'ca',
        'Greek' : 'el',
        'Slovak': 'sk',
        'Ukrainian': 'uk',
        'Lithuanian': 'lt',
        'Finnish': 'fi',
        }

LINK = '[https://l10n.opensuse.org/engage/%(project)s/%(lang)s https://l10n.opensuse.org/widgets/%(project)s/%(lang)s/status-badge.png]'

PROJECTS = {
        'Infrastructure and Installation' : {
            'download-o-o' : 'Download Page',
            'landing-page' : 'Web Site',
            'searchpage' : 'Search Page',
            'software-o-o' : 'Software Page',
            'release-notes-openSUSE' : 'Release Notes',
            'skelcd-openSUSE' : 'License',
            'yast-slide-show' : 'Slide Show',
            },
        'Software' : {
            'libzypp' : 'libzypp',
            'zypper' : 'zypper',
            'snapper' : 'snapper',
            'libstorage' : 'libstorage',
            },
        'YaST (1)' : {
            'yast-base': 'base',
            'yast-country': 'country',
            'yast-firewall': 'firewall',
            'yast-installation': 'installation',
            'yast-ncurses': 'ncurses',
            'yast-ncurses-pkg': 'ncurses-pkg',
            'yast-network': 'network',
            'yast-pam': 'pam',
            'yast-pkg-bindings': 'pkg-bindings',
            'yast-qt': 'qt',
            'yast-qt-pkg': 'qt-pkg',
            'yast-timezone_db': 'timezone_db',
            'yast-storage': 'storage',
            },
        'YaST (2)' : {
            'yast-control-center': 'control-center',
            'yast-oneclickinstall': 'oneclickinstall',
            'yast-online-update': 'online-update',
            'yast-online-update-configuration': 'online-update-configuration',
            'yast-ldap': 'ldap',
            'yast-mail': 'mail',
            'yast-packager': 'packager',
            'yast-registration': 'registration',
            'yast-security': 'security',
            'yast-services-manager': 'services-manager',
            'yast-snapper': 'snapper',
            'yast-storage': 'storage',
            'yast-update': 'update',
            'yast-users': 'users',
            'yast-sysconfig': 'sysconfig',
            },
        }

class TranslationTool(cmdln.Cmdln):
    def __init__(self, *args, **kwargs):
        cmdln.Cmdln.__init__(self, args, kwargs)

    def get_optparser(self):
        parser = cmdln.CmdlnOptionParser(self)
        parser.add_option("--dry", action="store_true", help="dry run")
        parser.add_option("--debug", action="store_true", help="debug output")
        parser.add_option("--verbose", action="store_true", help="verbose")
        return parser

    def postoptparse(self):
        level = None
        if self.options.debug:
            level  = logging.DEBUG
        elif self.options.verbose:
            level = logging.INFO

        logging.basicConfig(level = level)

        self.logger = logging.getLogger(self.optparser.prog)

    @cmdln.option("-f", "--force", action="store_true",
                  help="force something")
    def do_table(self, subcmd, opts, *args):
        """${cmd_name}: create table with translation badges from Weblate

        ${cmd_usage}
        ${cmd_option_list}
        """

        for category in sorted(PROJECTS.keys()):
            print '== %s ==' % category
            print '{| class="wikitable"'
            print '|-'
            print '!- Language !!', ' !! '. join([PROJECTS[category][p] for p in sorted(PROJECTS[category].keys())])
            for lang in sorted(LANGS.keys()):
                print '|-'
                print '| %s ||'%lang, ' || '.join([LINK%{'project':p, 'lang':LANGS[lang]} for p in sorted(PROJECTS[category].keys())])
            print '|}'

if __name__ == "__main__":
    app = TranslationTool()
    sys.exit( app.main() )

# vim: sw=4 et
