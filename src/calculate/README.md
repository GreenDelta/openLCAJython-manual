# Calculate

Calculating a product system produces its life cycle inventory and impact assessment results. You can
customize the calculation according to your requirements: you can choose the allocation method, the
impact assessment method, normalization and weighting set, the calculation type (lazy, eager or Monte
Carlo simulation) or whether to include regionalized calculations, cost calculations or data quality.

_Source: [openLCA 2 manual — Calculation and Result Analysis](https://greendelta.github.io/openLCA2-manual/res_analysis/index.html)_

<svg viewBox="0 0 660 230" role="img" aria-label="A product system and impact method feed a calculation setup that the system calculator runs to produce an LCA result" style="max-width:660px;width:100%;height:auto;font-family:sans-serif">
  <title>The calculation pipeline</title>
  <defs>
    <marker id="af3" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="14" y="16" width="150" height="40" rx="6"/>
    <rect x="14" y="96" width="150" height="40" rx="6"/>
    <rect x="214" y="56" width="170" height="40" rx="6"/>
    <rect x="434" y="56" width="170" height="40" rx="6"/>
    <rect x="434" y="150" width="170" height="40" rx="6"/>
    <line x1="164" y1="36" x2="212" y2="70" marker-end="url(#af3)"/>
    <line x1="164" y1="116" x2="212" y2="82" marker-end="url(#af3)"/>
    <line x1="384" y1="76" x2="432" y2="76" marker-end="url(#af3)"/>
    <line x1="519" y1="96" x2="519" y2="148" marker-end="url(#af3)"/>
  </g>
  <g fill="currentColor">
    <text x="89" y="40" text-anchor="middle" font-size="13">ProductSystem</text>
    <text x="89" y="120" text-anchor="middle" font-size="13">ImpactMethod</text>
    <text x="14" y="154" font-size="10" opacity="0.7">→ ImpactCategory → ImpactFactor (per Flow)</text>
    <text x="299" y="80" text-anchor="middle" font-size="13">CalculationSetup</text>
    <text x="519" y="80" text-anchor="middle" font-size="13">SystemCalculator</text>
    <text x="519" y="174" text-anchor="middle" font-size="13">LcaResult</text>
    <text x="519" y="208" text-anchor="middle" font-size="10" opacity="0.7">total impacts · inventory · contributions</text>
    <text x="172" y="46" font-size="10" opacity="0.85">system</text>
    <text x="168" y="104" font-size="10" opacity="0.85">withImpactMethod</text>
    <text x="388" y="70" font-size="10" opacity="0.85">calculate()</text>
    <text x="527" y="126" font-size="10" opacity="0.85">returns</text>
  </g>
</svg>

_A `ProductSystem` and an `ImpactMethod` feed a `CalculationSetup`; `SystemCalculator` runs it and
returns an `LcaResult`._

- [Simple calculation](simple.md)
- [Parameter redefinitions](parameter_redefinitions.md)
- [Sensitivity analysis](sensitivity_analysis.md)
- [Parameter redefinition sets](parameter_redefinition_sets.md)
- [Normalization and weighting sets](nw_sets.md)
- [Extended calculation setup](calculation_setup.md)
- [Advanced](advanced/README.md)
