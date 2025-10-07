<h1 align="center">Spotify Genre Classification & Trend Analysis</h1>

<p align="center">
<b>End-to-end data pipeline leveraging the Spotify API, web scraping, and machine learning to classify and analyze musical genres.</b>
</p>

<p align="center">
  <img src="assets/image1.png" height="200" width="auto">
  <img src="assets/image2.png" height="200" width="auto">
</p>

<hr>

<h2>Overview</h2>
<p>
This project builds a complete data workflow to collect, enrich, and analyze Spotify music data — from raw metadata extraction to genre classification and trend modeling.  
It demonstrates real-world skills in <b>data acquisition, preprocessing, NLP, and machine learning</b> by integrating multiple stages into one cohesive system.
</p>

<h2>Impact & Motivation</h2>
<p>
The music industry produces massive amounts of streaming data, but understanding <b>genre relationships</b> and <b>trends in popularity</b> remains challenging.  
This project shows how data engineering and ML techniques can turn raw Spotify metadata into actionable insights, such as:
</p>
<ul>
  <li>Automatically identifying parent genres from thousands of subgenres.</li>
  <li>Analyzing how musical preferences evolve over time.</li>
  <li>Exploring semantic relationships between genres using BERT embeddings.</li>
</ul>

<h2>Project Workflow</h2>

<pre>
1. Data Collection ─ <b>spotify_api.ipynb</b>  
   → Fetch song & artist metadata using the Spotify API  

2. Genre Enrichment ─ <b>genre_scrape.py</b>  
   → Scrape parent-genre mappings from online sources  

3. Genre Classification ─ <b>Final.ipynb</b>  
   → Train ML models to predict parent genres  

4. (Optional) Time-Series Analysis ─ <b>time_series.ipynb</b>  
   → Study popularity trends and temporal patterns  

5. (Optional) Semantic Encoding ─ <b>BERT_genre_encoder.ipynb</b>  
   → Cluster genres using Sentence-BERT embeddings
</pre>

<h2>Key Results</h2>
<ul>
  <li><b>Accurate genre classification:</b> Models such as Random Forest and CatBoost successfully predicted parent genres with strong performance.</li>
  <li><b>Data enrichment at scale:</b> Automated scraping extended Spotify’s metadata with hierarchical genre labels.</li>
  <li><b>Semantic exploration:</b> BERT embeddings revealed meaningful relationships between subgenres.</li>
  <li><b>Temporal insights:</b> Time-series models captured evolving trends in song popularity.</li>
</ul>
<p><i>(Detailed results and visuals are available inside each notebook.)</i></p>

<hr>

<h2>Tech Stack</h2>
<table>
<tr><th>Category</th><th>Tools & Libraries</th></tr>
<tr><td>Data Access</td><td>Spotify API, Spotipy</td></tr>
<tr><td>Data Processing</td><td>Pandas, NumPy, Regex, BeautifulSoup</td></tr>
<tr><td>Machine Learning</td><td>Scikit-Learn, CatBoost, XGBoost</td></tr>
<tr><td>Deep Learning / NLP</td><td>Sentence-Transformers, TensorFlow</td></tr>
<tr><td>Visualization</td><td>Matplotlib, Seaborn</td></tr>
<tr><td>Time-Series Modeling</td><td>Prophet, Statsmodels</td></tr>
<tr><td>Other</td><td>tqdm, Requests</td></tr>
</table>

<hr>

<h2>Repository Structure</h2>
<pre>
spotify-genre-analysis/
 ┣ 📂 notebooks/
 ┃ ┣ spotify_api.ipynb
 ┃ ┣ Final.ipynb
 ┃ ┣ time_series.ipynb
 ┃ ┗ BERT_genre_encoder.ipynb
 ┣ 📂 scripts/
 ┃ ┗ genre_scrape.py
 ┣ 📂 data/
 ┃ ┣ output_with_genres.csv
 ┃ ┗ parent_genre.csv
 ┣ requirements.txt
 ┣ .gitignore
 ┗ README.md
</pre>

<hr>

<h2>Setup & Usage</h2>

<h3>1️⃣ Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>2️⃣ Configure Spotify API credentials</h3>
<p>Create an app on the <a href="https://developer.spotify.com/dashboard/">Spotify Developer Dashboard</a> and add your <b>Client ID</b> and <b>Client Secret</b> in <code>spotify_api.ipynb</code>.</p>

<h3>3️⃣ Run the workflow</h3>
<pre><code># Step 1: Fetch Spotify metadata
jupyter notebook notebooks/spotify_api.ipynb

# Step 2: Scrape parent genres
python scripts/genre_scrape.py

# Step 3: Analyze and classify genres
jupyter notebook notebooks/Final.ipynb
</code></pre>

<h3>Optional notebooks</h3>
<ul>
  <li><code>notebooks/time_series.ipynb</code> → Analyze temporal trends</li>
  <li><code>notebooks/BERT_genre_encoder.ipynb</code> → Cluster genres semantically</li>
</ul>

<hr>

<h2>Insights & Takeaways</h2>
<ul>
  <li>Demonstrates <b>end-to-end ML system design</b>, from data acquisition to model evaluation.</li>
  <li>Combines <b>API integration, web scraping, feature engineering, and ML classification</b>.</li>
  <li>Showcases ability to <b>structure complex workflows</b> and communicate results clearly.</li>
  <li>Modular and extensible — each step can be reused for other data-driven projects.</li>
</ul>

<hr>

<h2>👤 Authors</h2>
<p><b>Álvaro Garabal Castro, Marc Camps, Ankur Chauhan, Serkan Musellim</b><br>
🎓 MSc in Artificial Intelligence, University of Edinburgh<br>
🔗 <a href="https://www.linkedin.com/in/alvarogarabal">LinkedIn</a> • 
<a href="https://github.com/yourusername">GitHub</a></p>

<hr>

<h2>Next Steps</h2>
<ul>
  <li>Develop an interactive dashboard for visualizing genre trends.</li>
  <li>Deploy the trained genre classifier as an API endpoint.</li>
  <li>Expand the dataset with additional streaming metrics.</li>
</ul>








