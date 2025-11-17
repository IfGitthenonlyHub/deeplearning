import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG51bURlY29kaW5ncyhzZWxmLCBzKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgaWYgbm90IHM6IHJldHVybiAwCiAgICAgICAgIGNpcGhlciA9IGRpY3QoKHN0cihrKzEpLHYpIGZvciBrLHYgaW4KICAgICAgICAgICAgICAgICAgICAgICBlbnVtZXJhdGUoImFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6IikpCiAgICAgICAgICMgZnVuaGFzaCA9IGRpY3QoKHN0cihrKSwxKSBmb3Igayx2IGluIGNpcGhlci5pdGVtcygpKQogICAgICAgICBmdW5oYXNoID0geyIiOjF9CiAgICAgICAgIGRlZiBoZWxwUmVjKHMpOgogICAgICAgICAgICAgaWYgcyBpbiBmdW5oYXNoOiByZXR1cm4gZnVuaGFzaFtzXQogICAgICAgICAgICAgcjEgPSAwCiAgICAgICAgICAgICBpZiBzWzBdIGluIGNpcGhlcjoKICAgICAgICAgICAgICAgICByMSA9IGhlbHBSZWMoc1sxOl0pCiAgICAgICAgICAgICByMiA9IDAKICAgICAgICAgICAgIGlmIGxlbihzKSA+PSAyIGFuZCBzWzoyXSBpbiBjaXBoZXI6CiAgICAgICAgICAgICAgICAgcjIgPSBoZWxwUmVjKHNbMjpdKQogICAgICAgICAgICAgcnZhbCA9IHIxICsgcjIKICAgICAgICAgICAgIGZ1bmhhc2hbc10gPSBydmFsCiAgICAgICAgICAgICAjIHByaW50KHMscnZhbCkKICAgICAgICAgICAgIHJldHVybiBydmFsCiAgICAgICAgIHJldHVybiBoZWxwUmVjKHMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
