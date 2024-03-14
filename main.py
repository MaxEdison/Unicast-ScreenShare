import http.server
import socketserver

class ScreenShot(http.server.BaseHTTPRequestHandler):
    def GetReq(self):
        pass



HOST = '0.0.0.0'
PORT = 8000

with socketserver.TCPServer((HOST, PORT), ScreenShot) as httpServer:
    print(f"Start HTTP server on {HOST}:{PORT}")

