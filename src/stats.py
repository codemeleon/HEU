"""
Python 3.6.8
Pandas 0.24.2
Numpy 1.16.2
Scypy 1.2.1
"""

from glob import glob
from os import path

import click
import numpy as np
import pandas as pd
import scipy.stats as stt


@click.command()
@click.option("-d", help="Folder containing csv files",
              type=str, default="../demo_data", show_default=True)
@click.option("-o", help="Output result file",
              type=str, default="../Results/Results.csv", show_default=True)
@click.option("-c", help="Binary Categorical variable", type=str,
              default="HIV STATUS", show_default=True)
def run(d, o, c):
    """ This sctipt is for p-value calculation based on the normality of the
    data from two different groups. If both group data are normally distributed
    based on shapiro test, ttest was used, else mannwhitneyu test.

    Note: Please  keep input files and results in separate folders.
    """

    result_tables = []

    for fl in glob(f"{d}/*"):

        fl_base = path.split(fl)[1].rsplit(".", 1)[0]
        data = pd.read_csv(fl)
        remaining_cols = set(data.columns) - set([c])

        tmp_result_table = {f"{fl_base} control": [],
                            f"{fl_base} case": [],
                            f"{fl_base} p-value": []}
        rows = []

        for col in remaining_cols:
            data_tmp = data[~pd.isnull(data[col])]
            data_tmp = data_tmp.groupby(c)[col].apply(list)
            if len(data_tmp) != 2:
                continue

            control = list(map(float, data_tmp.loc[0]))
            case = list(map(float, data_tmp.loc[1]))

            # Normality test
            try:
                control_p_val = stt.shapiro(control)[1]
                case_p_val = stt.shapiro(case)[1]
            except:
                continue

            rows.append(col)

            ctrl = ""
            cs = ""
            p_val = ""

            if (control_p_val > 0.05) and (case_p_val > 0.05):
                # Expecting case and control both are Normaly distributed
                cs = "%.2f[%.2f-%.2f]" % (np.mean(case),
                                          pd.DataFrame(case).describe(
                ).loc["min"].values[0],
                    pd.DataFrame(case).describe().loc["max"].values[0])

                ctrl = "%.2f[%.2f-%.2f]" % (np.mean(control),
                                            pd.DataFrame(control).describe(
                ).loc["min"].values[0],
                    pd.DataFrame(control).describe().loc["max"].values[0])
                p_val = "%.2e" % stt.ttest_ind(case, control).pvalue
            else:
                cs = "%.2f[%.2f-%.2f]" % (np.median(case),
                                          pd.DataFrame(case).describe(
                ).loc["25%"].values[0],
                    pd.DataFrame(case).describe().loc["75%"].values[0])

                ctrl = "%.2f[%.2f-%.2f]" % (np.median(control),
                                            pd.DataFrame(control).describe(
                ).loc["25%"].values[0],
                    pd.DataFrame(control).describe().loc["75%"].values[0])

                p_val = "%.2e" % stt.mannwhitneyu(case, control,
                                                  alternative='two-sided').pvalue
            tmp_result_table[f"{fl_base} control"].append(ctrl)
            tmp_result_table[f"{fl_base} case"].append(cs)
            tmp_result_table[f"{fl_base} p-value"].append(p_val)
        tmp_result_table = pd.DataFrame(tmp_result_table)
        tmp_result_table.index = rows
        result_tables.append(tmp_result_table)
    #  print(result_tables)

    df = result_tables[0]

    for rs in result_tables[1:]:
        df = df.merge(rs, left_on=df.index, right_on=rs.index, how='outer')
        df.index = df['key_0']
        del df['key_0']

    df.to_csv(o)


if __name__ == '__main__':
    run()
