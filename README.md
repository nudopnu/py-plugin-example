# Python Plugin Example 🔌

A sample setup for dynamically importing scripts in a plugin architecture from a compiled exe (from pyinstaller)

## Setup

```bash
pip install -r requirements.txt
pyinstaller main.py
cp -r plugins dist/main/plugins
cd dist/main
./main.exe
```
