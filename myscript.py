export DATASETTE_BASE=$(python -c 'import os; print(os.path.dirname(__import__("datasette").__file__))') \
pyinstaller -F \
    --add-data "$DATASETTE_BASE/templates:datasette/templates" \
    --add-data "$DATASETTE_BASE/static:datasette/static" \
    --hidden-import datasette.publish \
    --hidden-import datasette.publish.heroku \
    --hidden-import datasette.publish.cloudrun \
    --hidden-import datasette.facets \
    --hidden-import datasette.sql_functions \
    --hidden-import datasette.actor_auth_cookie \
    --hidden-import datasette.default_permissions \
    --hidden-import datasette.default_magic_parameters \
    --hidden-import datasette.blob_renderer \
    --hidden-import datasette.default_menu_links \
    --hidden-import uvicorn \
    --hidden-import uvicorn.logging \
    --hidden-import uvicorn.loops \
    --hidden-import uvicorn.loops.auto \
    --hidden-import uvicorn.protocols \
    --hidden-import uvicorn.protocols.http \
    --hidden-import uvicorn.protocols.http.auto \
    --hidden-import uvicorn.protocols.websockets \
    --hidden-import uvicorn.protocols.websockets.auto \
    --hidden-import uvicorn.lifespan \
    --hidden-import uvicorn.lifespan.on \
    $(which datasette)