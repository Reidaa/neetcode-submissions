class Solution:
    delimiter = "@"

    def encode(self, strs: List[str]) -> str:
        def numberToPaddedStr(n: int, length: int = 3):
            return str(n).rjust(length, "0")

        encoded = f"{numberToPaddedStr(len(strs))}{self.delimiter}"

        for sub in strs:
            encoded += f"{numberToPaddedStr(len(sub))}{self.delimiter}{sub}"

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        def getNextDelimiterIndex(s: str, start: int, delimiter: str):
            n = start

            while s[n] != delimiter:
                n += 1

            return n
        
        decoded = []
        to_cast_to_int = ""

        i = 0
        to_cast_to_int = s[i:getNextDelimiterIndex(s, i, self.delimiter)]
        wordNumber = int(to_cast_to_int)
        i += len(to_cast_to_int) + len(self.delimiter)

        for _ in range(0, wordNumber):
            to_cast_to_int = s[i:getNextDelimiterIndex(s, i, self.delimiter)]
            wordLen = int(to_cast_to_int)
            i += len(to_cast_to_int) + len(self.delimiter)
            decoded.append(s[i:i+wordLen])
            i += wordLen

        print(decoded)
        return decoded

