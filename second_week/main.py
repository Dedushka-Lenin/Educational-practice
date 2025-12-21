import sys
import signal

import sqlite3
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from internal.adapter.config import config
from internal.api.routes import get_apps_router


CONFIG_PATH = "config/conf.toml"

class Server:
    def get_application(self) -> FastAPI:
        conf = config.Get(CONFIG_PATH)

        try:
            self.conn = sqlite3.connect(conf.database.db_path)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            signal.signal(signal.SIGINT, self.handle_sigint)

            application = FastAPI(
                title=conf.api.project_name,
                debug=conf.api.debug,
                version=conf.api.version
            )

            routes = get_apps_router(self.conn, self.cursor)
            application.include_router(routes)

            application.add_middleware(
                CORSMiddleware,
                allow_origins=conf.api.cors_allowed_origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
            

            return application
        except sqlite3.Error as e:
            print(f"Ошибка подключения: {e}")
            return None

    def handle_sigint(self, signum, frame):
        self.close()
        sys.exit(0)

    def close(self):
        if hasattr(self, "cursor") and self.cursor:
            self.cursor.close()
        if hasattr(self, "connection") and self.conn:
            self.conn.close()

server = Server()
app = server.get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)