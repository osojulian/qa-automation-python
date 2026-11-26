# QA Automation Framework with Python

Automated tests built with Python and pytest:

- **UI tests** for [SauceDemo](https://www.saucedemo.com/) with Selenium, following the Page Object Model (POM).
- **API tests** for [Restful-Booker](https://restful-booker.herokuapp.com/) with `requests`, covering the full CRUD flow (create, read, update and delete bookings) with token authentication.

## Tech Stack

- Python
- pytest
- Selenium
- requests

## Project Structure

```
qa-automation-python/
├── api/                  # API clients: one class per resource (BookingApi)
├── pages/                # Page Objects: locators and actions for each page
├── tests/                # UI test cases
│   └── api/              # API test cases
│       └── conftest.py   # API fixtures (payload, credentials, token)
├── conftest.py           # Shared UI fixtures (WebDriver setup and teardown)
├── requirements.txt      # Project dependencies
└── README.md
```

## How to Run

**Prerequisites:** Python 3.x. Google Chrome is required for the UI tests.

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
   # All tests
   pytest -v

   # API tests only
   pytest tests/api -v

   # UI tests only
   pytest tests --ignore=tests/api -v
   ```

## Roadmap

- [x] Project setup with pytest fixtures
- [x] Smoke test for the login page
- [x] Page Object Model: login, inventory and cart pages
- [x] UI tests: login (positive and negative), add and remove from cart
- [x] UI tests: cart shows added products
- [x] Page Object Model: checkout pages
- [x] UI tests: full checkout flow (products and order confirmation)
- [x] BasePage with explicit waits (`WebDriverWait`)
- [x] UI tests: checkout negative cases (missing information)
- [x] API tests with `requests` against [Restful-Booker](https://restful-booker.herokuapp.com/): CRUD with token auth and fixtures
- [ ] UI tests with Playwright
- [ ] HTML test reports
- [ ] CI pipeline with GitHub Actions
- [ ] Linting with Ruff
