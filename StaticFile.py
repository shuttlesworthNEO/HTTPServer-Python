from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == "/":
			self.path = "/index_StaticFile.html"

		try:

			sendReply = False

			if self.path.endswith(".html"):
				mimtype = 'text/html'
				sendReply = True

			if self.path.endswith(".jpg"):
				mimtype = 'image/jpg'
				sendReply = True

			if self.path.endswith(".js"):
				mimtype = 'application/javascript'
				sendReply = True

			if self.path.endswith(".gif"):
				mimtype = 'image/gif'
				sendReply = True

			if self.path.endswith(".css"):
				mimtype = 'text/css'
				sendReply = True

			if sendReply == True:
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type', mimtype)
				self.end_headers()

				self.wfile.write(f.read())
				f.close()
			return

		except IOError:
			self.send_error(404, 'File not found: %s' % self.path)

try:

		server = HTTPServer(('',PORT_NUMBER), myHandler)
		print('Started HTTPServer on port', PORT_NUMBER)

		server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()