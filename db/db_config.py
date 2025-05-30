TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:admin@localhost:5432/arthmonitor"
    },
    "apps": {
        "models": {
            "models": ["arthmonitor.db.models"],
            "default_connection": "default",
        }
    }
}
