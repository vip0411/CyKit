import hashlib

def crack_hash(hash_value, dictionary_file, hash_type='md5'):
    with open(dictionary_file, 'r') as file:
        for word in file:
            word = word.strip()
            if hash_type == 'md5':
                word_hash = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                word_hash = hashlib.sha256(word.encode()).hexdigest()
            
            if word_hash == hash_value:
                return word
    return None
