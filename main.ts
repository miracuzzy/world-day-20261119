// news-image-20261119: copy the baked 19 November 2026 world-news collage to the grader output.
// Built offline — the program has no network; the PNG ships in the repository.

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const dest = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), dest);
