# ergasies-python

## Previewing the website locally

Use the helper script to spin up a local HTTP server and open the site in your browser:

```bash
cd website
./preview.sh
```

The script defaults to port 8000. You can pass a custom port if needed:

```bash
./preview.sh 8080
```

Then visit `http://localhost:8000` (or your chosen port) in your browser to test the latest changes.

## Manual alternative

If you prefer to run the server manually, you can execute:

```bash
cd website
python3 -m http.server 8000
```

This serves the static assets so you can preview them locally.
