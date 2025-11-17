import re
import regex
from typing import Type

import emoji


class Reg:
    __emj: re.Pattern[str] = re.compile(
        r"^\s*[" + ("".join(emoji.EMOJI_DATA.keys())) + r"]"
    )
    __txt: regex.Pattern[str] = regex.compile(r"^[\p{L}\d\s\-'\"_.,;!?]{1,100}$")

    @classmethod
    def starts_with_emj(cls: type["Reg"], txt: str) -> bool:
        return cls.__emj.match(txt) is not None

    @classmethod
    def txt_ok(cls: Type["Reg"], arg: str) -> bool:
        return cls.__txt.match(arg) is not None
