import http.server
import socketserver
import pyautogui
import io
import threading

class ScreenShot(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "multipart/x-mixed-replace; boundary=frame")
        self.end_headers()

        while True:

            scrnsht = pyautogui.screenshot()

            BinImg = io.BytesIO()
            scrnsht.save(BinImg, format='PNG')
            BinImg.seek(0)

            self.wfile.write(b"--frame\r\n")
            self.send_header("Content-type", "image/png")
            self.send_header("Content-length", len(BinImg.getvalue()))
            self.end_headers()

            self.wfile.write(BinImg.getvalue())
            self.wfile.write(b"\r\n")

HOST = '0.0.0.0'
PORT = 8000

with socketserver.TCPServer((HOST, PORT), ScreenShot) as httpServer:
    print(f"Start HTTP server on {HOST}:{PORT}")

    screenshot_thread = threading.Thread(target=httpServer.serve_forever, daemon=True)
    screenshot_thread.start()
    screenshot_thread.join()
