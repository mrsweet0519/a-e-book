import { chromium } from "../ebook/node_modules/playwright/index.mjs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const directory = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(directory, "main_thumbnail.html");
const outputPath = path.join(directory, "..", "kmong_main_652x488.png");

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({
  viewport: { width: 652, height: 488 },
  deviceScaleFactor: 1,
});

await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);
await page.locator(".thumbnail").screenshot({
  path: outputPath,
  animations: "disabled",
  caret: "hide",
});

console.log(`kmong_main_652x488.png 652x488`);
await browser.close();
