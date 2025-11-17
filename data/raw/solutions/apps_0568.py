import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dGVzdD1pbnQoaW5wdXQoKSkKZm9yIHQgaW4gcmFuZ2UodGVzdCk6CiBuPSBpbnQoaW5wdXQoKSkKCiBhZGo9W1tdIGZvciBpIGluIHJhbmdlKG4rMSldCgogZm9yIF8gaW4gcmFuZ2Uobi0xKToKICBhLGI9bGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpCiAgYWRqW2FdLmFwcGVuZChiKQogIGFkaltiXS5hcHBlbmQoYSkKIAoKICNwcmludChhZGopCiByb290PTEKIHEscz1bcm9vdF0sc2V0KFtyb290XSkKCiBmb3IgeCBpbiBxOgogIGFkalt4XT0gW3AgZm9yIHAgaW4gYWRqW3hdIGlmIHAgbm90IGluIHNdCiAgcS5leHRlbmQoYWRqW3hdKQogIHMudXBkYXRlKGFkalt4XSkKCiAjcHJpbnQoYWRqKQogYW5zPVRydWUKIGZvciBpIGluIHJhbmdlKG4rMSk6CiAgaWYobGVuKGFkaltpXSkgJTMhPTApOgogICBhbnM9RmFsc2UKIGlmKGFucyk6CiAgcHJpbnQoIllFUyIpCiAgZm9yIGkgaW4gcmFuZ2UobisxKToKICAgd2hpbGUobGVuKGFkaltpXSkpOgogICAgcHJpbnQoaSxhZGpbaV1bMF0sYWRqW2ldWzFdLGFkaltpXVsyXSkKICAgIGFkaltpXS5wb3AoMCkKICAgIGFkaltpXS5wb3AoMCkKICAgIGFkaltpXS5wb3AoMCkKIGVsc2U6CiAgcHJpbnQoIk5PIik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
