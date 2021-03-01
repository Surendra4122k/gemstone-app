import pandas as pd
import pydeck as pdk
import numpy as np
import streamlit as st

st.write("""## **Precious and Semi Precious stones in India**
 ##### _By - Surendra Patro_ """)
st.image('precsemi.jpg', caption='', use_column_width=True)

st.write("""Gemstones are minerals, rocks or organic matter that have been cut, 
polished and then fashioned into a piece of jewelry. In the 1800s, these gemstones were divided into two categories: **precious and semi precious stones** considering their value differentiation at that time.
Nowadays, the categorization is not always correct since the Value parameter is not the only criteria on which experts rely to in order to evaluate a stone.
The quality, the rarity, the provenance are to be taken into consideration.

### Precious stones - 
In regards the so-called precious stones, only four prevail: 
diamonds, rubies, emeralds and sapphires. Sometimes you will can see that a pearl, an opal or a jade are listed as a precious gemstone, but more often they are considered semi-precious.
Traditionally, these four precious stones have been the most expensive and sought after stones.""")
st.image('prec.jpg', caption = 'Precious Stones', use_column_width = True )

st.write("""### Semi precious stones -
Every other gemstone that isn’t one of those four is considered to be semi precious. 
The list goes on and on, but some of the more common ones are: alexandrite, agate, amethyst, aquamarine, garnet, lapis lazuli, moonstone, opal, pearl, peridot, rose quartz, spinel, tanzanite, tourmaline, turquoise and zircon.
This separation between precious and semi precious has no real scientific backing. For example, emerald is a variety of a beryl, so are aquamarines. Emerald is precious while aquamarine is semi precious. 
When this categorization came about, it was mainly due to the value and rarity differences between the 4 precious gemstones and the rest. Today some semi precious gemstones can be worth much more than a precious stone.
As an example, many natural pearls garner huge prices, often worth more than a low quality precious diamond, ruby, emerald or sapphire. Spinels are another example. Additionally, many semi precious stones can be more rare than some of the precious.
Demantoid garnets or tsavorite garnets and many other semi precious gemstones are hard to find, harder to mine and produced in much lower qualities than the precious gemstones.""")

st.image('semi.jpg', caption = 'Semi Precious Stones', use_column_width = True )

st.sidebar.image('woman.jpg', caption='', use_column_width=True)

st.sidebar.header("Select Gemstone for info")
gem = st.sidebar.selectbox("Gemstones found in India ", ('None', 'Corundum - Blue Sapphire', 'Corundum - Ruby' , 'Garnet', 'Beryl - Aquamarine', 'Beryl - Emerald', 'Chrysoberyl', 'Feldspar - Sunstone', 'Feldspar - Moonstone', 'Diamond'))

st.write(f""" ### You've selected {gem}
""")

if gem == "None" :
    st.write("_No gemstone has been selected._")
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

if gem == "Corundum - Blue Sapphire" :
    st.image('sapph.jpg', caption = 'Corundum - Blue Sapphire', use_column_width = True )
    x1 = 33.41
    x2 = 12.33
    x3 = 19.91
    x4 = 0
    y1 = 76.4
    y2 = 75.80
    y3 = 83.16
    y4 = 0
if gem == "Corundum - Ruby" :
    st.image('ruby.jpg', caption = 'Corundum - Ruby', use_column_width = True )
    x1 = 21.25
    x2 = 20.7
    x3 = 16.30
    x4 = 12.33
    y1 = 81.62
    y2 = 83.48
    y3 = 80.43
    y4 = 75.80

if gem == "Garnet" :
    st.image('garnet.jpg', caption = 'Garnet', use_column_width = True )
    x1 = 26.17
    x2 = 26.44
    x3 = 18.85
    x4 = 19.91
    y1 = 75.78
    y2 = 74.63
    y3 = 82.73
    y4 = 83.16

if gem == "Beryl - Aquamarine" :
    st.image('aqua.jpg', caption = 'Beryl - Aquamarine', use_column_width = True )
    x1 = 26.44
    x2 = 24.58
    x3 = 21.46
    x4 = 20.47
    y1 = 74.63
    y2 = 73.71
    y3 = 83.98
    y4 = 84.23

if gem == "Beryl - Emerald" :
    st.image('emerald.jpg', caption = 'Beryl - Emerald', use_column_width = True )
    x1 = 26.44
    x2 = 24.58
    x3 = 26.16
    x4 = 0
    y1 = 74.63
    y2 = 73.71
    y3 = 75.79
    y4 = 0

if gem == "Feldspar - Sunstone" :
    st.image('sun.jpg', caption = 'Feldspar - Sunstone', use_column_width = True )
    x1 = 26.73
    x2 = 24.46
    x3 = 10.88
    x4 = 11.01
    y1 = 85.67
    y2 = 85.59
    y3 = 78.15
    y4 = 76.95

if gem == "Diamond" :
    st.image('diamond.jpg', caption = 'Diamond', use_column_width = True )
    x1 = 24.71
    x2 = 19.01
    x3 = 16.30
    x4 = 0
    y1 = 80.18
    y2 = 81.88
    y3 = 80.43
    y4 = 0

if gem == "Chrysoberyl" :
    st.image('chryso.jpg', caption = 'Chrysoberyl', use_column_width = True )
    x1 = 21.25
    x2 = 21.46
    x3 = 18.32
    x4 = 0
    y1 = 81.62
    y2 = 83.98
    y3 = 82.87
    y4 = 0

if gem == "Feldspar - Moonstone" :
    st.image('moon.jpg', caption = 'Feldspar - Moonstone', use_column_width = True )
    x1 = 26.73
    x2 = 24.46
    x3 = 10.88
    x4 = 11.01
    y1 = 85.67
    y2 = 85.59
    y3 = 78.15
    y4 = 76.95

loc1 = [x1, y1]
loc2 = [x2, y2]
loc3 = [x3, y3]
loc4 = [x4, y4]
df = pd.DataFrame(np.array([loc1, loc2, loc3, loc4]), columns=['lat', 'lon'])
st.write(f" ### Geographic locations of {gem} in India - ")


st.pydeck_chart(pdk.Deck(
  map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
         latitude=28.7,
         longitude=77.102,
         zoom=3.5,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
           get_position='[lon, lat]',
            radius=80000,
            elevation_scale=10,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[lon, lat]',
             get_color='[200, 30, 0, 160]',
             get_radius=80000,
         ),
     ],
 ))


if gem == "Corundum - Blue Sapphire" :
   st.write(""" **Corundum** is an aluminum oxide that commonly forms hexagonal barrel-shaped prisms that taper at both ends or as thin tabular hexagonal plates.
   It has a hardness of 9 on the Mohs scale, making it one of the most durable commercial gemstones.
   It has no dominant cleavage and fractures in a conchoidal manner. 
   A high density of ~4.0 g/cm3 (most silicate minerals are ~2.6 g/cm3) results in corundum occurring in secondary placer deposits and recoverable by panning methods, similar to how you would recover placer gold. Blue corundum is called sapphire. """)

if gem == "Corundum - Ruby" :
    st.write(""" **Ruby** is the most valuable variety of the corundum mineral species, which also includes sapphire. Rubies can command the highest per-carat price of any colored stone. 
    This makes ruby one of the most important gems in the colored stone market. In its purest form, the mineral corundum is colorless. Trace elements that become part of the mineral’s crystal structure cause variations in its color. 
    Chromium is the trace element that causes ruby’s red, which ranges from an orangy red to a purplish red. The strength of ruby’s red depends on how much chromium is present—the more chromium, the stronger the red color. 
    Chromium can also cause fluorescence, which adds to the intensity of the red color.""")

if gem == "Garnet" :
    st.write(""" **Garnets** are a set of closely related minerals that form a group, resulting in gemstones in almost every color. Red garnets have a long history, but modern gem buyers can pick from a rich palette of garnet colors: greens, oranges, pinkish oranges, deeply saturated purplish reds, and even some blues.
Red garnet is one of the most common and widespread of gems, found in metamorphic rocks (which are rocks altered by heat and pressure) on every continent.""")

if gem == "Beryl - Aquamarine" :
    st.write(""" **Aquamarine** is the green-blue to blue variety of the mineral beryl. Its color is usually a light pastel greenish blue.
Heat treatment usually gives it a more bluish appearance. Aquamarine crystals are known to be large in size and relatively clean and well-formed, making them particularly valuable to collectors of mineral specimens.""")

if gem == "Beryl - Emerald" :
    st.write(""" **Emerald** is the green to greenish blue variety of beryl, a mineral species that also includes aquamarine as well as beryls in other colors.
Gem experts differ on the degree of green that makes one stone an emerald and another stone a less-expensive green beryl. Some people in the trade tend to give the name emerald to any green beryl colored by chromium.""")

if gem == "Feldspar - Sunstone" :
    st.write(""" **Sunstone** is a member of the feldspar group. Both the orthoclase and the plagioclase feldspar species boast a sunstone variety. Other feldspar group gems include moonstone, non-phenomenal orthoclase, phenomenal and non-phenomenal labradorite, and amazonite. There are many sunstone varieties. If aventurescence is present, gemologists call it aventurine feldspar. The aventurine feldspar from India has a red-brown bodycolor and sunny glitter. It’s perhaps the best-known sunstone variety.""")

if gem == "Diamond" :
    st.write(""" **Diamond** forms under high temperature and pressure conditions that exist only about 100 miles beneath the earth’s surface. Diamond’s carbon atoms are bonded in essentially the same way in all directions. 
    Without any one of these factors, diamond might be just another mineral. Fortunately, though, this special combination of chemical composition, crystal structure, and formation process gives diamonds the qualities that make them extraordinary.""")

if gem == "Chrysoberyl" :
    st.write(""" **Chrysoberyl** is a beryllium-aluminum oxide mineral with a chemical composition of BeAl2O4. It is distinctly different from the beryllium-aluminum silicate (Be3Al2(SiO3)6 mineral known as "beryl," although the similar names can cause confusion.
Chrysoberyl is not found in deposits that are large enough to allow it to be used as an ore of beryllium. Its only important use is as a gemstone; however, it excels in that use because of its very high hardness and its special properties of chatoyance and color change.""")

if gem == "Feldspar - Moonstone" :
    st.write(""" **Moonstone** is a variety of the feldspar-group mineral orthoclase. During formation, orthoclase and albite separate into alternating layers. When light falls between these thin layers it is scattered producing the phenomenon called adularescence. Adularescence is the light that appears to billow across a gem. 
    Sanidine is another feldspar mineral that can include adularescent gems called moonstones. To be called moonstone, a mineral’s actual identity is not as important as the beauty of its adularescence.""")

