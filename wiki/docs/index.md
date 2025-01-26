
# Cook The Flag

Cook The Flag is a web-based CTF tool that lets you easily extend its functionality with Python-based plugins. It simplifies the use of various CTF tools and techniques, making it easier to tackle a wide range of challenges, from web exploitation to cryptography, and more. The project is designed to grow over time with new features and capabilities.

## 📃 Features

 - 🧮 Basic Encryption (Base64, Hex, ...)
 - 🔨 Tools (Requests, NMap, ...)
 - 🔍 RegEx search
 - 🐳 Docker image

## 🌠 In the future
 - [ ] ➕ More tools (RsaCtfTool, ...)
 - [ ] 🔧 More conversions (Rot13, ...)
 - [ ] 🌐 Remote access 
## 🚀 Usage
```bash
curl -s https://raw.githubusercontent.com/zalo-alex/CookTheFlag/refs/heads/main/run.sh | bash
```
<details>
<summary>Other methods (Latest updates)</summary>

<h3>Using DockerHub</h3>

```bash
docker run --pull=always --volume ~/.cooktheflag:/data -p 8080:8080 azalo/cooktheflag
```

<h3>Using Dockerfile</h3>

```bash
git clone https://github.com/zalo-alex/CookTheFlag
cd CookTheFlag
sudo docker build -t cooktheflag .
sudo docker run --volume ~/.cooktheflag:/data -p 8080:8080 cooktheflag
```

<h3>Using Python</h3>

```bash
git clone https://github.com/zalo-alex/CookTheFlag
cd CookTheFlag
pip install -r requirements.txt
python app.py
```
</details>

## 👤 Contributions
You can make your own modules and share them with a pull request
