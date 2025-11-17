import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc2hvcnRlc3RDb21tb25TdXBlcnNlcXVlbmNlKHNlbGYsIHN0cjE6IHN0ciwgc3RyMjogc3RyKSAtPiBzdHI6CiAgICAgICAgbGFzdF9kcCA9IFtzdHIyWzpqXSBmb3IgaiBpbiByYW5nZShsZW4oc3RyMikgKyAxKV0KICAgICAgICAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBsZW4oc3RyMSkgKyAxKToKICAgICAgICAgICAgZHAgPSBbc3RyMVs6aV1dCiAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKDEsIGxlbihzdHIyKSArIDEpOgogICAgICAgICAgICAgICAgaWYgc3RyMVtpIC0gMV0gPT0gc3RyMltqIC0gMV06CiAgICAgICAgICAgICAgICAgICAgZHAuYXBwZW5kKGxhc3RfZHBbaiAtIDFdICsgc3RyMVtpIC0gMV0pCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGlmIGxlbihsYXN0X2RwW2pdKSA8IGxlbihkcFtqIC0gMV0pOgogICAgICAgICAgICAgICAgICAgICAgICBkcC5hcHBlbmQobGFzdF9kcFtqXSArIHN0cjFbaSAtIDFdKQogICAgICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgICAgIGRwLmFwcGVuZChkcFtqIC0gMV0gKyBzdHIyW2ogLSAxXSkKICAgICAgICAgICAgbGFzdF9kcCA9IGRwCiAgICAgICAgICAgIAogICAgICAgIHJldHVybiBsYXN0X2RwWy0xXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
