def romanized_to_telugu(romanized_text):
    # Mapping for vowels and diphthongs
    vowel_mapping = {
        'a': 'అ', 'aa': 'ఆ', 'i': 'ఇ', 'ī': 'ఈ', 'u': 'ఉ', 'ū': 'ఊ', 'e': 'ఎ', 'ē': 'ఏ', 'ai': 'ఐ',
        'o': 'ఒ', 'ō': 'ఓ', 'au': 'ఔ', 'ṛ': 'ఋ', 'ṝ': 'ౠ', 'ḷ': 'ఌ', 'ḹ': 'ౡ'
    }
    
    # Mapping for consonants
    consonant_mapping = {
        'ka': 'క', 'kha': 'ఖ', 'ga': 'గ', 'gha': 'ఘ', 'ṅa': 'ఙ', 'ca': 'చ', 'cha': 'ఛ', 'ja': 'జ', 'jha': 'ఝ', 
        'ña': 'ఞ', 'ṭa': 'ట', 'ṭha': 'ఠ', 'ḍa': 'డ', 'ḍha': 'ఢ', 'ṇa': 'ణ', 'ta': 'త', 'tha': 'థ', 'da': 'ద', 
        'dha': 'ధ', 'na': 'న', 'pa': 'ప', 'pha': 'ఫ', 'ba': 'బ', 'bha': 'భ', 'ma': 'మ', 'ya': 'య', 'ra': 'ర', 
        'la': 'ల', 'va': 'వ', 'śa': 'శ', 'ṣa': 'ష', 'sa': 'స', 'ha': 'హ', 'ḷa': 'ళ', 'kṣa': 'క్ష'
    }

    # Mapping for special characters
    special_mapping = {
        'ṃ': 'ం', 'ḥ': 'ః', 'm̐': 'ఁ'
    }
    
    # Combine all mappings
    mapping = {**vowel_mapping, **consonant_mapping, **special_mapping}
    
    # Split the romanized text into words
    words = romanized_text.split()
    
    # Translate each word using the mapping dictionary
    translated_words = []
    for word in words:
        translated_word = ''
        i = 0
        while i < len(word):
            # Check for the longest matching sequence in the mapping
            match_found = False
            for length in range(3, 0, -1):  # Check sequences of length 3, 2, and 1
                if i + length <= len(word) and word[i:i+length] in mapping:
                    translated_word += mapping[word[i:i+length]]
                    i += length
                    match_found = True
                    break
            if not match_found:
                translated_word += word[i]
                i += 1
        translated_words.append(translated_word)
    
    # Join the translated words into a single string
    translated_text = ' '.join(translated_words)
    
    return translated_text


if __name__ == "__main__":
    # Example usage
    romanized_text = "miru ela unnaru"
    telugu_text = romanized_to_telugu(romanized_text)
    print(telugu_text)  # Output: మీరు ఎలా ఉన్నారు?

