class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = []
        
        def findPartitions(string, partition):
            if not string:
                palindromePartitions.append(partition.copy())
                return
            
            for i in range(1, len(string) + 1):
                currString = string[:i]
                nextString = string[i:]
                if Solution.isPalindrome(self, currString):
                    findPartitions(nextString, partition + [currString])
            
        findPartitions(s, [])
        return palindromePartitions                                  
        
    def isPalindrome(self, string):
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True