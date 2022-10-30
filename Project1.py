from textwrap import wrap
import streamlit as st
import seaborn as sns
import pandas as pd
import altair as alt
import numpy as np
import missingno as msng
import io
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

Data = pd.read_csv("Mathematicians_data.csv")
st.write("""
        # Mathematicians Data Analysis"""
)
st.write(" My Goal is to observe the fields of work and professions of Mathematicians who got prestigious medals and Awards in their respective fields.")
opt1=st.radio("Let's explore the Data before visulaizing it.",('Data Set','Initial Data Analysis','Missingness Correlation','Missingness Plots'))

fig2 = msng.matrix(Data,sparkline=False, figsize=(10,7), fontsize=8, color=(0.1, 0.1, 1.0))
img_buf1 = io.BytesIO()
fig2.figure.savefig(img_buf1, format='png')

fig3 = msng.bar(Data,color="Darkblue", figsize=(10,7), fontsize=8)
img_buf2 = io.BytesIO()
fig3.figure.savefig(img_buf2, format='png')

fig4 = msng.heatmap(Data,cmap="ocean_r", figsize=(10,7), fontsize=8)
img_buf3 = io.BytesIO()
fig4.figure.savefig(img_buf3, format='png')

MyData = pd.DataFrame()
MyData['Name'] = Data['mathematicians']
MyData['Gender'] = ' '
Data['sex or gender'] = Data['sex or gender'].fillna('')
for i in range(0,len(MyData['Name'])):
    if("'male'" in Data['sex or gender'][i]):
        MyData['Gender'][i]='male'
    elif("'female'" in Data['sex or gender'][i]):
        MyData['Gender'][i]='female'
    else:
         MyData['Gender'][i]='Not Specified'

MyData['Instance'] = ' '
Data['instance of'] = Data['instance of'].fillna('')
for i in range(0,len(MyData['Name'])):
    if("'human'" in Data['instance of'][i]):
        MyData['Instance'][i]='human'
    else:
         MyData['Instance'][i]='eunuch'

Data['year of birth'] = Data['year of birth'].apply(pd.to_numeric, args=('coerce',))
Data['year of death'] = Data['year of death'].apply(pd.to_numeric, args=('coerce',))
MyData['year of birth'] = Data['year of birth']  
MyData['year of death'] = Data['year of death'] 

professor = ['professor', 'professeur', 'full professor', 'university teacher', 'teacher','school_teacher', 'head teacher', 'school teacher', 'high school teacher']
inventor = ['inventor', 'entrepreneur', 'patent inventor']
religious = ['religious', 'deacon', 'Judaic scholar', 'priest', 'Christian theology', 'vicar', 'cleric', 'missionary','Digambara monk', 'parson',  'faqih','hellenist', 'minister', 'occultist', 'rabbi', 'Bible translator', 'mystic', 'marja','Anglican priest', 'theologian', 'bishop', 'cardinal', 'monk', 'Catholic Priest', 'nun', 'Christian apologetics', 'astrologer']
linguist = ['linguist',  'interlinguist']
number_cruncher = ['number_cruncher', 'actuary', 'accountant', 'human computer']
political_scientist = ['political_scientist', 'political scientist', 'political writer', 'political philosopher', 'social scientist', 'archaeologist', 'demographer']
chemist = ['chemist', 'alchemist', 'metallurgist', 'mineralogist']
cryptographer = ['cryptographer', 'cryptoanalyst', 'criminologist', 'cryptologist']
physicist = ['physicist', 'theoretical physicist', 'biophysicist', 'astrophysicist', 'telegraphy', 'quantum physicist', 'theoretical physics']
status = ['status', 'noble', 'coin collecting', 'art collector', 'philatelist', 'numismatist', 'patron of the arts','philanthropist', 'sophist']
cool_random = ['cool_random', 'clockmaker', 'poker player', 'beekeeper', 'terrorist', 'astronaut', 'ufologist', 'poker player']
athlete = ['athlete', 'basketball player', 'taekwondo athlete', 'squash player',  'athletics competitor', 'Australian rules footballer', 'American football player', 'association football player', 'sport cyclist','rugby union player','tennis player', 'rower','association football manager', 'fencer', 'model',  'head coach', 'cricketer', 'lacrosse player', 'bodybuilding',  'bridge player', 'badminton player', 'association football referee']
economist = ['economist', 'game theory','economist', 'mathematical economics', 'econometrician', 'economic historian']
philosopher =  ['philosopher', 'epistemologist', 'metaphysician','French moralists','political philosopher', 'philosopher of science', 'ethicist', 'analytic philosopher', 'natural philosophy', 'philosopher of language','social philosopher']
biologist = ['biologist', 'neuroscientist','botanist', 'neurologist', 'genealogist','entomologist', 'physiologist','beekeeper','zoologist','theoretical biologist','cognitive scientist','geneticist','computational biologist']
musician = ['musician', 'singer', 'disc jockey', 'music educator', 'saxophonist','jazz musician','music theorist', 'musician',  'music historian','musicologist', 'violinist','composer', 'songwriter', 'pianist','cellist', 'singer-songwriter']
lawyer = ['lawyer', 'poet lawyer', 'jurist', 'judge']
businessperson = ['businessperson', 'entrepreneur', 'consultant', 'banker']
writer = ['writer', 'childrens writer', 'printmaker',' playwright','author','journalist', 'literary', 'poet lawyer', 'autobiographer', 'poet', 'literary critic', 'printer', 'science writer', 'scribe', 'opinion journalist', 'blogger', 'non-fiction writer', 'science fiction writer', 'newspaper editor', 'librettist', 'essayist', 'publisher', 'writer', 'grammarian', 'editor', 'novelist','biographer', 'epigrammatist']
politician =  ['politician', 'trade unionist', 'statesman', 'officer', 'civil servant','orator', 'chairperson', 'pacifist', 'public speaker', 'vice president','political prisoner', 'dissident', 'resistance fighter','anti-war activist', 'revolutionary', 'activist', 'politician''political activist','peace activist', 'anti-vaccine activist','human rights activist', 'diplomat']
health = ['health', 'diarist','radiologist', 'physician', 'pharmacist', 'paramedic', 'surgeon']
geologist = ['geologist', 'speleologist', 'calligrapher', 'geomatics engineering', 'historian of cartography', 'geologist', 'geographer', 'agronomist' 'oceanographer', 'selenographer', 'geophysicist', 'seismologist']
computer_science = ['computer_science', 'computer science', 'game designer','software engineer', 'roboticist',  'artificial intelligence researcher', 'computer scientist',  'computational biologist', 'programmer']
artist = ['artist', 'street artist', 'painter', 'art historian', 'photographer','sculptor']
engineer = [ 'engineer', 'civil engineer', 'aerospace engineer', 'mechanical engineer', 'engineer of roads and bridges', 'mining engineer', 'geomatics engineering',]
media = ['media', 'media critic', 'television presenter', 'television actor','screenwriter', 'stage actor', 'circus performer', 'actor', 'film actor','radio personality', 'film director', 'juggler', 'stage magician']
military = ['military', 'military historian', 'navy officer', 'military personnel']
chess = ['chess', 'chess player', 'chess official', 'chess composer']
historian = ['historian', 'literary historian','historian of science', 'historian of mathematics', 'philosophy historian']
mathematician = ['mathematician', 'statistician', 'topologist']
astronomer = ['astronomer', 'astronaut', 'aerospace engineer','astrophysicist', 'cosmographer','cosmologist']

professions = [professor, inventor, religious, linguist,number_cruncher, political_scientist, chemist, cryptographer,physicist, status, cool_random, athlete, economist, astronomer,philosopher, biologist, musician, lawyer, businessperson, writer,politician, health, geologist, computer_science, artist,engineer, media, military, chess, historian, mathematician]

columns = [i[0] for i in professions]

for i in range(len(professions)):
    MyData[columns[i]] = [0 for k in Data.mathematicians]
    for j in professions[i]:
        MyData.loc[MyData[columns[i]] == 0, columns[i]] = Data['occupation'].loc[MyData[columns[i]] == 0].str.contains(j)

famous_awards = ['Fields Medal', 'Abel Prize', 'Turing Award', 'Wolf Prize', 'Carl Friedrich Gauss Medal','Nevanlinna Prize', 'Chern Medal', 'Kyoto Prize']
for i in range(len(famous_awards)):
    MyData[(famous_awards[i])] = Data['award received'].str.contains(famous_awards[i])

MyData['field of work'] = Data['field of work'].str.replace(" ","")
fields_medal = MyData[MyData['Fields Medal']==1].reset_index(drop=True)
fields = []
counts = [0]*31
for i in range(len(fields_medal['field of work'])):
    string = str(fields_medal['field of work'][i])
    string = string.replace("[","")
    string = string.replace("]","")
    string = string.replace("'","")
    string = string.split(",")
    for i in string:
        if(i not in fields):
            fields.append(i)
            counts[fields.index(i)] = 1
        else:
            counts[fields.index(i)] += 1

Fields = pd.DataFrame()
Fields['fields'] = fields
Fields['count'] = counts
print(Data.columns)

MyData['languages'] = Data['languages spoken, written or signed'].str.replace(" ","")
langs = []
lcounts = []
for i in range(len(MyData['languages'])):
    string = str(MyData['languages'][i])
    string = string.replace("[","")
    string = string.replace("]","")
    string = string.replace("'","")
    string = string.split(",")
    for i in string:
        if(i not in langs):
            langs.append(i)
            lcounts.append(1)
        else:
            lcounts[langs.index(i)] += 1

Languages = pd.DataFrame()
Languages['Language'] = langs
Languages['count'] = lcounts


def birthFeats(df):
    df = df[~(df['approx. date of birth'])]
    df = df[df['year of birth'].notnull()].reset_index(drop=True)
    df['decade born'] = (df['year of birth'] / 10).astype(int)*10
    return df

def lifeFeats(df):
    df = birthFeats(df)
    df['Name']=MyData['Name']
    df['Gender']= MyData['Gender']
    df['Instance']=MyData['Instance']
    df['professor']=MyData['professor']
    df['mathematician']=MyData['mathematician']
    df['Fields Medal']=MyData['Fields Medal']
    df = df[df['year of death'].notnull()]
    df = df[~(df['approx. date of death'])]
    df['mid year'] = (df['year of death'] + df['year of birth']) / 2
    df['lifespan'] = df['year of death'] - df['year of birth']
    df = df.sort_values(by='mid year').reset_index(drop=True)
    return df

dates_life = lifeFeats(Data)
dates_birth = birthFeats(Data)
dates = lifeFeats(Data)
dates = dates[dates['year of birth'] > 0]
dates = dates.sort_values(by='mid year', ascending=False).reset_index(drop=True)



Profession=['professor', 'inventor', 'religious', 'linguist','number_cruncher', 'political_scientist',
     'chemist', 'cryptographer','physicist', 'status', 'cool_random', 'athlete', 'economist', 'astronomer','philosopher',
      'biologist', 'musician', 'lawyer', 'businessperson', 'writer','politician', 'health', 'geologist', 'computer_science',
       'artist','engineer', 'media', 'military', 'chess', 'historian', 'mathematician']
TrueVal = []
FalseVal = []
MaleCount=[]
FemaleCount=[]
FieldAwards=[]
for i in Profession:
    TrueVal.append(MyData[i].values.sum())
    FalseVal.append((~MyData[i]).values.sum())
    MaleCount.append(MyData[i][MyData['Gender']=='male'].values.sum())
    FemaleCount.append(MyData[i][MyData['Gender']=='female'].values.sum())
    FieldAwards.append(MyData[i][MyData['Fields Medal']==True].values.sum())

datanew = []
datanew.append(Profession)
datanew.append(TrueVal)
datanew.append(MaleCount) 
datanew.append(FemaleCount)
datanew.append(FieldAwards)

Profdet = pd.DataFrame(datanew).transpose()
Profdet.columns=['Profession', 'Count','Male Count','Female Count','Field Awards']

if(opt1=='Data Set'):
        st.dataframe(Data)
elif(opt1=='Initial Data Analysis'):
        opt2 = st.selectbox(
                'What do you want to know about the Data?',
                ('Shape','Columns','Describe','Info' ,'Correlation','Are there any NaNs?'))
        if(opt2=='Shape'):
                st.write(Data.shape)
        elif(opt2=='Columns'):
                st.write(list(Data.columns))
        elif(opt2=='Describe'):
                st.write(Data.describe())
        elif(opt2=='Info'):
                image1 = Image.open("Data_Info.png")
                st.image(image1)
        elif(opt2=='Correlation'):
                st.write(Data.corr())
        else:
                st.write(Data.isna())
                st.write('Yes, there are many NaNs.')
        
        

elif(opt1=='Missingness Correlation'):
        opt31 = st.selectbox('Select a column to get its missingness correlation with the other:',
        ['field of work','mathematicians','occupation','country of citizenship', 'place of birth', 'date of death', 
        'educated at'  ,'employer' , 'place of death', 'member of', 'employer.1' ,'doctoral advisor', 
        'languages spoken, written or signed',  'academic degree'  ,'doctoral student' , 'manner of death' , 
        'position held'  ,'award received', 'Erdős number' ,'instance of' ,'sex or gender',  
        'approx. date of birth',  'day of birth' , 'month of birth' , 'year of birth', 'approx. date of death', 
        'day of death','month of death', 'year of death'])
        opt32 = st.selectbox('Select any column to get its missingness correlation with the above column:',
        ['mathematicians','occupation','country of citizenship', 'place of birth', 'date of death', 
        'educated at'  ,'employer' , 'place of death', 'member of', 'employer.1' ,'doctoral advisor', 
        'languages spoken, written or signed',  'academic degree'  ,'doctoral student' , 'manner of death' , 
        'position held' ,'field of work' ,'award received', 'Erdős number' ,'instance of' ,'sex or gender',  
        'approx. date of birth',  'day of birth' , 'month of birth' , 'year of birth', 'approx. date of death', 
        'day of death','month of death', 'year of death'])
        st.write('The Missingness correlation of above columns is:')
        st.write(Data[opt31].isna().corr(Data[opt32].isna()))
        st.write("The Missingness correlation heatmap is as shown for the given Data:")
        fig1 = plt.figure(figsize=(10, 10))
        sns.heatmap(Data.isna().corr(),cmap='ocean')
        st.pyplot(fig1)
else:
        with st.sidebar:
                st.write('Select the type of plot:')
                M=st.button('Matrix')
                BG=st.button('Bar Graph')
                HM=st.button('Heat map')
        if(M):
                st.write("The Matrix of Missingness is:")
                st.image(img_buf1)
        if(BG):
                st.write("The Bar graph of Missingness is:")
                st.image(img_buf2)
        if(HM):
                st.write("The Heat Map of Missingness is:")
                st.image(img_buf3)

st.write("The Data is cleaned so that it can be visualized better.")


opt4=st.radio("Let's see the Modified Data that is obtained from the Initial Data:",
     ("Professions Data","Modified Data","Missingness Correlation"))
if(opt4=='Modified Data'):
        st.write(
    """
    - Eventhough there are many missing values, we can use the available values in comparing each other.
- As we saw, Missigness in Columns related to death has correlation with each other. Employer1 and Employer are totally correlated in missing values. So, we can remove the columns, which won't aid in gaining any new insights. 
- **Academic degree**, **Doctoral Student**, **Manner of Death** and **Position held** have very few Data, I think removing them will make visualizations better.
- **Place of Birth**, **Date of Death**, **Place of Death** and **Employer.1** won't be much helpful in analysing the Data.
- Some of the columns have data with lists and strings. Let's manipulate them.
- Let's create a new clean data to analyse.
    """
)
        st.dataframe(MyData)
elif(opt4=='Professions Data'):
        st.dataframe(Profdet)
else:
        st.write("The Missingness correlation heatmap is as shown for the given Data:")
        fig5 = plt.figure(figsize=(10, 10))
        sns.heatmap(MyData.isna().corr(),cmap='ocean')
        st.pyplot(fig5)

st.write("Let's see the Exploratory Data Analysis of the Data:")

opt5=st.radio("Select the plots you wish to explore:",
("Basic count plots","Lifespan Comparison plots","Profession plots","Mathematicians Feilds and Language plots"))
if(opt5=='Basic count plots'):
        opt6=st.selectbox("Select the Column to see their counts:",
        ('Fields Medal','Gender','Instance','year of birth','year of death','professor', 'inventor', 'religious', 
        'linguist','number_cruncher', 'political_scientist', 'chemist', 'cryptographer','physicist', 'status', 
        'cool_random', 'athlete', 'economist', 'astronomer','philosopher', 'biologist', 'musician', 'lawyer', 
        'businessperson', 'writer','politician', 'health', 'geologist', 'computer_science', 'artist','engineer', 
        'media', 'military', 'chess', 'historian', 'mathematician', 'Abel Prize', 'Turing Award', 
        'Wolf Prize', 'Carl Friedrich Gauss Medal','Nevanlinna Prize', 'Chern Medal', 'Kyoto Prize'))
        fig6=px.bar(MyData,x=opt6, hover_name=opt6,hover_data=['Name','Fields Medal'])
        st.plotly_chart(fig6)
elif(opt5=="Lifespan Comparison plots"):
        opt7=st.radio("Select type of the plots:",('Scatter plots','Violin plots'))
        if(opt7=='Scatter plots'):
                opt8=st.selectbox("Select the Column to see their lifespans:",
               ('Fields Medal','Gender','Name','Instance','year of birth','year of death','professor', 'mathematician'))
                fig8 = px.scatter(dates, x=opt8, y='lifespan',color=opt8,hover_data=['Name','Fields Medal'],color_discrete_sequence=["green", "blue", "purple"])
                st.plotly_chart(fig8)
        else:
                opt9=st.selectbox("Select the Column to see their lifespans:",
                ('Fields Medal','Gender','Instance','professor', 'mathematician'))
                fig9 = px.violin(dates, x=opt9, y='lifespan',hover_data=['Name','Fields Medal'],color=opt9,box=True,points='all',color_discrete_sequence=["green", "blue", "purple"])
                st.plotly_chart(fig9)
elif(opt5=="Profession plots"):
        opt10=st.selectbox("Select the type of plot:",
        ('Scatter plot','Bar plots','Pie Charts'))
        if(opt10=='Scatter plot'):
                opt101=st.selectbox("Select x-axis variable:",
                ('Field Awards','Count','Male Count','Female Count'))
                opt102=st.selectbox("Select y-axis variable:",
                ('Field Awards','Count','Male Count','Female Count'))
                fig9 = px.scatter(Profdet,x=opt101,y=opt102,color='Profession')
                st.plotly_chart(fig9)
        elif(opt10=='Bar plots'):
                opt103=st.select_slider('Do you want to remove the professor and mathematician row to see the graph more clearly?',
                options=['No', 'Yes'])
                if(opt103=='No'):
                        fig10 = go.Figure(data=[
                        go.Bar(name='Male', x=Profdet['Profession'], y=Profdet['Male Count']),
                        go.Bar(name='Female', x=Profdet['Profession'], y=Profdet['Female Count'])
                        ])
                        fig10.update_layout(barmode='group')
                        st.plotly_chart(fig10)
                else:
                        Nprofdet = Profdet.drop(Profdet.index[-1]).drop(Profdet.index[0])
                        fig11 = go.Figure(data=[
                        go.Bar(name='Male', x=Nprofdet['Profession'], y=Nprofdet['Male Count']),
                        go.Bar(name='Female', x=Nprofdet['Profession'], y=Nprofdet['Female Count'])
                        ])
                        fig11.update_layout(barmode='group')
                        st.plotly_chart(fig11)
        else:
                opt104=st.select_slider('Do you want to remove the professor and mathematicians row to see the others more clearly?',
                options=['No', 'Yes'])
                if(opt104=='No'):
                        opt105=st.selectbox("Select x-axis variable:",
                        ('Field Awards','Count','Male Count','Female Count'))
                        fig12 = px.pie(Profdet, values=opt105, names='Profession')
                        fig12.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig12)
                else:
                        Nprofdet = Profdet.drop(Profdet.index[-1]).drop(Profdet.index[0])
                        opt106=st.selectbox("Select x-axis variable:",
                        ('Field Awards','Count','Male Count','Female Count'))
                        fig13 = px.pie(Nprofdet, values=opt106, names='Profession')
                        fig13.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig13)
else:
        fig14=px.bar(Fields,x='fields',y='count',color='fields', text_auto=True)
        st.plotly_chart(fig14)
        Languages=Languages.drop(Languages.index[1]).drop(Languages.index[46:50])
        fig15=px.bar(Languages,x='Language',y='count',color='Language', text_auto=True)
        st.plotly_chart(fig15)

st.write("These plots were so helpful in knowing about the fields and professions of Mathematicians.")
st.write("Many Mathematicians were mathematicians by profession and some were professors.All the mathematicians who got Field medals are mathematicians and Professors by profession and their major fields were Topology, Algebra and Number theory.")
st.write("""I conclude that there will be something in the data that can be understood even in cases of missingness. 
       Here, there is no possibility of imputing because the data can't be replaced by mean or mode, because the data for those mathematicians was unknown. 
        In such cases we can't ignore the data, we should be able to analyse for those the data is present. In that way we may get some information regarding the data.""")
