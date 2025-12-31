# Selenium Practice Showcase 

This repository is a small but production-style Selenium UI automation framework built for interview demonstration.
Target web page: Rahul Shetty Academy Automation Practice Page.

## What this project demonstrates
- Component-based Page Object Model (POM)
- Explicit waits and stability strategies (no `sleep`, no WebElement caching)
- Handling:
  - Radio buttons / Checkboxes / Dropdown
  - Autocomplete (jQuery UI)
  - Alerts (accept/dismiss)
  - Show/Hide (visibility changes)
  - Hover menu
  - Switch window / switch tab
  - Web table calculation validation (sum vs displayed total)
- Test selection with markers (`smoke`, `regression`)
- Failure artifacts: screenshot + HTML page source
- Allure reporting for clear test result evidence

## Architecture
- `src/pages/`: page containers that aggregate components
- `src/components/`: reusable UI components (each owns locators + atomic actions)
- `src/core/`: framework utilities (driver factory, waits, base page, window manager, artifacts)
- `tests/`: test cases (BDD-ish style: intent-focused)
- `conftest.py`: pytest fixtures + failure hooks

## Stability strategies (why this is reliable)
- **No WebElement caching**: elements are re-located per action to reduce stale element failures
- **Centralized explicit waits**: visibility/clickability/presence checks are wrapped in `Waits`
- **Small retry on stale**: base actions retry once for SPA-like re-render

## CI Smoke Test Status
![UI Smoke Tests](https://github.com/lookcake/selenium-practice-showcase/actions/workflows/smoke.yml/badge.svg)


## How to run (local)
### 1) Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest -m smoke
pytest -m regression



