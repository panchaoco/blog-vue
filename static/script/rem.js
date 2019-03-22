(function () {
  setRem();
  window.addEventListener("resize", setRem);

  function setRem() {
    const html = document.documentElement;
    const hWidth = html.getBoundingClientRect().width;
    const fz = hWidth / 7.5;
    html.style.fontSize = fz <= 100 ? fz + 'px' : '100px';
  }

})()
