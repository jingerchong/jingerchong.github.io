(function () {
  var browser = document.querySelector('[data-project-browser]');
  if (!browser) return;

  var buttons = Array.prototype.slice.call(browser.querySelectorAll('[data-filter]'));
  var cards = Array.prototype.slice.call(browser.querySelectorAll('[data-project-card]'));
  var status = browser.querySelector('[data-project-filter-status]');

  function applyFilter(filter) {
    var activeFilter = filter || 'all';
    var visibleCount = 0;

    buttons.forEach(function (button) {
      button.setAttribute('aria-pressed', String(button.dataset.filter === activeFilter));
    });

    cards.forEach(function (card) {
      var tags = (card.dataset.tags || '').split('|').map(function (tag) { return tag.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); });
      var visible = activeFilter === 'all' || tags.indexOf(activeFilter) !== -1;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    status.textContent = 'Showing ' + visibleCount + (visibleCount === 1 ? ' project.' : ' projects.');
  }

  function filterFromHash() {
    var filter = window.location.hash.slice(1);
    return buttons.some(function (button) { return button.dataset.filter === filter; }) ? filter : 'all';
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      var filter = button.dataset.filter;
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', filter === 'all' ? window.location.pathname : '#' + filter);
      }
      applyFilter(filter);
    });
  });

  window.addEventListener('hashchange', function () { applyFilter(filterFromHash()); });
  applyFilter(filterFromHash());
}());
