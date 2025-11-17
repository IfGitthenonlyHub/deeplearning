import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGJmcyhzLHQsYik6CiAgICBxLHY9W3NdLHtzfQogICAgd2hpbGUgbGVuKHEpPjA6CiAgICAgICAgaSxqPXEucG9wKDApCiAgICAgICAgaWYgKGksaik9PXQ6cmV0dXJuIFRydWUKICAgICAgICBpZiBpIGluIChzWzBdKzIxMCxzWzBdLTIxMCkgb3IgaiBpbiAoc1sxXSsyMTAsc1sxXS0yMTApOnJldHVybiBUcnVlCiAgICAgICAgZm9yIGQsZSBpbiAoKGkrMSxqKSwoaSxqKzEpLChpLTEsaiksKGksai0xKSk6CiAgICAgICAgICAgIGlmIGQ+PTAgYW5kIGQ8MTAqKjYgYW5kIGU+PTAgYW5kIGU8MTAqKjYgYW5kIChkLGUpIG5vdCBpbiB2IGFuZCAoZCxlKSBub3QgaW4gYjoKICAgICAgICAgICAgICAgIHYuYWRkKChkLGUpKQogICAgICAgICAgICAgICAgcS5hcHBlbmQoKGQsZSkpCiAgICByZXR1cm4gRmFsc2UKY2xhc3MgU29sdXRpb246CiAgICBkZWYgaXNFc2NhcGVQb3NzaWJsZShzZWxmLCBiOiBMaXN0W0xpc3RbaW50XV0sIHM6IExpc3RbaW50XSwgdDogTGlzdFtpbnRdKSAtPiBib29sOgogICAgICAgIGI9c2V0KHR1cGxlKGkpIGZvciBpIGluIGIpCiAgICAgICAgcmV0dXJuIGJmcyh0dXBsZShzKSx0dXBsZSh0KSxiKSBhbmQgYmZzKHR1cGxlKHQpLHR1cGxlKHMpLGIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
