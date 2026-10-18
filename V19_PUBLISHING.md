# Version 19 — publishing and links

The homepage portrait and title now share a row; the upper painting conveyor is directly beneath both.

Wikipedia link remediation: uncertain and previously hard-coded search links now lead to Wikipedia searches instead of potentially missing specific biographies. See WIKIPEDIA_LINK_REVIEW.csv. This **does not certify** the existence of the remaining article URLs; a live HTTP verification against Wikipedia is still needed.

## Publish with GitHub Pages

The website contents (index.html, chapters/, assets/, etc.) need to be at repository root, not nested inside `v15 2`.

1. Push all these files into the existing `nikolairura1/baudillare` repository on its `main` branch. Because this edition is about 193 MB, upload using a Git client rather than a browser file-by-file upload.
2. In GitHub repository Settings → Pages, select **GitHub Actions** as the build and deployment source.
3. The bundled `.github/workflows/deploy.yml` will deploy the static site on each push.
4. Wait until the deployment workflow completes and verify images, chapter links and gallery search.
5. Once deployment completes, the expected URL is `https://nikolairura1.github.io/baudillare/` (not confirmed live at packaging time).

GitHub's 100 MB limit applies per file. Individual oversized assets must be optimized or hosted elsewhere if the push is rejected. The website remains a static HTML site and needs no server-side application.
