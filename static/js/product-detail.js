const qty = document.getElementById("qty");

document.getElementById("plus").onclick = () => {
  qty.value = parseInt(qty.value) + 1;
};

document.getElementById("minus").onclick = () => {
  if (qty.value > 1) {
    qty.value = parseInt(qty.value) - 1;
  }
};
