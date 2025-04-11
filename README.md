# Feedback Loops in Recommender Systems: Bias, Diversity, and Solutions
## Authors:
- **Elaina Longjohn**  
  GitHub: https://github.com/elongjohn
  
- **Mills Becouvarakis**  
  GitHub: https://github.com/millsbecouv
  
- **Shields Riggs**  
  GitHub: https://github.com/SWR22

- **Thokozile Munthali**  
  GitHub: https://github.com/author2

## Project Scope
Our project examines the negative effects of feedback loops in recommender systems. A feedback loop is a cycle where a user’s interactions with recommended items influence their future recommendations. This happens because every action a user takes—whether it's clicking, rating, or engaging with content—gets recorded in their profile, which then leads to more similar recommendations in the future.

The negative impacts of these feedback loops are significant, particularly the amplification of popularity bias. In this scenario, the preferences of the majority overpower those of minority groups, causing the recommender system to focus heavily on a narrow set of popular items. This limits both the diversity of recommendations and the potential for users to discover new, lesser-known content.

As a result, minority preferences are often drowned out by the mainstream, making it harder for niche or emerging products to get noticed. Through our project, we aim to address this issue by finding a way to reduce popularity bias and create a more level playing field for all products, free from the inherent biases built into recommender systems.


## Project Details
### 🔍 Problem Statement

We investigate the issue of feedback loops in recommender systems, where user interactions with popular content continuously reinforce the visibility of that content. This dynamic leads to **popularity bias**, which suppresses the discovery of niche items and limits recommendation diversity.
Our goal is to simulate and measure this bias—and explore ways to reduce it, creating fairer and more diverse recommendation environments.

<img src="https://github.com/user-attachments/assets/8792d0c2-a92d-4fe1-af72-2f347b464e42" width="400"/>

### 🧠 Research Foundation
We grounded our project in recent research on recommender system bias mitigation. The paper we selected is:

**"Feedback Loop and Bias Amplification in Recommender Systems" (2020)** – Proceedings of the ACM Web Conference  
📎 [Link to paper](https://dl.acm.org/doi/abs/10.1145/3340531.3412152)

This work provides both a theoretical and experimental framework for identifying and mitigating popularity bias through reweighting and counterfactual approaches.

### 🧪 Simulating a Recommender System
Two models show how feedback loops amplify popularity.

Model A: Repeats top picks → less diversity.

Model B: Adds exploration → more balance.

Score trends are visualized over time.

[Go to Simulation Section](#simulating-a-recommender-system)

### 🌐 Website Demo (GenAI)

We built a simulation using ClaudeAI to show how recommender systems amplify popularity bias.  
Even when users repeatedly engage with niche movies, the "For You" feed still favors popular items.  
This illustrates how feedback loops limit content diversity and make it harder for underrepresented items to break through.

[Go to Website Section](#Website-Demo:-popularity-Bias-in-Action)

### ✅ Project Management: GitHub Kanban Board
We tracked our work using a **GitHub Project Board** organized into several categories

[View our Kanban board](https://github.com/users/Thokozile23/projects/8)

### 🤖 Responsible AI Considerations
Recommender systems can unintentionally reinforce popularity bias, limit content diversity, and raise ethical concerns around user privacy and manipulation. We explore these risks and highlight simple strategies like boosting diversity, improving transparency, and minimizing data use.

[Go to Responsible AI Section](#responsible-ai-considerations-recommender-system-biases)

### 🚀 Future Developments

- Improve diversity in recommendations.
- Let users customize recommendation settings.
- Explore privacy-first AI (e.g., federated learning).
- Show transparent metrics on how suggestions are made.

[Go to Future Developments Section](#future-developments)


### 🔗 References

Our project is grounded in recent work highlighting how recommender systems amplify bias through feedback loops. These systems tend to favor popular content, often at the expense of diversity and fairness.

We explored multiple peer-reviewed studies, including:
- A simulation framework for bias amplification in recommender systems
- Guidelines for aligning recommender design with European AI regulations
- A tutorial on identifying and mitigating common algorithmic biases

🔗 [See full references](#references)

---

## Simulating a Recommender System
### 1. Dataset & Setup
We use a simulated dataset of cereal brand "products" with initial randomized popularity scores to mimic the behavior of user-item interactions in a recommender system. This allows us to focus on the **structure and effects** of feedback loops without needing user identifiers.

### 2. Feedback Loop Simulations

We created two models to compare behavior:

- **Model A: No Exploration**  
  - Recommends the top 4 products repeatedly based on their score.
  - Simulates how recommender systems reinforce popular items.
  
- **Model B: With Exploration Boosts**  
  - Recommends the top 4 products, but also adds small boosts to 2 low-performing products each round.
  - Simulates efforts to promote diversity and disrupt the feedback loop.

➡️ **[Run the simulation → Final Project Sample Code.py](./Final_Project_Sample_Code.py)**

### 3. Visualization

The simulation plots how each product's score evolves over 20 iterations.  
- In **Model A**, the same few products dominate over time.  
- In **Model B**, more products stay in the mix due to exploration.

## Website Demo: Popularity Bias in Action

We developed an interactive simulation using **ClaudeAI** to showcase how popularity bias manifests in recommendation systems.

- Users simulate interacting with movies by clicking on them.
- Despite repeated clicks on niche movies, the system heavily favors **popular content** in its "For You" feed.
- Niche items take a long time—and significantly more engagement—to surface in recommendations.
- This demonstrates how feedback loops reinforce already-popular items, making it harder for diverse or underrepresented content to gain visibility.

🔗 [Try the Demo – Popularity Bias & Feedback Loops Simulation](https://claude.site/artifacts/ccbba4e1-d462-4835-a628-b096dd31fec1)

The tool highlights how recommender systems can unintentionally limit discovery and diversity, even when user preferences shift toward niche interests.

## Responsible AI considerations:

### Understanding Recommender System Biases

Understanding the biases present in recommender systems (RSs) is crucial, as these biases can significantly impact the fairness, accuracy, and trustworthiness of recommendations. The biases within RSs can be categorized into four main types: data biases, cognitive biases, position/presentation biases, and algorithmic/model biases.

-  Data Bias:
Data biases occur when the training data used by the recommender system is unbalanced or not fully representative of the entire user base. For example, certain demographic groups may be underrepresented, leading to recommendations that fail to reflect the diversity of users or perpetuate existing inequalities.

- Coginitive Bias:
Cognitive biases are influenced by human mental shortcuts or heuristics, which can affect how users interact with the system. Examples include the anchoring effect, where users rely too heavily on the first piece of information they encounter, or the recency effect, which may cause users to favor items that are more recent rather than more relevant.

- Position/Presentation Bias:
Position or presentation biases arise from the way recommendations are displayed to users. Items placed at the top of the list, for example, are more likely to be selected, regardless of their actual relevance to the user. This form of bias is often unintentional but can significantly skew the user experience.

-  Algorithmic/Model Bias
Algorithmic or model biases are embedded in the recommendation algorithms themselves, often due to the way models are trained or the data they use. These biases can amplify existing stereotypes or reinforce behaviors by overemphasizing certain patterns in user data, such as preferences based on past behaviors or demographic factors.

![image](https://github.com/user-attachments/assets/13ef7933-f24c-44c1-8fe7-18e8f9aefaed)

### Ethical Concerns:

-  Marginalization of Minority Voices: 
Efforts to counter popularity bias may inadvertently sideline mainstream content, raising questions about fairness to all creators.

-  Balance Between Diversity and Relevance: 
Striving for diversity might lead to recommendations that feel irrelevant or forced, potentially frustrating users.

-  Algorithmic Manipulation: 
Overcompensation for popularity bias could be exploited by bad actors to artificially amplify niche or low-quality content.

-  Transparency Issues: 
Users may not fully understand adjustments made to recommendations, raising concerns about opacity in how content is prioritized.

- Bias Trade-offs: 
Correcting one form of bias (popularity) might unintentionally introduce new biases, such as favoring specific minority groups over others.


## What's next? Help us envision future developments and concerns. 

## Future Developments

### 1. **Integrate Enhanced Diversity Algorithms**
Continued refinement of algorithms to ensure even greater inclusion of underrepresented or niche content, allowing for tailored recommendations that go beyond mainstream preferences.

### 2. **Implement User Customization Options**
Provide users with more tools to adjust recommendation settings (e.g., adjusting for diversity or prioritizing specific interests) to empower individual agency.

### 3. **Explore Ethical AI Practices**
Lead by example by integrating cutting-edge, privacy-preserving machine learning techniques, such as federated learning, to minimize invasive data collection.

### 4. **Offer Transparent Metrics**
Develop a dashboard to display how recommendations are generated, showcasing the balance between popularity, diversity, and user preferences.

## References

- **Mansoury, M., Abdollahpouri, H., Pechenizkiy, M., Mobasher, B., & Burke, R. (2020).**  
  *Feedback Loop and Bias Amplification in Recommender Systems*.  
  In *Proceedings of the 29th ACM International Conference on Information & Knowledge Management (CIKM '20)*, pp. 2145–2148.  
  [https://doi.org/10.1145/3340531.3412152](https://doi.org/10.1145/3340531.3412152)  
  **Summary:** Explores how recommender systems amplify bias through feedback loops, and proposes a simulation framework for offline analysis.

- **Di Noia, T., Tintarev, N., Fatourou, P., & Schedl, M. (2022).**  
  *Recommender Systems under European AI Regulations*.  
  *Communications of the ACM*, 65(4), 69–73.  
  [https://doi.org/10.1145/3512728](https://doi.org/10.1145/3512728)  
  **Summary:** Discusses the impact of European AI regulation on recommender systems, highlighting transparency, fairness, and accountability.

- **Chen, J., Wang, X., Feng, F., & He, X. (2021).**  
  *Bias Issues and Solutions in Recommender System: Tutorial on the RecSys 2021*.  
  In *Proceedings of the 15th ACM Conference on Recommender Systems (RecSys '21)*, pp. 825–827.  
  [https://doi.org/10.1145/3460231.3473321](https://doi.org/10.1145/3460231.3473321)  
  **Summary:** Provides a tutorial-style overview of biases in recommendation systems and outlines methods for mitigating them to improve fairness.
