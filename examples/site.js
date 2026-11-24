// Documentation site chrome: the header theme switch, shared by every page.
// Not part of the kit. The saved choice is applied on every page, with or
// without a switch, so the theme stays the same while moving between chapters.
(function () {
  var root = document.documentElement;
  var key = 'jm-theme';

  // Set before the body is parsed so the switch takes its space from the first
  // paint; site.css hides it only when this script has not run.
  root.setAttribute('data-site-js', '');

  function apply(theme) {
    if (theme === 'light' || theme === 'dark') root.setAttribute('data-theme', theme);
    else root.removeAttribute('data-theme');
    document.querySelectorAll('[data-set-theme]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.setTheme === (theme || 'system')));
    });
    document.dispatchEvent(new CustomEvent('site:themechange'));
  }

  var saved = null;
  try { saved = localStorage.getItem(key); } catch (e) {}
  apply(saved || 'system');

  document.addEventListener('DOMContentLoaded', function () {
    apply(saved || 'system');
    document.querySelectorAll('[data-set-theme]').forEach(function (b) {
      b.addEventListener('click', function () {
        var theme = b.dataset.setTheme;
        try { localStorage.setItem(key, theme); } catch (e) {}
        apply(theme);
      });
    });
  });
})();
