# Local lesson server

From the repository root, run:

```sh
python lessons/serve.py
```

The server listens on all LAN interfaces at port `8000`. On a phone connected
to the same network, open:

```text
http://<computer-LAN-IP>:8000/lessons/
```

Only `lessons/`, `assets/`, and `reference/` are exposed. Use `--port` to
choose another port, or `--host 127.0.0.1` to restrict access to the computer.
