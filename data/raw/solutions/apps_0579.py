import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGNoZWNrKCk6CiAgICBwcmVmID0gWzBdKm47cHJlZlswXT1hWzBdO3N1ZmYgPSBbMF0qbjtzdWZmWy0xXT1hWy0xXQogICAgZm9yIGkgaW4gcmFuZ2UgKDEsbik6cHJlZltpXSA9IHByZWZbaS0xXXxhW2ldO3N1ZmZbbi1pLTFdID0gc3VmZltuLWldfGFbbi1pLTFdCiAgICBpZiBzdWZmWzFdPT1rOnJldHVybiAwCiAgICBlbGlmIHByZWZbbi0yXT09azpyZXR1cm4gbi0xCiAgICBlbHNlOgogICAgICAgIGZvciBpIGluIHJhbmdlICgxLG4tMSk6CiAgICAgICAgICAgIGlmIHByZWZbaS0xXXxzdWZmW2krMV0gPT0gazpyZXR1cm4gaQogICAgICAgIHJldHVybiAtMQpmb3IgeiBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogICAgbixrPVtpbnQoaSkgZm9yIGkgaW4gaW5wdXQoKS5zcGxpdCgpXTthPVtpbnQoaSkgZm9yIGkgaW4gaW5wdXQoKS5zcGxpdCgpXTthbnMsYXJyID0gW10sWzBdKm4KICAgIGZvciBpIGluIHJhbmdlIChuKToKICAgICAgICBpZiBrfGFbaV0gIT0gazphW2ldID0gYVtpLTFdfGFbKGkrMSklKG4pXTthbnMuYXBwZW5kKGkrMSk7YXJyW2ldPTEKICAgIHggPSAwO2NvdW50ID0gMAogICAgZm9yIGkgaW4gcmFuZ2UgKG4pOnh8PWFbaV0gICAgICAKICAgIGlmIHghPSBrOnByaW50KC0xKQogICAgZWxzZToKICAgICAgICB5ID0gY2hlY2soKQogICAgICAgIGlmIHkgPT0gLTE6cHJpbnQoLTEpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UgKHksbit5KToKICAgICAgICAgICAgICAgIGlmIGFycltpJW5dPT0wOmFycltpJW5dPT0xO2Fucy5hcHBlbmQoKGklbikrMSkKICAgICAgICAgICAgcHJpbnQoKmFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
