# Artwork images

Place image files here, then add them to the relevant chapter Markdown file using HTML:

```html
<figure class="artwork">
  <img src="{{ '/assets/images/your-file.jpg' | relative_url }}" alt="Description">
  <figcaption>
    <strong>Artist, <em>Title</em></strong><br>
    Date, medium, collection. Source and rights note.
  </figcaption>
</figure>
```
