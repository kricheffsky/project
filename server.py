import tornado.ioloop
import tornado.web
import sqlite3
# import b64encode
import os

admin_password = 123456  # Реальный пароль администратора коммитить на ГитХаб НИЗЯ!
port = 8888
db_path = "./datalogin.db"
pages = {
    "user_page": "./html/Mainpage.html",
    "admin_page": "./html/Mainpage1.html"
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(pages["user_page"])
    def post(self):
        password = self.get_argument("password", None)
        if not password == admin_password:
            self.render(pages["admin_page"], message="Неверный пароль")
        else:
            # session_key = b64encode(os.urandom(69)).decode("utf-8")
            self.set_cookie(auth, password)
            cur.execute("INSERT INTO sessions VALUES (?, ?, 1)", (password, session_key))

def init_db(db_path):
    db = sqlite3.connect(db_path)  # Подключаем базу данных sqlite3
    cur = db.cursor()  # Создаем курсор для работы с SQL
    cur.execute("SELECT * FROM sqlite_master")  # Получаем список таблиц
    if len(cur.fetchall()) == 0:  # Если таблиц 0, значит, база данных новая, пустая
        cur.execute("CREATE TABLE sessions (password VARCHAR, session_key VARCHAR UNIQUE, alive BOOLEAN)")  # и для сессий
    return db, cur  # База данных готова, возвращаем обратно инструменты для работы с ней

def make_app():
    return tornado.web.Application([
         (r"/", MainHandler),
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)

if __name__ == "__main__":
   db, cur = init_db(db_path)
   app = make_app()
   app.listen(port)
   tornado.ioloop.IOLoop.current().start() 










