// Automated accessibility check for every page in examples/.
// Runs axe-core (WCAG 2.0, 2.1 and 2.2, levels A and AA) in Chromium, in light
// and dark themes, at desktop (1280px) and phone (375px) widths, and fails if a
// page scrolls sideways. Usage: npm test (or node tests/a11y.mjs).
// Automated checks find only some problems: keyboard and screen reader checks
// by hand are still needed (see README).

import { readdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { chromium } from 'playwright';

const require = createRequire(import.meta.url);
const axeSource = readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const pages = readdirSync(join(root, 'examples')).filter((f) => f.endsWith('.html')).sort();
const tags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'];
const viewports = [
  { name: 'desktop', width: 1280, height: 900 },
  { name: 'phone', width: 375, height: 800 },
];

const browser = await chromium.launch();
let failures = 0;

for (const page of pages) {
  for (const colorScheme of ['light', 'dark']) {
    for (const vp of viewports) {
      const tab = await browser.newPage({ viewport: { width: vp.width, height: vp.height }, colorScheme });
      const errors = [];
      tab.on('pageerror', (e) => errors.push(e.message));
      await tab.goto(pathToFileURL(join(root, 'examples', page)).href);
      await tab.addScriptTag({ content: axeSource });
      const result = await tab.evaluate((runTags) => window.axe.run(document, { runOnly: { type: 'tag', values: runTags } }), tags);
      const overflow = await tab.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      const label = `${page} ${colorScheme} ${vp.name}`;
      const problems = [];
      for (const v of result.violations) {
        problems.push(`${v.id} (${v.impact}): ${v.help}`);
        for (const node of v.nodes.slice(0, 3)) problems.push(`    ${node.target.join(' ')}`);
      }
      if (overflow > 0) problems.push(`page scrolls sideways by ${overflow}px`);
      for (const e of errors) problems.push(`script error: ${e}`);
      if (problems.length) {
        failures += 1;
        console.log(`FAIL ${label}\n  ${problems.join('\n  ')}`);
      } else {
        console.log(`pass ${label} (${result.passes.length} rules passed, ${result.incomplete.length} need a manual check)`);
      }
      await tab.close();
    }
  }
}

await browser.close();
console.log(`\n${pages.length} page(s) x 2 themes x 2 widths; ${failures} failing run(s).`);
process.exit(failures ? 1 : 0);
