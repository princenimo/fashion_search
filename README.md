# Personalized Fashion Search with Marqo

This repository walks through building a personalized fashion search experience using [Marqo](https://www.marqo.ai/). The goal is to show how product metadata and historical user behavior can be combined to improve search relevance using modern vector and hybrid search techniques.

You’ll go from raw data preparation to indexing, ranking, and finally interacting with the search system through a lightweight UI. Along the way, we demonstrate how features like exact-match boosting and revenue-based modifiers can influence ranking quality and downstream conversion.

A more detailed narrative explanation of the approach is available in this accompanying article:  
👉 https://marqo.ai/blog/improving-search-relevance-in-fashion

<p align="center">
  <img src="assets/ui.png"/>
</p>

---

## Step 0: Install and Run Marqo (Docker)

Marqo runs as a service and requires **Docker**.

1. Install Docker for your operating system (Mac, Windows, or Linux):  
   https://docs.docker.com/get-docker/

2. Start the Docker application.

3. Pull and run the latest Marqo image:

```bash
docker pull marqoai/marqo:latest
docker rm -f marqo
docker run --name marqo -it -p 8882:8882 marqoai/marqo:latest
```

Once running, Marqo will be available locally at:
```
http://localhost:8882
```

If you encounter issues, you can ask questions in the Marqo Community:
https://community.marqo.ai/

---

## Step 1: Environment Setup

Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Step 2: Preparing the Data

Effective search relies on combining **static product information** with **behavioral signals** derived from user interactions. In this demo, we work with three related datasets:

1. Product data  
2. Raw search logs  
3. Aggregated historical signals  

### Product Data

We use a 15k-item subset of the [`Marqo/fashion200k`](https://huggingface.co/datasets/Marqo/fashion200k) dataset. To better resemble a production catalogue, additional attributes such as price and stock availability are included.

The product CSV is located at:
```
./data_processing/data/product_data.csv
```

Example format:

```csv
image_url,_id,product_name,category,cost,in_stock
https://marqo-tutorial-public.s3.us-west-2.amazonaws.com/fashion/fashion200k/16066811_1.jpeg,16066811_1,black skinny cotton twill cargo pants,pants,17.6,True
```

---

### Search Logs

User interaction data is simulated using curated search logs that reflect typical e-commerce behavior (views, clicks, add-to-cart events, purchases).

Download the search log CSV:
https://marqo-tutorial-public.s3.us-west-2.amazonaws.com/fashion/fashion-search-demo/search_log.csv

Place it in:
```
data_processing/data/
```

Example rows:

```csv
query,_id,action,days_ago_action_performed
green candy dress,91055827_0,click,30
green candy dress,71246356_0,purchased,1
```

---

### Historical Search Features

Raw logs are aggregated into structured historical signals such as clicks, purchases, and revenue over multiple time windows.

A precomputed version is included at:
```
./data_processing/data/historical_data.csv
```

To regenerate it:

```bash
python3 data_processing/generate_historical_data.py
```

---

### Merging and Preparing Documents

Merge product and historical data:

```bash
python3 data_processing/generate_merged_data.py
```

Convert merged data into JSON documents with boosters and modifiers:

```bash
python3 data_processing/generate_modifiers.py
```

Final documents are stored at:
```
./data_processing/data/complete_data.json
```

---

## Step 3: Creating and Populating the Marqo Index

Create the index:

```bash
python3 marqo/create_index.py
```

Check index status:
https://cloud.marqo.ai/indexes/

Add documents:

```bash
python3 marqo/add_documents.py
```

---

## Step 4: Running the Search Interface

Launch the Streamlit app:

```bash
streamlit run app.py
```

Supported search modes:
- Tensor search  
- Hybrid search  
- Hybrid + exact match boosting  
- Hybrid + boosters + revenue modifiers  

---

## Step 5: Optional Cleanup

This demo provisions an index with GPU inference and a storage shard (≈ **$1.03/hour**).  
Delete the index when finished:

```bash
python3 marqo/delete_index.py
```
