import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgIGRlZiBldmFsUlBOKHNlbGYsIHRva2Vucyk6CiAgICAgIiIiCiAgICAgOnR5cGUgdG9rZW5zOiBMaXN0W3N0cl0KICAgICA6cnR5cGU6IGludAogICAgICIiIgogICAgIHMgPSBbXQogICAgIGZvciB0b2tlbiBpbiB0b2tlbnM6CiAgICAgICBpZiB0b2tlbiA9PSAiKyI6CiAgICAgICAgIGEgPSBpbnQocy5wb3AoKSkKICAgICAgICAgYiA9IGludChzLnBvcCgpKQogICAgICAgICBzLmFwcGVuZChhK2IpCiAgICAgICBlbGlmIHRva2VuID09ICIvIjoKICAgICAgICAgYSA9IGludChzLnBvcCgpKQogICAgICAgICBiID0gaW50KHMucG9wKCkpCiAgICAgICAgIHMuYXBwZW5kKGIvYSkKICAgICAgIGVsaWYgdG9rZW4gPT0gIioiOgogICAgICAgICBhID0gaW50KHMucG9wKCkpCiAgICAgICAgIGIgPSBpbnQocy5wb3AoKSkKICAgICAgICAgcy5hcHBlbmQoYSpiKQogICAgICAgZWxpZiB0b2tlbiA9PSAiLSI6CiAgICAgICAgIGEgPSBpbnQocy5wb3AoKSkKICAgICAgICAgYiA9IGludChzLnBvcCgpKQogICAgICAgICBzLmFwcGVuZChiLWEpCiAgICAgICBlbHNlOgogICAgICAgICBzLmFwcGVuZCh0b2tlbikKICAgICBpZiBsZW4ocykgaXMgbm90IDE6CiAgICAgICByZXR1cm4gRmFsc2UKICAgICBlbHNlOgogICAgICAgcmV0dXJuIGludChzLnBvcCgpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
