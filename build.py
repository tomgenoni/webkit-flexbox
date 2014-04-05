import os
import shutil
from mako.template import Template
from mako.lookup import TemplateLookup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

entry_html = ""

def get_sub_dirs(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

subdirs = get_sub_dirs("content")

for dir in subdirs:

    # Read files to get data.
    ex_note = open('content/'+dir+'/note.txt').read()
    ex_css_2012 = open('content/'+dir+'/_code_2012.scss').read()
    ex_html = open('content/'+dir+'/code.html').read()

    # HTML preformatter.
    lexer = get_lexer_by_name("html", stripall=True)
    formatter = HtmlFormatter(cssclass="source")
    ex_html_pre = highlight(ex_html, lexer, formatter)

    # HTML preformatter.
    lexer = get_lexer_by_name("scss", stripall=True)
    formatter = HtmlFormatter(cssclass="source")
    ex_css_2012 = highlight(ex_css_2012, lexer, formatter)

    # Use the template to dump the data.
    entry_tmpl = Template(filename='templates/entry.mako')
    entry_html += entry_tmpl.render(template_note=ex_note, template_css_2012=ex_css_2012, template_html=ex_html, template_html_pre=ex_html_pre)


build_file = open('index.html', 'w+')

layout_tmpl = Template(filename='templates/layout.mako')

build_file.write(layout_tmpl.render(template_entry_html=entry_html))