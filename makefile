run:
	uvicorn app.main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

css:
	tailwindcss -i styles/main.css -o static/css/main.css --watch

css-minify:
	tailwindcss -i styles/main.css -o static/css/main.css --minify

# hot-reload: https://verdantfox.com/blog/how-to-hot-reload-fastapi-and-flask-apps-on-html-css-and-javascript-changes
hot-reload:
	browser-sync 'http://localhost:8000' 'static' --watch --files .