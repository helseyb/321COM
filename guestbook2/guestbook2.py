from google.appengine.api import users
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT  = jinja.Enviroment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(_file_),'templates')),
    Extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current-User()
        logout_url = users.create_logout-url(self.request.path)
        if user:
            template= JINJA_ENVIRONMENT.get_template('welcome.html')
template_values= {
    
    'user':user.nickname(),
    'url_logout':logout_url,
    'url_logout_text' :'Log out',   
    }

self.response.write(template.render(template_vlaues))
else:
    self.redirect(users.create_login_url(self.request.uri))
    
def post(self):
    users = user.get_current_user()
    logout_url = user.create_logout_url(self.request.path)
    if user:
        template - JINJA ENVIROMENT.get_template('guest.html')
        templates_values = {
            'user': user.nickname(),
            'url_logout': logout_url,
            'url_logout_text' : 'Log out'
            'greetings' : self.request.get(content'))
                                           }
                                           
self.response.write(template.render(template_vaules)
                    
    else:
    self.redirect(users.create_login_url(self.request.url)
                  
application = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/sign' , MainPage),
     ], debug=True)
                  
                  
                  
                    
    
                                            