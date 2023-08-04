<h1 align="center">
    Autoreport
  <br>
</h1>

<h4 align="center">autoreport generates bug report templates for security researchers</h4>


<p align="center">
  <a href="#usage">⛏️ Usage</a>
  &nbsp;&nbsp;&nbsp;
  <a href="#finding-your-token">🔍 Finding your token</a>
  &nbsp;&nbsp;&nbsp;
  <a href="#acknowledgements">🙏 Acknowledgements</a>
  <br>
</p>


## Usage

Run the script with the following command:

```bash
python autoreport.py -gt "XSS on query endpoint"
```


## Finding your token

Log into [Poe](https://poe.com) on any desktop web browser, then open your browser's developer tools (also known as "inspect") and look for the value of the p-b cookie in the following menus:

- Chromium: Devtools > Application > Cookies > poe.com
- Firefox: Devtools > Storage > Cookies
- Safari: Devtools > Storage > Cookies

Paste the cookie value in `config.ini`:

```
[DEFAULT]
API_KEY = COOKIE_HERE
```


## Acknowledgements

This project utilizes the [poe-api](https://github.com/ading2210/poe-api) for interacting with the Poe Bot. Poe-API is a reverse engineered API wrapper for Quora's Poe, which allows you free access to OpenAI's ChatGPT and GPT-4, as well as Anthropic's Claude.
