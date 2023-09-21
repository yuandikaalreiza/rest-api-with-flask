from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "my store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}