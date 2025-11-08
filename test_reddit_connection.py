"""
Test script to verify Reddit API credentials are working
Run this before using the main collector script
"""

import praw

# Replace with your credentials
REDDIT_CONFIG = {
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET',
    'user_agent': 'mental_health_research_bot/1.0'
}

def test_connection():
    """
    Test Reddit API connection
    """
    print("="*60)
    print("Testing Reddit API Connection")
    print("="*60)
    
    try:
        # Initialize Reddit
        reddit = praw.Reddit(
            client_id=REDDIT_CONFIG['client_id'],
            client_secret=REDDIT_CONFIG['client_secret'],
            user_agent=REDDIT_CONFIG['user_agent']
        )
        
        print("\n✓ Successfully connected to Reddit API!")
        print(f"✓ Read-only mode: {reddit.read_only}")
        
        # Test by fetching a subreddit
        print("\nTesting subreddit access...")
        subreddit = reddit.subreddit('depression')
        print(f"✓ Successfully accessed r/depression")
        print(f"  - Subscribers: {subreddit.subscribers:,}")
        print(f"  - Description: {subreddit.public_description[:100]}...")
        
        # Fetch a few posts to verify
        print("\nFetching sample posts...")
        post_count = 0
        for post in subreddit.hot(limit=3):
            post_count += 1
            print(f"\n  Post {post_count}:")
            print(f"    Title: {post.title[:60]}...")
            print(f"    Author: u/{post.author}")
            print(f"    Score: {post.score}")
        
        print("\n" + "="*60)
        print("✓ ALL TESTS PASSED!")
        print("Your Reddit API credentials are working correctly.")
        print("You can now run the main collector script.")
        print("="*60)
        
        return True
        
    except praw.exceptions.PRAWException as e:
        print(f"\n✗ PRAW Error: {e}")
        print("\nPlease check:")
        print("  1. Your client_id and client_secret are correct")
        print("  2. Your Reddit app type is set to 'script'")
        print("  3. You have an active internet connection")
        return False
        
    except Exception as e:
        print(f"\n✗ Unexpected Error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
