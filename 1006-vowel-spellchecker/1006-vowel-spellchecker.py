class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels_set = {"a", "e", "i", "o", "u"}

        def replace_vowels(s):

            out_str = ""
            for ch in s:
                if ch in vowels_set:
                    out_str += "#"
                else:
                    out_str += ch

            return out_str
        
        wordlist_set = set(wordlist)

        wordlist_lower_dict = dict()
        for word in wordlist:
            
            if(word.lower() not in wordlist_lower_dict):
                wordlist_lower_dict[word.lower()] = word
        
        wordlist_replace_dict = dict()
        for lower, original in wordlist_lower_dict.items():

            replaced = replace_vowels(lower)

            if(replaced not in wordlist_replace_dict):
                wordlist_replace_dict[replaced] = original
        
        ans = []
        for query in queries:

            if(query in wordlist_set):
                ans.append(query)
            
            else:
                query_lower = query.lower()
                if(query_lower in wordlist_lower_dict):
                    ans.append(wordlist_lower_dict[query_lower])
                
                else:
                    replaced = replace_vowels(query_lower)
                    
                    if(replaced in wordlist_replace_dict):
                        ans.append(wordlist_replace_dict[replaced])
                
                    else:
                        ans.append("")
                        
        return ans     