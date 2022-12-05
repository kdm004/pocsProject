from fuzzywuzzy import fuzz
from fuzzywuzzy import process



iran = fuzz.ratio("bosnia Herzegovina", "bosnia herz")
print(iran)