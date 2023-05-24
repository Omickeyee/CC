import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
       self.response.write("<h1>Fabonacci Series</h1>")
       self.response.write("<ul>")
       a, b= 0, 1
       for i in range (1,9):
            self.response.write("<li>"+str(a)+"</li>")
            a, b= b, a+b
       self.response.write("</ul>")
       
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
           
