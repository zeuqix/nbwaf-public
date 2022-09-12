from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import nbwaf
import os
import subprocess

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        alw, status, perm, lastpath, ext = nbwaf.check(self.path, "conf.json")
        print("Path = " + self.path + " , İzin = " + str(alw) , ", Dosya Durumu = " + str(status) , ", Yetki = " + str(perm), ", LastPath = " + lastpath)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
