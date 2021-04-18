# My take on a filtob replacement

## How config.json works

strictLevel determines if the swear detection is more strict or not (0 is low, 1 is high)<br/>
strictLevel 0 ignores all words from the modified word dictionary (such as "penistone" or multiple words like "fish it") and the words in the false positive list (like "gayfish")<br/>
strictLevel 1 detects all swear words even if they're inside words or false positives ("gayfish" becomes "bonkfish", "penistone" becomes "bonktone", etc)<br/>
<br/>
falsePositives obviously contains all false positives<br/>
the same goes for filteredWords<br/>
<br/>
similarChars contains all characters that the filter replaces for their actual character.<br/>
For example, "o":"0Ȫ" means that the filter will replace any 0 and Ȫ that the sentence might have with an "o" to then check for any swear words.<br/>


## The word dictionary
The word dictionary contains all english words except for the ones that derive from a swear word. If a new swear word is added into filteredWords, you need to remove any ocurrences of that swear word in the word dictionary, or else these would get considered as english words and be ignored.