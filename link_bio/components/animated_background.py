import reflex as rx


def animated_background() -> rx.Component:
    return rx.fragment(
        rx.html(
            '<canvas id="bg-beams" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;display:block;"></canvas>'
        ),
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="0",
            pointer_events="none",
            bg="rgba(5, 5, 8, 0.4)",
        ),
        rx.script("""
(function() {
  var _bg = window._bgBeams = window._bgBeams || {};

  function start() {
    var canvas = document.getElementById('bg-beams');
    if (!canvas) { if (!_bg.waiting) { _bg.waiting = true; setTimeout(start, 100); } return; }
    _bg.waiting = false;
    if (_bg.animId) { cancelAnimationFrame(_bg.animId); }

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
      var total = 20;
      beams = [];
      for (var i = 0; i < total; i++) beams.push(createBeam(i, total));
    }

    function createBeam(index, total) {
      return {
        x: Math.random() * W * 1.5 - W * 0.25,
        y: Math.random() * H * 2 - H * 0.5,
        width: 20 + Math.random() * 40,
        length: H * 2,
        angle: -35 + Math.random() * 10,
        speed: 0.3 + Math.random() * 0.6,
        opacity: 0.06 + Math.random() * 0.10,
        hue: 200 + Math.random() * 60,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: 0.02 + Math.random() * 0.03,
      };
    }

    function resetBeam(beam, index, total) {
      var col = index % 3;
      var sp = W / 3;
      beam.y = H + 50;
      beam.x = col * sp + sp / 2 + (Math.random() - 0.5) * sp * 0.5;
      beam.width = 60 + Math.random() * 80;
      beam.speed = 0.2 + Math.random() * 0.3;
      beam.hue = 200 + (index * 60) / total;
      beam.opacity = 0.08 + Math.random() * 0.06;
    }

    function drawBeam(beam) {
      ctx.save();
      ctx.translate(beam.x, beam.y);
      ctx.rotate((beam.angle * Math.PI) / 180);
      var po = beam.opacity * (0.8 + Math.sin(beam.pulse) * 0.2);
      var grad = ctx.createLinearGradient(0, 0, 0, beam.length);
      grad.addColorStop(0, 'hsla(' + beam.hue + ',80%,60%,0)');
      grad.addColorStop(0.15, 'hsla(' + beam.hue + ',80%,60%,' + (po * 0.5) + ')');
      grad.addColorStop(0.4, 'hsla(' + beam.hue + ',80%,60%,' + po + ')');
      grad.addColorStop(0.6, 'hsla(' + beam.hue + ',80%,60%,' + po + ')');
      grad.addColorStop(0.85, 'hsla(' + beam.hue + ',80%,60%,' + (po * 0.5) + ')');
      grad.addColorStop(1, 'hsla(' + beam.hue + ',80%,60%,0)');
      ctx.fillStyle = grad;
      ctx.fillRect(-beam.width / 2, 0, beam.width, beam.length);
      ctx.restore();
    }

    function animate() {
      ctx.clearRect(0, 0, W, H);
      ctx.filter = 'blur(30px)';
      for (var i = 0; i < beams.length; i++) {
        var b = beams[i];
        b.y -= b.speed;
        b.pulse += b.pulseSpeed;
        if (b.y + b.length < -100) resetBeam(b, i, beams.length);
        drawBeam(b);
      }
      _bg.animId = requestAnimationFrame(animate);
    }

    resize();
    window.addEventListener('resize', resize);
    animate();
  }

  function tryStart() { start(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryStart);
  } else {
    tryStart();
  }

  var mo = new MutationObserver(function() {
    if (document.getElementById('bg-beams')) start();
  });
  mo.observe(document.body || document.documentElement, { childList: true, subtree: true });

  window.addEventListener('pageshow', function(e) { if (e.persisted) setTimeout(tryStart, 50); });
  window.addEventListener('popstate', function() { setTimeout(tryStart, 100); });
})();
"""),
    )
