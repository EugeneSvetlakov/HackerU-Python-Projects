"""
This type stub file was generated by pyright.
"""

from scapy.compat import Any, Callable, Optional

"""
Color themes for the interactive console.
"""
class ColorTable:
    colors = ...
    inv_map = ...
    def __repr__(self): # -> Literal['<ColorTable>']:
        ...
    
    def __getattr__(self, attr): # -> str:
        ...
    
    def ansi_to_pygments(self, x: str) -> str:
        ...
    


Color = ...
def create_styler(fmt: Optional[Any] = ..., before: str = ..., after: str = ..., fmt2: str = ...) -> Callable:
    ...

class ColorTheme:
    def __repr__(self) -> str:
        ...
    
    def __reduce__(self): # -> tuple[Type[Self@ColorTheme], tuple[()], tuple[()]]:
        ...
    
    def __getattr__(self, attr: str) -> Callable:
        ...
    
    def format(self, string, fmt): # -> Any:
        ...
    


class NoTheme(ColorTheme):
    ...


class AnsiColorTheme(ColorTheme):
    def __getattr__(self, attr: str) -> Callable:
        ...
    
    style_normal = ...
    style_prompt = ...
    style_punct = ...
    style_id = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_odd = ...
    style_even = ...
    style_opening = ...
    style_active = ...
    style_closed = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class BlackAndWhite(AnsiColorTheme, NoTheme):
    ...


class DefaultTheme(AnsiColorTheme):
    style_normal = ...
    style_prompt = ...
    style_punct = ...
    style_id = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_opening = ...
    style_active = ...
    style_closed = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class BrightTheme(AnsiColorTheme):
    style_normal = ...
    style_punct = ...
    style_id = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class RastaTheme(AnsiColorTheme):
    style_normal = ...
    style_prompt = ...
    style_punct = ...
    style_id = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class ColorOnBlackTheme(AnsiColorTheme):
    """Color theme for black backgrounds"""
    style_normal = ...
    style_prompt = ...
    style_punct = ...
    style_id = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_opening = ...
    style_active = ...
    style_closed = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class FormatTheme(ColorTheme):
    def __getattr__(self, attr: str) -> Callable:
        ...
    


class LatexTheme(FormatTheme):
    style_prompt = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class LatexTheme2(FormatTheme):
    style_prompt = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_left = ...
    style_right = ...
    style_logo = ...


class HTMLTheme(FormatTheme):
    style_prompt = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_left = ...
    style_right = ...


class HTMLTheme2(HTMLTheme):
    style_prompt = ...
    style_not_printable = ...
    style_layer_name = ...
    style_field_name = ...
    style_field_value = ...
    style_emph_field_name = ...
    style_emph_field_value = ...
    style_packetlist_name = ...
    style_packetlist_proto = ...
    style_packetlist_value = ...
    style_fail = ...
    style_success = ...
    style_even = ...
    style_odd = ...
    style_left = ...
    style_right = ...


def apply_ipython_style(shell: Any) -> None:
    """Updates the specified IPython console shell with
    the conf.color_theme scapy theme."""
    ...
