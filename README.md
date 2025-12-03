# DevOps Hello – Flask alkalmazás

Egyszerű "Hello world" webalkalmazás Python + Flask használatával.  
Az alkalmazás HTTP-n elérhető, és a böngészőben az alábbi szöveget adja vissza:

> Hello DevOps from Péter!

A projekt célja, hogy ezen a nagyon egyszerű alkalmazáson keresztül bemutassa az alap DevOps lépéseket:
- kódkészítés (Python)
- buildelés
- verziókövetés (Git, trunk-based development)
- konténerizálás (Docker)
- később: CI pipeline (GitHub Actions + container registry)

---

## 1. Követelmények

- Python 3
- Internetkapcsolat (a Flask letöltéséhez első futtatáskor)
- Opcionálisan: Docker (ha helyben is szeretnénk futtatni konténerben)

---

## 2. Alkalmazás futtatása helyben

Az alábbi lépések segítségével egy külső felhasználó is el tudja indítani az alkalmazást.

A parancsokat mindig abban a könyvtárban kell futtatni, ahol az `app.py` és a `requirements.txt` található.

### 2.1. Függőségek telepítése

```bash
py -m pip install -r requirements.txt 

``` 

### 2.2. Alkalmazás indítása

Az alkalmazást az alábbi parancs indítja el a projekt könyvtárában:

```bash
py app.py 

```


---

## 3. Docker használata

Az alkalmazás Docker konténerben is futtatható.  
Ehhez a projekt gyökerében található `Dockerfile` használható.

> Megjegyzés: a Docker parancsok olyan környezetben futtathatók, ahol a Docker telepítve van  
> (pl. fejlesztői gépen vagy CI környezetben, mint a GitHub Actions futtatókörnyezete).

---

### 3.1. Előfeltétel
Telepített Docker (pl. Docker Desktop Windowsra), vagy olyan CI környezet, ahol Docker már elérhető (pl. GitHub Actions futtatókörnyezet).

---

### 3.2. Docker image buildelése

```bash
docker build -t devops-hello:v1 .

```

Ez a parancs elkészít egy devops-hello:v1 nevű Docker image-et a projekt forráskódjából.

---

### 3.3. Konténer futtatása

```bash
docker run -p 8080:8080 devops-hello:v1

```

A konténer elindul, és az alkalmazás HTTP-n elérhető lesz:

http://127.0.0.1:8080 vagy http://localhost:8080


---

