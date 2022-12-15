import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import statistics as stats
import plotly.express as px
import dash_bootstrap_components as dbc


########################DATOS##############################

url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2SbYhQ01W6gyOwm_BfZpZUOH1peuA8QMlj03-wPvRt2Us_4gmXKrZYhDHPmBi4Q/pub?output=csv'
df=pd.read_csv(url)

url2='https://docs.google.com/spreadsheets/d/e/2PACX-1vTRsVAq_5SGisQBZXkdJpv9DcWVLZwzyQDrmEihhd9doYYLPTKsCNFIo62Ojo9MXAeKUHr3_s26EcbB/pub?output=csv'
df2=pd.read_csv(url2)

# url3='https://docs.google.com/spreadsheets/d/e/2PACX-1vT2ZkhX_wxekZxQ-mCb3KuRWvmjOxshMZO962yYLgqzyX6ACjLevOJOCoTmXvWlR6ZX5tjLv3KMZBKz/pub?output=csv'
# df4=pd.read_csv(url3)

#######################################################

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server=app.server

app.layout=html.Div((
    html.Div([
        html.Div([
            html.Img(src="data:image/png;base64,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",style={'width':'145%'})
        
        ],),
        

    ],style = { 'display': 'flex','flex-direction': 'row','white-space': 'pre','heigth':'200px','background-color':'white'}), 


    html.Div([
        dcc.Dropdown(id = 'area',
        multi = False,
        clearable =False,
        disabled = False,
        style = {'display': True,'width':'300px'},
        value = 'PUNTAJE GLOBAL',
        placeholder = 'Seleccione área',
        options = [{'label': c, 'value': c} for c in df2['areas'].unique()]),

        html.Div([
            dcc.RangeSlider(
                id='slider', # any name you'd like to give it
                marks={
                2017: '2017',     # key=position, value=what you see
                2018: '2018',
                2019: '2019',
                2020: '2020',
                2021: '2021',
                2022: {'label': '2022', 'style': {'color':'#f50', 'font-weight':'bold'}},
                },
                 step=1, 
                min=2017,
                max=2022,
                value=[2017,2022],     # default value initially chosen
                dots=True,             # True, False - insert dots, only when step>1
                allowCross=True,      # True,False - Manage handle crossover
                disabled=False,        # True,False - disable handle
                pushable=1,            # any number, or True with multiple handles
                updatemode='mouseup',  # 'mouseup', 'drag' - update value method
                included=True,         # True, False - highlight handle
                vertical=False,        # True, False - vertical, horizontal slider
                verticalHeight=30,    # hight of slider (pixels) when vertical=True
                className='None',
                tooltip={'always_visible':False,  # show current slider values
                    'placement':'topRight'},
            ),

        ],style={'width':'80%'}),

        
    ],style={'width': '100%','display': 'flex'}),


    # html.Div([
    #     html.Div([
    #         html.Div(id = 'text1',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text2',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text3',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text4',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text5',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    # ],style={'display': 'flex','flex-wrap': 'wrap','justify-content': 'center','margin-top': '10px','gap': '10px'}),

    html.Div([
        html.Div([
            dcc.Graph(id = 'chart2',config = {'displayModeBar': False},style={'width':'475px','height':'375px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),

        html.Div([
            dcc.Graph(id = 'chart1',config = {'displayModeBar': False},style={'width':'440px','height':'375px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),


        html.Div([
            dcc.Graph(id = 'funnel_chart',config = {'displayModeBar': False},style={'width':'390px','height':'410px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),        

    ],style={'display': 'flex','flex-direction': 'row','margin-top': '10px','gap': '10px','background-color': 'white'}),
    # style={'display': 'flex','flex-direction': 'row'}
    # ,style={'background-color': '#335476','width': '480px','height': '420px','margin-top':'2px'}


    #     html.Div([
    #     html.Div([
    #         dcc.Graph(id = 'chart3',config = {'displayModeBar': False},style={'width':'660px','height':'375px'}),
    #     ],style={'border-style':'dotted','border-color':'blue'}),


    #     html.Div([
    #         dcc.Graph(id = 'box',config = {'displayModeBar': False},style={'width':'660px','height':'410px'}),
    #     ],style={'border-style':'dotted','border-color':'blue'}),        

    # ],style={'display': 'flex','flex-direction': 'row','margin-top': '10px','gap': '10px'}),
))



############### CALLBACKS #################################
# @app.callback(
#     Output(component_id='text1', component_property='children'),
#     Input(component_id='area', component_property='value')
# )
# def avg(choose):
#     filtro=df[df['AÑO']==2022]
#     avera=round(stats.mean(filtro[choose]),2)
#     return [            html.P('Promedio 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera]


# @app.callback(
#     Output(component_id='text2', component_property='children'),
#     Input(component_id='area', component_property='value')
# )
# def avg(choose2):
#     filtro=df[df['AÑO']==2022]
#     avera2=round(stats.stdev(filtro[choose2]),2)
#     return [html.P('Desviación 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera2]

# @app.callback(
#     Output(component_id='text3', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose3):
#     filtro=df[df['AÑO']==2022]
#     avera3=round(stats.median(filtro[choose3]),2)
#     return [html.P('Mediana 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera3]

# @app.callback(
#     Output(component_id='text4', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose4):
#     filtro=df[df['AÑO']==2022]
#     avera4=round(np.percentile(filtro[choose4],25),2)
#     return [html.P('Cuartil 1 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera4]


# @app.callback(
#     Output(component_id='text5', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose5):
#     filtro=df[df['AÑO']==2022]
#     avera5=round(np.percentile(filtro[choose5],75),2)
#     return [html.P('Cuartil 3 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera5]



#######################GRÁFICAS######################3
@app.callback(
    Output(component_id='chart1', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph5(mao,slid):
    if mao=='MATEMATICAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2022.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

        # fig.update_layout(width=534.5, height=440, autosize=False)

      
        
        return fig
    
    elif mao=='CIENCIAS NATURALES' or mao=='SOCIALES Y CIUDADANAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=40),
            (df[mao]>40)&(df[mao]<=55),
            (df[mao]>55)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2022.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        # fig.update_layout(width=534.5, height=440, autosize=False)

       
         
        return fig

    elif mao=='LECTURA CRITICA':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=65),
            (df[mao]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2022.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

     
        
  
        return fig


    elif mao=='INGLES':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=47),
            (df[mao]>47)&(df[mao]<=57),
            (df[mao]>57)&(df[mao]<=67),
            (df[mao]>67)&(df[mao]<=78),
            (df[mao]>78)],['A-','A1','A2','B1','B2'])
        edad=['A-','A1','A2','B1','B2']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2022.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

  
        return fig


    else :
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=221),
            (df[mao]>221)&(df[mao]<=299),
            (df[mao]>299)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2022.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        return fig

#######################GRÁFICAS######################3

@app.callback(
    Output(component_id='chart2', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)
def update_graph2(mate2,slider): 
    linea=df['AÑO'].between(slider[0],slider[1],inclusive='both')
    linea15=df[linea] 
    inicial=linea15.groupby('AÑO').agg({mate2:'mean'}).reset_index()
    inicial[mate2]=round(inicial[mate2],1)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(range(slider[0],(slider[1]+1))),
            y=list(inicial[mate2]),
            line=dict(width=2),
            showlegend=False,
            mode="lines+text",
            hoverinfo="none",
            text=list(inicial[mate2]),  # one for each point..
            textposition="bottom center",  # changed to make it visible on right
            textfont=dict(color="black"),
        
        )
    )   
    fig.update_layout(title=dict(text='Puntaje promedio prueba saber',font=dict(size=15)),title_x=0.5,xaxis_title='Año',yaxis_title='Puntaje',plot_bgcolor='rgba(0,0,0,0)')

  

    # fig.update_layout(width=400, height=350, autosize=True)        

    return fig

##################################################

@app.callback(
    Output(component_id='funnel_chart', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph(lola,slide10):

    linea=df['AÑO'].between(slide10[0],slide10[1],inclusive='both')
    linea5=df[linea]
    inicial2=linea5.groupby('AÑO').agg({lola:'std'}).reset_index()
    inicial2[lola]=round(inicial2[lola],2)
    inicial=linea5.groupby('AÑO').agg({lola:'mean'}).reset_index()
    inicial[lola]=round(inicial[lola],2)  
   

    fig = go.Figure()
    fig.add_trace(go.Bar(
    y=list(range(slide10[0],(slide10[1]+1))),
    x=list(inicial[lola]),
    text = list(inicial[lola]),
    textposition="inside",
    name='Promedio',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
    fig.add_trace(go.Bar(
    y=list(range(slide10[0],(slide10[1]+1))),
    x=list(inicial2[lola]),
    text = list(inicial2[lola]),
    textposition="inside",
    name='Desviación',
    orientation='h',
    marker=dict(
        color='green',
        line=dict(color='green', width=3)
    ),
    
))

    fig.update_layout(barmode='stack',plot_bgcolor='rgba(0,0,0,0)',title=dict(text='Promedio y desviación historica',font=dict(size=15)),title_x=0.5)

    return fig

# @app.callback(
#     Output(component_id='chart3', component_property='figure'),
#     Input(component_id='area', component_property='value'),
#     Input(component_id='slider', component_property='value')
# )

# def update_graph(mao,slid):
#     if mao=='MATEMATICAS':
#         df['Nivel']=np.select([
#             (df[mao]>0)&(df[mao]<=35),
#             (df[mao]>35)&(df[mao]<=50),
#             (df[mao]>50)&(df[mao]<=70),
#             (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
#         linea2=df[linea]    
#         linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
#         linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
#         fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

      
        
#         return fig
    
#     elif mao=='CIENCIAS NATURALES' or mao=='SOCIALES Y CIUDADANAS':
#         df['Nivel']=np.select([
#             (df[mao]>0)&(df[mao]<=40),
#             (df[mao]>40)&(df[mao]<=55),
#             (df[mao]>55)&(df[mao]<=70),
#             (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
#         linea2=df[linea]    
#         linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
#         linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
#         fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
       
         
#         return fig

#     elif mao=='LECTURA CRITICA':
#         df['Nivel']=np.select([
#             (df[mao]>0)&(df[mao]<=35),
#             (df[mao]>35)&(df[mao]<=50),
#             (df[mao]>50)&(df[mao]<=65),
#             (df[mao]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
#         linea2=df[linea]    
#         linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
#         linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
#         fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        
  
#         return fig


#     elif mao=='INGLES':
#         df['Nivel']=np.select([
#             (df[mao]>0)&(df[mao]<=47),
#             (df[mao]>47)&(df[mao]<=57),
#             (df[mao]>57)&(df[mao]<=67),
#             (df[mao]>67)&(df[mao]<=78),
#             (df[mao]>78)],['A-','A1','A2','B1','B2'])
#         edad=['A-','A1','A2','B1','B2']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
#         linea2=df[linea]    
#         linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
#         linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
#         fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

  
#         return fig


#     else :
#         df['Nivel']=np.select([
#             (df[mao]>0)&(df[mao]<=221),
#             (df[mao]>221)&(df[mao]<=299),
#             (df[mao]>299)],['Insuficiente','Mínimo','Satisfactorio'])
#         edad=['Insuficiente','Mínimo','Satisfactorio']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
#         linea2=df[linea]    
#         linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
#         linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
#         fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

#         return fig


# @app.callback(
#     Output(component_id='box', component_property='figure'),
#     Input(component_id='area', component_property='value'),
#     Input(component_id='slider', component_property='value')
# )

# def update_graph4(mao4,slid4):
#     if mao4=='MATEMATICAS':
#         df['Nivel']=np.select([
#             (df[mao4]>0)&(df[mao4]<=35),
#             (df[mao4]>35)&(df[mao4]<=50),
#             (df[mao4]>50)&(df[mao4]<=70),
#             (df[mao4]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
#         linea2=df[linea]
#         fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
#         fig.update_layout(
#                         plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
#                     )
        
#         return fig
    
#     elif mao4=='CIENCIAS NATURALES' or mao4=='SOCIALES Y CIUDADANAS':
#         df['Nivel']=np.select([
#             (df[mao4]>0)&(df[mao4]<=40),
#             (df[mao4]>40)&(df[mao4]<=55),
#             (df[mao4]>55)&(df[mao4]<=70),
#             (df[mao4]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
#         linea2=df[linea]
#         fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año')  
#         fig.update_layout(
#                         plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
#                     )
        
#         return fig
 


#     elif mao4=='LECTURA CRITICA':
#         df['Nivel']=np.select([
#             (df[mao4]>0)&(df[mao4]<=35),
#             (df[mao4]>35)&(df[mao4]<=50),
#             (df[mao4]>50)&(df[mao4]<=65),
#             (df[mao4]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
#         edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
#         linea2=df[linea]
#         fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año')  
#         fig.update_layout(
#                         plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
#                     )       
#         return fig


#     elif mao4=='INGLES':
#         df['Nivel']=np.select([
#             (df[mao4]>0)&(df[mao4]<=47),
#             (df[mao4]>47)&(df[mao4]<=57),
#             (df[mao4]>57)&(df[mao4]<=67),
#             (df[mao4]>67)&(df[mao4]<=78),
#             (df[mao4]>78)],['A-','A1','A2','B1','B2'])
#         edad=['A-','A1','A2','B1','B2']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
#         linea2=df[linea]
#         fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
#         fig.update_layout(
#                         plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
#                     )   
#         return fig

#     else :
#         df['Nivel']=np.select([
#             (df[mao4]>0)&(df[mao4]<=221),
#             (df[mao4]>221)&(df[mao4]<=299),
#             (df[mao4]>299)],['Insuficiente','Mínimo','Satisfactorio'])
#         edad=['Insuficiente','Mínimo','Satisfactorio']
#         df['Nivel']= pd.Categorical(df['Nivel'], edad)
#         linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
#         linea2=df[linea]
#         fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
#         fig.update_layout(
#                         plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
#                     )          
#         return fig
##################################################################


############################


if __name__ == "__main__":
    app.run_server(debug = True)
