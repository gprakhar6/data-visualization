import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

fname_india_min = "India_Min_Temperatures_1901-2012_1.csv";
fname_india_max = "India_Max_Temperatures_1901-2012_1.csv";
df_min = pd.read_csv(fname_india_min, index_col=0);
df_max = pd.read_csv(fname_india_max, index_col=0);

str_types = ['Min', 'Max']
dfs = [df_min, df_max]
xtics = [1, 2, 3, 4];
labels = ['JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC'];

fig = plt.figure(figsize=(10, 6), dpi=80);
fig_r = 1;
fig_c = 2;
fig_n = 1;
for (df, t) in zip(dfs, str_types):
    coln1 = df.loc[:, ['JAN-FEB']].to_numpy().flatten();
    coln2 = df.loc[:, ['MAR-MAY']].to_numpy().flatten();
    coln3 = df.loc[:, ['JUN-SEP']].to_numpy().flatten();
    coln4 = df.loc[:, ['OCT-DEC']].to_numpy().flatten();
    coln = [coln1, coln2, coln3, coln4];
    ax = fig.add_subplot(fig_r, fig_c, fig_n, title=t+"-Temperature 1901-2012");
    fig_n += 1;
    plt.ylabel("degree celsius");
    plt.xticks(xtics, labels);
    ax.violinplot(coln);

#plt.savefig("violin-plot.png", dpi=256);    
plt.show();
fig.clear();
plt.close();

fig = plt.figure(figsize=(10, 6), dpi=80);
fig_r = 1;
fig_c = 2;
fig_n = 1;
for (df, t) in zip(dfs, str_types):
    coln1 = df.loc[:, ['JAN-FEB']].to_numpy().flatten();
    coln2 = df.loc[:, ['MAR-MAY']].to_numpy().flatten();
    coln3 = df.loc[:, ['JUN-SEP']].to_numpy().flatten();
    coln4 = df.loc[:, ['OCT-DEC']].to_numpy().flatten();
    coln = [coln1, coln2, coln3, coln4];
    ax = fig.add_subplot(fig_r, fig_c, fig_n, title=t+"-Temperature 1901-2012");
    fig_n += 1;
    plt.ylabel("degree celsius");
    ax.set_xticklabels(labels);
    ax.boxplot(coln, whis=10.0);

#plt.savefig("box-plot.png", dpi=256);    
plt.show();
fig.clear();
plt.close();

fig_r = 2;
fig_c = 2;
fig_n = 1;

fig = plt.figure(figsize=(16, 8), dpi=80);
for l in labels:
    min_yrwise = df_min.loc[:, [l]].to_numpy().flatten();
    max_yrwise = df_max.loc[:, [l]].to_numpy().flatten();
    corln = ((min_yrwise * max_yrwise).mean()  -
             min_yrwise.mean() * max_yrwise.mean()) / (min_yrwise.std() * max_yrwise.std());
    ax = fig.add_subplot(fig_r, fig_c, fig_n, title=l);
    fig_n += 1;
    ax.plot(min_yrwise, max_yrwise, '*', label="cor="+"{:.2f}".format(corln));
    ax.legend(loc="upper right")    
#plt.savefig("scatter.png", dpi=256);
plt.show();
fig.clear();


    
fig_r = 2;
fig_c = 1;
fig_n = 1;

fig = plt.figure(figsize=(16, 8), dpi=80);
for (df,t) in zip(dfs, str_types):
    yrwise = df.loc[:, ['ANNUAL']].to_numpy().flatten();
    ax = fig.add_subplot(fig_r, fig_c, fig_n);
    fig_n += 1;
    ax.plot(range(1901, 2013), yrwise, '*-', label=t+" Temperature");
    ax.legend(loc="upper right")    
#plt.savefig("line-plot.png", dpi=256);
plt.show();
fig.clear();
