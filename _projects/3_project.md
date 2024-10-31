---
layout: page
title: Predicting EV Charging Demand(SAS Curiosity Cup)
description: A novel approach to forecasting EV charging demand through traffic data, achieving 2nd place in the SAS Curiosity Cup.
img: /assets/img/ev-demand-background.jpg
# redirect: https://unsplash.com
importance: 1
category: Research
---

A data-driven approach to forecast electric vehicle (EV) charging demand by analyzing traffic flows. This project, developed for the **SAS Curiosity Cup 2024**, was awarded **2nd place in Data Analysis**, competing against 107 teams from 19 countries.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/traffic-flow-overview.jpg" title="Traffic Flow Data Analysis for EV Demand Prediction" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

**Background:**  
With the rapid growth in EV adoption, there’s a critical need for efficient charging infrastructure. Traditional demand forecasting relies heavily on specific station usage data, which is often unavailable due to privacy regulations. To address this gap, our project leverages **traffic flow data** to estimate EV charging demand, focusing on vehicles exiting highways in California. This unique approach aims to predict demand patterns without direct access to granular station data.

---

### Key Components

- **Data Collection and Preprocessing**: Utilized traffic data from California’s I210 Corridor, sourced from the Caltrans PeMS database. Our team processed over 700 days of traffic data across multiple sensors to prepare it for analysis.

- **Forecasting Pipeline**: Multiple models were tested within the SAS Forecast Studio pipeline, including ARIMAX, Exponential Smoothing, and Neural Network-based models, to evaluate predictive accuracy. Our final choice was a **Stacked Model (NN + Time Series)** due to its effectiveness in balancing prediction accuracy and computational efficiency.

  <div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/forecasting-pipeline.jpg" title="Forecasting Pipeline Models and Workflow" class="img-fluid rounded z-depth-1" %}
    </div>
  </div>

- **Demand Estimation Technique**: Developed a three-step methodology to estimate the number of EVs likely requiring charging, factoring in vehicle exit rates, traffic volume, and EV ratios.

- **Visualization and Analysis**: To validate model accuracy and forecasted demand, we created various heat maps and graphical representations of traffic patterns. These visuals enabled a deeper understanding of traffic flow variations and helped refine our predictions for charging demand.

  <div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/visualization-analysis.jpg" title="Visualization of Traffic Flow and Forecasted Demand" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/predicted-traffic-heatmap.jpg" title="Predicted Traffic Flow Heat Map for 04-24-2018" class="img-fluid rounded z-depth-1" %}
    </div>
  </div>

---

### Technical Stack

- **Data Source**: Caltrans PeMS for traffic flow data
- **Software**: SAS Forecast Studio, SAS Viya for data processing and model evaluation

### Presentation

As part of the SAS Curiosity Cup competition, we presented our findings to a global audience. You can watch the full presentation here: [Presentation Video](https://drive.google.com/file/d/1DMhQXusxH984wqGK-CzVcuGfbRKRSVd0/view?pli=1)

### Conclusion

This project demonstrates an innovative approach to estimating EV charging demand by analyzing indirect data sources like traffic flow. Our methodology addresses data scarcity issues in EV infrastructure planning and has potential applications in urban planning and energy management.

### Additional Documents

- [Project Report](/assets/pdf/The Curiosity Cup Challenge - 2024.pdf)
