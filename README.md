# **🔪 tensor-scalpel**

De-censor & compress LLMs using Quantum Physics.  
An educational demo of the tensor network math behind Multiverse Computing's DeepSeek R1 Slim.

---
![Scalpel](./img/Tensor-Network-Scalpel.png)
---

## **🧠 Overview**

This repository contains a technical demonstration of the methods described in recent news regarding the "de-censorship" and compression of the **DeepSeek R1** model.

It explains the intersection of **Quantum Physics (Tensor Networks)** and **AI (Large Language Models)**, specifically focusing on two claims:

1. **Extreme Compression:** Shrinking a model by >50% using **Matrix Product Operators (MPOs)**.
2. **De-Censorship:** Surgically removing "propaganda" or "safety" vectors from the model weights using **Singular Value Decomposition (SVD)**.

## **📂 The Modules**

### **1. The Theory (CONCEPTS_AND_THEORY.md)**

**Start Here.** A layman's guide to the physics and math behind the code.

* Why Brains = Quantum States.
* What is a "Bond Dimension"?
* How SVD acts as a scalpel.

### **2. The Scalpel: Surgical Bias Removal (01_The_Scalpel_SVD.ipynb)**

This notebook demonstrates the "De-censorship" aspect.

* **Concept:** We treat the model's weights as a collection of "concepts" rather than just numbers.  
* **Method:** We use **Singular Value Decomposition (SVD)** to isolate the specific mathematical direction that corresponds to a "censorship" trigger.  
* **Action:** We mathematically "ablate" (remove) that direction from a **GPT-2** model without retraining it, effectively removing a specific behavior.

### **3. The Shrink Ray: Tensor Networks & MPOs (02_The_Shrink_Ray_MPO.ipynb)**

This notebook explains the "Quantum" aspect used for compression.

* **Concept:** Standard matrices ($N \times N$) are inefficient. Quantum physics uses **Matrix Product Operators (MPOs)** to represent complex systems efficiently.
* **Method:** We demonstrate how to reshape a neural network layer into a "Tensor Train" and compress it using the "Bond Dimension" ($\chi$).
* **Code:** Uses tensor_lib.py to simulate MPO layers.

### **4. Bibliography (BIBLIOGRAPHY.md)**

A curated list of the academic lineage (2014–2025), tracing the evolution from "CompactifAI" to "DeepSeek R1 Slim".

## **🚀 How to Use**

1. **Install dependencies:**  
   pip install torch numpy matplotlib transformers

2. Run the De-Censorship Demo:
   Open 01_The_Scalpel_SVD.ipynb in Jupyter. This will download a small GPT-2 model, inject a "virus" (censorship bias), and then surgically remove it.
3. Run the Compression Demo:
   Open 02_The_Shrink_Ray_MPO.ipynb to explore how reshaping matrices allows for massive parameter reduction.

## **⚠️ Technical Note**

While DeepSeek R1 is a massive 600B+ parameter model, these demos use **GPT-2** (Small) and synthetic layers. This ensures the code runs on standard consumer hardware (CPUs/Laptops) while illustrating the exact same mathematical principles used in the large-scale implementation.