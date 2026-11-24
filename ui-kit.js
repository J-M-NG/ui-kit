/*!
 * ui-kit.js (optional, dependency-free). MIT licence. See LICENSE.
 * Every component works without this file; it only adds behaviour.
 *
 * Sortable table: add data-jm-sortable to a <table class="jm-table">, and
 *   data-sort="number" or data-sort="text" (default) to each <th> that sorts.
 *   A cell may carry data-sort-value to sort by something other than its text.
 * Table filter: <input data-jm-filter="table-id"> hides rows whose text does not
 *   contain the typed words. An element with role="status" and
 *   data-jm-filter-status="table-id" receives the count in words.
 * Tabs: add data-jm-tabs to .jm-tabs; buttons use role="tab" with aria-controls.
 * Dialog: buttons with data-jm-dialog-open="id" call showModal() on <dialog id="id">.
 */
(function () {
  'use strict';

  function cellValue(row, index, type) {
    var cell = row.cells[index];
    var raw = cell ? (cell.getAttribute('data-sort-value') || cell.textContent).trim() : '';
    if (type === 'number') {
      var n = parseFloat(raw.replace(/[^0-9.\-]/g, ''));
      return isNaN(n) ? -Infinity : n;
    }
    return raw.toLowerCase();
  }

  function makeSortable(table) {
    var body = table.tBodies[0];
    var headers = table.querySelectorAll('thead th[data-sort]');
    headers.forEach(function (th) {
      var label = th.textContent.trim();
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'jm-sort';
      button.textContent = label;
      th.textContent = '';
      th.appendChild(button);
      th.setAttribute('aria-sort', 'none');
      button.addEventListener('click', function () {
        var direction = th.getAttribute('aria-sort') === 'ascending' ? 'descending' : 'ascending';
        headers.forEach(function (other) { other.setAttribute('aria-sort', 'none'); });
        th.setAttribute('aria-sort', direction);
        var index = th.cellIndex;
        var type = th.getAttribute('data-sort');
        var rows = Array.prototype.slice.call(body.rows);
        rows.sort(function (a, b) {
          var x = cellValue(a, index, type);
          var y = cellValue(b, index, type);
          var result = x < y ? -1 : x > y ? 1 : 0;
          return direction === 'ascending' ? result : -result;
        });
        rows.forEach(function (row) { body.appendChild(row); });
      });
    });
  }

  function makeFilter(input) {
    var table = document.getElementById(input.getAttribute('data-jm-filter'));
    if (!table || !table.tBodies[0]) return;
    var status = document.querySelector('[data-jm-filter-status="' + table.id + '"]');
    function apply() {
      var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      Array.prototype.forEach.call(table.tBodies[0].rows, function (row) {
        var text = row.textContent.toLowerCase();
        var match = words.every(function (w) { return text.indexOf(w) !== -1; });
        row.hidden = !match;
        if (match) shown += 1;
      });
      if (status) status.textContent = 'Showing ' + shown + ' of ' + table.tBodies[0].rows.length + ' rows';
    }
    input.addEventListener('input', apply);
    apply();
  }

  function makeTabs(root) {
    var tabs = root.querySelectorAll('[role="tab"]');
    var panels = root.querySelectorAll('[role="tabpanel"]');
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
      });
      panels.forEach(function (p) {
        p.hidden = p.id !== tab.getAttribute('aria-controls');
      });
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        var next = i;
        if (e.key === 'ArrowRight') next = (i + 1) % tabs.length;
        else if (e.key === 'ArrowLeft') next = (i - 1 + tabs.length) % tabs.length;
        else if (e.key === 'Home') next = 0;
        else if (e.key === 'End') next = tabs.length - 1;
        else return;
        e.preventDefault();
        tabs[next].focus();
        select(tabs[next]);
      });
    });
    var current = root.querySelector('[role="tab"][aria-selected="true"]') || tabs[0];
    if (current) select(current);
  }

  function makeDialogs() {
    document.querySelectorAll('[data-jm-dialog-open]').forEach(function (btn) {
      var id = btn.getAttribute('data-jm-dialog-open');
      var dialog = document.getElementById(id);
      if (!dialog || !dialog.showModal) return;
      btn.addEventListener('click', function () { dialog.showModal(); });
    });
    document.querySelectorAll('.jm-dialog').forEach(function (dialog) {
      dialog.addEventListener('cancel', function (e) { e.preventDefault(); dialog.close(); });
    });
  }

  document.querySelectorAll('table[data-jm-sortable]').forEach(makeSortable);
  document.querySelectorAll('input[data-jm-filter]').forEach(makeFilter);
  document.querySelectorAll('[data-jm-tabs]').forEach(makeTabs);
  makeDialogs();
})();
