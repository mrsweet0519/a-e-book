import { chromium } from "../ebook/node_modules/playwright/index.mjs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(directory, "detail_page.html");
const htmlUrl = pathToFileURL(htmlPath).href;

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({
  viewport: { width: 1000, height: 2200 },
  deviceScaleFactor: 1,
});

await page.goto(htmlUrl, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);

const panels = page.locator(".detail-panel");
const count = await panels.count();

for (let index = 0; index < count; index += 1) {
  const panel = panels.nth(index);
  const fileName = await panel.getAttribute("data-file");
  if (!fileName) {
    continue;
  }

  const outputPath = path.join(directory, fileName);
  await panel.screenshot({
    path: outputPath,
    animations: "disabled",
    caret: "hide",
  });

  const box = await panel.boundingBox();
  const width = Math.round(box?.width ?? 0);
  const height = Math.round(box?.height ?? 0);
  console.log(`${fileName} ${width}x${height}`);
}

await browser.close();
