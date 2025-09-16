# 예시 3: 단어 빈도 분석
text = "python is great python is easy python programming is fun"
words = text.split()

print("\n3) 단어 빈도 분석:")
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 빈도순으로 정렬하여 출력
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}번")
