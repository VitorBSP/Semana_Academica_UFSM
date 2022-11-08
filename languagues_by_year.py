#%%
import plotly.graph_objects as go
from easeimage.utils import io
import pandas as pd
# %%
languages = ['Portugol', 'HTML', 
            'Portugol','HTML', 'C', 

            'PHP', 'HTML', 'CSS', 
            'PHP', 'JAVA', 'SQL',
            
            'PHP', 'JAVA SCRIPT', 'SQL',
            'PHP', 'SQL', 'JAVA SCRIPT',
            
            'PHP',
            'R', 
            
            'PYTHON',
            'R',
            
            'R', 'PYTHON',
            'R', 'PYTHON', 'SQL',
            
            'R',
            'R', 'SQL',
            
            'R', 'PYTHON',
            'PYTHON', 'JULIA', 'R', 
            
            'C', 'SCALA', 'C++']
year = [2015.25, 2015.25,
        2015.75, 2015.75, 2015.75,

        2016.25, 2016.25, 2016.25,
        2016.75, 2016.75, 2016.75,
        
        2017.25, 2017.25, 2017.25,
        2017.75, 2017.75, 2017.75,

        2018.25, 
        2018.75,

        2019.25, 
        2019.75,
        
        2020.25, 2020.25,
        2020.75, 2020.75, 2020.75,
        
        2021.25, 
        2021.75, 2021.75,
        
        2022.25, 2022.25,
        2022.75, 2022.75, 2022.75,
        
        2023.5, 2023.5, 2023.5]
order = [3,2,
        3,2,1,
        3,2,1,
        3,2,1,
        3,2,1,
        3,2,1,
        3,
        3,
        3,
        3,
        3,2,
        3,2,1,
        3,
        3,2,
        3,2,
        3,2,1,
        3,2,1
        ]

df = pd.DataFrame({'order' : order, 
                    'langs' : languages,
                    'year' : year})

df['order'] = df['order'].map({3 : 3, 2 :2.5, 1 : 2})
cores_languages = {
                    'Portugol' : "#F1BD07",
                    'HTML' : '#DD4B25',
                    'C' : "#6295CB",
                    'PHP' : '#7377AD',
                    'CSS' : '#254BDD',
                    'JAVA' : '#E06C00',
                    'SQL' : '#E01B23',
                    'JAVA SCRIPT' : '#EFD81D',
                    'R' : '#1E63AC',
                    'PYTHON' : '#B48E00',
                    'JULIA' : '#A575BB',
                    'SCALA' : '#D73222',
                    'C++' : '#15961B'
                    }
#%%

fig = go.Figure()
for languages in df['langs'].unique():
    fig.add_trace(go.Scatter(
    x=df.query('langs == @languages')['year'],
    y=df.query('langs == @languages')['order'],
    name=languages, 
    marker=dict(color=cores_languages[languages])))
fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=40))
fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showticklabels=True,
    ),
    margin=dict(l=40, r=40, b=0, t=40),
    legend=dict(
        font_size=10,
        yanchor='top',
        xanchor='left',
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    hovermode='closest')
fig.update_xaxes(
    ticktext = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 'Futuro'],
    tickvals = [2015.5, 2016.5, 2017.5, 2018.5, 2019.5, 2020.5, 2021.5, 2022.5, 2023.5],
    anchor = 'free', position = 1,
    tickfont_size = 18)
fig.update_yaxes(
    ticktext = ['Prioridade', 'Secundário', 'Útil'],
    tickvals = [3, 2.5, 2])
fig.show()
# %%
