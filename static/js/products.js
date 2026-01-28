function toggleCategories() {
  const panel = document.getElementById("categoriesPanel");
  const arrow = document.getElementById("catArrow");

  if (!panel || !arrow) return;

  panel.classList.toggle("hide");
  arrow.classList.toggle("rotate");
}

//
//
//function openFilter() {
//  document.getElementById("filterDrawer").classList.add("open");
//  document.getElementById("filterOverlay").classList.add("show");
//}
//
//function closeFilter() {
//  document.getElementById("filterDrawer").classList.remove("open");
//  document.getElementById("filterOverlay").classList.remove("show");
//}
