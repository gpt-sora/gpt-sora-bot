from playwright.sync_api import sync_playwright
import os

def run():
    # Legge email e password da variabili ambientali
    email = os.environ["SORA_EMAIL"]
    password = os.environ["SORA_PASSWORD"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://sora.com")

        # (E qui potrai fare il login con email/password se vuoi automatizzare il login)
        # Esempio: page.fill("input[name='email']", email)

        page.screenshot(path="sora_screenshot.png")
        print("✅ Screenshot salvato come sora_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
