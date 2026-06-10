import reflex as rx


def animated_background() -> rx.Component:
    return rx.fragment(
        rx.html(
            '<canvas id="bg-beams" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;"></canvas>'
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            bg="rgba(5, 5, 8, 0.03)",
            style={
                "backdropFilter": "blur(50px)",
                "-webkit-backdrop-filter": "blur(50px)",
                "animation": "beamOverlay 10s ease-in-out infinite",
            },
        ),
        rx.script("""
(function() {
  function init() {
    var canvas = document.getElementById('bg-beams');
    if (!canvas) { setTimeout(init, 100); return; }
    if (canvas.dataset.beamReady) return;
    canvas.dataset.beamReady = 'true';

  var ctx = canvas.getContext('2d');
  var beams = [];
  var W, H;

  function resize() {
    var dpr = window.devicePixelRatio || 1;
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.scale(dpr, dpr);

    var total = Math.floor(30);
    beams = [];
    for (var i = 0; i < total; i++) {
      beams.push(createBeam(i, total));
    }
  }

  function createBeam(index, total) {
    var angle = -35 + Math.random() * 10;
    return {
      x: Math.random() * W * 1.5 - W * 0.25,
      y: Math.random() * H * 1.5 - H * 0.25,
      width: 30 + Math.random() * 60,
      length: H * 2.5,
      angle: angle,
      speed: 0.3 + Math.random() * 0.8,
      opacity: 0.08 + Math.random() * 0.12,
      hue: 190 + Math.random() * 70,
      pulse: Math.random() * Math.PI * 2,
      pulseSpeed: 0.02 + Math.random() * 0.03,
    };
  }

  function resetBeam(beam, index, total) {
    var column = index % 3;
    var spacing = W / 3;
    beam.y = H + 100;
    beam.x = column * spacing + spacing / 2 + (Math.random() - 0.5) * spacing * 0.5;
    beam.width = 100 + Math.random() * 100;
    beam.speed = 0.3 + Math.random() * 0.4;
    beam.hue = 190 + (index * 70) / total;
    beam.opacity = 0.12 + Math.random() * 0.08;
    return beam;
  }

  function drawBeam(beam) {
    ctx.save();
    ctx.translate(beam.x, beam.y);
    ctx.rotate((beam.angle * Math.PI) / 180);

    var po = beam.opacity * (0.8 + Math.sin(beam.pulse) * 0.2);
    var grad = ctx.createLinearGradient(0, 0, 0, beam.length);
    grad.addColorStop(0, 'hsla(' + beam.hue + ',85%,65%,0)');
    grad.addColorStop(0.1, 'hsla(' + beam.hue + ',85%,65%,' + (po * 0.5) + ')');
    grad.addColorStop(0.4, 'hsla(' + beam.hue + ',85%,65%,' + po + ')');
    grad.addColorStop(0.6, 'hsla(' + beam.hue + ',85%,65%,' + po + ')');
    grad.addColorStop(0.9, 'hsla(' + beam.hue + ',85%,65%,' + (po * 0.5) + ')');
    grad.addColorStop(1, 'hsla(' + beam.hue + ',85%,65%,0)');

    ctx.fillStyle = grad;
    ctx.fillRect(-beam.width / 2, 0, beam.width, beam.length);
    ctx.restore();
  }

  function animate() {
    ctx.clearRect(0, 0, W, H);
    ctx.filter = 'blur(35px)';

    var total = beams.length;
    for (var i = 0; i < total; i++) {
      var b = beams[i];
      b.y -= b.speed;
      b.pulse += b.pulseSpeed;
      if (b.y + b.length < -100) resetBeam(b, i, total);
      drawBeam(b);
    }

    requestAnimationFrame(animate);
  }

  resize();
  window.addEventListener('resize', resize);
  animate();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""),
    )
