import os
from bottle import Bottle, default_app, run, hook, response

app = Bottle()

with app:
    assert app is default_app()

    # Capture routes defined in other modules
    import index

    # After first push to heroku, set environment variable with:
    # heroku config:set APP_LOCATION=heroku
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=int(os.environ.get('PORT', 8000)), debug=True)