# Baudelaire Salons v16

Open `index.html`. Each Salon has a linked illustration gallery; each chapter also has a horizontally scrollable strip. Hover over artwork markers to see their canonical folder. The edit dialog shows read-only folder paths.

## Artworks

Add your image as `assets/artworks/<slot-id>/artwork.jpg` (or PNG, JPEG, WEBP, GIF). The exact folder is displayed on hover, and all mappings are in `ARTWORK_MANIFEST.csv`. Do not use the archived originals in `legacy-artwork-folders`; they are kept to prevent data loss. After adding new illustrations, run `python3 rebuild_galleries.py` to refresh the two static overview galleries, or use the existing inline chapter display immediately.

The legacy JSON slot editing feature stores edits in browser localStorage, not HTML. Export those edits before changing browsers or publishing. Old browser state can be reset by clearing site storage if titles look stale.

## Editorial backlog

The corrected image mappings, artist names and links are a mechanical repair, **not a full primary-source catalogue verification**. In particular, Scheffer/Pensotti/Landelle/Schlesinger/Cottin/Richard titles need individual catalogue checks. Revisit the section on landscape and portraiture to add further catalogue-supported candidates, marking works not exhibited in the relevant Salon distinctly. Review artist portrait identity matches across 1845/1846; existing shared paths are preserved.

