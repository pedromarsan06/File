from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def homepage():
	dic = {
"lang":"python-termux", "page":"homepage", "lib":"FastAPI"
}
	return dic

