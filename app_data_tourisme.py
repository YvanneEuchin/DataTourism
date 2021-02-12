import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 
from pathlib import Path
import plotly.express as px 
import geopandas as gpd
import streamlit.components.v1 as components
import json
from urllib.request import urlopen
from PIL import Image
import base64
import csv

data0 = pd.DataFrame()

@st.cache
def dept_geo() :
    with urlopen('https://france-geojson.gregoiredavid.fr/repo/departements.geojson') as response:
        france_regions_geo = json.load(response)
        return france_regions_geo
france_regions_geo = dept_geo()



@st.cache
def load_data():
    data1 = pd.read_csv('df_produit.csv', sep=' ', dtype={"code_departement":"str"}, error_bad_lines=False, low_memory = False)
    data1 = data1[['poi','categorie_mere','sous_categorie', 'code_departement','latitude','longitude', 'photo','ville','createur_donnée','fournisseur']]
    data1 = data1.rename(columns={'categorie_mere':'categorie'})
    lowercase = lambda x: str(x).lower()
    data1.rename(lowercase, axis='columns', inplace=True)
    data1.longitude = data1.longitude.round(4)
    data1.latitude = data1.latitude.round(4)
    return data1

   
                
data1 = load_data()
#st.write(data)


@st.cache
def load_data():
    data2 = pd.read_csv('df_fete.csv', sep=' ', dtype={"code_departement":"str"}, error_bad_lines=False, low_memory = False)
    data2 = data2[['poi','categorie_mere','sous_categorie','code_departement','region','latitude','longitude','photo','ville','createur_donnée','fournisseur']]
    data2 = data2.rename(columns={'categorie_mere':'categorie'})
    lowercase = lambda x: str(x).lower()
    data2.rename(lowercase, axis='columns', inplace=True)
    data2.longitude = data2.longitude.round(4)
    data2.latitude = data2.latitude.round(4)
    return data2


                
data2 = load_data()
#st.write(data1)


@st.cache
def load_data():
    data3 = pd.read_csv('df_lieu.csv', sep=' ', dtype={"code_departement":"str"}, error_bad_lines=False, low_memory = False)
    data3 = data3[['poi','categorie_mere','sous_categorie','code_departement','region','latitude','longitude','photo','ville','createur_donnée','fournisseur']]
    data3 = data3.rename(columns={'categorie_mere':'categorie'})
    lowercase = lambda x: str(x).lower()
    data3.rename(lowercase, axis='columns', inplace=True)
    data3.longitude = data3.longitude.round(4)
    data3.latitude = data3.latitude.round(4)
    return data3


                
data3 = load_data()
#st.write(data2)


@st.cache
def load_data():
    data4 = pd.read_csv('df_it.csv', sep=' ', dtype={"code_departement":"str"}, error_bad_lines=False, low_memory = False)
    data4 = data4[['poi','categorie_mere','sous_categorie','code_departement','region','latitude','longitude','photo','ville','createur_donnée','fournisseur']]
    data4 = data4.rename(columns={'categorie_mere':'categorie'})
    lowercase = lambda x: str(x).lower()
    data4.rename(lowercase, axis='columns', inplace=True)
    data4.longitude = data4.longitude.round(4)
    data4.latitude = data4.latitude.round(4)
    return data4


                
data4 = load_data()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style1.css")



@st.cache
def load_data_erreur(allow_output_mutation=True):
    data5 = pd.concat([data1,data2,data3,data4])
    e_lat_lon = (data5[(data5.latitude.round(4) > 52)|(data5.latitude.round(4) < 41)|(data5.longitude.round(4) >10)|(data5.longitude.round(4) <-6)])
    e_lat_lon["t_pb"] = "lat_lon"
    e_lat_lon['len_dpt'] = e_lat_lon.code_departement.astype(str).apply(len)
    e_lat_lon = e_lat_lon[e_lat_lon.len_dpt == 2]
    e_lat_lon = e_lat_lon.iloc[:,0:-1]
    return e_lat_lon
data_erreur = load_data_erreur()


@st.cache
def load_data_erreur_map(allow_output_mutation=True):
	data6 = pd.concat([data1,data2,data3,data4])
	e_lat_lon2 = (data6[(data6.latitude.round(4) > 52)|(data6.latitude.round(4) < 41)|(data6.longitude.round(4) >10)|(data6.longitude.round(4) <-6)])
	e_lat_lon2["t_pb"] = "lat_lon"
	e_lat_lon2['len_dpt'] = e_lat_lon2.code_departement.astype(str).apply(len)
	e_lat_lon2 = e_lat_lon2[e_lat_lon2.len_dpt == 2]
	e_lat_lon2 = e_lat_lon2.iloc[:,0:-1]

	for i in list(e_lat_lon2.index):
		if abs(e_lat_lon2.longitude[i])>180:
			e_lat_lon2.drop(i,inplace=True)
    
			
	for i in list(e_lat_lon2.index):
		if abs(e_lat_lon2.latitude[i])>90:
			e_lat_lon2.drop(i,inplace=True)
	return e_lat_lon2

data_erreur_map = load_data_erreur_map()


def get_table_download_link(df):
	csv = data_erreur.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()  
	href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'	




link = '[LinkedIn](https://www.linkedin.com/in/michael-desforges/)'
link1 = '[LinkedIn](http://linkedin.com/in/carlamorenoh)'
link2 = '[LinkedIn](http://www.linkedin.com/in/yvanne-euchin)'
link4 = '[LinkedIn](https://www.linkedin.com/in/corentin-guillo-2a7a82150/)'
link5 = '[LinkedIn](https://www.linkedin.com/in/amar-barache-bb22061b7/)'



def main():

	menu = ["Team","Lieu d'intérêt", "Evénement", "Produit", "Itinéraire", "Maintenance"]
	choice = st.sidebar.radio("Menu", menu)

	

	if choice == "Team":
		


		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


		st.markdown("<h1 style='text-align: center; font-size:15px; color:#A11F40;'>Qu'est ce que DATAtourisme ?</h1>", unsafe_allow_html=True)   

		st.markdown("<h1 style='text-align: center; font-size:29px; color:#57565B;'></h1>", unsafe_allow_html=True)   
		

		col1, col2, col3 = st.beta_columns((1,13,1))   		
   				
		with col1:
   		   
   		   st.markdown("")

		with col2:
			st.markdown("DATAtourisme est un dispositif national visant à faciliter l’accès aux données publiques d’information touristique produites à travers les territoires par les offices de tourisme et les comités départements ou régionaux du tourisme. Il se matérialise par une plateforme de collecte, de normalisation et de diffusion de données en open data, directement reliée aux bases de données territoriales, et repose sur l’animation d’une communauté d’utilisateurs. Le dispositif est copiloté par la Direction générale des entreprises et la fédération ADN Tourisme. Les données collectées sont relatives au recensement de l’ensemble des événements et points d’intérêt touristiques de France (musées, monuments, sites naturels, activités, itinéraires, expos et concerts, etc)", unsafe_allow_html=True)   


		with col3:
			st.markdown("")


		st.markdown("<h1 style='text-align: center; font-size:29px; color:#57565B;'></h1>", unsafe_allow_html=True)   


		st.markdown("<h1 style='text-align: center; font-size:29px; color:#57565B;'></h1>", unsafe_allow_html=True)   




		if st.button("Team"):
   		   st.balloons()





#		st.markdown("<h1 style='text-align: center; font-size:29px; color:#57565B;'>Team</h1>", unsafe_allow_html=True)   

		



		col1, col2, col3, col4, col5 = st.beta_columns(5)   		
   				
		with col1:
   		   
   		   st.image("cm1.jpg", use_column_width=True)
   		   st.markdown("""**Carla&#8239;Moreno**""")
   		   st.markdown("""*Scrum Master*""")
   		   st.markdown(link1, unsafe_allow_html=True)

		with col2:
   		   
   		   st.image("cc.jpg", use_column_width=True)
   		   st.markdown("""**Corentin&#8239;Guillo**""")
   		   st.markdown("""*Product Owner*""")
   		   st.markdown(link4, unsafe_allow_html=True)


		with col3:
   		   
   		   st.image("Yvanne.jpg", use_column_width=True)	
   		   st.markdown("""**Yvanne&#8239;Euchin**""")
   		   st.markdown("""*Equipe Tech*""")
   		   st.markdown(link2, unsafe_allow_html=True)



		with col4:
		   st.image("md.jpg", use_column_width=True)
		   st.markdown("""**Michael&#8239;Desforges**""")
		   st.markdown("""*Equipe Tech*""")
		   st.markdown(link, unsafe_allow_html=True)


		with col5:
		   st.image("ab.jpg", use_column_width=True)
		   st.markdown("""**Amar&#8239;Barache**""")
		   st.markdown("""*Equipe Tech*""")
		   st.markdown(link5, unsafe_allow_html=True)



		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


		page_bg_img = '''
		<style>
		body {
		background-image: url("https://i.ibb.co/cD9CndX/nuages2.jpg");
		background-size: cover;
		}
		</style>
		'''

		st.markdown(page_bg_img, unsafe_allow_html=True)


	if choice == "Produit":
		data = data1




		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')

		st.markdown("<h1 style='text-align:center; font-size:29px; color: #57565B;'>Produit</h1>", unsafe_allow_html=True)




		if st.checkbox('voir dataframe'):
		   st.write(data.iloc[0:100,:])
		 
				 


		f" POI : **{len(data1.index)}** sur **{len(data1.index)+len(data2.index)+len(data3.index)+len(data4.index)}** au total"

		f" Créateurs de données : **{len(data1.createur_donnée.unique())}**"

		f" Fournisseurs : **{len(data1.fournisseur.unique())}**"

		f" Villes : **{len(data1.ville.unique())}**"

		f" POI avec photo :  **{int(round(data1.photo.sum()/len(data1.photo.index)*100))}%**"


				 

		st.markdown(""" # **Densité de POI** """)

		fig = px.density_mapbox(data, lat='latitude', lon='longitude', radius=4,
                        center={"lat": 46.037763, "lon": 4.4}, zoom=4, color_continuous_midpoint = 5,
                        mapbox_style='carto-positron', color_continuous_scale=['blue','grey','darkgrey','red','red'])
		fig.update_layout(coloraxis_showscale=False,margin=dict( l=0, r=0, b=0, t=0, pad = 4 ))
		fig.update_traces(hoverinfo='skip', hovertemplate=None)
		st.plotly_chart(fig)

		



		st.markdown("""# **Par départements**""")


		fig = px.choropleth_mapbox(data, 
                           geojson=france_regions_geo, 
                           color=data.code_departement.value_counts(),
                           locations=data.code_departement.value_counts().index.tolist(), 
                           featureidkey='properties.code',
                           opacity=1,
                           center={"lat": 46.037763, "lon": 2.062783},
                           mapbox_style="carto-positron", zoom=4)

		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.plotly_chart(fig)


		st.markdown(""" # **Répartition des sous-categories** """)
		

		x = list(data.sous_categorie.str.split(',',expand = True).stack().explode().value_counts().drop("HébergementProduit",axis=0).index)
		y=list(data.sous_categorie.str.split(',',expand = True).stack().explode().value_counts().drop("HébergementProduit",axis=0))
		fig = px.bar(x=x,y=y,color_discrete_sequence =['#A11F40'])
		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},showlegend=False,yaxis=dict(title=None), xaxis=dict(title=None,type="category"))
		st.plotly_chart(fig)

		

		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')





	elif choice == "Evénement":
		data = data2



		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')

		st.markdown("<h1 style='text-align:center; font-size:29px; color: #57565B;'>Evénement</h1>", unsafe_allow_html=True)



		if st.checkbox('voir dataframe'):
		   st.write(data.iloc[0:100,:])
		 

		f" POI : **{len(data2.index)}** sur **{len(data1.index)+len(data2.index)+len(data3.index)+len(data4.index)}** au total"

		f" Créateurs de données : **{len(data2.createur_donnée.unique())}**"

		f" Fournisseurs : **{len(data2.fournisseur.unique())}**"

		f" Villes : **{len(data2.ville.unique())}**"

		f" POI avec photo :  **{int(round(data2.photo.sum()/len(data2.photo.index)*100))}%**"
			
		

		st.markdown(""" # **Densité de POI** """)

		fig = px.density_mapbox(data, lat='latitude', lon='longitude', radius=4,
                        center={"lat": 46.037763, "lon": 4.4}, zoom=4, color_continuous_midpoint = 5,
                        mapbox_style='carto-positron', color_continuous_scale=['blue','grey','darkgrey','red','red'])
		fig.update_layout(coloraxis_showscale=False,margin=dict( l=0, r=0, b=0, t=0, pad = 4 ))
		fig.update_traces(hoverinfo='skip', hovertemplate=None)
		st.plotly_chart(fig)

		st.markdown("""# **Par départements**""")

		fig = px.choropleth_mapbox(data, 
                           geojson=france_regions_geo, 
                           color=data.code_departement.value_counts(),
                           locations=data.code_departement.value_counts().index.tolist(), 
                           featureidkey='properties.code',
                           opacity=1,
                           center={"lat": 46.037763, "lon": 2.062783},
                           mapbox_style="carto-positron", zoom=4)

		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.plotly_chart(fig)


		st.markdown(""" # **Répartition des sous-categories** """)

		x = list(data.sous_categorie.str.split(', ',expand = True).stack().explode().value_counts().index)
		y=list(data.sous_categorie.str.split(', ',expand = True).stack().explode().value_counts())
		fig = px.bar(x=x,y=y,color_discrete_sequence =['#A11F40'])
		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},showlegend=False,yaxis=dict(title=None), xaxis=dict(title=None,type="category"))
		st.plotly_chart(fig)


		

		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')



	elif choice == "Lieu d'intérêt":
		data = data3



		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


		st.markdown("<h1 style='text-align:center; font-size:29px; color: #57565B;'>Lieux d'intérêt</h1>", unsafe_allow_html=True)



		if st.checkbox('voir dataframe'):
		   st.write(data.iloc[0:100,:])
		   
		   
		



		f" POI : **{len(data3.index)}** sur **{len(data1.index)+len(data2.index)+len(data3.index)+len(data4.index)}** au total"

		f" Créateurs de données : **{len(data3.createur_donnée.unique())}**"

		f" Fournisseurs : **{len(data3.fournisseur.unique())}**"

		f" Villes : **{len(data3.ville.unique())}**"

		f" POI avec photo :  **{int(round(data3.photo.sum()/len(data3.photo.index)*100))}%**"

				

		st.markdown(""" # **Densité de POI** """)

		fig = px.density_mapbox(data, lat='latitude', lon='longitude', radius=4,
                        center={"lat": 46.037763, "lon": 4.4}, zoom=4, color_continuous_midpoint = 5,
                        mapbox_style='carto-positron', color_continuous_scale=['blue','grey','darkgrey','red','red'])
		fig.update_layout(coloraxis_showscale=False,margin=dict( l=0, r=0, b=0, t=0, pad = 4 ))
		fig.update_traces(hoverinfo='skip', hovertemplate=None)
		st.plotly_chart(fig)

		st.markdown("""# **Par départements**""")

		fig = px.choropleth_mapbox(data, 
                           geojson=france_regions_geo, 
                           color=data.code_departement.value_counts(),
                           locations=data.code_departement.value_counts().index.tolist(), 
                           featureidkey='properties.code',
                           opacity=1,
                           center={"lat": 46.037763, "lon": 2.062783},
                           mapbox_style="carto-positron", zoom=4)

		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.plotly_chart(fig)

		st.markdown(""" # **Répartition des sous-categories** """)

		x = list(data.sous_categorie.str.split(', ',expand = True).stack().explode().value_counts().index)
		y=list(data.sous_categorie.str.split(', ',expand = True).stack().explode().value_counts())
		fig = px.bar(x=x,y=y,color_discrete_sequence =['#A11F40'])
		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},showlegend=False,yaxis=dict(title=None), xaxis=dict(title=None,type="category"))
		st.plotly_chart(fig)



		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')



	elif choice == "Itinéraire":
		data = data4




		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


		st.markdown("<h1 style='text-align:center; font-size:29px; color: #57565B;'>Itinéraire</h1>", unsafe_allow_html=True)



		if st.checkbox('voir dataframe'):
		   st.write(data.iloc[0:100,:])
		 		   

		f" **POI** : **{len(data4.index)}** sur **{len(data1.index)+len(data2.index)+len(data3.index)+len(data4.index)}** au total"

		f" Créateurs de données : **{len(data4.createur_donnée.unique())}**"

		f" Fournisseurs : **{len(data4.fournisseur.unique())}**"

		f" Villes : **{len(data4.ville.unique())}**"

		f" POI avec photo :  **{int(round(data4.photo.sum()/len(data4.photo.index)*100))}%**"

				 	

		st.markdown(""" # **Densité de POI** """)

		fig = px.density_mapbox(data, lat='latitude', lon='longitude', radius=4,
                        center={"lat": 46.037763, "lon": 4.4}, zoom=4, color_continuous_midpoint = 5,
                        mapbox_style='carto-positron', color_continuous_scale=['blue','grey','darkgrey','red','red'])
		fig.update_layout(coloraxis_showscale=False,margin=dict( l=0, r=0, b=0, t=0, pad = 4 ))
		fig.update_traces(hoverinfo='skip', hovertemplate=None)
		st.plotly_chart(fig)

		st.markdown("""# **Par départements**""")

		fig = px.choropleth_mapbox(data, 
                           geojson=france_regions_geo, 
                           color=data.code_departement.value_counts(),
                           locations=data.code_departement.value_counts().index.tolist(), 
                           featureidkey='properties.code',
                           opacity=1,
                           center={"lat": 46.037763, "lon": 2.062783},
                           mapbox_style="carto-positron", zoom=4)

		fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
		st.plotly_chart(fig)

		

				

			
		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')

	elif choice == "Maintenance":

		image = Image.open('DATAtourisme.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


		mdp = st.text_input("Mot de passe ?")


		st.write()
		if mdp == "Les+tour1stes.":
			if st.checkbox('voir dataframe'):
				st.write(data_erreur)
				st.markdown("")
				download = st.button('télécharger')
				if download:
					csv = data_erreur.to_csv(index=False)
					b64 = base64.b64encode(csv.encode()).decode()  
					linko= f'<a href="data:file/csv;base64,{b64}" download="data_erreur.csv">Download csv file</a>'
					st.markdown(linko, unsafe_allow_html=True)
				 	

			f" Départements sans fournisseurs : **{data_erreur[data_erreur.fournisseur.isna()].code_departement.unique()}**"
			f" Départements sans créateur : **{data_erreur[data_erreur.createur_donnée.isna()].code_departement.unique()}**"
			f" Fournisseurs sans région : **{data_erreur[data_erreur.region.isna()].fournisseur.unique()}**"
			st.markdown("")
			st.markdown(""" # **Carte des erreurs latitude & longitude** """)
			st.markdown("")
			st.map(data_erreur_map)

		image = Image.open('WCS.png')
		st.image(image, use_column_width = True, output_format = 'PNG')


				



	else:
		st.subheader("""  """)

	
	
		
		
if __name__ == '__main__':
		main()








































