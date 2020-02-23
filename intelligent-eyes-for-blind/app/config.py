def configure_app(app):

    # MySQL
    app.config["MYSQL_DATABASE_HOST"] = "localhost"
    app.config["MYSQL_CORE_DATABASE"] = "blind_eyes"
    app.config["MYSQL_DATABASE_USER"] = "root"
    app.config["MYSQL_DATABASE_PASSWORD"] = "Thor@12345"
