import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const preset = require("@als-computing/colors");
const { sky, slate, finch } = preset.theme.extend.colors;
const outPath = join(dirname(fileURLToPath(import.meta.url)), "..", "tailwind", "als-tokens.css");

const lines = [
	":root {",
	`  --als-sky-darkest: ${sky.darkest};`,
	`  --als-sky-dark: ${sky.dark};`,
	`  --als-sky-mid: ${sky.base};`,
	`  --als-sky-light: ${sky.light};`,
	`  --als-slate-dark: ${slate.dark};`,
	`  --als-slate-deep: ${slate.mid};`,
	`  --als-slate-mid: ${slate.base};`,
	`  --als-slate-light: ${slate.light};`,
	`  --als-finch-border: ${finch.navy};`,
	`  --als-finch-border-hover: ${finch.cyan};`,
	`  --als-finch-surface: ${finch.white};`,
	`  --als-finch-neutral-border: ${finch["mist-hover"]};`,
	`  --als-finch-slate-blue: ${finch["slate-blue"]};`,
	`  --als-finch-sky-hover: ${finch["sky-hover"]};`,
	`  --als-finch-charcoal: ${finch.charcoal};`,
	`  --als-finch-navy-deep: ${finch["navy-hover"]};`,
	"}",
	"",
].join("\n");

writeFileSync(outPath, lines, "utf8");
