# Safe Walking App: Helping provide security and peace of minds to your late night walks# 

### Motivation: ###
Millions have to avoid walking late at night, resort to calling their friends, or just risk going through potentially dangerous routes on their late night walks. Unless you are a city local with experience of all the shady areas, it is difficult to know all the unsafe areas in a city. It is prohibitively time consuming for tourists, travelers, or even those with limited experience of specific areas of the city to manually check the path that google maps provides them all the time. 

### Solution: ###
We have created an application to help you conveniently determine a safe walking path, as well as to keep you safe during your walk. This app can serve to determine a path between two points in NYC, not only based on distance, but also based on safety. It does this while also showing you the locations of streetlights in NYC, as well as a safe word recognition feature, that can be used to discretely trigger alerts in case of an emergency for the user during their walk. 

### Execution: ###
1. We have scraped the map data for the NYC area using osmnx, and stored the graph data. This contains all the walking paths and locations available in NYC, which we can manipulate for path finding.
2. We then used data from the public records of the city of New York, https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Map-Year-to-Date-/2fra-mtpn, to determine past crimes and the locations these crimes have been committed. We tested various variables, such as time of day, presence of artificial lights, time of year etc. We decided on creating a safety score based on the amount of crimes committed in that block, during this particular 2 month stretch of Septemeber - October, from the past 6 years.
3. Using these safety scores, and the previous graph data with lengths between nodes, we multiplied the two to create a safe walking variable for each of the edges. This was used to balance the need to find short paths, with the need to avoid dangerous neighborhoods.
4. We implemented an A* algorithm for path finding between the start and ending points with our custom weight.
5. Next, we scraped data to determine the locations of over 100,000 unique streetlights within NYC from more public record data, available here, https://data.cityofnewyork.us/Social-Services/Street-Light-Road-map-/2bxc-5zsq. This was plotted on the graph along with a circle with set radius, to visually represent the well lit areas along the path of the user. 
6. [Anurag enter info about the location autocomplete stuff here] 
7. To compliment this service we implemented a NLP audio detection AI to recognize your voice along the walk. We set up a safe word registration, that allows the user to pick a safe word, that when said, can trigger an emergency response, such as making emergency alerts or calls.

### Challenges ###
1. During the process of testing out the various features, we implented an astral calculator to determine the stage of sunlight for each of the crimes, as well as weather data. However, this was disregarded for it's relatively low impact on the relative rank of neighborhoods as safe or unsafe. 
2. We tried integrating direct calls or location sharing features, however, because this was a computer application, sending messages or calls proved to be a security risk, and was left unimplemented.
3. Another feature that we looked into was using the H11NY API to access the cameras in NYC and look along each path and location to determine whether areas were safe or unsafe for real time risk assessment. A major difficulty in this however, was that only 500 cctv cameras were publically accessible, which wouldn't cover a large enough portion of the city to prove useful. 

### Future Direction ### 
1. A mobile version of the application shuld be created to more conveniently serve our users, as well as to access features like live location sharing and sending emergency alerts to 911 and close family from the safe word recognition.
2. This can also be expanded to more major cities such as Tokyo, Singapore, London, and more, which have relatively open data that can be used in applications such as this. We can also rely on scraping from google earth data to find the locations of streetlights and cctv cameras to showcase those on our application in areas without as public areas.
3. We can integrate a feature that provides unique cationary warnings based on the risks present in the locations traversed by each path, based on an AI LLM taking in the crime data in those areas, as well as general suggestions, to give a specific response to users.
4. Taking in the user's unique demographics, can be used to weight crimes and risk factors along a path to adjust them based on the different prevelances of crimes against different ages, genders, or races.

### Key Technologies and Datasets used 
1. https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Map-Year-to-Date-/2fra-mtpn
2. https://data.cityofnewyork.us/Social-Services/Street-Light-Road-map-/2bxc-5zsq
3. Flask
4. Osmnx
6. Folium
7. Astral.Sun
8. A* path finding algorithm
9. NLP audio recognition [ayushe insert what you used]
10. Text to Location recognition [anurug insert what u used here]




