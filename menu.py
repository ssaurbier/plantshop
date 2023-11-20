import streamlit as st
import pandas as pd
from PIL import Image
import requests

# Page setup
st.set_page_config(layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>Steve's Greenery</h1>", unsafe_allow_html=True)

# Add space below the title
st.write("<br><br>", unsafe_allow_html=True)

# Splitting the page into two columns for the description and photograph
col1, spacer, col2 = st.columns([5, 1, 5])  

# Overview in  left column
with col1:
    description = """
    Welcome to my plant shop! 

    * **About** 
      * I live on the UWS and grow a lot of plants. Pruning is a basic element of plant care, and at this point, I'm generating a few plants a month from maintenance - I am a small-time plantfarmer by accident. See below for context.

    * **Offering** 
      * I'm selling plants. I have any stage of plant development: from a single cutting, up to fully mature and custom arrangements.
        * <u>Cutting</u>: You pick, I cut.
        * <u>Rooted Cutting</u>: This is a cutting that is rooted, either in dirt or water. You need to plant it.
        * <u>Planted Cutting</u>: This is just a rooted cutting in a nursery pot with dirt. Put it in its spot - it's ready to go.
        * <u>Mature Stem</u>: This is a stem I've been growing for a while. It's just living life, but you can have it.
        * <u>Full Plants</u>: I have about 90 plants. I'm not going to price them all out, but you're welcome to them.
        * <u>Custom arrangements</u>: Get the perfect plants for your living space. Have a concrete vision, but no green thumb? I'll make it for you. Don't know what you want? We'll figure it out.

    * **Pricing** 
      * The table is priced per-stem, in consideration of dirt and nursery pots, as relevant. e.g., 10 pothos cuttings are \$5, and 4 potted aglaonema stems are $40. 

    * **Availability** 
      * What I have listed is what I have readily available. I have plenty of other species.

    * **Other Services** 
      * <u>Plant Doctor</u>: Are your plants sick? They can probably bounce vack. I'll diagnose problems and find a solution. 
      * <u>Plant Sitter</u>: Going on a long vacation? Do you have a calathea that hates you? I'll take good care of them while you're gone.

    * **[Plant Care Advice](#plant-care-advice)**
      * I plan on adding to this section.

    All photos below are generic. I have too many plants to photograph, and they're often repotted. Browse through the selection and find the perfect plant for your spaaaaaace. Happy planting!
    """
    st.markdown(description, unsafe_allow_html=True)



# Pic in right column
with col2:
    image_path = "aglaonema.jpg"
    image = Image.open(image_path)
    image = image.rotate(-90, expand=True)
    st.image(image, width=600)

st.write("<br><br>", unsafe_allow_html=True)

#  table data
plants = ["Pothos", "Algerian Ivy", "Kalanchoe", "Philodendron Brasil", "Maranta", 
          "ZZ", "Ti Plant", "Aglaonema", "Haworthia", 
          "Monstera Adansonii", "Monstera Deliciosa"]

prices = {
    "Cutting": ["$0.50", "$2.00", "$2.00", "$2.00", "$3.00", 
                "$3.00", "$4.00", "$4.00", "$4.00", 
                "$4.00", "$4.00"],
    "Rooted Cutting": ["$1.00", "$4.00", "$4.00", "$4.00", "$5.00", 
                       "$5.00", "$8.00", "$8.00", "$8.00", 
                       "$8.00", "$8.00"],
    "Planted Cutting": ["$3.00", "$7.00", "$7.00", "$7.00", "$10.00", 
                        "$10.00", "$15.00", "$15.00", "$15.00", 
                        "$15.00", "$15.00"],
    "Mature Stem": ["$4.00", "$10.00", "$10.00", "$10.00", "$15.00", 
                    "$15.00", "$20.00", "$20.00", "$20.00", 
                    "$20.00", "$20.00"]
}

# CSS to build table
custom_css = """
<style>
table {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
}
th, td {
    text-align: center;
}
td:nth-child(1) {
    text-align: left;
}
</style>
"""


# inject CSS with markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(prices, index=[f"<a href='#{plant.replace(' ', '-').lower()}'>{plant}</a>" for plant in plants])

st.markdown("<h1 style='text-align: center;'>Menu</h1>", unsafe_allow_html=True)

# Displaying the table using markdown
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
st.write("<br><br><br>", unsafe_allow_html=True)



plant_details = {
    "Fittonia": {
        "Sun Exposure": "Bright indirect light",
        "Soil Type": "Moist, well-draining soil",
        "Native Area": "Tropical rainforests of South America, principally Peru",
        "Toxicity": "Non-toxic",
        "Ease of Ownership": "4/5",
        "Light": "As a tropical plant that naturally grows in the humid, bright shade of tropical forests, this plant prefers similar conditions when grown as a houseplant. It dislikes full sunlight, preferring bright, indirect sun, such as that offered by north-facing windows. It will also thrive under fluorescent lights.",
        "Soil": "Fittonia grows well in standard potting soil with a peat-moss base. The soil should retain some moisture but should also drain well.",
        "Water": "Keeping the plant appropriately moist can be a challenge. Nerve plant is prone to collapse if it's allowed to dry out. Although it will recover quickly if thoroughly watered, repeated fainting spells will eventually take their toll on the plant. At the other extreme, Fittonia plants that are allowed to stagnate in water will develop yellowed, limp leaves.",
        "Atmosphere & Humidity": "Nerve plant thrives at temperatures around 70 degrees Fahrenheit but will tolerate a range from the low 60s to low 80s. These plants prefer humid conditions similar to those found in rainforests. Regular misting will keep the plants from drying out. In arid climates or during the dry months of winter, using a room humidifier may be helpful. Terrariums or bottle gardens are naturally moist environments well suited to the plant.",
        "Fertilizer": "During its growing season, feed plants weekly with a weak dose of liquid fertilizer formulated for tropical plants. A balanced 5-5-5 fertilizer diluted to half strength is a good formulation.",
        "Propagation": "Nerve plants propagate readily from leaf-tip cuttings. Take the leaf-tip cuttings in late spring or early summer, at the same time you repot the plant. Make sure to include at least two growing nodes on the cutting to obtain the best results. Once you've potted up the cutting in a peat-based soil mix, you can expect roots to sprout within two to three weeks. Use of a rooting hormone is not usually necessary, but if your conditions are less than ideal (too dry or too cool), rooting hormone might increase your chances of success.",
        "img_link": "https://gardengoodsdirect.com/cdn/shop/files/red-fittonia-7857539678272_560x560_crop_center.jpg?v=1695438257"
    },
    "Ti Plant": {
        "Sun Exposure": "Partial sun",
        "Soil Type": "Loamy or sandy",
        "Native Area": "Eastern Asia, Australia, Pacific Islands",
        "Toxicity": "Toxic to cats and dogs",
        "Ease of Ownership": "3/5",
        "Light": "Select a location that gets a whole day of full to partially filtered sunlight. While Ti can tolerate lots of heat, this 'good luck plant' doesn't have quite enough fortune to handle drought. Ensure that the roots stay moist in light filtered shade. Too much direct light and heat may cause the foliage to burn.",
        "Soil": "Ti plants prefer slightly acidic soil that is fertile and well-drained. Maintain moisture in sandy or loamy soil (avoid wet or hard clay and sites where there could be salt spray). If planted in an area that is too shady or soggy, roots and stems may rot, snail and slug damage may occur, and the plant will be susceptible to leaf spot. When planting, gently remove the ti plant from its pot. Dust off any excess soil from its roots. Cut any damaged or dead roots so all that is left of the root system is healthy, firm and white. Establish in the ground. Firmly cover with soil around the root ball.",
        "Water": "Water deeply at soil level to keep the foliage dry. Continue to water regularly during the growing season. Tepid, not cold, water will encourage the soil to dry out somewhat, but not completely, in between irrigation. A two- to -six-inch deep layer of mulch, four inches away from the trunk's base, will keep the water from evaporating. In fall and winter, water sparingly.",
        "Atmosphere & Humidity": "",
        "Fertilizer": "Whether potted or planted outside, feed ti plants with a slow-release fertilizer that is well-balanced in nitrogen, phosphorus and potassium (8-8-8 or 10-10-10). Spread the fertilizer evenly around the soil at least one foot away from the plant's base. Water deeply.",
        "Propagation": "Propagate by simple layering or divisions. Learn to spread the good fortune of the Ti plant around your garden and you'll be rewarded with vibrant foliage for years to come.",
        "img_link": "https://exoticforest.com/cdn/shop/products/2White_29ab2a34-4f1e-494e-b0b0-f8b940bd22c0_2400x.jpg?v=1630787433"
    },
    "Aglaonema": {
        "Sun Exposure": "Full, partial shade",
        "Soil Type": "Peaty, moist, well-drained",
        "Native Area": "Asia",
        "Toxicity": "Toxic, especially to pets",
        "Ease of Ownership": "4/5",
        "Light": "Darker green varieties of Chinese evergreens can grow in near-shade, while the variegated varieties require a bit more bright light. Take care not to expose any of the plants (no matter the variety) to direct sunlight, as the harsh rays can easily burn the delicate leaves.",
        "Soil": "Ultimately, the Chinese evergreen isn't particularly picky when it comes to the soil it's planted in. Typically, a well-drained, slightly acidic potting soil is perfect for the plant. If you find that your chosen soil is retaining too much water, try mixing in sand or perlite to aid in drainage. You should also make sure to plant your Chinese evergreen in a pot with ample drainage holes at its base.",
        "Water": "The Chinese evergreen plant thrives in moist—but not water-logged—soil. To achieve this balance, water your plant thoroughly, then allow it to dry out before watering again. You can maintain this cadence through the spring, summer, and fall, tapering off in the winter (but never letting the plant dry out completely).",
        "Atmosphere & Humidity": "These plants do not like cold drafts or temperatures below 65 degrees Fahrenheit. Be sure to keep your Chinese evergreen away from windows or vents that blast in cool temperatures—the warmer the spot you can find, the better. Due to its high humidity requirements, some growers consider Chinese evergreen to be a greenhouse plant. It will do best in the warm, humid, and bright environment of a greenhouse, but it can be successfully grown indoors by coming as close as possible to these conditions. To increase the humidity levels around your plant, mist it frequently, and consider placing it in a humidity-prone area of your home, like your kitchen or bathroom. If your home is particularly dry, you can invest in a small space humidifier to put near your plant.",
        "Fertilizer": "For best results, feed your Chinese evergreen with slow-release pellets or liquid fertilizer twice a year, at the beginning and end of its growing season.",
        "Propagation": "Chinese evergreens can be propagated using stem cuttings or by dividing the plants during repotting. To propagate with stem cuttings, wait until the middle of the summer (when the weather is the warmest) and select a stem from the mother plant that's several inches long. Plant cut side down it in a separate pot, in soil that has been treated with a rooting hormone. Keep the soil moist and the cutting should take root within three to four weeks.",
        "img_link": "https://cdn-jcikh.nitrocdn.com/DsiAFwZamduvjHAuLuxHIpjGGdDXxppJ/assets/images/optimized/rev-a92e0a6/littleprinceplants.com/wp-content/uploads/2021/09/Aglaonema-Jazzed-Gems%E2%84%A2-Sapphire-Suzanne-Chinese-Evergreen-Plant-4-scaled.jpg"
    },
    "Kalanchoe": {
        "Sun Exposure": "Full , partial sun",
        "Soil Type": "Well-draining, potting or succulent",
        "Native Area": "Africa",
        "Toxicity": "Very toxic to animals",
        "Ease of Ownership": "4/5",
        "Light": "Kalanchoe plants need a lot of sunlight to bloom, so they should be kept in a room with an abundance of bright, natural light. Avoid placing them on windowsills or in direct sunlight, however, as it can scorch the leaves and cause the plant not to bloom.",
        "Soil": "A Kalanchoe plant will grow best in well-drained soil, so choose or create a blend that doesn't retain too much moisture, like a 50 percent potting soil and 50 percent cactus mix or a 60 percent peat moss and 40 percent perlite mix. To ensure proper drainage and avoid an overly-moist environment, you can also plant your Kalanchoe in a clay pot, which can help wick excess water from the soil.",
        "Water": "If you have a habit of forgetting to water your plants every once in a while, a Kalanchoe may be the perfect pick for you. The hearty plant does well with minimal water, requiring a complete saturation only every few weeks or so (and even less often during the winter months). Let the soil of your Kalanchoe dry out completely in between waterings (this helps to prevent root rot), then water to the point of saturation. If you're not sure if the soil is adequately dry (and therefore, ready to be watered), simply stick your finger into the first few inches—if you feel any moisture at all, check back again in a few days. Because the Kalanchoe is a succulent, its leaves are actually capable of storing water, so even if you time your watering a few days late, the plant will be just fine.",
        "Atmosphere & Humidity": "Environment is important to the Kalanchoe, though it's not as picky other indoor houseplants. Generally, your plant will thrive at temperatures ranging from 55–80 degrees Fahrenheit—meaning, with the exception of not letting the plant freeze, you don't have to do much to create the proper indoor environment. When it comes to humidity, the Kalanchoe plant is not picky and does not require certain moisture levels in the air.",
        "Fertilizer": "Like most flowering plants, Kalanchoe can benefit from fertilizer. This is especially important around the time of bloom, so feed with a well-balanced fertilizer blend once a month during the spring and summer months. If you're struggling to help your plant achieve its flowering potential, look for a fertilizer blend that includes potassium, which can help it produce added buds next time it blooms.",
        "Propagation": "Kalanchoe is very simple to propagate. To do so, cut a segment of stem several inches long from a mature plant. Allow it to dry out for a few days, or until the end appears to have 'healed' shut. Then, plant in soil comprised of the same mixture (above) used to grow the mother plant. Let sit (do not water) and the stem should take root within a month.",
        "img_link": "https://assets.eflorist.com/site/EF-12330/assets/products/PHR_/sku11391064.jpg"
    },
    "Algerian Ivy": {
        "Sun Exposure": "Whatever",
        "Soil Type": "Neutral, well-draining",
        "Native Area": "North Africa",
        "Toxicity": "Mildly Toxic",
        "Ease of Ownership": "5/5",
        "Light": "This ground cover will grow best in full shade to partial sun. Its color contrast will be strongest in a location with ample indirect light, but it can be grown in shady areas and beneath trees also. Avoid full sun to avoid the leaves getting crisped in summer.",
        "Soil": "Algerian ivy can be grown in most any soil with decent drainage. It's drought tolerant but does best in a moderately moist soil in partial shade.",
        "Water": "This ivy is drought tolerant, but in warmer zones it should be grown where it won't dry out in full sun. It doesn't generally need extra watering, but anecdotally some gardeners find the colors are more vibrant if it has steady moisture. If there is an unusually dry spring, some watering will help it generate spring growth sooner.",
        "Atmosphere & Humidity": "Other than being planted in its recommended hardiness zones, there are no temperature requirements for Algerian ivy. If your area has harsh winters, you will want to plant it where it will have some shelter from strong or drying winds, or places where run off and freezing could cause it to be encased in ice for long periods of time.",
        "Fertilizer": "",
        "Propagation": "Propagate with semi-hardwood cuttings of the vines in late summer. Grow in containers and plant the following spring after frost danger has passed.",
        "img_link": "https://unclejohnsplants.com/wp-content/uploads/2023/03/Algerian-Green-Ivy-HB-Front.jpg"
    },
    "Philodendron Brasil": {
        "Sun Exposure": "Partial sun",
        "Soil Type": "Loamy, well-drained",
        "Native Area": "Central America, South America",
        "Toxicity": "Toxic to humans and animals",
        "Ease of Ownership": "5/5",
        "Light": "Philodendrons typically grow best in partial sunlight. They naturally would get dappled light under a tropical canopy, not direct sun. Indoors, set them up by a window that gets bright, indirect light. Too little light can result in leggy growth with lots of space in between the leaves. But too much light can cause many of the leaves to turn yellow at the same time. (Only a few leaves yellowing is typically just normal aging.)",
        "Soil": "Philodendrons like a loose potting soil that’s rich in organic matter. The soil must have good drainage. For container plants, it’s recommended to replace your philodendron’s soil every couple of years or so. These plants are sensitive to salts that accumulate in the soil via watering, which can cause leaf browning and yellowing. You can periodically flush out some of the salts by watering your container thoroughly until water comes out of its drainage holes. But eventually the soil will need refreshing.",
        "Water": "These plants generally like a moderate amount of soil moisture. Water whenever the top inch of soil has dried out. Both overwatering and underwatering can cause the leaves to droop, so gauge when it’s time to water by the soil dryness and not necessarily the leaves. Philodendrons don’t do well sitting in soggy soil, as this can lead to root rot. The non-climbing varieties tend to have a little more drought tolerance than the vining species.",
        "Atmosphere & Humidity": "The temperature tolerance of philodendrons varies based on the species. In general, they should not be exposed to temperatures below 55 degrees Fahrenheit. Indoors, protect them from cool drafts, such as those from an air-conditioning vent. These plants do like humidity, so if you live in a dry climate you might have to boost humidity around your philodendron. To do so, you can mist the plant every few days with water from a spray bottle. You also can place the container on a tray of pebbles filled with water, ensuring that the bottom of the container isn't touching the water, which can lead to root rot.",
        "Fertilizer": "Use a balanced liquid fertilizer monthly on your plant in the spring and summer. Then, reduce feeding to every six to eight weeks in the fall and winter. If your plant isn’t getting enough food, its growth will be slower than normal and its leaves might appear smaller than usual.",
        "Propagation": "The vining philodendrons are easy to propagate from cuttings. Simply cut roughly a 6-inch portion of the stem, and place it in a container of water to develop roots. Using a rooting hormone will increase the chances of success, but it's usually not necessary. Once several roots have developed, pot the cutting in moist soil.",
        "img_link": "https://gardengoodsdirect.com/cdn/shop/files/philodendron-brasil-13501913628714_1200x1200.jpg?v=1695335829"
    },
    "ZZ": {
        "Sun Exposure": "Whatever",
        "Soil Type": "Well-draining, potting or succulent",
        "Native Area": "Asia",
        "Toxicity": "Mildly Toxic",
        "Ease of Ownership": "5/5",
        "Light": "ZZ plants are tolerant of a wide range of lighting conditions which makes them well-suited to indoor growing. While ZZ plants can ‘technically’ survive without any natural light, they do best in bright, indirect light and can quickly become leggy when not given enough light. Avoid direct sunlight as this can scorch the leaves of a ZZ plant.",
        "Soil": "ZZ plants are not overly picky about their potting medium as long as it is well-draining. Most standard potting mixes should be sufficient for your ZZ plant. If additional drainage is required, mixing in perlite or sand will help.",
        "Water": "Thanks to their thick rhizomes, ZZ plants are extremely drought-tolerant and can handle infrequent watering. In general, ZZ plants should be watered once the soil dries out completely—usually once every week or two depending on their growing conditions. But if necessary, ZZ plants can survive months without water, so it is better to under-water your ZZ plant than to over-water it.",
        "Atmosphere & Humidity": "Average household temperatures and humidity are fine for ZZ plants. In general, ZZ plants do not tolerate cold temperatures well (no lower than 45F) so avoid placing your ZZ plant in a location close to drafts or particularly cold areas of your home. ZZ plants don't require humid conditions, but if your home runs on the dry side consider increasing the humidity around your ZZ plant by purchasing a humidifier or placing it on top of a water tray.",
        "Fertilizer": "Generally, ZZ plants do not require regular fertilizing to thrive. However, to keep the plant in optimal health, fertilize your ZZ plant with indoor plant fertilizer diluted to half-strength one to two times during its active growing season.",
        "Propagation": "ZZ plants propagate in two main ways: through division, and through leaf cuttings. Propagation by division is the simplest way to create more ZZ plants—simply separate the rhizomes the next time you repot your ZZ plant and plant in a separate container. Alternatively, ZZ plants can also be propagated by leaf cuttings. Take a cutting from a mature ZZ plant that has at least two leaves and a portion of the stem and plant it in a well-draining soil mix. Place the cutting in a warm spot that receives bright (but not direct) light throughout the day. This method takes longer than propagation by division and you may be waiting six to nine months before any new rhizomes begin to grow!",
        "img_link": "https://aerogarden.com/dw/image/v2/BGFS_PRD/on/demandware.static/-/Sites-consolidated-master-catalog/default/dw552dd7e6/images/hi-res/000680105_Full_2000x2000.jpg?sw=800&sh=800"
    },
    "Monstera Adansonii": {
        "Sun Exposure": "Partial sun",
        "Soil Type": "Moist, well-drained",
        "Native Area": "Central America",
        "Toxicity": "Toxic",
        "Ease of Ownership": "5/5",
        "Light": "Because of the Swiss cheese plant's tropical origin, Monstera adansonii needs sunlight, but it's best if the light is bright and indirect. It's used to thriving under the cover of large trees in the jungle, and the foliage can easily burn if it's exposed to too much direct sun. If direct sunlight is unavoidable, limit exposure to just two or three hours of morning sun.",
        "Soil": "Swiss cheese plants grow best in peat-based potting mix, which will help to trap moisture in the soil without causing it to become waterlogged. For strong growth, aim for a soil pH between 5.5 and 7.",
        "Water": "Swiss cheese plants like to be consistently moist but not soaked. Before watering your Swiss cheese plant, stick your finger into the soil about an inch deep. If the soil feels nearly dry to the touch, it's time to water the plant. Irrigate until a little water runs out of the container's drainage holes.",
        "Atmosphere & Humidity": "Swiss cheese plants like to be consistently moist but not soaked. Before watering your Swiss cheese plant, stick your finger into the soil about an inch deep. If the soil feels nearly dry to the touch, it's time to water the plant. Irrigate until a little water runs out of the container's drainage holes.",
        "Fertilizer": "To fertilize a Swiss cheese plant, use a balanced fertilizer made for houseplants. A fertilizer with an N-P-K ration of 5-2-3 is perfect to keep the roots and leaves of the Swiss cheese plant healthy. After potting a new Swiss cheese plant, wait at least four to six months to fertilize it, as potting mix typically already has slow-release fertilizer in it, and the sensitive roots need time to settle after the disturbance of repotting. After that, fertilize your Swiss cheese plant monthly during the growing season (March-September), using an all-purpose liquid fertilizer that has been diluted by half.",
        "Propagation": "Monsteras propagate incredible easily via cuttings.",
        "img_link": "https://www.planetnatural.com/wp-content/uploads/2023/04/monstera-adansonii.jpg"
    },
    "Monstera Deliciosa": {
        "Sun Exposure": "Partial sun",
        "Soil Type": "Well-drained",
        "Native Area": "Central America",
        "Toxicity": "Toxic",
        "Ease of Ownership": "5/5",
        "Light": "This evergreen prefers bright, indirect sunlight between 65 and 75 degrees Fahrenheit. Too much direct light in warmer months may burn the foliage. Still, set indoor plants outside at least once a year in direct sunlight to encourage lush growth.",
        "Soil": "When established in a container, it requires peat-based potting media. Outdoors, it is suitable for light sandy, medium loamy, and heavy clay soils with acid or neutral pH. Even so, it thrives most in well-drained, moderately moist soil. You'll also spot intricate aerial roots growing out of the soil, which benefit the plant by supporting the stems that hold leaves that can grow up to 3 feet long.",
        "Water": "Give the plant regular waterings during the growing season every one to two weeks. Water until excess drains through drainage holes. Do not return the excess water to the plant's container because it has taken all the necessary water. The soil will need to dry out slightly in between waterings. Water only occasionally in fall and winter. To increase humidity indoors, mist the foliage using a spray bottle of demineralized water or rainwater.",
        "Atmosphere & Humidity": "Monstera deliciosa grows best in temperatures between 65 and 85 degrees Fahrenheit. It can tolerate temperatures down to 50 F and up to 90 F but will stop growing at these extremes. It prefers high humidity, about 60%. Mist it or provide a humidifier to keep its leaves moist daily.",
        "Fertilizer": "Choose a balanced liquid 20-20-20 fertilizer to feed the plant every few weeks during the growing season. Dilute 1/2 teaspoon of the fertilizer in a gallon of water. Use the diluted fertilizer in place of regular watering. Pour the mixture into the soil until it begins to flow out of the drainage holes. Throw out the excess diluted fertilizer because the plant has taken what it needs and cannot use the extra that it drains off.",
        "Propagation": "Monstera deliciosa can be easily propagated by stem cuttings from pruning.",
        "img_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNaGmxP_E1uAD-rztg4rVJyut0QDKreMGVYw&usqp=CAU"
    },
    "Haworthia": {
        "Sun Exposure": "Full, partial sun",
        "Soil Type": "Sandy, well-drained",
        "Native Area": "Africa",
        "Toxicity": "Non-toxic",
        "Ease of Ownership": "5/5",
        "Light": "Haworthia species like bright light but not exceptionally strong direct sunlight. They make attractive small potted houseplants and can be moved outdoors for the summer months. In their native environment, they are often found in the slight shade of a rock or other object. Indoors, haworthias do best near an east- or west-facing window.",
        "Soil": "These plants like sandy or gravelly soil with excellent drainage. Use a cactus potting mix or another fast-draining potting soil for container plants. Mix the soil with perlite, aquarium gravel, or pumice to improve soil drainage.",
        "Water": "Water whenever the top inch of soil has dried out during spring and summer, but ensure the soil is never waterlogged. Reduce watering to just enough in the fall and winter to keep the leaves plump. Never allow water to collect in the rosette; this can lead to rot.",
        "Atmosphere & Humidity": "Haworthia species like warm temperatures between 70 and 95 degrees Fahrenheit in the summer and cool temperatures down to 50 degrees Fahrenheit in the winter. They can be damaged when temperatures fall to 40 degrees Fahrenheit and lower. Humidity isn't an issue for this plant. It requires good ventilation, especially at night when it takes in carbon dioxide for photosynthesis.",
        "Fertilizer": "Follow label instructions to fertilize haworthia during the spring and summer growing seasons with a cactus fertilizer. Don't feed during the fall and winter.",
        "Propagation": "The best way to propagate haworthia plants is via its offsets, the tiny pups, or new plants growing from the base of a parent plant. Propagation via offsets prevents the parent plant from becoming overcrowded. A convenient time to propagate haworthia is when it has overgrown its container and needs to be repotted. Hawthoria is best propagated via the division of its offsets.",
        "img_link": "https://idiggreenacres.com/cdn/shop/products/Succulents_Haworthia_Limifolia_c68964cf-b602-4543-8d2a-7c827de885a9_1024x1024.jpg?v=1640798497"
    },
    "Maranta": {
        "Sun Exposure": "Bright indirect",
        "Soil Type": "Moist but well-drained",
        "Native Area": "South America",
        "Toxicity": "Non-toxic",
        "Ease of Ownership": "5/5",
        "Light": "Hang or set your prayer plant near a window where it will receive indirect sunlight. Never set your plant in direct sunlight because the sun will scorch the plant’s leaves or the leaves will develop blotches or patches and fade in color intensity. Prayer plants are generally tolerant of lower light areas. In the winter, when the plants go into dormancy (and sometimes die back completely), provide them with bright light to maintain growth.",
        "Soil": "Prayer plants can prosper in a variety of soils, as long as they're well-draining. Typically, a traditional potting mix works fine, but you can make your own by combining two parts sphagnum peat moss, one part loamy soil, and one part perlite or coarse sand together. In addition, the soil should be acidic, with a pH of 6.0. To improve drainage, add rocks or gravel to the bottom of your pot and be sure that the pot has ample drainage holes.",
        "Water": "During their growing season, water your prayer plant frequently (whenever the top layer becomes dry) and never allow the potting soil to dry out completely. These plants are very susceptible to drought and will not survive long if left unwatered. However, to avoid fungal problems, do not let water sit directly on the leaves or let the plant get soggy. Both insufficient water and overwatering your plant can cause the leaves to turn yellow and drop. When watering your prayer plant, use water that is at least at room temperature, if not slightly warm.",
        "Atmosphere & Humidity": "Prayer plants prefer normal household temperatures between 60 and 80 degrees Fahrenheit. Prolonged lower temperatures can damage the leaves and cause them to drop from the plant. Additionally, prayer plants thrive best in a very humid environment. To increase the humidity available to your plant, you can place a small humidifier nearby, or place the plant atop a tray that has been filled with small stones and water. You can also mist the leaves frequently with room temperature or slightly warm water.",
        "Fertilizer": "Fertilize your prayer plant every two weeks from early spring through fall (reducing to once a month in winter) with a water-soluble houseplant fertilizer diluted to half-strength. If you use too little fertilizer, your plant will grow slowly or hardly at all. However, too much fertilizer can burn the plant's roots—its leaves will start to brown and the plant can even die.",
        "Propagation": "Propagating prayer plants is a surprisingly easy way to increase your collection and make use of larger mother plants.",
        "img_link": "https://midwestfoliage.com/cdn/shop/products/marantared.jpg?v=1640230141"
    },
        "Pothos": {
        "Sun Exposure": "Whatever",
        "Soil Type": "Moist but well-drained",
        "Native Area": "Asia",
        "Toxicity": "Toxic",
        "Ease of Ownership": "5/5",
        "Light": "Pothos likes sun or shade, but you need to watch if it's in too much of either one. When grown indoors, pothos prefers bright but indirect light. Variegated plants sometimes lose their leaf pattern and revert to all-green foliage if they don't receive enough light. Moving them to brighter conditions usually restores the variegation. Suddenly pale-looking leaves mean the plant is receiving too much direct sun.",
        "Soil": "Pothos plants thrive in ordinary, well-draining potting soil that can be on the dry side or even rocky. Pothos thrives in a soil pH ranging from 6.1 to 6.8. It is tolerant of a range of conditions, from neutral to slightly acidic.",
        "Water": "Let your pothos plant's soil dry out completely between waterings. If left in continually damp soil, the plant's roots will rot. Black spots on the leaves (or the sudden collapse of the plant) indicate that the soil has been kept too wet. The plant will indicate when it needs water. When it starts to droop, it needs water to revive it. However, don’t wait until the leaves start to shrivel or the plant will lose some leaves. Dry, brown edges mean the plant was kept dry for too long.",
        "Atmosphere & Humidity": "Pothos should be kept in temperatures that are consistently above 50 degrees. These plants prefer temperatures between 65 and 75 degrees. Pothos plants grow best in high humidity, but they're also very tolerant of low-humidity conditions. If you like, you can increase humidity around the plant by keeping it in a typically humid area of the home, such as a bathroom, or grouping the plant with other tropical houseplants to create a more humid microclimate.",
        "Fertilizer": "Pothos plants are not heavy feeders, but they can benefit from occasional fertilizing during the growing season. Feed pothos plants with a balanced houseplant fertilizer once per month during the spring and summer. Avoid fertilizing in winter when the plant goes dormant.",
        "Propagation": "Pothos are incredibly easy to propagate.",
        "img_link": "https://peaceloveandhappiness.club/cdn/shop/products/houseplants-golden-pothos-6-hanging-1.jpg?v=1658269780"
    }
}

# Individual plant listings with structured data
for plant in plants:
    st.markdown(f"<h2 id='{plant.replace(' ', '-').lower()}'>{plant}</h2>", unsafe_allow_html=True)

    # Creating three columns for table, spacer, and image
    col1, spacer, col2 = st.columns([3, 1, 2])  # Adjust the ratio as needed

    # Displaying information in first column
    with col1:
        st.write("<br><br><br>", unsafe_allow_html=True)

        basic_info_table = pd.DataFrame([plant_details[plant]], 
                                        columns=["Ease of Ownership", "Sun Exposure", "Soil Type", 
                                                 "Native Area", "Toxicity"],
                                        index=[plant])
        st.table(basic_info_table)

    # Spacer column
    with spacer:
        st.write("")

    with col2:
        image_url = plant_details[plant].get("img_link", "")
        if image_url:
            st.image(image_url, width=300)  # Adjust width as needed

    st.markdown("### Care Instructions")
    for key in ["Light", "Soil", "Water", "Atmosphere & Humidity", "Fertilizer", "Propagation"]:
        st.markdown(f"- **{key}**: {plant_details[plant][key]}")

    st.write("<br><br>", unsafe_allow_html=True)

st.markdown("<a name='plant-care-advice'></a>", unsafe_allow_html=True)
st.markdown("## Plant Care Advice", unsafe_allow_html=True)
st.markdown("### Guide to plant lighting", unsafe_allow_html=True)

# Centering  image  
image_url = "https://tonkadale.com/product_images/uploaded_images/light-diagram-v4.jpg"
st.markdown("<div style='text-align: center;'><img src='{}' alt='Light Requirements for Plants' style='width: 85%;'></div>".format(image_url), unsafe_allow_html=True)