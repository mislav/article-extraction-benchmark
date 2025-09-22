#!/usr/bin/env python3
import gzip
import json
import subprocess
import sys
from pathlib import Path
from tempfile import mkstemp


def main():
    output = {}
    for path in Path('html').glob('*.html.gz'):
        item_id = path.stem.split('.')[0]

        with gzip.open(path, 'rt', encoding='utf8') as f:
            html = f.read()
        
        # get extracted content from Readability.js
        result = subprocess.run(
            ["node", "cli.js"],
            input=html,
            cwd=Path(__file__).parent / "readability_js",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(f"Error processing {path}: {result.stderr}", file=sys.stderr)
            continue

        output[item_id] = {'articleBody': result.stdout}
    (Path('output') / 'readability_js.json').write_text(
        json.dumps(output, sort_keys=True, ensure_ascii=False, indent=4),
        encoding='utf8')


if __name__ == '__main__':
    main()
