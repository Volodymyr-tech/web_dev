from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("main_page.html", mode="r", encoding="utf-8") as file:
            data = file.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        # Получение длины данных из заголовка запроса
        content_length = int(self.headers['Content-Length'])
        # Чтение данных из тела запроса
        post_data = self.rfile.read(content_length)
        # Печать данных в консоль
        print("Received POST data:", post_data.decode("utf-8"))

        # Отправка ответа на POST-запрос
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Data received", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
