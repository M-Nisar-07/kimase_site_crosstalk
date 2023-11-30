import pandas as pd

from utils import (get_query, get_d , generate_matrix , getCDF , trypsin_digest, 
                   get_query_d)

from utils_diff import (generate_matrix_dif)

from myplot import get_plot
kianase = 'PAK1'
CUT_OFF = 0

# ==========================PROFILING=============================

q = get_query(kianase)
df = get_d(q)
df = generate_matrix(df , CUT_OFF )
df = getCDF(df)
df = trypsin_digest(df)
get_plot(df['p-Value'], df['CDF'], kianase,"profiling")

df.to_excel(f"{kianase}_Profiling_PTM_corss_talk_pval.xlsx", index=False)


# ==========================DIFFERENTIAL-up===========================

q = get_query_d(kianase , "Up-regulated")
df = get_d(q)
df = generate_matrix_dif(df , CUT_OFF )


df.to_excel(f"{kianase}_upreg_PTM_corss_talk_pval.xlsx", index=False)

