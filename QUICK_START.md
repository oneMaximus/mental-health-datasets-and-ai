# QUICK START - Reddit Mental Health Data Collector

## 📦 What You Got
- `reddit_mental_health_collector.py` - Main data collector
- `test_reddit_connection.py` - Test your Reddit API setup
- `requirements.txt` - Required Python packages
- `SETUP_GUIDE.md` - Detailed documentation

---

## 🚀 Quick Setup (3 Steps)

### Step 1: Install Packages
```bash
pip install praw pandas openpyxl
```

### Step 2: Get Reddit API Credentials
1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in:
   - Name: `research_bot` (or anything)
   - Type: Select **"script"**
   - Redirect URI: `http://localhost:8080`
4. Click "Create app"
5. Copy your credentials:
   - `client_id` = text under "personal use script"
   - `client_secret` = text next to "secret"

### Step 3: Update Credentials
Edit **BOTH** Python files and replace:
```python
'client_id': 'YOUR_CLIENT_ID',        # paste here
'client_secret': 'YOUR_CLIENT_SECRET'  # paste here
```

---

## ✅ Test Your Setup
```bash
python test_reddit_connection.py
```
If you see "ALL TESTS PASSED", you're ready!

---

## 📊 Collect Data
```bash
python reddit_mental_health_collector.py
```

### What It Does:
1. Searches 9 mental health conditions across 25+ subreddits
2. Filters for posts mentioning being **"diagnosed"**
3. Collects: Date, Title, Description, Subreddit, URL
4. Exports to Excel with separate sheets per disorder

### Output Example:
`mental_health_reddit_data_20241108_143022.xlsx`

**9 Sheets:**
- Depression
- ADHD
- Anxiety
- Bipolar
- PTSD
- Autism
- Schizophrenia
- OCD
- Eating_Disorder

---

## 🎯 Disorders & Subreddits Covered

| Disorder | Subreddits |
|----------|-----------|
| **Depression** | r/depression, r/depression_help, r/mentalhealth |
| **ADHD** | r/ADHD, r/ADHDmemes, r/adhdwomen |
| **Anxiety** | r/Anxiety, r/HealthAnxiety, r/socialanxiety |
| **Bipolar** | r/bipolar, r/bipolar2, r/BipolarReddit |
| **PTSD** | r/ptsd, r/CPTSD, r/traumatoolbox |
| **Autism** | r/autism, r/aspergers, r/AutismTranslated |
| **Schizophrenia** | r/schizophrenia, r/schizoaffective, r/Psychosis |
| **OCD** | r/OCD, r/OCDmemes, r/OCDRecovery |
| **Eating Disorder** | r/EatingDisorders, r/EDAnonymous, r/fuckeatingdisorders |

---

## ⚙️ Customization

### Collect More Posts
Edit line 250 in `reddit_mental_health_collector.py`:
```python
post_limit=500  # Change from 200 to any number
```

### Add More Subreddits
Edit lines 25-35, add to any list:
```python
'Depression': ['depression', 'depression_help', 'YOUR_SUBREDDIT'],
```

### Add More Diagnosis Keywords
Edit lines 40-55, add patterns:
```python
r'\bclinically diagnosed\b',
r'\bmy therapist confirmed\b',
```

---

## 🔍 Diagnosis Detection

The script looks for posts containing:
- "diagnosed", "diagnosis"
- "formally diagnosed", "officially diagnosed"
- "my doctor diagnosed", "psychiatrist diagnosed"
- "recently diagnosed", "just diagnosed"
- And more variations...

---

## ⏱️ Performance

**Expected Runtime:** 5-15 minutes (default settings)
- Depends on: number of posts, subreddit activity, Reddit API speed
- Built-in delays to respect Reddit rate limits (60 requests/min)

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Invalid credentials" | Double-check client_id and client_secret |
| "403 HTTP response" | Change user_agent string slightly |
| No data collected | Increase post_limit or try different subreddits |
| Script is slow | Normal - Reddit API requires rate limiting |

---

## ⚠️ Important Notes

### Ethical Considerations:
- ✅ Public Reddit data only
- ✅ Use for research/analysis purposes
- ❌ Do NOT identify or contact users
- ❌ Do NOT share personally identifiable information
- ⚖️ Follow Reddit Terms of Service
- 📋 Consider IRB approval for academic research

### Diagnosis Filtering Accuracy:
- Uses keyword-based filtering
- Not 100% accurate - manual review recommended
- Some posts may be self-diagnosis despite keywords
- Best used as initial screening for further analysis

---

## 📈 Example Output Format

**Excel Sheet - Depression:**

| Date | Title | Description | Subreddit | URL |
|------|-------|-------------|-----------|-----|
| 2024-11-08 14:30 | Just got diagnosed | My psychiatrist diagnosed me with MDD... | r/depression | https://reddit.com/... |
| 2024-11-07 09:15 | Newly diagnosed | After months of therapy, I was officially... | r/depression_help | https://reddit.com/... |

---

## 📚 Need More Help?

📖 Read `SETUP_GUIDE.md` for detailed instructions
🌐 Reddit API: https://www.reddit.com/dev/api
📦 PRAW Docs: https://praw.readthedocs.io

---

## 🔄 Quick Commands Cheat Sheet

```bash
# Install packages
pip install -r requirements.txt

# Test connection
python test_reddit_connection.py

# Collect data
python reddit_mental_health_collector.py

# View Excel file (if you have pandas installed)
python -c "import pandas as pd; print(pd.read_excel('mental_health_reddit_data_*.xlsx', sheet_name='Depression').head())"
```

---

**Happy Data Collecting! 🎉**
