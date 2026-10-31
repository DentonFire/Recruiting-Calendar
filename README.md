# Ready to Serve: Recruiting Content Calendar (site)

Single-file static site (`index.html`) mirroring the Frontline Report CRR calendar at https://dentonfire.github.io/Calendar/, built from CRRO Manual Section 6.4.

## Deploy to GitHub Pages (same pattern as the Calendar repo)
1. Create a new repo under the `dentonfire` GitHub org, e.g. `Recruiting-Calendar` (or `Ready-to-Serve`).
2. Upload `index.html` to the repo root and commit to `main`.
3. Repo Settings > Pages > Source: Deploy from a branch > `main` / `/ (root)` > Save.
4. Site publishes at `https://dentonfire.github.io/Recruiting-Calendar/` within a minute or two.

## Two things to update before publishing
- **Key Dates strip** (top of page): registration month, exam date, PAT/background window, academy start. Currently shows the Oct 2026 / Jan 2027 cycle with "confirm exact date" notes.
- **LINKS block** (bottom of page, in the `<script>`): NEOGOV and the Careers page are set to real City of Denton URLs. Ride-along request, PAT prep guide, and newsletter signup currently fall back to the Careers page. Replace those three with the real destinations and every reference on the page updates.

## What's on the page
- Hero, dynamic "THIS MONTH" banner, sticky controls (show/hide post copy, jump to month)
- Intro, Current Cycle Key Dates, Publishing Schedule, Platform Guidelines
- Year at a Glance grid (current month auto-highlighted)
- 12 month sections: Why This Month, 4 weekly cards, Facebook/LinkedIn/X copy with Copy buttons and X character counts, Copy Month button, Recruiting Tool Connection
- Flex Month Topic Bank, Implementation Notes, Recruiting Tools Reference (6 cards incl. cross-link to the Frontline Report), footer

## Edition Archive
The `ARCHIVE` list at the bottom of `content.py` drives the "Ready to Serve Edition Archive" section. Add each new edition (date, title, conta.cc link, status, one-paragraph takeaway) when it goes out, then rebuild. August 2026 uses the flex slot for the Ready to Serve reveal and catch-up; the original flex posts live on as the "Standing August set" under the Flex Month Topic Bank (`FLEX_STANDING` in `content.py`).

## Rebuilding
`content.py` holds all copy; `build.py` generates `index.html`. Edit content, run `python3 build.py`.
