import reflex as rx


def animated_background(
    has_active_reminders: bool = False,
    has_upcoming_reminders: bool = False,
    disable_center_dimming: bool = False,
) -> rx.Component:
    return rx.fragment(
        rx.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"
        ),
        rx.script(
            f"""
(function() {{
  var _nb = window._nebulaBg = window._nebulaBg || {{}};

  function init() {{
    var container = document.getElementById('nebula-bg');
    if (!container) {{ _nb.waitTimer = setTimeout(init, 100); return; }}
    if (container._nebulaActive) return;
    container._nebulaActive = true;

    if (typeof THREE === 'undefined') {{ setTimeout(init, 200); return; }}

    var props = {{
      hasActiveReminders: {'true' if has_active_reminders else 'false'},
      hasUpcomingReminders: {'true' if has_upcoming_reminders else 'false'},
      disableCenterDimming: {'true' if disable_center_dimming else 'false'},
    }};

    var renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: false }});
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    var scene = new THREE.Scene();
    var camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
    var clock = new THREE.Clock();

    var vertexShader = [
      'varying vec2 vUv;',
      'void main() {{',
      '  vUv = uv;',
      '  gl_Position = vec4(position, 1.0);',
      '}}',
    ].join('\\n');

    var fragmentShader = [
      'precision highp float;',
      'varying vec2 vUv;',
      'uniform vec2 iResolution;',
      'uniform float iTime;',
      'uniform vec2 iMouse;',
      'uniform bool hasActiveReminders;',
      'uniform bool hasUpcomingReminders;',
      'uniform bool disableCenterDimming;',
      '',
      'mat2 m(float a) {{',
      '  float c = cos(a), s = sin(a);',
      '  return mat2(c, -s, s, c);',
      '}}',
      '',
      'float map(vec3 p) {{',
      '  p.xz *= m(iTime * 0.4);',
      '  p.xy *= m(iTime * 0.3);',
      '  vec3 q = p * 2.0 + iTime;',
      '  return length(p + vec3(sin(iTime * 0.7))) * log(length(p) + 1.0)',
      '       + sin(q.x + sin(q.z + sin(q.y))) * 0.5 - 1.0;',
      '}}',
      '',
      'void main() {{',
      '  vec2 uv = vUv * iResolution / min(iResolution.x, iResolution.y) - vec2(0.9, 0.5);',
      '  uv.x += 0.4;',
      '  vec3 col = vec3(0.0);',
      '  float d = 2.5;',
      '',
      '  for (int i = 0; i <= 5; i++) {{',
      '    vec3 p = vec3(0.0, 0.0, 5.0) + normalize(vec3(uv, -1.0)) * d;',
      '    float rz = map(p);',
      '    float f = clamp((rz - map(p + 0.1)) * 0.5, -0.1, 1.0);',
      '',
      '    vec3 base;',
      '    if (hasActiveReminders) {{',
      '      base = vec3(0.05, 0.2, 0.5) + vec3(4.0, 2.0, 5.0) * f;',
      '    }} else if (hasUpcomingReminders) {{',
      '      base = vec3(0.05, 0.3, 0.1) + vec3(2.0, 5.0, 1.0) * f;',
      '    }} else {{',
      '      base = vec3(0.1, 0.3, 0.4) + vec3(5.0, 2.5, 3.0) * f;',
      '    }}',
      '',
      '    col = col * base + smoothstep(2.5, 0.0, rz) * 0.7 * base;',
      '    d += min(rz, 1.0);',
      '  }}',
      '',
      '  vec2 fc = vUv * iResolution;',
      '  float dist = distance(fc, iResolution * 0.5);',
      '  float radius = min(iResolution.x, iResolution.y) * 0.5;',
      '  float dim = disableCenterDimming ? 1.0 : smoothstep(radius * 0.3, radius * 0.5, dist);',
      '',
      '  if (!disableCenterDimming) {{',
      '    col = mix(col * 0.3, col, dim);',
      '  }}',
      '',
      '  gl_FragColor = vec4(col, 1.0);',
      '}}',
    ].join('\\n');

    var uniforms = {{
      iTime: {{ value: 0 }},
      iResolution: {{ value: new THREE.Vector2() }},
      iMouse: {{ value: new THREE.Vector2() }},
      hasActiveReminders: {{ value: props.hasActiveReminders }},
      hasUpcomingReminders: {{ value: props.hasUpcomingReminders }},
      disableCenterDimming: {{ value: props.disableCenterDimming }},
    }};

    var material = new THREE.ShaderMaterial({{
      vertexShader: vertexShader,
      fragmentShader: fragmentShader,
      uniforms: uniforms,
    }});

    var mesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
    scene.add(mesh);

    function resize() {{
      var w = container.clientWidth;
      var h = container.clientHeight;
      renderer.setSize(w, h);
      uniforms.iResolution.value.set(w, h);
    }}

    function onMouseMove(e) {{
      uniforms.iMouse.value.set(e.clientX, window.innerHeight - e.clientY);
    }}

    window.addEventListener('resize', resize);
    window.addEventListener('mousemove', onMouseMove);

    var initW = container.clientWidth || window.innerWidth;
    var initH = container.clientHeight || window.innerHeight;
    renderer.setSize(initW, initH);
    uniforms.iResolution.value.set(initW, initH);

    renderer.setAnimationLoop(function() {{
      uniforms.iTime.value = clock.getElapsedTime();
      renderer.render(scene, camera);
    }});

    container._nebulaCleanup = function() {{
      window.removeEventListener('resize', resize);
      window.removeEventListener('mousemove', onMouseMove);
      renderer.setAnimationLoop(null);
      material.dispose();
      mesh.geometry.dispose();
      renderer.dispose();
      if (container.contains(renderer.domElement)) {{
        container.removeChild(renderer.domElement);
      }}
    }};
  }}

  if (_nb.cleanup) _nb.cleanup();
  _nb.cleanup = function() {{
    var c = document.getElementById('nebula-bg');
    if (c && c._nebulaCleanup) {{ c._nebulaCleanup(); c._nebulaActive = false; }}
  }};

  init();

  var mo = new MutationObserver(function() {{
    var c = document.getElementById('nebula-bg');
    if (c && !c._nebulaActive) init();
  }});
  mo.observe(document.body || document.documentElement, {{ childList: true, subtree: true }});

  window.addEventListener('pageshow', function(e) {{ if (e.persisted) setTimeout(init, 50); }});
  window.addEventListener('popstate', function() {{ setTimeout(init, 100); }});
}})();
            """
        ),
        rx.box(
            id="nebula-bg",
            position="fixed",
            inset="0",
            z_index="0",
            pointer_events="none",
            bg="#050508",
        ),
    )
