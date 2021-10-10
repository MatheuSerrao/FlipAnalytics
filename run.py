from app import app
from routes.means_router import means_router
from routes.volatility_router import volatility_router

routes = [
    means_router,
    volatility_router
]

for router in routes:
    router.apply()

app.run(host='0.0.0.0', port=7000, debug=True)
