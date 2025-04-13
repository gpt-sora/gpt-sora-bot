from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://sora.com")
        page.screenshot(path="sora_screenshot.png")
        print("Screenshot salvato come sora_screenshot.png")
        browser.close()

if __name__ == "__main__":
    run()
