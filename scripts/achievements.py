#!/usr/bin/env python3
"""Write a stable achievements panel for the profile README."""

from pathlib import Path


SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 180" role="img" aria-label="Ashish S. Mishra GitHub achievements">
<rect width="900" height="180" rx="12" fill="#161b22"/>
<text x="42" y="52" fill="#f0f6fc" font-family="Arial,sans-serif" font-size="25" font-weight="700">GitHub achievements</text>
<text x="42" y="88" fill="#8b949e" font-family="Arial,sans-serif" font-size="16">Building, learning, and shipping across software, AI, and cloud projects.</text>
<g font-family="Arial,sans-serif" font-size="14" font-weight="600">
  <rect x="42" y="113" width="178" height="36" rx="7" fill="#21262d" stroke="#30363d"/><text x="62" y="136" fill="#79c0ff">Software development</text>
  <rect x="234" y="113" width="150" height="36" rx="7" fill="#21262d" stroke="#30363d"/><text x="254" y="136" fill="#79c0ff">AI exploration</text>
  <rect x="398" y="113" width="144" height="36" rx="7" fill="#21262d" stroke="#30363d"/><text x="418" y="136" fill="#79c0ff">Open source</text>
</g>
</svg>
"""

Path("assets/metrics.achievements.svg").write_text(SVG, encoding="utf-8")