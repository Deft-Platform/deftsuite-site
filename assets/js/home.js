/* ============================================================
   home.js — corner ticks, the hero walkthrough, the toggle
   ============================================================ */
(function () {
  'use strict';

  /* ---- Corner ticks on every framed panel ---- */
  document.querySelectorAll('.frame').forEach(function (f) {
    ['tl', 'tr', 'bl', 'br'].forEach(function (c) {
      var i = document.createElement('i');
      i.className = 'tick tick--' + c;
      i.setAttribute('aria-hidden', 'true');
      f.appendChild(i);
    });
  });

  /* ---- Hero: a questionnaire question answered across the suite ---- */
  var demo = document.querySelector('.demo');
  if (demo) {
    var steps = demo.querySelectorAll('.step');
    var text = demo.querySelector('.answer__text');
    var state = demo.querySelector('.state');
    var replay = demo.querySelector('.replay');
    var full = text.getAttribute('data-answer');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var timers = [];

    function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
    function setState(kind, label) {
      state.className = 'state state--' + kind;
      state.textContent = label;
    }
    function finalState() {
      steps.forEach(function (s) { s.classList.add('is-on'); });
      text.textContent = full;
      setState('done', 'APPROVED · PUBLISHED TO TRUST PORTAL');
    }
    function type(i) {
      text.textContent = full.slice(0, i);
      if (i < full.length) later(function () { type(i + 2); }, 18);
      else {
        setState('wait', 'AWAITING APPROVAL');
        later(function () { setState('done', 'APPROVED · PUBLISHED TO TRUST PORTAL'); }, 1800);
      }
    }
    function run() {
      timers.forEach(clearTimeout); timers = [];
      if (reduce) { finalState(); return; }
      steps.forEach(function (s) { s.classList.remove('is-on'); });
      text.textContent = '';
      setState('wait', 'DRAFTING');
      steps.forEach(function (s, n) { later(function () { s.classList.add('is-on'); }, 600 + n * 1100); });
      later(function () { type(0); }, 600 + steps.length * 1100);
    }

    if ('IntersectionObserver' in window) {
      var seen = false;
      new IntersectionObserver(function (e) {
        if (e[0].isIntersecting && !seen) { seen = true; run(); }
      }, { threshold: 0.3 }).observe(demo);
    } else { finalState(); }
    replay.addEventListener('click', run);
  }

  /* ---- Questionnaire: without / with Deft ---- */
  var q = document.querySelector('[data-view]');
  if (q) {
    document.querySelectorAll('.seg button').forEach(function (b) {
      b.addEventListener('click', function () {
        q.setAttribute('data-view', b.getAttribute('data-set'));
        document.querySelectorAll('.seg button').forEach(function (o) {
          o.setAttribute('aria-pressed', String(o === b));
        });
      });
    });
  }
})();
