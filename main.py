
# Main Application file

import os

import webapp2
import jinja2


from google.appengine.api import memcache

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               variable_start_string='((',
                               variable_end_string='))',
                               autoescape = True)


class Handler(webapp2.RequestHandler):
  def initialize(self, *a, **kw):
    super(Handler, self).initialize(*a, **kw)

  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))


class MainHandler(Handler):
  def get(self):
    self.render('master.tmpl.html')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)

# dev_appserver.py --port 8888 .
# appcfg.py update .
# http://kubicki-jack.appspot.com/
# import pdb; pdb.set_trace()
