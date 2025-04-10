# Simulating a Recommender System with Feedback Loop Only (No Exploration)

# Step 1: Brand setup
brands = [
    'Frosted Flakes', 'Kashi', 'Special K', 
    'Life Cereal', 'Lucky Charms', 'Cocoa Puffs', 
    'Honey Nut Cheerios', 'Cinnamon Toast Crunch', 'Corn Flakes', 'Raisin Bran'
]

# Random starting popularity scores
np.random.seed(42)
initial_scores = np.random.randint(50, 200, size=len(brands))

# Create DataFrame with scores
products_df = pd.DataFrame({
    'brand': brands,
    'popularity': initial_scores.astype(float),
    'score': initial_scores.astype(float)
})

# Step 2: Feedback loop config
iterations = 20
top_k = 4  # Number of top items to reinforce
score_history = {brand: [] for brand in products_df['brand']}

# Step 3: Run feedback loop with no exploration
for i in range(iterations):
    # Select top_k brands based on current score
    top_items = products_df.nlargest(top_k, 'score')

    # Log current scores for plotting
    for brand in products_df['brand']:
        current_score = products_df.loc[products_df['brand'] == brand, 'score'].values[0]
        score_history[brand].append(current_score)

    # Increase score for top brands only (feedback loop)
    boost = np.random.rand(top_k) * 10
    products_df.loc[top_items.index, 'score'] += boost

# Step 4: Plot results
score_df = pd.DataFrame(score_history)
top_brands = score_df.iloc[-1].sort_values(ascending=False).head(6).index
score_df[top_brands].plot(figsize=(12, 6), marker='o')
plt.title("Feedback Loop Without Exploration for Cereal Brands")
plt.xlabel("Iteration")
plt.ylabel("Recommendation Score")
plt.legend(title="Cereal Brand", bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


#########################################################################
#########################################################################


# Simulating a Recommender System with Feedback Loop and Exploration

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Brand setup
brands = [
    'Cinnamon Toast Crunch', 'Corn Flakes', 'Special K', 
    'Honey Nut Cheerios', 'Raisin Bran', 'Cocoa Puffs', 
    'Life Cereal', 'Frosted Flakes', 'Kashi', 'Lucky Charms'
]


np.random.seed(42)
initial_scores = np.random.randint(50, 200, size=len(brands))

products_df = pd.DataFrame({
    'brand': brands,
    'popularity': initial_scores.astype(float),
    'score': initial_scores.astype(float)
})

# Step 2: Tracking
iterations = 20
top_k = 4
explore_k = 2  # Number of lower-ranked brands to explore
score_history = {brand: [] for brand in products_df['brand']}

# Step 3: Feedback loop + stronger exploration
for i in range(iterations):
    # Recommend top_k products
    top_items = products_df.nlargest(top_k, 'score')

    # Log current scores
    for brand in products_df['brand']:
        current_score = products_df.loc[products_df['brand'] == brand, 'score'].values[0]
        score_history[brand].append(current_score)

    # Feedback boost for top items
    boost = np.random.rand(top_k) * 10
    products_df.loc[top_items.index, 'score'] += boost

    # Exploration: randomly boost 2 of the bottom 4 brands
    bottom_items = products_df.nsmallest(4, 'score')
    explore_indices = bottom_items.sample(explore_k).index
    products_df.loc[explore_indices, 'score'] += np.random.uniform(8, 12, size=explore_k)

# Step 4: Plot results
score_df = pd.DataFrame(score_history)
top_brands = score_df.iloc[-1].sort_values(ascending=False).head(6).index
score_df[top_brands].plot(figsize=(12, 6), marker='o')
plt.title("Improved Feedback Loop with Exploration for Cereal Brands")
plt.xlabel("Iteration")
plt.ylabel("Recommendation Score")
plt.legend(title="Cereal Brand", bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()