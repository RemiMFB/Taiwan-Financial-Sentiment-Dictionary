# Taiwan Financial Sentiment Dictionary

This repository provides a dictionary for sentiment analysis of Traditional Chinese financial news in Taiwan. The lexicon was constructed using data derived from major Taiwanese news sources.
Features:
 - Lexicon in Excel format (XLSX).
 - Clear versioning and release policy.
 - Quality assurance checks.
 - Documentation of the construction workflow (LLM labeling → PMI filtering → human or LLM validation).

The full paper, entitled 台灣財經情緒字典與議題分類字詞之編製與應用:大型語言模型之協作與分類評估, detailing this work, can be downloaded from: https://remi.ctmnthu.com/portfolio-archive/financial-dictionary/  

Paper Abstract:
 
本文旨在利用台灣的財經新聞文本，建立分類模型以篩選出台灣慣用的新聞字詞，並透過大型語言模型 (LLMs) 的協助，對這些新聞詞彙進行檢視、擴充以及情緒分類的確認。不同於既有文獻，本文還針對「景氣」、「貨幣政策」、「利率」等特定財經議題建構分類字詞，以填補這方面的不足。經過一系列的篩選，我們選出 7,814 個財經情緒詞彙；經過比對，有 1/4 以上的財經慣用詞彙並未收錄於現有的情緒字典中。若以中央銀行公佈的會議新聞稿為樣本外的文本，以 LLMs 的分類結果為標準，比較不同字典的情緒分類精確度可以發現，本文的財經情緒字典在運算時間與成本上較 LLMs 更具優勢，而在分類的精確度雖不及 LLMs，確優於現有的情緒字典。此外，我們也發現，依本文所編製的情緒字典來建構情緒指標，該指標對許多台灣總體經濟變數有顯著的解釋能力與預測力，其表現均優於現有字典所建構的指標內容。最後，我們也觀察到，依據不同議題所建構的分類詞彙與情緒指標，能更細緻捕捉文本中的語意差異，進一步提升文字資料轉化為數據的內涵。

## Quick start
- Download the current release from the **Releases** page once you publish this repo.
- Data files live in `data/`:
  - `RemiDictionary.xlsx` — Main financial sentiment dictionary
  - `TopicExchangeRate.xlsx` — Topic lexicon: Exchange Rate 
  - `TopicGrowth.xlsx` — Topic lexicon: Growth 
  - `TopicInterestRate.xlsx` — Topic lexicon: Interest Rate 
  - `TopicMonetaryPolicy.xlsx` — Topic lexicon: Monetary Policy 
  - `TopicPrice.xlsx` — Topic lexicon: Price


## Versioning & release schedule
- **Scheme**: `2025.06.01` (`YYYY.MM.PATCH`). Year–month reflect the release window; PATCH increments for hotfixes that do not change definitions.
- **Schedule**: Annual releases (on December). Event-driven hotfixes are allowed.
- **Frozen archives**: Every release is tagged and published on GitHub Releases. Users can cite a specific version for replication.
- **Changelog**: See `CHANGELOG.md` for human-readable changes.

## Citation & DOI
-  [![DOI](https://zenodo.org/badge/1052554974.svg)](https://doi.org/10.5281/zenodo.17076771
Also provide citation metadata in `CITATION.cff`.

## Licenses
- **Code**: MIT License (see `LICENSE-CODE`).
- **Data**: Creative Commons Attribution 4.0 International (CC BY 4.0) (see `LICENSE-DATA`).

## Construction workflow
```mermaid
flowchart LR
  A(LLM labeling: propose candidates) --> B(PMI filtering + heuristics)
  B --> C(Human review & policy checks)
  C --> D(Validation metrics: accuracy / F1)
  D --> E(Release + tag + changelog)
```
- Full details are in `WORKFLOW.md`, including checkpoints, error metrics, and QA steps.

## Governance & deprecation policy
- Rules for retiring obsolete terms and blocking short-lived buzzwords are in `POLICY.md`.
- Contributions follow `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.
- Use GitHub Issues to propose new terms; each term should include source examples and justification.

## Download formats
- Excel provided. R/Python usage snippets are included below.

### Load in R
```r
library(openxlsx)
library(stringr)
rPathFile= "data/RemiDictionary.xlsx"
sentence = "亞洲方面，日本因經濟復甦漸趨明朗，日本央行於八月間結束零利率政策，將無擔保隔夜拆款利率的操作目標調高至Ｏ．二五%，惟因通貨緊縮現象暫難消除，寬鬆貨幣政策的立場仍然不變；"
Positive = read.xlsx(rPathFile, "Positive")[, 1]
Negative = read.xlsx(rPathFile, "Negative")[, 1]

# 計算情感詞的函數
CountSentiment = function(str_v, sentiment_v, replace_c = '***'){
   result   = rep(0, length(str_v))
   for(i in 1:length(sentiment_v)){
      check    = str_detect(str_v, sentiment_v[i])
      if(sum(check) > 0){
         result = result + check
         str_v  = str_replace_all(str_v, sentiment_v[i], replace_c)
      }
   }
   return(result)
}

# 計算正面和負面詞的數量
n.positive = CountSentiment(sentence, Positive)
n.negative = CountSentiment(sentence, Negative)

cat('正面詞數量: ', n.positive, '\n')
cat('負面詞數量: ', n.negative, '\n')
```
### Load in Python
```python
import pandas as pd
import re

# 讀取 Excel 中的字典
rPathFile = "data/RemiDictionary.xlsx"
positive_words = pd.read_excel(rPathFile, sheet_name="Positive").iloc[:, 0].tolist()
negative_words = pd.read_excel(rPathFile, sheet_name="Negative").iloc[:, 0].tolist()

sentence = "亞洲方面，日本因經濟復甦漸趨明朗，日本央行於八月間結束零利率政策，將無擔保隔夜拆款利率的操作目標調高至Ｏ．二五%，惟因通貨緊縮現象暫難消除，寬鬆貨幣政策的立場仍然不變；"

# 計算情感詞的函數
def count_sentiment(str_v, sentiment_v, replace_c='***'):
    result = 0
    for word in sentiment_v:
        if re.search(word, str_v):
            result += len(re.findall(word, str_v))
            str_v = re.sub(word, replace_c, str_v)
    return result

# 計算正面和負面詞的數量
n_positive = count_sentiment(sentence, positive_words)
n_negative = count_sentiment(sentence, negative_words)

print(f"正面詞數量: {n_positive}")
print(f"負面詞數量: {n_negative}")

```

