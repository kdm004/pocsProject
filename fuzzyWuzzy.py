from fuzzywuzzy import fuzz
from fuzzywuzzy import process



ratio = fuzz.token_set_ratio("DougBookwriter2", "Andorran")
print(ratio)



