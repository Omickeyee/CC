import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
     
        self.response.write("<h1> Table Of 10 : </h1>")
        self.response.write("<ul>")
        for i in range(1,11):
          result=i*10
          self.response.write("<li>10 x" +str(i) +"=" +str(result) +"</li>")
        self.response.write("</ul>")
         
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
