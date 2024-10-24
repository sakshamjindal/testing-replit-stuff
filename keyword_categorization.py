import re
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def categorize_search_volume(volume):
    if 0 <= volume <= 500:
        return "Low"
    elif 501 <= volume <= 5000:
        return "Medium"
    else:
        return "High"

def categorize_keyword_difficulty(kd):
    if 0 <= kd <= 30:
        return "Low"
    elif 31 <= kd <= 60:
        return "Medium"
    elif kd > 60:
        return "High"

def categorize_cpc(cpc):
    if 0 <= cpc <= 20:
        return "Low"
    elif 21 <= cpc <= 50:
        return "Medium"
    elif cpc > 50:
        return "High"

def categorize_competitor_density(density):
    if 0 <= density <= 0.35:
        return "Low"
    elif 0.36 <= density <= 0.60:
        return "Medium"
    elif density > 0.60:
        return "High"

def categorize_intent(keyword):
    transactional = ["buy", "purchase", "order", "shop", "deal", "price"]
    informational = ["how", "what", "why", "when", "where", "guide", "tutorial"]
    commercial = ["best", "top", "review", "compare", "vs"]
    
    keyword_lower = keyword.lower()
    
    if any(word in keyword_lower for word in transactional):
        return "Transactional"
    elif any(word in keyword_lower for word in informational):
        return "Informational"
    elif any(word in keyword_lower for word in commercial):
        return "Commercial"
    else:
        return "Navigational"

def is_question(keyword):
    question_words = ["what", "how", "why", "when", "where", "which", "who", "is", "are", "can", "do", "does"]
    return any(keyword.lower().startswith(word) for word in question_words)

def is_product_specific(keyword):
    product_specifics = ["dimension", "size", "quality", "cost", "feature", "specification", "mm"]
    return any(word in keyword.lower() for word in product_specifics)

def is_long_tail(keyword):
    score = 0
    
    word_count = len(keyword.split())
    if word_count >= 3:
        score += 1
    
    specificity_indicators = ['how to', 'best', 'vs', 'review', 'guide', 'tips', 'for']
    if any(indicator in keyword.lower() for indicator in specificity_indicators):
        score += 1
    
    if re.search(r'\d', keyword):
        score += 1
    
    question_words = ['what', 'why', 'how', 'where', 'when', 'who']
    if any(keyword.lower().startswith(word) for word in question_words):
        score += 1
    
    return score >= 2

def contains_location(keyword):
    doc = nlp(keyword)
    return any(ent.label_ == "GPE" for ent in doc.ents)

def is_category_keyword(status):
    return "category" in status.lower()

def is_product_keyword(status):
    return "product" in status.lower()

def categorize_keywords(df):
    df['Search Volume Category'] = df['Volume'].apply(categorize_search_volume)
    df['Keyword Difficulty Category'] = df['Keyword Difficulty'].apply(categorize_keyword_difficulty)
    df['CPC Category'] = df['CPC (INR)'].apply(categorize_cpc)
    df['Competitor Density Category'] = df['Competitive Density'].apply(categorize_competitor_density)
    df['Intent'] = df['Keyword'].apply(categorize_intent)
    df['Is Question'] = df['Keyword'].apply(is_question)
    df['Is Product Specific'] = df['Keyword'].apply(is_product_specific)
    df['Is Long Tail'] = df['Keyword'].apply(is_long_tail)
    df['Contains Location'] = df['Keyword'].apply(contains_location)
    df['Is Category Keyword'] = df['Categorised'].apply(lambda x: is_category_keyword(x))
    df['Is Product Keyword'] = df['Categorised'].apply(lambda x: is_product_keyword(x))
    return df
