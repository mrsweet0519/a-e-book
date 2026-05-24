import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const inputPath = path.resolve(__dirname, 'index.html');
const outputFileName = '\uc720\ud29c\ube0c\uc74c\uc545\ucc44\ub110_\uc218\uc775\ud654\uac00\uc774\ub4dc_2026_\ud06c\ubabd\ud310\ub9e4\uc6a9_\ucd5c\uc885\ubcf8_v2.pdf';
const outputPath = path.resolve(__dirname, '..', outputFileName);

let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch (e) {
  console.log('Playwright is missing. Installing local dependency...');
  execSync('npm install', { stdio: 'inherit', cwd: __dirname });
  ({ chromium } = await import('playwright'));
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  await page.goto(pathToFileURL(inputPath).href, { waitUntil: 'networkidle' });
  
  await page.waitForSelector('.cover-wrapper');
  await page.waitForFunction(
    () => Array.from(document.images).every((img) => img.complete && img.naturalWidth > 0),
    null,
    { timeout: 30000 }
  );
  await page.evaluate(() => document.fonts && document.fonts.ready);

  const brokenImages = await page.$$eval('img', (imgs) =>
    imgs
      .filter((img) => !img.complete || img.naturalWidth === 0)
      .map((img) => img.getAttribute('src'))
  );
  if (brokenImages.length > 0) {
    throw new Error(`Broken image references: ${brokenImages.join(', ')}`);
  }
  
  await page.pdf({
    path: outputPath,
    format: 'A4',
    preferCSSPageSize: true,
    printBackground: true,
    displayHeaderFooter: false
  });

  await browser.close();
  console.log(`PDF created: ${outputPath}`);
})();
