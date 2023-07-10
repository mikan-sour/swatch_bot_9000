const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/index.ts'],
  outfile: 'dist/index.js',
  platform: 'node',
  target: 'ES2020',
  bundle: true,
  sourcemap: true,
}).catch(() => process.exit(1));