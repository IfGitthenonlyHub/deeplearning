import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIGogaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIGMgPSBsaXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIGluZGV4ID0gWzBdKm4KICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgIGluZGV4W2NbaV0tMV09aQogICAgbWEgPSAwCiAgICBtaSA9IG4KICAgIGFucyA9IFsnMCddKm4KICAgICMgcHJpbnQoaW5kZXgpCiAgICBmb3IgayBpbiByYW5nZShuKToKICAgICAgICBtYSA9IG1heChpbmRleFtrXSxtYSkKICAgICAgICBtaSA9IG1pbihpbmRleFtrXSxtaSkKICAgICAgICAjcHJpbnQoayxtcixpbmRleFtrXS1pbmRleFswXSkKICAgICAgICBpZiBtYS1taTw9azoKICAgICAgICAgICAgYW5zW2tdPScxJwogICAgcHJpbnQoJycuam9pbihhbnMpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
