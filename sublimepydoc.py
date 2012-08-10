import re
import webbrowser

import sublime_plugin


class OpenPythonModuleUnderCursorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        module = self.view.substr(self.view.word(self.view.sel()[0].begin()))
        webbrowser.open_new(module_to_url[module])

    def is_enabled(self):
        return '.python ' in self.view.scope_name(self.view.sel()[0].begin())


class OpenPythonModuleCommand(sublime_plugin.TextCommand):
    '''Opens one of the modules in the modules dict below.'''
    def run(self, edit):
        def x(result):
            if result != -1:
                webbrowser.open_new(module_to_url[modules[result]])

        self.view.window().show_quick_panel(modules, x)


def printstdlib():
    import urllib2
    response = urllib2.urlopen('http://docs.python.org/py-modindex.html')
    html = response.read()
    print list(re.findall('href="library/(.*).html#', html))

stdlib = ['__builtin__', '__future__', '__main__', '_winreg', 'abc', 'aepack', 'aetools', 'aetypes', 'aifc', 'al', 'al', 'anydbm', 'undoc', 'argparse', 'array', 'ast', 'asynchat', 'asyncore', 'atexit', 'audioop', 'autogil', 'base64', 'basehttpserver', 'bastion', 'bdb', 'binascii', 'binhex', 'bisect', 'bsddb', 'undoc', 'bz2', 'calendar', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'carbon', 'cd', 'undoc', 'cgi', 'cgihttpserver', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorpicker', 'colorsys', 'commands', 'compileall', 'compiler', 'compiler', 'compiler', 'configparser', 'contextlib', 'cookie', 'cookielib', 'copy', 'copy_reg', 'pickle', 'profile', 'crypt', 'stringio', 'csv', 'ctypes', 'curses', 'curses.ascii', 'curses.panel', 'curses', 'datetime', 'dbhash', 'dbm', 'decimal', 'gl', 'difflib', 'dircache', 'dis', 'distutils', 'dl', 'doctest', 'docxmlrpcserver', 'dumbdbm', 'dummy_thread', 'dummy_threading', 'easydialogs', 'email', 'email.charset', 'email.encoders', 'email.errors', 'email.generator', 'email.header', 'email.iterators', 'email.message', 'email.mime', 'email.parser', 'email.util', 'codecs', 'codecs', 'errno', 'exceptions', 'fcntl', 'filecmp', 'fileinput', 'macostools', 'fl', 'fl', 'fl', 'fm', 'fnmatch', 'formatter', 'fpectl', 'fpformat', 'fractions', 'framework', 'ftplib', 'functools', 'future_builtins', 'gc', 'gdbm', 'gensuitemodule', 'getopt', 'getpass', 'gettext', 'gl', 'gl', 'glob', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'hotshot', 'hotshot', 'htmllib', 'htmllib', 'htmlparser', 'httplib', 'ic', 'undoc', 'imageop', 'imaplib', 'imgfile', 'imghdr', 'imp', 'importlib', 'imputil', 'inspect', 'io', 'itertools', 'jpeg', 'json', 'keyword', '2to3', 'linecache', 'locale', 'logging', 'logging.config', 'logging.handlers', 'undoc', 'macos', 'macostools', 'macpath', 'undoc', 'mailbox', 'mailcap', 'marshal', 'math', 'md5', 'mhlib', 'mimetools', 'mimetypes', 'mimewriter', 'mimify', 'miniaeframe', 'mmap', 'modulefinder', 'msilib', 'msvcrt', 'multifile', 'multiprocessing', 'multiprocessing', 'multiprocessing', 'multiprocessing', 'multiprocessing', 'multiprocessing', 'mutex', 'undoc', 'netrc', 'new', 'nis', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'os.path', 'ossaudiodev', 'parser', 'pdb', 'pickle', 'pickletools', 'pipes', 'undoc', 'pkgutil', 'platform', 'plistlib', 'popen2', 'poplib', 'posix', 'posixfile', 'pprint', 'profile', 'profile', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 're', 'readline', 'repr', 'resource', 'rexec', 'rfc822', 'rlcompleter', 'robotparser', 'runpy', 'sched', 'scrolledtext', 'select', 'sets', 'sgmllib', 'sha', 'shelve', 'shlex', 'shutil', 'signal', 'simplehttpserver', 'simplexmlrpcserver', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3', 'ssl', 'stat', 'statvfs', 'string', 'stringio', 'stringprep', 'struct', 'subprocess', 'sunau', 'sunaudio', 'sunaudio', 'symbol', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'termios', 'test', 'test', 'textwrap', 'thread', 'threading', 'time', 'timeit', 'tix', 'tkinter', 'token', 'tokenize', 'trace', 'traceback', 'ttk', 'tty', 'turtle', 'types', 'unicodedata', 'unittest', 'urllib', 'urllib2', 'urlparse', 'user', 'userdict', 'userdict', 'userdict', 'uu', 'uuid', 'undoc', 'undoc', 'warnings', 'wave', 'weakref', 'webbrowser', 'whichdb', 'winsound', 'wsgiref', 'wsgiref', 'wsgiref', 'wsgiref', 'wsgiref', 'wsgiref', 'xdrlib', 'xml.dom', 'xml.dom.minidom', 'xml.dom.pulldom', 'xml.etree.elementtree', 'pyexpat', 'xml.sax', 'xml.sax.handler', 'xml.sax.utils', 'xml.sax.reader', 'xmlrpclib', 'zipfile', 'zipimport', 'zlib']

module_to_url = {}
for module in stdlib:
    module_to_url[module] = 'http://docs.python.org/library/%s.html' % module

module_to_url['sublime'] = 'http://www.sublimetext.com/docs/2/api_reference.html'
module_to_url['sublime_plugin'] = 'http://www.sublimetext.com/docs/2/api_reference.html'

modules = module_to_url.keys()
