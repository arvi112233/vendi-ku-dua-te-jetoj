(function () {
  const FALLBACK =
    "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1600&q=85";

  function initProgress() {
    const bar = document.createElement("div");
    bar.className = "scroll-progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);

    window.addEventListener(
      "scroll",
      () => {
        const doc = document.documentElement;
        const max = doc.scrollHeight - doc.clientHeight;
        const scrolled = max > 0 ? doc.scrollTop / max : 0;
        bar.style.transform = `scaleX(${Math.min(1, Math.max(0, scrolled))})`;
      },
      { passive: true }
    );
  }

  function initImages() {
    document.querySelectorAll("img.content-image, .home-card img").forEach((img) => {
      img.addEventListener("error", function onErr() {
        if (this.dataset.fallbackApplied) return;
        this.dataset.fallbackApplied = "1";
        this.src = FALLBACK;
      });
    });
  }

  function initReveal() {
    const targets = document.querySelectorAll(
      ".content-section, .figure-block, .fact-box, .student-info, .home-card, .toc-table, .lead, .section-title"
    );

    targets.forEach((el, i) => {
      el.classList.add("reveal");
      el.style.setProperty("--reveal-delay", `${Math.min(i * 0.07, 0.55)}s`);
    });

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -30px 0px" }
    );

    targets.forEach((el) => io.observe(el));
  }

  function initHeaderScroll() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 20);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initTocRows() {
    document.querySelectorAll(".toc-table tbody tr").forEach((row, i) => {
      row.style.transition = "transform 0.25s ease, background 0.25s ease";
      row.style.transitionDelay = `${i * 0.02}s`;
    });
  }

  function initParallaxHero() {
    const hero = document.querySelector(".hero");
    if (!hero || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    window.addEventListener(
      "scroll",
      () => {
        const y = window.scrollY;
        if (y < 600) {
          hero.style.setProperty("--parallax", `${y * 0.25}px`);
        }
      },
      { passive: true }
    );
  }

  document.addEventListener("DOMContentLoaded", () => {
    initProgress();
    initImages();
    initReveal();
    initHeaderScroll();
    initTocRows();
    initParallaxHero();
  });
})();
