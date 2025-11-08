# Reddit Mental Health Data Collector - Setup Guide

## Overview
This tool collects Reddit posts from users who are **diagnosed** with various mental health conditions and exports the data to Excel with separate sheets for each disorder.

## Mental Health Conditions Covered
- Depression
- ADHD
- Anxiety
- Bipolar Disorder
- PTSD
- Autism
- Schizophrenia
- OCD
- Eating Disorders

---

## Step 1: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install praw pandas openpyxl
```

---

## Step 2: Get Reddit API Credentials

### 2.1 Create a Reddit Account
- Go to https://www.reddit.com and create an account if you don't have one

### 2.2 Create a Reddit App
1. Go to https://www.reddit.com/prefs/apps
2. Scroll down and click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: Mental Health Research Bot (or any name)
   - **App type**: Select "script"
   - **Description**: Data collection for research (optional)
   - **About URL**: Leave blank
   - **Redirect URI**: http://localhost:8080
4. Click "Create app"

### 2.3 Get Your Credentials
After creating the app, you'll see:
- **client_id**: The string under "personal use script" (looks like: dj2dkl3jd9sk2)
- **client_secret**: The string next to "secret" (looks like: 9sdk2-dkj3d_ksjd93d)

---

## Step 3: Configure the Script

Open `reddit_mental_health_collector.py` and update these lines (around line 18-22):

```python
REDDIT_CONFIG = {
    'client_id': 'YOUR_CLIENT_ID',      # Replace with your client_id
    'client_secret': 'YOUR_CLIENT_SECRET',  # Replace with your client_secret
    'user_agent': 'mental_health_research_bot/1.0'
}
```

Example:
```python
REDDIT_CONFIG = {
    'client_id': 'dj2dkl3jd9sk2',
    'client_secret': '9sdk2-dkj3d_ksjd93d',
    'user_agent': 'mental_health_research_bot/1.0'
}
```

---

## Step 4: Run the Script

```bash
python reddit_mental_health_collector.py
```

The script will:
1. Connect to Reddit API
2. Search through multiple subreddits for each disorder
3. Filter for posts mentioning being "diagnosed"
4. Collect Date, Title, Description for each post
5. Export to Excel with separate sheets for each disorder

---

## Output

The script creates an Excel file: `mental_health_reddit_data_YYYYMMDD_HHMMSS.xlsx`

### Excel Structure:
- **Separate sheet for each disorder**
- **Columns**: Date | Title | Description | Subreddit | URL
- **Formatted** with colored headers and wrapped text

---

## Customization Options

### Adjust Number of Posts Collected
In `reddit_mental_health_collector.py`, find this line (around line 250):
```python
post_limit=200  # Adjust this number based on your needs
```
Increase for more posts, decrease for faster collection.

### Add More Subreddits
Update the `DISORDERS` dictionary (around line 25) to include more subreddits:
```python
'Depression': ['depression', 'depression_help', 'mentalhealth', 'YOUR_SUBREDDIT'],
```

### Modify Diagnosis Keywords
Update `DIAGNOSIS_KEYWORDS` list (around line 40) to add more search terms:
```python
r'\bmy psychiatrist\b',
r'\bcertified diagnosis\b',
```

---

## Important Notes

### Ethical Considerations
- This data is from public Reddit posts
- Respect user privacy - do not identify or contact users
- Use data responsibly for research/analysis only
- Consider Reddit's Terms of Service and API usage guidelines

### Rate Limiting
- Reddit API has rate limits (60 requests per minute)
- The script includes built-in delays to prevent hitting limits
- If you get rate limit errors, increase the `time.sleep()` values

### Diagnosis Filtering
The script filters for posts mentioning:
- "diagnosed", "diagnosis", "formally diagnosed"
- "officially diagnosed", "professionally diagnosed"
- "my doctor diagnosed", "psychiatrist diagnosed"
- And more variants

**Note**: This is keyword-based filtering and may not be 100% accurate. Manual review of results is recommended for research purposes.

---

## Troubleshooting

### Error: "Invalid credentials"
- Double-check your `client_id` and `client_secret`
- Make sure there are no extra spaces
- Verify your Reddit app is set to "script" type

### Error: "Received 403 HTTP response"
- Your app may not have access to certain subreddits
- Try changing the `user_agent` string
- Some subreddits may be private or restricted

### No data collected
- The subreddit may not have many posts with diagnosis keywords
- Try increasing `post_limit` number
- Check if subreddits are active (some may be inactive)

### Script runs slow
- This is normal - Reddit API rate limiting requires delays
- Collection time depends on number of posts and subreddits
- Estimated time: 5-15 minutes for default settings

---

## Sample Output Preview

**Depression Sheet:**
| Date | Title | Description | Subreddit | URL |
|------|-------|-------------|-----------|-----|
| 2024-11-08 14:30:22 | Just got diagnosed with MDD | My psychiatrist diagnosed me yesterday... | r/depression | https://reddit.com/... |

**ADHD Sheet:**
| Date | Title | Description | Subreddit | URL |
|------|-------|-------------|-----------|-----|
| 2024-11-08 10:15:43 | Finally officially diagnosed at 28 | After years of struggling, I was formally diagnosed... | r/ADHD | https://reddit.com/... |

---

## Support

For issues or questions:
1. Check Reddit API documentation: https://www.reddit.com/dev/api
2. Check PRAW documentation: https://praw.readthedocs.io
3. Verify your Reddit app settings

---

## License & Disclaimer

This tool is for educational and research purposes. Always:
- Follow Reddit's Terms of Service
- Respect user privacy
- Use data ethically
- Consider getting IRB approval for research use
- Comply with data protection regulations (GDPR, etc.)
