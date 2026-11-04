# QA Automation Framework with Python

Automated UI tests for [SauceDemo](https://www.saucedemo.com/)
built with Python, Selenium and pytest, following the Page Object Model (POM).

## Tech Stack

- Python
- Selenium
- pytest

## Project Structure

```
qa-automation-python/
├── pages/            # Page Objects: locators and actions for each page
├── tests/            # Test cases
├── conftest.py       # Shared pytest fixtures (WebDriver setup and teardown)
├── requirements.txt  # Project dependencies
└── README.md
```

## How to Run

**Prerequisites:** Python 3.x and Google Chrome installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/osojulian/qa-automation-python.git
   cd qa-automation-python
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv

   # Windows (Git Bash)
   source .venv/Scripts/activate

   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tests:
   ```bash
   pytest -v
   ```

## Roadmap

- [x] Project setup with pytest fixtures
- [x] Smoke test for the login page
- [ ] Page Object Model for login, inventory, cart and checkout
- [ ] UI tests: login, add to cart and checkout flows
- [ ] API tests with `requests` against [Restful-Booker](https://restful-booker.herokuapp.com/)
- [ ] UI tests with Playwright
- [ ] HTML test reports
- [ ] CI pipeline with GitHub Actions
- [ ] Linting with Ruff