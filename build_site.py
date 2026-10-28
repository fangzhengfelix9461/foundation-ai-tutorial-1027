from pathlib import Path
import hashlib,json,shutil
root=Path(__file__).parent
dest=root/'_site'
dest.mkdir(exist_ok=True)
for name in ['index.html','style.css','reader.js','.nojekyll','coverage.json','source-manifest.json']:
    shutil.copyfile(root/name,dest/name)
shutil.copytree(root/'assets',dest/'assets',dirs_exist_ok=True)
manifest=json.loads((root/'pdf-parts'/'manifest.json').read_text())
data=b''.join((root/'pdf-parts'/name).read_bytes() for name in manifest['parts'])
assert hashlib.sha256(data).hexdigest()==manifest['sha256'], 'PDF integrity mismatch'
(dest/'source.pdf').write_bytes(data)
print('Verified original PDF:',len(data),'bytes;',manifest['sha256'])
