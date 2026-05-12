import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const inputPath = path.resolve(__dirname, 'index.html');
const outputPath = path.resolve(__dirname, '..', '유튜브음악채널_수익화가이드_2026_최종검수_4차.pdf');

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
  
  await page.waitForSelector('.cover-image');
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
