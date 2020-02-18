from app.manage import create_app

__all__ = ["app"]

app = create_app()

from app.apis import *
