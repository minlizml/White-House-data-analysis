from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud


df=pd.read_csv('data.csv',index_col=0)


df.groupby('issue').title.count().plot(
    kind='pie',
    title='Trump White House News Release by Issue',
    ylabel="",
    autopct="%.1f%%",   #保留一位小數
)
plt.show()

df.groupby('type').title.count().plot(
    kind='pie',
    title='Trump White House News Release by Type',
    ylabel="",
    autopct="%.1f%%",   #保留一位小數
)
plt.show()


df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].apply(lambda d: datetime(year=d.year, month=1, day=1))
df["month"] = df["date"].apply(lambda d: datetime(year=d.year, month=d.month, day=1))

df_year_issue = pd.DataFrame(df.groupby(["year", "issue"]).title.count())
df_year_issue.pivot_table(values="title", index="year", columns="issue").plot(
    kind="area",
    title="Trump White House News Release by Issue and Year"
)
plt.show()

df_year_type = pd.DataFrame(df.groupby(["year", "type"]).title.count())
df_year_type.pivot_table(values="title", index="year", columns="type").plot(
    kind="area",
    title="Trump White House News Release by Type and Year"
)
plt.show()

df_month_issue = pd.DataFrame(df.groupby([df["month"], "issue"]).title.count())
df_month_issue.pivot_table(values="title", index="month", columns="issue").plot(
    kind="area",
    title="Trump White House News Release by Issue and Month"
)
plt.show()

df_month_type = pd.DataFrame(df.groupby([df["month"], "type"]).title.count())
df_month_type.pivot_table(values="title", index="month", columns="type").plot(
    kind="area",
    title="Trump White House News Release by Type and Month"
)
plt.show()

text = " ".join(df["title"].tolist())
cloud = wordcloud.WordCloud(
    background_color="white",
    width=1920,
    height=1080
)
cloud.generate(text)
plt.imshow(cloud)
plt.axis("off")
plt.show()


