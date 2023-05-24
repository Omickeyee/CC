import webapp2
   
class MainPage(webapp2.RequestHandler):
      def get(self):
        for i in range (5):
           self.response.write("Name: Omkar Khade<br>")
           self.response.write("Seat No.: 33239<br>")
           self.response.write("Department: IT<br>")
           self.response.write('<br>')
           
app= webapp2.WSGIApplication([('/',MainPage)],debug=True)
