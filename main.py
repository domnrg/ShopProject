from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки GET-запросов """
        routes = {
            "/": "main.html",
            "/catalog": "Catalog.html",
            "/category": "Category.html",
            "/contacts": "Contacts.html",
        }
        file_name = routes.get(self.path)

        if file_name and os.path.exists(file_name):
            # Отправляем страницу
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open(file_name, "r", encoding="utf-8") as f:
                self.wfile.write(bytes(f.read(), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Страница не найдена</h1>", "utf-8"))
            return

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен: http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
