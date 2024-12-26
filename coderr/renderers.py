from rest_framework.renderers import JSONRenderer
import json
from decimal import Decimal

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        def format_value(value):
            if isinstance(value, Decimal):
                return float(f"{value:.2f}")
            if isinstance(value, dict):
                return {key: format_value(val) for key, val in value.items()}
            if isinstance(value, list):
                return [format_value(item) for item in value]
            return value

        data = format_value(data)
        return super().render(data, accepted_media_type, renderer_context)
