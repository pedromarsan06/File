from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class user(BaseModel):
	nome: str
	idade: int
@app.get('/')
def homepage():
	dic = {
"lang":"python-termux", "page":"homepage", "lib":"FastAPI"
}
	return dic
@app.post('/user/')
def creat(User:user):
	return {"mensagem":f"user = {User.nome}, years = {User.idade}"}

