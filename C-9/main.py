import webapp2
import urllib2
import json
class MainPage(webapp2.RequestHandler):
    def get(self):
                self.response.write('<html><body>')
                self.response.write('<form action="/forecast" method="post">')
                self.response.write('University Name : <input type="text" name="uname"><br>')
                self.response.write('<input type="submit" value="Search">')
                self.response.write('</form></body></html>')
class ForecastHandler(webapp2.RequestHandler):
    def post(self):
            uname = self.request.get('uname')
            url = 'http://universities.hipolabs.com/search?name=' + uname

            response = urllib2.urlopen(url).read()
            data = json.loads(response)
            for ele in data:
                self.response.write('<html><body>')
                self.response.write('<p>' + str(ele['name']) + '</p>')
                self.response.write('</body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/forecast', ForecastHandler)
], debug=True)