from http.server import BaseHTTPRequestHandler
import os
import create_html

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        create_html.run()
        self.path = 'index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]

            if request_extension != ".py":
                f = open(self.path).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)