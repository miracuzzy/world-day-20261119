// news-image-20261119 — ship the 19 November 2026 world-news collage to the grader.
// Offline only: no network; entry.png is baked beside this file.

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';

const dest = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
mkdirSync(dirname(dest), { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), dest);
