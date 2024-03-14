import http.server
import socketserver

class ScreenShot(http.server.BaseHTTPRequestHandler):
    def GetReq(self):

        self.send_response(200)
        self.send_header("Content-type", "multipart/x-mixed-replace; boundary=frame")
        self.end_headers()

        while True:

            scrnsht = pyautogui.screenshot()

            BinImg = io.BytesIO()
            scrnsht.save(BinImg, format='PNG')
            BinImg.seek(0)

            

HOST = '0.0.0.0'
PORT = 8000

with socketserver.TCPServer((HOST, PORT), ScreenShot) as httpServer:
    print(f"Start HTTP server on {HOST}:{PORT}")

