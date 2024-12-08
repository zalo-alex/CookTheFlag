
# 🏴 Cook The Flag

Cook The Flag is a web-based CTF tool that lets you easily extend its functionality with Python-based plugins. It simplifies the use of various CTF tools and techniques, making it easier to tackle a wide range of challenges, from web exploitation to cryptography, and more. The project is designed to grow over time with new features and capabilities.
## 📃 Features

 - 🧮 Basic Encryption (Base64, Hex, ...)
 - 🔨 Tools (Requests, ...)
 - 🔍 RegEx search

## 🌠 In the future
 - [ ] ➕ More tools (NMap, RsaCtfTool, ...)
 - [ ] 🔧 More conversions (Rot13, ...)
 - [ ] 🌐 Remote access 
 - [ ] 🐳 Docker image
## 🚀 Installation
```bash
docker run -p 8080:8080 azalo/cooktheflag
```
<details>
<summary>Other methods (Latest updates)</summary>

### Using Dockerfile
```bash
git clone https://github.com/zalo-alex/CookTheFlag
cd CookTheFlag
sudo docker build -t cooktheflag .
sudo docker run -p 8080:8080 cooktheflag
```

### Using Python

```bash
git clone https://github.com/zalo-alex/CookTheFlag
cd CookTheFlag
pip install -r requirements.txt
python main.py
```
</details>

## 👤 Contributionsa
You can make your own modules and share them with a pull request
