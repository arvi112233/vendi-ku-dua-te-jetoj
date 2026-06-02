const PAGES = [
  { num: 1, file: "index.html", title: "Hyrja" },
  { num: 2, file: "rreth-projektit.html", title: "Rreth Projektit" },
  { num: 3, file: "pse-new-york.html", title: "Pse New York?" },
  { num: 4, file: "historia.html", title: "Historia" },
  { num: 5, file: "gjeografia.html", title: "Gjeografia" },
  { num: 6, file: "klima.html", title: "Klima" },
  { num: 7, file: "popullsia.html", title: "Popullsia" },
  { num: 8, file: "manhattan.html", title: "Manhattan" },
  { num: 9, file: "brooklyn.html", title: "Brooklyn" },
  { num: 10, file: "queens.html", title: "Queens" },
  { num: 11, file: "bronx.html", title: "Bronx" },
  { num: 12, file: "staten-island.html", title: "Staten Island" },
  { num: 13, file: "transporti.html", title: "Transporti" },
  { num: 14, file: "metroja.html", title: "Metropolitana" },
  { num: 15, file: "shkollat.html", title: "Shkollat" },
  { num: 16, file: "universitetet.html", title: "Universitetet" },
  { num: 17, file: "karriera.html", title: "Karriera" },
  { num: 18, file: "kostoja.html", title: "Kostoja e Jetesës" },
  { num: 19, file: "banesa.html", title: "Banesat" },
  { num: 20, file: "kultura.html", title: "Kultura" },
  { num: 21, file: "muzeet.html", title: "Muzeet" },
  { num: 22, file: "central-park.html", title: "Central Park" },
  { num: 23, file: "times-square.html", title: "Times Square" },
  { num: 24, file: "statuja-e-lirise.html", title: "Statuja e Lirisë" },
  { num: 25, file: "ura-brooklyn.html", title: "Ura e Brooklyn" },
  { num: 26, file: "sporti.html", title: "Sporti" },
  { num: 27, file: "gastronomia.html", title: "Gastronomia" },
  { num: 28, file: "festivalet.html", title: "Festivalet" },
  { num: 29, file: "siguria.html", title: "Siguria" },
  { num: 30, file: "konkluzioni.html", title: "Konkluzioni" },
];

const AUTHOR = {
  name: "Harvard Zani",
  school: 'SHKA "26 Nëntori"',
  city: "Tiranë",
  subject: "Gjuha Shqipe",
  grade: "Klasa IX",
};

function getCurrentPage() {
  const path = window.location.pathname.split("/").pop() || "index.html";
  return PAGES.find((p) => p.file === path) || PAGES[0];
}

function buildHeader(current) {
  const pagesLinks = PAGES.map(
    (p) =>
      `<a href="${p.file}"${p.num === current.num ? ' aria-current="page"' : ""}>${p.num}. ${p.title}</a>`
  ).join("");

  return `
    <header class="site-header">
      <div class="header-inner">
        <a class="logo" href="index.html">
          Vendi ku dua të jetoj
          <span>${AUTHOR.subject} · ${AUTHOR.grade}</span>
        </a>
        <span class="author-chip">${AUTHOR.name}</span>
        <span class="page-badge">Faqja ${current.num} / 30</span>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="all-pages">
          Menu
        </button>
        <nav class="main-nav" aria-label="Navigimi kryesor">
          <a href="index.html" class="nav-link-hide-mobile">Hyrja</a>
          ${current.num > 1 ? `<a href="${PAGES[current.num - 2].file}" class="nav-link-hide-mobile">Mbrapa</a>` : ""}
          ${current.num < 30 ? `<a href="${PAGES[current.num].file}" class="nav-link-hide-mobile">Para</a>` : ""}
        </nav>
        <div class="nav-pages" id="all-pages" hidden>
          <div class="nav-pages-grid">${pagesLinks}</div>
        </div>
      </div>
    </header>
  `;
}

function buildPageNav(current) {
  const prev = current.num > 1 ? PAGES[current.num - 2] : null;
  const next = current.num < 30 ? PAGES[current.num] : null;
  let html = '<nav class="page-nav" aria-label="Faqet e projektit">';
  html += prev
    ? `<a class="prev" href="${prev.file}">${prev.title}</a>`
    : "<span></span>";
  html += next
    ? `<a class="next" href="${next.file}">${next.title}</a>`
    : "<span></span>";
  html += "</nav>";
  return html;
}

function buildFooter() {
  return `
    <footer class="site-footer">
      <p class="footer-name">${AUTHOR.name}</p>
      <p>${AUTHOR.grade} · ${AUTHOR.school}, ${AUTHOR.city}</p>
      <p>Projekt për lëndën <strong>${AUTHOR.subject}</strong> — <em>Vendi ku dua të jetoj: New York City</em></p>
      <p>30 faqe · Viti shkollor 2025–2026</p>
    </footer>
  `;
}

function initNavigation() {
  const current = getCurrentPage();
  const headerSlot = document.getElementById("site-header");
  const footerSlot = document.getElementById("site-footer");

  if (headerSlot) {
    headerSlot.innerHTML = buildHeader(current);
  } else {
    document.body.insertAdjacentHTML("afterbegin", buildHeader(current));
  }

  const pageNavHtml = buildPageNav(current);
  const footerHtml = buildFooter();

  if (footerSlot) {
    footerSlot.innerHTML = pageNavHtml + footerHtml;
  } else {
    document.body.insertAdjacentHTML("beforeend", pageNavHtml + footerHtml);
  }

  const toggle = document.querySelector(".nav-toggle");
  const panel = document.getElementById("all-pages");
  if (toggle && panel) {
    toggle.addEventListener("click", () => {
      const open = panel.classList.toggle("open");
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  document.querySelectorAll(".main-nav a").forEach((link) => {
    if (link.getAttribute("href") === current.file) link.classList.add("active");
  });
}

document.addEventListener("DOMContentLoaded", initNavigation);
