import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IHN0ZGluLHN0ZGVycgpkZWYgcmwoKToKICAgIHJldHVybiBbaW50KHcpIGZvciB3IGluIHN0ZGluLnJlYWRsaW5lKCkuc3BsaXQoKV0KCmRlZiBwMShuLCBzLCBsZSk6CiAgICByID0gW10KICAgIGIgPSBpID0gMAogICAgd2hpbGUgaSA8IG46CiAgICAgICAgdHJ5OgogICAgICAgICAgICBuaSA9IHMuaW5kZXgobGUsIGkpICsgMQogICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgICAgICBuaSA9IG4KICAgICAgICByICs9IGxpc3QocmFuZ2UobmksIGksIC0xKSkKICAgICAgICBpID0gbmkKICAgIHJldHVybiByCgp0LCA9IHJsKCkKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBuLHMgPSBzdGRpbi5yZWFkbGluZSgpLnNwbGl0KCkKICAgIG4gPSBpbnQobikKICAgIHByaW50KCoobiAtIHggKyAxIGZvciB4IGluIHAxKG4sIHMsICc+JykpKQogICAgcHJpbnQoKnAxKG4sIHMsICc8Jykp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
