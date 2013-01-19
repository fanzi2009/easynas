#---------------------------------------------------#
#             #
# copy from woodlog at www.djangocn.org by limodou #
#             #
#---------------------------------------------------#

import re
import cgi

re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>\b((http|ftp)://.*?))(\s|$)', re.S|re.M|re.I )

def text2html(text):
 def do_sub(m):
  c = m.groupdict()
  if c['htmlchars']:
   return cgi.escape(c['htmlchars'])
  if c['lineend']:
   return '<br>'
  elif c['space']:
   t = m.group().replace('\t', '&nbsp;'*4)
   t = t.replace(' ', '&nbsp;')
   return t
  elif c['space'] == '\t':
   return ' '*4;
  else:
   last = m.groups()[-1]
   if last in ['\n', '\r', '\r\n']: 
    last = '<br>'
   return '<a href="%s">%s</a>%s' % (c['protocal'], c['protocal'], last)
 return re.sub(re_string, do_sub, text)
