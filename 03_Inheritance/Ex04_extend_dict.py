from __future__ import annotations
from typing import Optional

class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        """In effect, max(self, key=len), but less obscure"""
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest
    

if __name__ == "__main__":
    articles_read = LongNameDict()
    articles_read['lucy'] = 42
    articles_read['c_c_phillips'] = 6
    articles_read['steve'] = 7
    print(articles_read.longest_key())

    print(max(articles_read, key=len))

