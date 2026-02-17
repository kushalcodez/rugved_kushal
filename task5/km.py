import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("penguins.csv")

# Select features and species, drop missing values
data = df[[
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "species"
]].dropna()

X = data[[
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = kmeans.fit_predict(X_scaled)

# Plot clusters with species meaning
plt.figure()

for cluster_id in sorted(data["Cluster"].unique()):
    cluster_data = data[data["Cluster"] == cluster_id]
    
    # Find dominant species in this cluster
    dominant_species = cluster_data["species"].mode()[0]
    
    plt.scatter(
        cluster_data["bill_length_mm"],
        cluster_data["bill_depth_mm"],
        label=f"Cluster {cluster_id} → {dominant_species}"
    )

plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.title("KMeans Clusters Interpreted Using Species")
plt.legend(title="Cluster Meaning")
plt.show()
