---
layout: page
title: Synthetic Data Generation for EV Charging Demand Forecasting
description: A project focused on overcoming data scarcity in EV infrastructure through synthetic data generation and machine learning.
img: assets/img/operations_research_purdue_logo.jpg
importance: 2
category: Research
---

This project aims to address the lack of granular, publicly accessible data on EV charging demand by generating synthetic data to improve forecasting accuracy. This ongoing research project involves three main phases: **synthetic data generation**, **demand forecasting**, and **optimization modeling**.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/synthetic-data-overview.jpg" title="Overview of the Synthetic Data Generation Process" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

**Abstract:**  
With the rapid adoption of electric vehicles (EVs), demand forecasting for charging infrastructure is increasingly essential. Traditional models, reliant on historical data, are limited by data availability. Our project generates high-quality synthetic data using advanced models such as **Variational Autoencoders (VAEs)** and **TimeGAN** to replicate realistic EV charging patterns, providing a robust foundation for demand prediction models.

---

### Key Components

- **Synthetic Data Generation**:  
  We employ multiple approaches to create synthetic time-series data that reflects real-world EV charging behavior:

  - **TimeGAN**: Focuses on generating time-dependent sequences by combining GANs with RNNs. This model captures both static and dynamic patterns in data.
  - **VAE (Variational Autoencoder)**: A probabilistic model that learns to compress and recreate data by encoding it into a latent space. The encoder compresses the input data, and the decoder reconstructs or generates new data from the latent space, maintaining essential features.
  - **ETS Model (Exponential Smoothing State Space)**: Selected for cases where deep learning models are unsupported by SAS Viya, providing trend and seasonality capture.

  <div class="row justify-content-sm-center">
    <div class="col-md-6">
      {% include figure.liquid path="assets/img/timegan-diagram.jpg" title="TimeGAN Model Workflow" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-md-6">
      {% include figure.liquid path="assets/img/ets-model-output.jpg" title="ETS Model Synthetic Data Output" class="img-fluid rounded z-depth-1" %}
    </div>
  </div>

- **Correlation Evaluation**:  
  We assess the quality of synthetic data by calculating feature-wise and time-wise correlations to ensure fidelity to the original dataset. This helps maintain key relationships and temporal dynamics in the data.

- **Demand Forecasting with Machine Learning**:  
  Utilizing CNNs and RNNs (LSTM and GRU layers), our demand prediction models capture short- and long-term dependencies in EV charging behavior. Hyperparameter tuning and preprocessing ensure model generalization and accuracy.

- **Optimization Modeling**:  
  A Real-Time Pricing (RTP) model is implemented in SAS Viya to adjust charging prices dynamically, enhancing grid efficiency by distributing demand and promoting off-peak usage.

### Weekly Progress Updates

1. **TimeGAN Implementation**:  
   Set up and configured TimeGAN for time-series data generation, addressing issues with module imports and ensuring compatibility in Google Colab.

2. **ETS Model in SAS Viya**:  
   Used the ETS model to generate synthetic data where deep learning models were unsupported, yielding expanded data for improved forecasting.

3. **VAE Framework Development**:  
   Constructed a VAE framework with an encoder, latent vectors, and a decoder to facilitate flexible data generation.

4. **Challenges and Solutions**:  
   Encountered compatibility issues with libraries, data type handling, and GPU resource limitations. Applied adjustments such as data type conversions and metadata updates for smooth model execution.

---

### Technical Stack

- **Models**: TimeGAN, VAE, ETS Model
- **Platform**: Google Colab, SAS Viya for data generation and optimization modeling, Python

### Current Status

This research is still in progress, with ongoing model tuning and evaluation. No final results have been obtained yet.
