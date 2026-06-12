class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for txt in s:
            if not txt in sdict:
                sdict[txt] = 1
            else:
                sdict[txt] += 1
        for txt in t:
            if txt not in tdict:
                tdict[txt] = 1
            else:
                tdict[txt] += 1
        if len(s) > len(t): 
            for key, value in sdict.items():
                if key in tdict and tdict[key] == value:
                    pass
                elif not key in tdict:
                    return False
                elif tdict[key] != value:
                    return False
        else:
            for key, value in tdict.items():
                if key in sdict and sdict[key] == value:
                    pass
                elif not key in sdict:
                    return False
                elif sdict[key] != value:
                    return False
        return True
