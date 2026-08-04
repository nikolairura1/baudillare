# The Mirror of Art — GitHub Pages site

A GitHub Pages-ready Jekyll site with one page for each internal subsection of *The Mirror of Art*.

## Publish

1. Create a new GitHub repository.
2. Upload the contents of this folder to the repository root.
3. In **Settings → Pages**, choose **Deploy from a branch**.
4. Select the `main` branch and `/ (root)`.
5. Save. GitHub will build the site automatically.

## Edit text

Each subsection is a Markdown file in `chapters/`. The text is OCR-derived and should be proofread against the scan.

## Add artwork images

Put images in `assets/images/`, then insert a `<figure class="artwork">…</figure>` block into the relevant Markdown file. A commented example is already present in the chapter layout.

## Change the title or description

Edit `_config.yml`.

## Local preview

With Ruby and Bundler installed:

```bash
bundle exec jekyll serve
```

GitHub Pages can build this simple site without a custom theme or plugin.
