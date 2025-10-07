# OmoiAi - Common Interest Discovery Tool

## Overview

OmoiAi is a tool that extracts common keywords from posts on X (formerly Twitter) to help identify shared interests between users. The tool excludes Japanese stopwords and uses natural language processing to extract common topics.

---

## Key Features

1. **Post Data Retrieval**
   - Retrieves posts from specified users using the X API or mock data.
2. **Common Keyword Extraction**
   - Uses TinySegmenter for Japanese tokenization and extracts common keywords after removing stopwords.
3. **Mock Data Support**
   - Allows operation verification using mock data instead of real posts.

---

## Technologies Used

- **Python Libraries**
  - `dotenv`: for loading environment variables
  - `tinysegmenter`: for Japanese tokenization
  - `argparse`: for parsing command-line arguments
  - `urllib`: for accessing external resources

- **External Resources**
  - [stopwords-ja](https://github.com/stopwords-iso/stopwords-ja): Japanese stopword list

---

## Installation

1. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

2. Set environment variables by creating a `.env` file with the following content:

    ```env
    X_API_KEY="YOUR_X_API_KEY"
    X_API_KEY_SECRET="YOUR_X_API_KEY_SECRET"
    X_ACCESS_TOKEN="YOUR_X_ACCESS_TOKEN"
    X_ACCESS_TOKEN_SECRET="YOUR_X_ACCESS_TOKEN_SECRET"
    ```

---

## Usage

### Using Real Data

Run the following command:

```bash
python main.py --user1 <User1_ID> --user2 <User2_ID>
```

Example:

```bash
python main.py --user1 "user1_id" --user2 "user2_id"
```

### Using Mock Data

Run the following command:

```bash
python main.py --mock
```

## Notes

- When using the X API, make sure your API keys are set correctly.
- When using mock data, do not specify `--user1` or `--user2`.

---

## Challenges & Future Plans

- **Improving Japanese Tokenization**
  - Currently using TinySegmenter, but considering switching to higher-accuracy tools such as MeCab or GiNZA.

- **Implementing a Web UI**
  - Planning to extend the command-line tool into a web application.

- **Introducing Sentiment Analysis**
  - Analyze the emotional nuance of common keywords to provide deeper insights.
