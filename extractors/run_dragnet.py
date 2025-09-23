#!/usr/bin/env python3
import gzip
import json
from pathlib import Path

# Prerequisites: numpy, Cython, libxml2 headers
#
# -e git+https://github.com/dragnet-org/dragnet.git@1b65e7b0897ca061b5c90b3eefffbfc156a0cc3b#egg=dragnet
from dragnet import extract_content


def main():
    output = {}
    for path in Path('html').glob('*.html.gz'):
        with gzip.open(path, 'rt', encoding='utf8') as f:
            html = f.read()
        item_id = path.stem.split('.')[0]
        content = extract_content(html, encoding='utf8')
        output[item_id] = {'articleBody': content}
    (Path('output') / 'dragnet.json').write_text(
        json.dumps(output, sort_keys=True, ensure_ascii=False, indent=4),
        encoding='utf8')


if __name__ == '__main__':
    main()
