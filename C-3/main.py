import webapp2

class MainPage(webapp2.RequestHandler):
      def get(self):
        i=0
        while(i<10):
         self.response.write("Name : Omkar Khade<br>")
         self.response.write("Seat No. : 33239<br>")
         self.response.write("Department : IT<br>")
         self.response.write('<br>')
         i=i+1
         
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
