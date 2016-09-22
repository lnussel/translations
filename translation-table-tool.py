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

LANGS = {
        'ar': 'Arabic',
        'pt_BR': 'Brazilian Portuguese',
        'zh_CN': 'Chinese Simplified',
        'zh_TW': 'Chinese Traditional',
        'cs': 'Czech',
        'nl': 'Dutch',
        'fr': 'French',
        'de': 'German',
        'hu': 'Hungarian',
        'it': 'Italian',
        'ja': 'Japanese',
        'ko': 'Korean',
        'pl': 'Polish',
        'ru': 'Russian',
        'es': 'Spanish',
        'sv': 'Swedish',
        }

LINK = '[https://l10n.opensuse.org/engage/%(project)s/%(lang)s https://l10n.opensuse.org/widgets/%(project)s/%(lang)s/status-badge.png]'

PROJECTS = {
        'download-o-o' : 'Download Page',
        'landing-page' : 'Web Site',
        'searchpage' : 'Search Page',
        'libzypp' : 'libzypp',
        'release-notes-openSUSE' : 'Release Notes',
        'skelcd-openSUSE' : 'License',
        'yast-slide-show' : 'Slide Show',
        'zypper' : 'zypper',
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

        print '{| class="wikitable"'
        print '|-'
        print '!- Language !!', ' !! '. join([PROJECTS[p] for p in sorted(PROJECTS.keys())])
        for lang in sorted(LANGS.keys()):
            print '|-'
            print '| %s ||'%LANGS[lang], ' || '.join([LINK%{'project':p, 'lang':lang} for p in sorted(PROJECTS.keys())])
        print '|}'

if __name__ == "__main__":
    app = TranslationTool()
    sys.exit( app.main() )

# vim: sw=4 et
