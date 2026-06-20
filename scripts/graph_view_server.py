#!/usr/bin/env python3
"""Realtime knowledge-graph view (stdlib only)."""
import base64
import hashlib
import struct

_WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def ws_accept(key):
    """RFC6455 Sec-WebSocket-Accept for a client's Sec-WebSocket-Key."""
    digest = hashlib.sha1((key + _WS_GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode("ascii")


def ws_frame(text):
    """A single unmasked FIN+text WebSocket frame carrying a UTF-8 string."""
    payload = text.encode("utf-8")
    n = len(payload)
    header = bytearray([0x81])
    if n < 126:
        header.append(n)
    elif n < 65536:
        header.append(126)
        header += struct.pack(">H", n)
    else:
        header.append(127)
        header += struct.pack(">Q", n)
    return bytes(header) + payload
