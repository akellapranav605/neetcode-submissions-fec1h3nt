class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            length = str(len(s))
            encoded_str += length+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        print(s)
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + length+1
        return res