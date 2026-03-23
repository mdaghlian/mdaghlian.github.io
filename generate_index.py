import os

files = sorted(os.listdir("ctx_files"))

links = "\n".join(
    f'    <li><a href="ctx_files/{f}">{f}</a></li>'
    for f in files
    if not f.startswith(".")  # skip hidden files
)

html = f"""<html>
<body>
  <h1>Marcus Daghlian GitHub Pages</h1>
  <p>Welcome to my website!</p>
  <h1>Files in ctx_files</h1>
  <ul>
{links}
  </ul>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)

print("index.html updated!")