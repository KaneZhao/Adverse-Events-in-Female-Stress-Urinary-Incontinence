# Adverse Events in Female Stress Urinary Incontinence Mesh Surgeries

This project analyzes patient treatment and symptoms related to adverse events in mesh surgeries for female stress urinary incontinence (SUI). The workflow includes data cleaning, preprocessing, exploratory data analysis, topic modeling, semi-supervised learning, sentiment analysis, and a chatbot built on the processed data.

## Table of Contents

- [Introduction](#introduction)
- [Project Workflow](#project-workflow)
  - [1. Data Cleaning](#1-data-cleaning)
  - [2. Preprocess Combined Data](#2-preprocess-combined-data)
  - [3. Exploratory Data Analysis (EDA)](#3-exploratory-data-analysis-eda)
  - [4. Topic Modeling](#4-topic-modeling)
  - [5. Semi-supervised Learning](#5-semi-supervised-learning)
  - [6. Sentiment Analysis](#6-sentiment-analysis)
  - [7. Chatbot](#7-chatbot)
- [Usage](#usage)
- [Results](#results)

## Introduction

The project focuses on analyzing medical records related to SUI mesh surgeries. The primary goals are to understand adverse events through topic modeling, label the severity of symptoms using semi-supervised learning, and classify the sentiment of patient experiences.

## Project Workflow

### 1. Data Cleaning

In this step, data was extracted from multiple sources and merged into a unified dataset.

### 2. Preprocess Combined Data

Text data was preprocessed with the following steps:

- Expand contractions (e.g., "can't" → "cannot")
- Tokenization
- Convert to lowercase
- Remove punctuation
- Remove stop words
- Remove words starting with a digit
- Parts of Speech (POS) tagging
- Lemmatization and stemming
- Create Bag of Words (BOW)
- Calculate Term Frequency and Term Frequency-Inverse Document Frequency (TF-IDF)
- Sentencization and sentence-level lemmatization and stemming

### 3. Exploratory Data Analysis (EDA)

Explored the data to understand the distribution of key features, patterns, and trends within the dataset.

### 4. Topic Modeling

Built LDA and NMF models to extract key topics from the patient narratives. The most coherent topics were selected after fine-tuning the models.

### 5. Semi-supervised Learning

Implemented a semi-supervised learning approach to label the data. The process involved:

- Using manually labeled data
- Applying label propagation to infer labels for the unlabeled data

### 6. Sentiment Analysis

Performed sentiment classification on the dataset, identifying the severity of symptoms from the text, with labels ranging from 'least severe' to 'most severe.'

### 7. Chatbot

Developed a chatbot that utilizes the processed dataset to provide insights into SUI-related questions. The chatbot was built using pre-trained models like BERT and T5 with context.
