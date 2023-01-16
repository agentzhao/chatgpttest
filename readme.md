# chatgptapi

- Using [mmabrouk/chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper)
- [Flask](https://github.com/pallets/flask)

Optional

```
python3 -m venv chatgptapi
source chatgptapi/bin/activate
```

Install dependencies

```
pip3 install -r requirements.txt
```

```
pip3 install flask
pip3 install git+https://github.com/mmabrouk/chatgpt-wrapper
playwright install firefox
chatgpt install
```

Testing api

```
curl --location --request POST 'http://localhost:5000/chat' \
--header 'Content-Type: application/json' \
--data-raw '{"message":"Hello, world!"}'

```

should return a response like so

```
{
    "response":"Hello, world!"
}
```

- pipreqs (generate requirements.txt file)
