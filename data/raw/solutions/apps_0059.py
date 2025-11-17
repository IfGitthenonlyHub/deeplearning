import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4gPSBpbnQoaW5wdXQoKSkKICAgIGFucyA9IDAKICAgIGFkaiA9IFtdCiAgICBhID0gdHVwbGUobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKICAgIGExID0gaXRlcihhKQogICAgbmV4dChhMSkKICAgIGZvciBhaSwgYWogaW4gemlwKGEsIGExKToKICAgICAgICBpZiBhaSA+IC0xIDwgYWo6CiAgICAgICAgICAgIGFucyA9IG1heChhbnMsIGFicyhhaSAtIGFqKSkKICAgICAgICBlbGlmIGFpICE9IGFqOgogICAgICAgICAgICBhZGouYXBwZW5kKGFpICsgYWogKyAxKQogICAgbWluX2FkaiwgbWF4X2FkaiA9IChtaW4oYWRqKSwgbWF4KGFkaikpIGlmIGFkaiBlbHNlICgwLCAwKQogICAgcHJpbnQobWF4KGFucywgKG1heF9hZGogLSBtaW5fYWRqICsgMSkgLy8gMiksIChtaW5fYWRqICsgbWF4X2FkaikgLy8gMik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
