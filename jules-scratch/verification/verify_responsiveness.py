from playwright.sync_api import sync_playwright, expect
import os

def run(playwright):
    # Définir les tailles de vue pour le test
    desktop_viewport = {'width': 1920, 'height': 1080}
    mobile_viewport = {'width': 375, 'height': 667} # iPhone SE

    # Lancer le navigateur
    browser = playwright.chromium.launch(headless=True)

    # Chemin vers le fichier local
    base_path = "file://" + os.path.abspath("public")
    home_url = f"{base_path}/index.html"

    # --- Test sur Desktop ---
    context_desktop = browser.new_context(viewport=desktop_viewport)
    page_desktop = context_desktop.new_page()
    page_desktop.goto(home_url)
    expect(page_desktop.get_by_role("heading", name="Stéphan Uniatowitz")).to_be_visible()
    page_desktop.screenshot(path="jules-scratch/verification/responsive_desktop.png")
    context_desktop.close()

    # --- Test sur Mobile ---
    context_mobile = browser.new_context(viewport=mobile_viewport)
    page_mobile = context_mobile.new_page()
    page_mobile.goto(home_url)
    expect(page_mobile.get_by_role("heading", name="Stéphan Uniatowitz")).to_be_visible()
    page_mobile.screenshot(path="jules-scratch/verification/responsive_mobile.png")
    context_mobile.close()

    browser.close()

with sync_playwright() as playwright:
    run(playwright)