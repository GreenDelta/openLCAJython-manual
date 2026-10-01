# Calculate

Calculating a product system produces its life cycle inventory and impact assessment results. You can
customize the calculation according to your requirements: you can choose the allocation method, the
impact assessment method, normalization and weighting set, the calculation type (lazy, eager or Monte
Carlo simulation) or whether to include regionalized calculations, cost calculations or data quality.

_Source: [openLCA 2 manual — Calculation and Result Analysis](https://greendelta.github.io/openLCA2-manual/res_analysis/index.html)_

<svg viewBox="0 0 420 480" role="img" aria-label="A product system and an impact method feed a calculation setup; the system calculator runs it and returns an LCA result" style="max-width:420px;width:100%;height:auto;font-family:sans-serif">
  <title>The calculation pipeline</title>
  <defs>
    <marker id="af3" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="24" y="16" width="168" height="46" rx="6"/>
    <rect x="228" y="16" width="168" height="46" rx="6"/>
    <rect x="120" y="150" width="180" height="46" rx="6"/>
    <rect x="120" y="268" width="180" height="46" rx="6"/>
    <rect x="120" y="386" width="180" height="46" rx="6"/>
    <line x1="108" y1="62" x2="178" y2="148" marker-end="url(#af3)"/>
    <line x1="312" y1="62" x2="242" y2="148" marker-end="url(#af3)"/>
    <line x1="210" y1="196" x2="210" y2="266" marker-end="url(#af3)"/>
    <line x1="210" y1="314" x2="210" y2="384" marker-end="url(#af3)"/>
  </g>
  <g fill="currentColor">
    <text x="108" y="36" text-anchor="middle" font-size="13">ProductSystem</text>
    <text x="108" y="52" text-anchor="middle" font-size="9" opacity="0.7">life cycle model</text>
    <text x="312" y="34" text-anchor="middle" font-size="13">ImpactMethod</text>
    <text x="312" y="50" text-anchor="middle" font-size="9" opacity="0.7">ImpactCategory → ImpactFactor</text>
    <text x="210" y="178" text-anchor="middle" font-size="13">CalculationSetup</text>
    <text x="210" y="296" text-anchor="middle" font-size="13">SystemCalculator</text>
    <text x="210" y="414" text-anchor="middle" font-size="13">LcaResult</text>
    <text x="210" y="452" text-anchor="middle" font-size="10" opacity="0.7">total impacts · inventory · contributions</text>
    <text x="158" y="110" text-anchor="start" font-size="10" opacity="0.85">system</text>
    <text x="282" y="110" text-anchor="start" font-size="10" opacity="0.85">withImpactMethod</text>
    <text x="218" y="236" font-size="10" opacity="0.85">calculate()</text>
    <text x="218" y="354" font-size="10" opacity="0.85">returns</text>
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
