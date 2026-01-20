function toggleCategories() {
  const panel = document.getElementById("categoriesPanel");
  const arrow = document.getElementById("catArrow");

  if (!panel) return;

  panel.classList.toggle("hide");
  arrow.classList.toggle("rotate");
}
