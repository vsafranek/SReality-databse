from http.server import BaseHTTPRequestHandler, HTTPServer

import webbrowser
import http.server
import create_html
from server import Server
from save_data import update_database

hostName = "localhost"
serverPort = 8080
class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        create_html.run()
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webbrowser.open("http://127.0.0.1:8080", new=0, autoraise=True)
    update_database()
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


