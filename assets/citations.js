document.querySelectorAll('[data-bibtex]').forEach((button) => {
  let reset;
  button.addEventListener('click', async () => {
    const status = button.nextElementSibling;
    clearTimeout(reset);
    try {
      await navigator.clipboard.writeText(button.dataset.bibtex);
      button.textContent = 'Copied';
      status.textContent = 'BibTeX copied to clipboard.';
    } catch (error) {
      button.textContent = 'Retry';
      status.textContent = 'Could not copy. Please allow clipboard access and try again.';
    }
    reset = setTimeout(() => { button.textContent = 'Cite'; status.textContent = ''; }, 3000);
  });
});
