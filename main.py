from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки GET-запросов """
        try:
            with open("Contacts.html", "r", encoding="utf-8") as f:
                html_content = f.read()
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Страница не найдена</h1>", "utf-8"))
            return

        # Отправляем страницу
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен: http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
