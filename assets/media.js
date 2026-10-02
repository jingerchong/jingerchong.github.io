// Local loops stay user-controlled when reduced motion is requested.
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const loops = document.querySelectorAll('video[data-loop]');
function updateLoops() {
  loops.forEach(video => {
    if (reducedMotion.matches) {
      video.pause();
      video.removeAttribute('autoplay');
    } else {
      video.muted = true;
      video.setAttribute('autoplay', '');
      video.play().catch(() => {});
    }
  });
}
reducedMotion.addEventListener('change', updateLoops);
updateLoops();
