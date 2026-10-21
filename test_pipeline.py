from scraper import scrape_website
from summarizer import summarize_text

url = input("Enter website URL: ")
print("\nScraping website...")

title, text = scrape_website(url)

print(f"\nPage Title: {title}")
print(f"Characters extracted: {len(text)}")

print(f"\nGenerating Summary...")
summary = summarize_text(text)

print("\n---  AI SUMMARY  ---\n")
print(summary)