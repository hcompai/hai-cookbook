"""Image utilities."""

import base64
from io import BytesIO
from mimetypes import types_map

from PIL import Image, ImageDraw


def draw_image_with_click(image: Image.Image, x: int, y: int):
    """Draw a click on an image with absolute coordinates."""
    draw = ImageDraw.Draw(image)
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="red", outline="red")
    return image


def convert_image_to_base64_url(image: Image.Image, format: str = "JPEG") -> str:
    """Convert an image to a base64 URL.

    Args:
        image: PIL image.
        format: Image format supported by Pillow (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

    Returns:
        Base64 URL.
    """
    mime_type = _get_mime_type_from_format(format=format)
    data = _encode_image_to_base64_string(image=image, format=format)
    return f"data:{mime_type};base64,{data}"


def _get_mime_type_from_format(format: str) -> str:
    """Get the mime type associated to the PIL image format.

    Args:
        format: PIL image format.

    Returns:
        MIME type associated to the PIL image format.
    """
    for extension, mime_type in types_map.items():
        pil_format = Image.registered_extensions().get(extension)
        if format == pil_format:
            return mime_type
    raise ValueError(f"Format {format} not supported")


def _encode_image_to_base64_string(image: Image.Image, format: str, jpeg_quality: int = 90) -> str:
    """Encodes an image to a base64 string.

    Args:
        image: PIL image.
        format: Image format supported by Pillow (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
        jpeg_quality: JPEG compression quality.

    Returns:
        Base64 encoded string.
    """
    buffer = BytesIO()
    if format == "JPEG":
        image.convert("RGB").save(buffer, format=format, quality=jpeg_quality)
    else:
        image.save(buffer, format=format)
    base64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return base64_str
