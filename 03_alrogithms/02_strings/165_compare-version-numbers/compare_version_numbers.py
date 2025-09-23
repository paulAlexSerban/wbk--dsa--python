class VersionComparator:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split version strings into lists of revision numbers (as integers)
        revs1 = [int(r) for r in version1.split('.')]
        revs2 = [int(r) for r in version2.split('.')]
        
        # Pad the shorter list with zeros at the end
        maxlen = max(len(revs1), len(revs2))
        revs1.extend([0] * (maxlen - len(revs1)))
        revs2.extend([0] * (maxlen - len(revs2)))
        
        # Compare each revision
        for a, b in zip(revs1, revs2):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0