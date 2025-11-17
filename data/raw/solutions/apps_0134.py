import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtRHVwRGlnaXRzQXRNb3N0TihzZWxmLCBOOiBpbnQpIC0+IGludDoKICAgICAgICBMID0gbGlzdChtYXAoaW50LCBzdHIoTiArIDEpKSkKICAgICAgICByZXMsIG4gPSAwLCBsZW4oc3RyKE4gKyAxKSkKCiAgICAgICAgZGVmIEEobSwgbik6CiAgICAgICAgICAgIHJldHVybiAxIGlmIG4gPT0gMCBlbHNlIEEobSwgbiAtIDEpICogKG0gLSBuICsgMSkKCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSwgbik6IHJlcyArPSA5ICogQSg5LCBpIC0gMSkKICAgICAgICBzID0gc2V0KCkKICAgICAgICBmb3IgaSwgeCBpbiBlbnVtZXJhdGUoTCk6CiAgICAgICAgICAgIGZvciB5IGluIHJhbmdlKDAgaWYgaSBlbHNlIDEsIHgpOgogICAgICAgICAgICAgICAgaWYgeSBub3QgaW4gczoKICAgICAgICAgICAgICAgICAgICByZXMgKz0gQSg5IC0gaSwgbiAtIGkgLSAxKQogICAgICAgICAgICBpZiB4IGluIHM6IGJyZWFrCiAgICAgICAgICAgIHMuYWRkKHgpCiAgICAgICAgcmV0dXJuIE4gLSByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
