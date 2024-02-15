import pandas as pd

from utils import (get_query, get_d , generate_matrix , getCDF , trypsin_digest, 
                   get_query_d)

from utils_diff import (generate_matrix_dif)

from myplot import get_plot
kianase = 'TAOK1'
CUT_OFF = 0

# ==========================PROFILING=============================

q = get_query(kianase)
df = get_d(q)
df = generate_matrix(df , CUT_OFF )
df = getCDF(df)
# df = trypsin_digest(df)
# get_plot(dfs['p-Value'], df['CDF'], kianase,"profiling")
df.to_excel(f"OUTPUT/{kianase}_profiling.xlsx", index=False)

# ==========================DIFFERENTIAL-up=======================

# q = get_query_d(kianase , "differential")
# df = get_d(q)
# df = generate_matrix_dif(df , CUT_OFF )
# df = getCDF(df)
# # df = trypsin_digest(df)
# # get_plot(df['p-Value'], df['CDF'], kianase,"differential")
# df.to_excel(f"{kianase}_uudd.xlsx", index=False)
 
# df.to_excel(f"{kianase}_uddu.xlsx", index=False)
