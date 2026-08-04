
const button = document.querySelector('.toc-toggle');
const toc = document.querySelector('.toc');
if (button && toc) {
  button.addEventListener('click', () => {
    const open = toc.classList.toggle('is-open');
    button.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}
