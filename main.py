import asyncio
from app import app

if __name__ == "__main__":
   app.bootstrap()
   # run the app within asyncio
   asyncio.run(app.run())
