import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIG1haW4oKToKICAgIGgsIHYgPSBodiA9IChbMF0sIFswXSkKICAgIGYgPSB7J1cnOiAodiwgLTEpLCAnUyc6ICh2LCAxKSwgJ0EnOiAoaCwgLTEpLCAnRCc6IChoLCAxKX0uZ2V0CiAgICBmb3IgXyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogICAgICAgIGRlbCBoWzE6XSwgdlsxOl0KICAgICAgICBmb3IgbCwgZCBpbiBtYXAoZiwgaW5wdXQoKSk6CiAgICAgICAgICAgIGwuYXBwZW5kKGxbLTFdICsgZCkKICAgICAgICB4ID0geSA9IDEKICAgICAgICBmb3IgbCBpbiBodjoKICAgICAgICAgICAgbGgsIGEsIG4gPSAobWluKGwpLCBtYXgobCkpLCAyMDAwMDEsIDAKICAgICAgICAgICAgZm9yIGIgaW4gZmlsdGVyKGxoLl9fY29udGFpbnNfXywgbCk6CiAgICAgICAgICAgICAgICBpZiBhICE9IGI6CiAgICAgICAgICAgICAgICAgICAgYSA9IGIKICAgICAgICAgICAgICAgICAgICBuICs9IDEKICAgICAgICAgICAgbGUgPSBsaFsxXSAtIGxoWzBdICsgMQogICAgICAgICAgICB4LCB5ID0geSAqIGxlLCB4ICogKGxlIC0gKG4gPCAzIDw9IGxlKSkKICAgICAgICBwcmludCh4IGlmIHggPCB5IGVsc2UgeSkKCgpkZWYgX19zdGFydGluZ19wb2ludCgpOgogICAgbWFpbigpCgpfX3N0YXJ0aW5nX3BvaW50KCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
