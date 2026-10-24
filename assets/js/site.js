/* site.js — shared behaviour for deftsuite.com pages (footer year). */
(function () {
  'use strict';
  var y = document.querySelector('.foot__base span');
  if (y) y.textContent = '© ' + new Date().getFullYear() + ' Deft';
})();
