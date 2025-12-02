# DevOps Hello – Flask alkalmazás

Egyszerű "Hello world" webalkalmazás Python + Flask használatával.  
Az alkalmazás HTTP-n elérhető, és a böngészőben az alábbi szöveget adja vissza:

> Hello DevOps from Péter!

## 1. Követelmények

- Python 3
- Internet kapcsolat (a Flask letöltéséhez első futtatáskor)

## 2. Alkalmazás futtatása

Az alábbi lépésekkel egy külső felhasználó is el tudja indítani az alkalmazást.

### 2.1. Függőségek telepítése

A projekt gyökerében (ahol az `app.py` és a `requirements.txt` található):

```bash
py -m pip install -r requirements.txt
