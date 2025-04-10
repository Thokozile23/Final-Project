# Final-Project

## Nice visuals to illustrate your main concepts and why this project is important for businesses. 

## Authors:
- **Elaina Longjohn**  
  GitHub:https://github.com/elongjohn

- **Mills Becouvarakis**  
  GitHub: https://github.com/millsbecouv
  
- **Shields Riggs**  
  GitHub: https://github.com/author1

- **Thokozile Munthali**  
  GitHub: https://github.com/author2

## Project Scope: Be as specific as possible with the scope of your project (which should be as narrowly focused as possible.) 
Our project examines the negative effects of feedback loops in recommender systems. A feedback loop is a cycle where a user’s interactions with recommended items influence their future recommendations. This happens because every action a user takes—whether it's clicking, rating, or engaging with content—gets recorded in their profile, which then leads to more similar recommendations in the future.

The negative impacts of these feedback loops are significant, particularly the amplification of popularity bias. In this scenario, the preferences of the majority overpower those of minority groups, causing the recommender system to focus heavily on a narrow set of popular items. This limits both the diversity of recommendations and the potential for users to discover new, lesser-known content.

As a result, minority preferences are often drowned out by the mainstream, making it harder for niche or emerging products to get noticed. Through our project, we aim to address this issue by finding a way to reduce popularity bias and create a more level playing field for all products, free from the inherent biases built into recommender systems.

## Website: Popularity Bias & Feedback Loops Simulation
https://claude.site/artifacts/79270026-7cfb-4106-a677-2b3b898d03d5


## Project Details: With logical organization and clear but concise writeups. 


### 🔍 Problem Statement 
We investigate the issue of feedback loops in recommender systems, where user interactions with popular content continuously reinforce the visibility of that content. This dynamic leads to **popularity bias**, which suppresses the discovery of niche items and limits recommendation diversity. Our goal is to simulate and measure this bias—and explore ways to reduce it.

### 🧠 Research Foundation
We grounded our project in recent research on recommender system bias mitigation. The paper we selected is:

**"De-biasing the User Feedback Loop in Recommender Systems" (2022)** – Proceedings of the ACM Web Conference  
📎 [Link to paper]([https://dl.acm.org/doi/10.1145/3485447.3511993]](https://dl.acm.org/doi/10.1145/3460231.3473321))

This work provides both a theoretical and experimental framework for identifying and mitigating popularity bias through reweighting and counterfactual approaches.

### 🛠️ Technical Implementation

#### 1. Dataset & Ingestion
- We use the **MovieLens 100K** dataset (static, well-documented).
- Ingested via **pandas** and optionally **Spark** for scalability.
- Merged `ratings`, `movies`, and `users` into one interaction dataset.

#### 2. Feedback Loop Simulation
- Built two recommender models:
  - **Model A (Biased):** Uses user ratings without correction — replicates the feedback loop.
  - **Model B (Adjusted):** Penalizes popular items or adds diversity boosting weights.
- Ran multiple simulation rounds where model output influences user profile → recreating the loop effect.

#### 3. Bias & Diversity Metrics
Tracked changes over time in:
- **Gini coefficient** of item exposure
- **Coverage** of long-tail items
- **Distribution** of recommended item popularity

Visualized how Model A's recommendations converge on fewer items over time, while Model B maintains higher diversity.

#### 4. Optional ML Component
- Built a **logistic regression** model to predict whether an item would be recommended, based on popularity score and user behavior, to illustrate systemic drift.

### 🌐 Website Demo (GenAI)
We created a simple interactive **GenAI-powered demo** using **Google Sheets + Claude/Gemini**:

- The user pastes a list of recommended items.
- The GenAI script classifies them as:
  - "Popular mainstream"
  - "Diverse/long-tail"
  - Suggests alternative under-represented items.

This demonstrates how feedback loops can be detected and softened with **LLM augmentation**.

### ✅ Project Management: GitHub Kanban Board
We tracked our work using a **GitHub Project Board** organized into:

- **To-Do**: Research reading, model design, visualization plan  
- **Ongoing**: Data processing, simulation testing  
- **Done**: Feedback loop model, metrics implementation  
- **Future Ideas**: Applying to e-commerce data, building a fairness-aware recommender  

We will present the board live and discuss how we used it to manage our tasks and coordinate as a team.

### 🤖 Responsible AI Considerations
- **Bias Awareness:** Recommender systems inherently favor majority preferences. We aim to identify and reduce this using fairness-aware modeling.
- **Transparency:** All simulation assumptions and model decisions are clearly documented.
- **Explainability:** We visualize how recommendation patterns evolve—showing when and how minority preferences are drowned out.
- **Mitigation Strategies:** Include weighting, diversity re-ranking, and hybrid models to encourage exposure to lesser-known items.

### 🔗 References
1. Abdollahpouri, H., Burke, R., & Mobasher, B. (2022). *De-biasing the User Feedback Loop in Recommender Systems*. The Web Conference (WWW).  
   ➤ https://dl.acm.org/doi/10.1145/3485447.3511993  
2. **MovieLens Dataset**: https://grouplens.org/datasets/movielens/  
3. Ricci et al. (2022). *Recommender Systems Handbook*. (Supporting theory)

## What's next? Help us envision future developments and concerns. 

## Responsible AI considerations: Recommender System Biases
![image](https://github.com/user-attachments/assets/13ef7933-f24c-44c1-8fe7-18e8f9aefaed)

Understanding the biases present in recommender systems (RSs) is crucial, as these biases can significantly impact the fairness, accuracy, and trustworthiness of recommendations. The biases within RSs can be categorized into four main types: data biases, cognitive biases, position/presentation biases, and algorithmic/model biases.

- Data Bias:
Data biases occur when the training data used by the recommender system is unbalanced or not fully representative of the entire user base. For example, certain demographic groups may be underrepresented, leading to recommendations that fail to reflect the diversity of users or perpetuate existing inequalities.

- Coginitive Bias:
Cognitive biases are influenced by human mental shortcuts or heuristics, which can affect how users interact with the system. Examples include the anchoring effect, where users rely too heavily on the first piece of information they encounter, or the recency effect, which may cause users to favor items that are more recent rather than more relevant.

- Position/Presentation Bias:
Position or presentation biases arise from the way recommendations are displayed to users. Items placed at the top of the list, for example, are more likely to be selected, regardless of their actual relevance to the user. This form of bias is often unintentional but can significantly skew the user experience.

- Algorithmic/Model Bias
Algorithmic or model biases are embedded in the recommendation algorithms themselves, often due to the way models are trained or the data they use. These biases can amplify existing stereotypes or reinforce behaviors by overemphasizing certain patterns in user data, such as preferences based on past behaviors or demographic factors.

-Ethical Concerns:

1. Reinforcement of Existing Biases
   
Concern: AI-driven recommendation systems can inadvertently reinforce existing popularity biases by promoting content that is already popular, while neglecting content from underrepresented groups or niche creators.

Ethical Implication: This can lead to a lack of diversity in what users are exposed to, limiting access to new or lesser-known content. Over time, this creates a feedback loop where already popular content continues to dominate, and marginalized creators or topics are continuously excluded.

Solution: A balanced recommendation approach should be used, incorporating mechanisms to give fair exposure to less popular but high-quality content, ensuring that all creators have the opportunity to be discovered.

2. Erosion of Diversity
   
Concern: Popularity bias in AI recommendations could undermine diversity by prioritizing a narrow set of choices that cater to the mainstream, neglecting minority interests, cultures, and perspectives.

Ethical Implication: This undermines pluralism, reducing the variety of content available to users and failing to support underrepresented or emerging creators, leading to a homogenized experience for all users.

Solution: Ethical AI systems should integrate diversity-aware algorithms, which ensure that the recommendation system does not exclusively favor the majority but includes a wider range of content.

3. User Manipulation and Exploitation
   
Concern: If an AI system prioritizes popularity over quality, it could manipulate users into repeatedly consuming trending or viral content without considering whether it aligns with their true preferences or needs. This could be driven by the platform’s commercial interests (e.g., promoting content that generates more engagement).

Ethical Implication: Users could be exploited by being nudged toward content that increases engagement, rather than being empowered to explore content based on their own informed decisions.

Solution: Platforms should ensure transparency in their recommendation algorithms, giving users the autonomy to understand and adjust their preferences. They should prioritize user well-being and agency over pure commercial or engagement-driven objectives.

4. Privacy Concerns
   
Concern: AI systems that use popularity bias may require extensive user data to personalize recommendations. While using popularity bias might seem like a way to improve content recommendations, it could still rely on invasive data collection practices.

Ethical Implication: The more data that is collected to enhance recommendations, the greater the risk to users’ privacy. There is a possibility that user data could be misused or inadequately protected, raising ethical concerns about user consent and data security.

Solution: Platforms should ensure that user data is handled ethically, with strong privacy protections in place. They should also minimize the amount of data required for content recommendations, giving users more control over their data and how it is used.


## References:
https://research.ebsco.com/c/bq4orh/viewer/pdf/nqcpkx6jdv

[https://dl.acm.org/doi/pdf/10.1145/3340531.3412152](https://dl.acm.org/doi/abs/10.1145/3340531.3412152)

https://dl.acm.org/doi/10.1145/3460231.3473321
