from .core.application import Application

print("importing routes...")

app = Application()
get, post, put, delete = app.route()

