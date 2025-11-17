import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGYoeCwgeSwgYSwgYik6IHJldHVybiB4ID4gYSBvciB5ID4gYiBvciAoYSAtIHgpICUgMyBvciAoYiAtIHkpICUgMwpkZWYgZyh4LCB5LCBhLCBiKTogcmV0dXJuIGYoeCwgeSwgYSwgYikgYW5kIGYoeCwgeSwgYiwgYSkKZm9yIGkgaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKICAgIG4sIHUsIGEsIGIgPSBtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpCiAgICB2LCBzLCB0ID0gbiAtIHUsIGEgKyBiLCAyICogYiAtIGEgaWYgYiA+IGEgZWxzZSAyICogYSAtIGIKICAgIHByaW50KCdubycgaWYgZyhzLCB0LCB1LCB2KSBhbmQgZyhzICsgYSwgcyArIGIsIHUsIHYpIGVsc2UgJ3llcycp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
