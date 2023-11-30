import pandas as pd 
from scipy.stats import fisher_exact
import numpy as np 
import os 
from itertools import chain


from utils import get_combinations


def remove_dup(list_of_dicts):
    unique_dicts_set = {frozenset(d.items()) for d in list_of_dicts}
    unique_dicts = [dict(s) for s in unique_dicts_set] 
    return unique_dicts

def get_n00(s1,s2,t):
    union_set = {frozenset(d.items()) for d in s1} | {frozenset(d.items()) for d in s2}
    return len(t)-len(union_set)


def get_nud(s1,s2):

    list_of_dicts = []

    for s1s in s1:
        c1,e1 = next(iter(s1s.items()))
        if (e1 == "Up-regulated"):
            list_of_dicts.append(s1s)

    for s2s in s2:
        c2,e2 = next(iter(s2s.items()))
        if (e2 == "down-regulated"):
            list_of_dicts.append(s2s)

    return (len(remove_dup(list_of_dicts)))

def get_ndu(s1,s2):
    list_of_dicts = []

    for s1s in s1:
        c1,e1 = next(iter(s1s.items()))
        if (e1 == "down-regulated"):
            list_of_dicts.append(s1s)


    for s2s in s2:
        c2,e2 = next(iter(s2s.items()))
        if (e2 == "Up-regulated"):
            list_of_dicts.append(s2s)

    return (len(remove_dup(list_of_dicts)))


def get_uudd(s1,s2):
    pairs_list_1 = [list(d.items())[0] for d in s1]
    pairs_list_2 = [list(d.items())[0] for d in s2]
    total_matches = sum(pair in pairs_list_2 for pair in pairs_list_1)

    return total_matches

def get_n(s1,s2,df, total):

    s1_con = df.at[s1,'condition_exp']
    s2_con = df.at[s2,'condition_exp']

    s1_con = remove_dup(s1_con)
    s2_con = remove_dup(s2_con)
    total = remove_dup(total)

    n_00 = get_n00(s1_con,s2_con,total) 
    n_ud = get_nud(s1_con,s2_con)
    n_du = get_ndu(s1_con,s2_con)
    n_uudd = get_uudd(s1_con,s2_con)
    
    data = np.array([[n_00,n_ud],[n_du,n_uudd]])
    _ ,p_value = fisher_exact(data, alternative = 'greater')
    
    return n_00, n_ud, n_du, n_uudd, p_value

def generate_matrix_dif(df, CUT_OFF):
    

    df = df.groupby('mapped_phosphosite').agg(pd.Series.tolist).reset_index()
    df['count'] = df["exp_condition"].apply(lambda x:len(x))

    df['up_count'] = df["expression"].apply(lambda x:x.count("Up-regulated"))
    df['down_count'] = df["expression"].apply(lambda x:x.count("down-regulated")) 

    df = df.sort_values(by=['count'], ascending=False)

    df = df.loc[df['count'] >= CUT_OFF]
    
    all_sites = df['mapped_phosphosite'].reset_index()

    df['condition_exp'] = df.apply(lambda x:dict(zip(x["exp_condition"],x["expression"])), axis = 1)

    df = df[['mapped_phosphosite','condition_exp']]

    df["condition_exp"] = df["condition_exp"].apply(lambda x:[ {k:v} for k,v in x.items()])

    total_ex = df["condition_exp"].tolist()

    total_ex = list(chain.from_iterable(total_ex))

    df.set_index("mapped_phosphosite", inplace = True)

    df_comb = get_combinations(all_sites)

    result = df_comb.apply(lambda x:get_n(x['site1'],x['site2'], df , total_ex), axis = 1)


    df_comb[['n_00','n_ud','n_du','n_uudd','p-Value']] = pd.DataFrame(result.tolist())

    df_comb.drop_duplicates(inplace=True)

    df_comb.sort_values(by=['p-Value'], inplace=True)

    return df_comb
