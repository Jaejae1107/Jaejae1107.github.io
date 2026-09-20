(() => {
  const filters = document.querySelector(".filters");
  if (!filters) return;
  filters.hidden = false;
  const cards = [...document.querySelectorAll(".project-card")];
  const status = document.querySelector("#filter-status");
  filters.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-filter]");
    if (!button) return;
    const category = button.dataset.filter;
    filters.querySelectorAll("button").forEach((item) => {
      item.setAttribute("aria-pressed", String(item === button));
    });
    let visible = 0;
    cards.forEach((card) => {
      card.hidden = category !== "all" && card.dataset.category !== category;
      if (!card.hidden) visible += 1;
    });
    status.textContent = document.documentElement.lang === "ko" ? `${visible}개의 프로젝트가 표시됩니다.` : `${visible} projects shown.`;
  });
})();
