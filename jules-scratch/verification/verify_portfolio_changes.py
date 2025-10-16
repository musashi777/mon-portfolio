from playwright.sync_api import sync_playwright, expect
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()

    base_path = "file://" + os.path.abspath("public")

    # Naviguer directement vers la page du projet GLPI car index.html n'est pas généré
    page.goto(f"{base_path}/projets/installation-serveur-glpi/index.html")

    # Vérifier la page de projet unifiée (GLPI)
    expect(page.get_by_role("heading", name="Projet : Installation et Configuration d'un Serveur GLPI")).to_be_visible()
    expect(page.get_by_role("heading", name="1. Contexte et Objectifs Business")).to_be_visible()
    expect(page.get_by_role("heading", name="2. Guide d'Installation Technique Détaillé")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/01_project_page_check.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)