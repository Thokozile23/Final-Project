🔁 ## **Feedback Loops in Recommender Systems: Bias, Diversity, and Solutions**

## Authors:
- **Elaina Longjohn**  
  GitHub: https://github.com/elongjohn
  
- **Mills Becouvarakis**  
  GitHub: https://github.com/millsbecouv
  
- **Shields Riggs**  
  GitHub: https://github.com/SWR22

- **Thokozile Munthali**  
  GitHub: https://github.com/Thokozile23

## Project Scope

Our project explores the negative impacts of feedback loops in recommender systems, with a particular focus on how they reinforce and amplify popularity bias. A feedback loop occurs when a user's interactions such as clicks, ratings, and engagement are tracked and recorded as data to inform future recommendations.

While this type of personalization can enhance user experience, it often creates self-reinforcing cycles where users are repeatedly exposed to similar content. This process tends to favor popular items, allowing the preferences of the majority to dominate while underrepresenting those of minority or niche groups. As a result, recommendation diversity is reduced, and lesser-known or emerging products struggle to gain visibility. This not only limits user discovery but also perpetuates existing inequalities in the marketplace. 

We seek to examine these challenges and propose strategies to reduce popularity bias, ultimately promoting a more equitable recommendation environment, enhancing customer experience, and supporting broader product engagement and long-tail monetization for businesses.

We aim explore this issue from both a technical and ethical standpoint. We will examine how algorithmic design contributes to biased outcomes through a detailed simulation. Furthermore, we aim to prototype and test a solution to reduce this bias using a movie website we developed as a testbed.

## Project Details
### 🔍 Problem Statement
We investigate the major challenge feedback loops in recommender systems create by reinforcing **popularity bias**. Creating a cycle that limits exposure to diverse or niche content, making it harder for new or underrepresented items to be discovered. This imbalance not only affects user satisfaction and engagement but also limits growth opportunities for lesser-known creators or products. Our project addresses this issue by simulating how popularity bias evolves and investigating ways to reduce it, with the goal of promoting fairer, more inclusive, and diverse recommendation systems.

The picture below illustrates the feedback loop cycle in recommender systems:

<img src="https://github.com/user-attachments/assets/8792d0c2-a92d-4fe1-af72-2f347b464e42" width="400"/>

### 🧠 Research Foundation
Our project is based on a recent academic research focused on identifying and addressing bias in recommender systems. A key paper that informed our work is "**Feedback Loop and Bias Amplification in Recommender Systems**" (2020), published by the ACM Web Conference. This study investigates how feedback loops—where user interactions with recommended content influence future recommendations—can enhance existing biases within the system over time. It highlights that recommender algorithms often overemphasize popular items due to repeated exposure, reinforcing popularity bias and limiting content diversity.

The link to the research paper we selected is:
📎 [Link to paper](https://dl.acm.org/doi/abs/10.1145/3340531.3412152)

### 🧪 Simulating a Recommender System
To understand how feedback loops contribute to popularity bias and the lack of diversity in recommender systems, we simulate two models to showcase different behaviors in the recommendation process.

**Model A**: Repeated Exposure to Top Picks

In this model, the recommender system continually prioritizes the most popular items based on user interactions, leading to a cycle where the top picks are repeatedly recommended to users. As a result, the system reinforces existing preferences, making it increasingly difficult for lesser-known or niche items to gain visibility. Over time, this causes a reduction in the diversity of recommendations, with users being exposed primarily to mainstream content. The model's score trends show a clear preference for popular items, with a steady decline in the exploration of new content.

**Model B**: Incorporating Exploration

Model B introduces an element of exploration, where the system occasionally recommends less popular or new items alongside the top picks. This approach is designed to break the cycle of popularity reinforcement and encourage a more balanced distribution of recommendations. By integrating exploration, the system promotes greater content diversity and provides users with a wider range of items to discover. In this model, score trends over time demonstrate a more balanced recommendation pattern, where niche and emerging items receive more attention, improving both the variety of recommendations and user engagement with new content.

These two models are analyzed and compared by visualizing their score trends over time, providing insights into how feedback loops influence recommendation dynamics. The findings from these simulations will guide our understanding of how to reduce popularity bias and design fairer, more diverse recommender systems.

Link to the simulation we created is:

[Go to Simulation Section](#simulating-a-recommender-system)

### 🌐 Website Demo (GenAI)

We developed an interactive movie recommendation website using by ClaudeAI to visually demonstrate how feedback loops in recommender systems contribute to popularity bias. The simulation mimics a user engaging with various types of movie content—especially niche or lesser-known films. Despite this engagement, the "For You" feed continues to prioritize already popular titles, showing how recommender algorithms often override individual preferences in favor of widespread trends. 

This behavior highlights how feedback loops restrict content diversity, reinforce the visibility of mainstream items, and make it increasingly difficult for underrepresented or new content to gain traction. The website serves as both a learning tool and a prototype environment to explore interventions that could promote fairer, more inclusive recommendation outcomes.

Link to our website can be found below:

[Go to Website Section](#website-demo-popularity-bias-in-action)

### ✅ Project Management: GitHub Kanban Board

To effectively manage and track the progress of our project, we utilized a GitHub Project Board. This tool allowed us to break down our tasks and milestones into clear, actionable categories, helping ensure transparency, collaboration, and accountability throughout the project. Our board was organized into several key sections, each representing different stages of the project workflow:

1.	Backlog: This section contained tasks and ideas that needed to be explored or completed but hadn’t yet been assigned a priority. These were initially brainstormed tasks, research questions, and any outstanding decisions that could inform the next steps of the project.
   
2.	To Do: Once tasks were clearly defined and prioritized, they were moved to this section. These were the tasks ready to be worked on, including activities such as coding, data collection, literature review, and modeling.
   
3.	In Progress: Tasks actively being worked on were moved here. For example, developing simulations, writing the project report, or conducting data analysis would appear in this category. This section allowed us to keep track of who was working on what and ensured there was no duplication of effort.
   
4.	Review: After tasks were completed, they were moved to this section for peer review and validation. This stage helped ensure the quality and accuracy of our work, with team members reviewing each other's contributions before finalizing them.
   
5.	Done: Once tasks passed review and were fully completed, they were moved to the Done section. This gave us a clear view of our progress and allowed us to track the overall completion of project deliverables.


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

## Business Implications:

Recommender systems play a vital role in modern business, influencing everything from online shopping and entertainment choices to chatbots and fantasy sports. As technology continues to advance, their significance in daily life and business strategy cannot be overstated. Companies depend on these systems to deliver personalized, data-driven suggestions that help users make informed decisions—whether about purchases, customer engagement, or even lifestyle changes. Exceptional recommender systems are the foundation of some of the biggest businesses in the world including Amazon, Netflix, and Google, which help them generate a combined market cap of over $4.16 trillion. Knowing how to use recommenders and what they do can be a game-changing tool for businesses, big or small. Understanding how recommender systems work and how to leverage them can be a transformative asset for businesses of any size. However, it's important to recognize their limitations. Recommenders aren’t always fair, they inadvertently reinforce existing biases, shaping perceptions that can change how a person sees a product or business, leading to favoritism or exclusion. Therefore, businesses must carefully weigh the benefits against the risks and make thoughtful decisions about their implementation. Recommenders are here to stay and regardless of the challenges that they propose. To remain competitive and customer-focused, businesses need to understand what recommenders are, how they function, and how best to use them in alignment with their goals. 


## Responsible AI considerations:

### Understanding Recommender System Biases

Understanding the biases present in recommender systems (RSs) is crucial, as these biases can significantly impact the fairness, accuracy, and trustworthiness of recommendations. The biases within RSs can be categorized into four main types: data biases, cognitive biases, position/presentation biases, and algorithmic/model biases.

- Data Bias:
Data bias occurs when training data is unbalanced or not fully representative of all users. This can lead to recommendations that overlook certain demographic groups and reinforce existing inequalities.

- Cognitive Bias:
Cognitive biases stem from human mental shortcuts that shape how users interact with the system. Effects like anchoring or recency can cause users to favor initial or recent items over more relevant ones.

- Position/Presentation Bias:
This bias arises from how recommendations are displayed, with top-listed items receiving more attention. Even if less relevant, their placement can skew user choices and overall system effectiveness.

- Algorithmic/Model Bias:
Algorithmic bias is rooted in how models are built and trained, often reflecting the flaws in their data. These biases can reinforce stereotypes or overemphasize certain user patterns, limiting diversity in recommendations.

![image](https://github.com/user-attachments/assets/13ef7933-f24c-44c1-8fe7-18e8f9aefaed)

### Ethical Concerns:

-  Balance Between Diversity and Relevance: 
Striving for diversity might lead to recommendations that feel irrelevant or forced, potentially frustrating users.

-  Algorithmic Manipulation: 
Overcompensation for popularity bias could be exploited by other people or businesses to artificially amplify niche or low-quality content.

-  Transparency Issues: 
Users may not fully understand adjustments made to recommendations, raising concerns about opacity in how content is prioritized.

- Bias Trade-offs: 
Correcting one form of bias (popularity) might unintentionally introduce new biases, such as favoring specific minority groups over others.


## What's next? Help us envision future developments

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
